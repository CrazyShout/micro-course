# Extra Resources · historical preview

@@ N135 | x01-applications | learn | XN2:66-67
Q_EN: What are the question, answer, authority and additional sections in a DNS message?
Q_ZH: DNS 消息中的 question、answer、authority 和 additional 部分分别做什么？
A_EN: The question names the requested record. Answers provide records addressing it. Authority records identify relevant authoritative servers, while additional records can supply useful supporting data such as server addresses. The header also carries an identifier and flags. An additional record is not automatically the final answer to the original question.
A_ZH: Question 指明查询的记录，answer 提供回答该查询的记录，authority 标识相关权威服务器，additional 可提供服务器地址等辅助信息。首部还包含标识符与标志。Additional 中的记录并不自动等于原问题的最终答案。

@@ N136 | x01-applications | learn | XN2:68
Q_EN: How does registering a domain differ from publishing a host's address record?
Q_ZH: 注册域名与发布某主机的地址记录有什么区别？
A_EN: Registration and delegation establish which authoritative name servers serve a domain. Those authoritative servers then publish records such as an A record for a web host and MX records for mail. Ownership/delegation information and a particular service's address are separate layers, so changing one does not automatically update every other record.
A_ZH: 注册与委派确定由哪些权威名称服务器负责域名，这些服务器再发布网站主机的 A 记录、邮件的 MX 记录等。所有权或委派信息，与某个服务的具体地址属于不同层次，修改其中一项不会自动更新其他全部记录。

@@ N137 | x01-applications | learn | XN2:71-74
Q_EN: Why can peer-to-peer distribution scale differently from client-server distribution?
Q_ZH: 为什么 P2P 文件分发的扩展方式不同于客户端—服务器模式？
A_EN: In client-server distribution, the server uploads a complete copy to each client. In P2P, peers can upload pieces they have already received, adding aggregate upload capacity as the group grows. The server must still introduce every piece at least once, and slow peer downloads can remain bottlenecks.
A_ZH: 客户端—服务器模式中，服务器要向每个客户端上传完整副本。P2P 中，节点可上传自己已收到的分块，节点增加时也增加了总体上传能力。但服务器仍需至少引入每一块一次，下载很慢的节点也仍可能成为瓶颈。

@@ N138 | x01-applications | learn | XN2:72-74
Q_EN: What ideal lower bounds govern distribution of an F-bit file to N peers?
Q_ZH: 向 N 个节点分发 F bit 文件，有哪些理想时间下界？
A_EN: Let server upload be us, peer uploads ui and minimum peer download dmin. Client-server needs at least $\max(NF/u_s,F/d_{\min})$. P2P needs at least $\max(F/u_s,F/d_{\min},NF/(u_s+\sum_i u_i))$. These fluid-model bounds ignore packet overhead, piece availability and scheduling limits; a bound is not automatically an achievable measured time.
A_ZH: 设服务器上传速率为 us、节点上传为 ui、最慢下载为 dmin。客户端—服务器模式至少需 $\max(NF/u_s,F/d_{\min})$；P2P 至少需 $\max(F/u_s,F/d_{\min},NF/(u_s+\sum_i u_i))$。这些流体模型下界忽略分组开销、分块可用性和调度限制，不自动等于实际可达到的时间。

@@ N139 | x01-applications | worked | XN2:73-75
Q_EN: Distribute a file F=1 Gbit to N=10 clients. Server upload us=100 Mbps, each client upload is 10 Mbps, and the slowest client download dmin=50 Mbps. Find ideal client–server and P2P distribution-time lower bounds.
Q_ZH: 把 F=1 Gbit 文件分发给 N=10 个客户端。服务器上传 us=100 Mbps，各客户端上传 10 Mbps，最慢客户端下载 dmin=50 Mbps。求客户端—服务器与 P2P 的理想分发时间下界。
A_EN: Client-server terms are 100 s and 20 s, giving 100 s. P2P terms are 10 s, 20 s and $10\,\text{Gbit}/200\,\text{Mbps}=50$ s, giving 50 s. All rates use bits per second. This added example illustrates capacity constraints, not an actual BitTorrent measurement.
A_ZH: 客户端—服务器的两项为 100 s、20 s，取最大值得 100 s。P2P 的三项为 10 s、20 s，以及 $10\,\text{Gbit}/200\,\text{Mbps}=50$ s，得到 50 s。各速率均以 bit/s 计，这是容量约束的补充例子，不是实际 BitTorrent 测量。

@@ N140 | x01-applications | learn | XN2:76-80
Q_EN: What purposes do rarest-first selection and peer reciprocation serve in the lecture's BitTorrent model?
Q_ZH: 课件的 BitTorrent 模型中，最稀有块优先和节点互惠分别有什么作用？
A_EN: Rarest-first selection helps keep scarce pieces available across the swarm. Reciprocation gives peers an incentive to upload to one another, while optimistic unchoking explores new partners. These mechanisms address piece diversity and incentives, which aggregate upload-capacity formulas alone do not capture.
A_ZH: 最稀有块优先有助于维持群体中稀缺分块的可用性。互惠机制鼓励节点相互上传，乐观解锁则探索新的交换对象。这些机制分别处理分块多样性与激励问题，单靠总体上传容量公式无法反映它们。

@@ N141 | x01-applications | learn | XN2:82-88
Q_EN: How does DASH adapt video quality to changing network conditions?
Q_ZH: DASH 如何根据网络变化调整视频质量？
A_EN: The server provides multiple encoded representations divided into segments and described by a manifest. The client estimates conditions and requests an appropriate representation for each next segment. It trades visual quality against rebuffering risk and switching behavior. Adaptation is a client-side decision process, not a guarantee of uninterrupted playback.
A_ZH: 服务器提供多种编码质量，将视频分段，并用清单描述。客户端估计网络状况，为下一段请求适当版本，在画质、卡顿风险和切换行为之间取舍。自适应是客户端的决策过程，并不保证播放永不中断。

@@ N142 | x01-applications | learn | XN2:89-92
Q_EN: What problem does a content distribution network solve?
Q_ZH: 内容分发网络解决什么问题？
A_EN: A CDN places or caches content at multiple locations and directs a client to a suitable delivery server. This can reduce long-haul traffic and avoid reliance on one overloaded origin. Selection can depend on network conditions and policy, not just geographic distance. A cache miss may still require fetching from another location.
A_ZH: CDN 在多个位置放置或缓存内容，并把客户端引导到适当服务器，可减少远距离流量，降低对单一过载源站的依赖。节点选择可取决于网络状况和策略，不仅是地理距离。缓存未命中时，仍可能需要从其他位置获取内容。

@@ N143 | x01-applications | learn | XN2:94-101
Q_EN: What is the basic UDP server/client socket workflow?
Q_ZH: UDP 服务器与客户端的基本 socket 流程是什么？
A_EN: A server creates a datagram socket and binds a local address/port. It receives a datagram together with the sender's address and can reply to that address. A client sends to the server's destination and receives a response. UDP has no transport handshake or accept step, and the application must handle missing or unexpected responses.
A_ZH: 服务器创建数据报 socket，并绑定本地地址和端口；接收数据报时同时获得发送者地址，可向该地址回复。客户端向服务器目标地址发送，再接收响应。UDP 没有传输层握手或 accept 步骤，应用需自行处理丢失或非预期的回复。

@@ N144 | x01-applications | learn | XN2:102-105
Q_EN: Why does a TCP server have a listening socket and separate connected sockets?
Q_ZH: TCP 服务器为什么同时需要监听 socket 和独立的连接 socket？
A_EN: The listening socket waits for incoming connections. Accept returns a connected socket for one peer, while the listening socket remains available for later clients. Data exchange uses the connected socket. Closing one client's connection need not stop the whole server; concurrency and lifetime management are application design choices.
A_ZH: 监听 socket 等待新连接，accept 为某个对端返回连接 socket，监听 socket 则继续接收后续客户端。数据交换使用连接 socket。关闭一个客户端连接不必停止整个服务器，并发方式与生命周期管理由应用设计决定。

@@ N145 | x01-applications | check | XN2:95,102-105
Q_EN: Why is one send call not guaranteed to match one recv call on TCP?
Q_ZH: TCP 中，为什么一次 send 不保证对应一次 recv？
A_EN: TCP delivers an ordered byte stream, not application message boundaries. A receive can contain part of a message or data from several sends. Applications need framing, such as a length prefix or a delimiter with escaping. A successful send also does not establish that the peer application has processed the message.
A_ZH: TCP 提供有序字节流，不保留应用消息边界。一次接收可能只有半条消息，也可能包含多次发送的数据。应用需要长度前缀，或带转义规则的分隔符等分帧方式。发送调用成功也不证明对端应用已经处理了消息。

@@ N146 | x01-applications | learn | XN2:98-105
Q_EN: Why must socket applications distinguish text from bytes?
Q_ZH: Socket 应用为什么必须区分文本与字节？
A_EN: The transport carries bytes. An application encodes text with an agreed encoding before sending and decodes after assembling the required bytes. A multi-byte character can be split across TCP reads, so decoding each arbitrary fragment independently can fail. Protocol lengths must state whether they count bytes or characters.
A_ZH: 传输层承载的是字节，应用按约定编码发送文本，并在收集到所需字节后解码。一个多字节字符可能跨越两次 TCP 读取，独立解码每个任意片段可能失败。协议长度还必须说明计的是字节数还是字符数。

@@ N147 | x01-applications | check | XN2:102-105; XPROJ:2-6
Q_EN: What should a robust stream-message receive loop do?
Q_ZH: 可靠的字节流消息接收循环应做什么？
A_EN: Keep a buffer, accumulate incoming bytes, and parse only complete frames according to the protocol. Preserve leftover bytes for the next frame. Treat an empty TCP receive as end-of-stream, and handle timeouts or malformed lengths explicitly. These are application-protocol requirements beyond TCP's byte-delivery service.
A_ZH: 维护缓冲区，累积收到的字节，并按协议只解析完整消息帧；剩余字节留给下一帧。TCP 接收返回空字节串表示流结束，超时或错误长度应明确处理。这些是应用协议责任，超出了 TCP 的字节交付服务。

@@ N148 | x01-applications | check | XN2:69,95-105
Q_EN: What is the difference between identifying a network endpoint and authenticating its user?
Q_ZH: 标识网络端点与认证其用户有什么区别？
A_EN: IP addresses and ports direct traffic to an endpoint. They do not prove who controls it or whether application data is authentic. Checksums and TCP reliability detect certain transmission problems, not malicious impersonation. An application requiring identity or confidentiality needs an appropriate security protocol in addition to socket communication.
A_ZH: IP 地址与端口把流量送到端点，但不证明谁控制该端点，也不证明应用数据真实。校验和及 TCP 可靠性用于处理某些传输问题，并不防止恶意冒充。需要身份或机密性的应用，还需适当的安全协议，不能只依赖 socket 通信。

@@ N149 | x02-transport | learn | XN3:4-15
Q_EN: What do transport multiplexing and demultiplexing mean?
Q_ZH: 传输层的复用与解复用是什么意思？
A_EN: Multiplexing combines data from several application sockets for network transmission. Demultiplexing uses transport-header and address information to deliver arriving data to the appropriate socket. IP delivery to a host and transport delivery to a process are separate steps. Port numbers are part of this mapping, not physical network connectors.
A_ZH: 复用把多个应用 socket 的数据交给网络传输；解复用利用传输层首部和地址信息，把到达数据交给相应 socket。IP 将数据送到主机，与传输层将数据交给进程，是不同步骤。端口号是这种映射的一部分，不是物理插口。

@@ N150 | x02-transport | learn | XN3:11-15; XNT5:1
Q_EN: How do the lecture's UDP and established TCP demultiplexing keys differ?
Q_ZH: 课件中 UDP 与已建立 TCP 连接的解复用标识有何区别？
A_EN: In the basic model, a UDP receive socket is selected by local destination IP and port, so datagrams from several senders can arrive at it. An established TCP connection is identified by source IP/port and destination IP/port together. Socket API options and connected UDP can add filtering, so the basic model is not a complete specification of every OS socket behavior.
A_ZH: 基础模型中，UDP 接收 socket 由本地目的 IP 和端口选择，因此多个发送者的数据报可进入同一 socket。已建立 TCP 连接则由源 IP/端口与目的 IP/端口共同标识。API 选项及连接式 UDP 还可增加过滤，因此基础模型并非所有操作系统 socket 行为的完整规范。

@@ N151 | x02-transport | learn | XN3:17-18; XUDP:Format-Fields
Q_EN: What fields are in the UDP header, and does UDP length include that header?
Q_ZH: UDP 首部有哪些字段？UDP length 是否包含首部？
A_EN: Source port, destination port, length and checksum are each 16 bits, giving an 8-byte header. The UDP length counts header plus payload, not the enclosing IP header. Therefore a 100-byte payload has UDP length 108 bytes. Length must be interpreted at the protocol layer to which the field belongs.
A_ZH: 源端口、目的端口、长度和校验和各占 16 bit，首部共 8 byte。UDP length 包含首部与载荷，但不含外层 IP 首部，因此 100 byte 载荷对应 UDP length 108 byte。读取长度时必须明确字段所属协议层。

@@ N152 | x02-transport | learn | XN3:17-19
Q_EN: Which services does UDP itself not guarantee?
Q_ZH: UDP 本身不保证哪些服务？
A_EN: UDP does not itself guarantee delivery, ordering, duplicate suppression, retransmission or congestion control. An application can implement additional mechanisms above UDP, so “uses UDP” does not imply that the entire application must be unreliable. Likewise, no handshake does not imply every UDP application will have lower total latency.
A_ZH: UDP 本身不保证交付、顺序、去重、重传或拥塞控制。应用可在 UDP 之上加入额外机制，因此“使用 UDP”不代表整个应用一定不可靠。同样，没有握手也不意味着所有 UDP 应用的总体时延都更低。

@@ N153 | x02-transport | learn | XN3:19-20; XUDP:Fields
Q_EN: How is the Internet checksum formed, and what does UDP additionally cover through its pseudo-header?
Q_ZH: 互联网校验和如何形成？UDP 伪首部额外保护什么信息？
A_EN: Add 16-bit words with one's-complement arithmetic, wrap end-around carries, then complement the result. UDP covers its header and data plus a pseudo-header containing IP source/destination, protocol and UDP length. The pseudo-header is used in computation rather than sent as an extra UDP header. Passing this check means no detectable checksum error, not proven authenticity.
A_ZH: 使用反码加法累加 16 bit 字，最高位进位回卷相加，最后按位取反。UDP 除首部和数据外，还覆盖含 IP 源/目的地址、协议及 UDP 长度的伪首部。伪首部参与计算，并不是额外发送的 UDP 首部。校验通过只表示未检出此类差错，不证明真实性。

@@ N154 | x02-transport | worked | XN3:19-20
Q_EN: Using 16-bit one's-complement arithmetic, find the checksum of words 0xFFFF and 0x0001.
Q_ZH: 用 16 bit 反码加法，求 0xFFFF 与 0x0001 两个字的校验和。
A_EN: Their ordinary sum is 0x10000. Wrap the carry into the low 16 bits to obtain 0x0001, then complement to get 0xFFFE. Including this checksum in the one's-complement sum gives 0xFFFF. Ignoring the end-around carry would produce the wrong checksum.
A_ZH: 普通相加得到 0x10000，将进位回卷到低 16 bit，得到 0x0001，再取反得到 0xFFFE。把该校验和一起反码相加会得到 0xFFFF。若忽略进位回卷，就会算错。

@@ N155 | x02-transport | check | XN3:19-20; XN6:11-13
Q_EN: Can a checksum detect every possible corruption?
Q_ZH: 校验和能检测所有可能的数据损坏吗？
A_EN: No. Different bit patterns can share the same checksum, and compensating changes can leave the sum unchanged. Error-detection strength depends on the code and error pattern. A checksum is useful for accidental corruption, but it is not a collision-resistant cryptographic integrity mechanism or a proof that the receiver obtained the original data.
A_ZH: 不能，不同位模式可能具有相同校验和，互相抵消的变化也可能使和不变。检错能力取决于编码和错误模式。校验和适合处理意外损坏，但不是抗碰撞的密码学完整性机制，也不是接收数据等于原数据的证明。

@@ N156 | x02-transport | learn | XN3:22-34
Q_EN: What extra mechanisms are needed when a channel can corrupt data or acknowledgments?
Q_ZH: 信道可能损坏数据或确认消息时，需要增加哪些机制？
A_EN: Detect corruption, send feedback and retransmit when necessary. But a corrupted acknowledgment leaves the sender unsure whether data arrived. Simply retransmitting can deliver duplicates unless the protocol also identifies transmissions. Reliable-transfer design must handle errors on the feedback path as well as on the forward data path.
A_ZH: 需要检错、反馈和必要时重传。但确认消息损坏时，发送者无法确定数据是否已到达；如果没有传输标识，直接重传可能导致重复交付。因此可靠传输既要处理正向数据路径，也要处理反向反馈路径的错误。

@@ N157 | x02-transport | learn | XN3:34-39
Q_EN: Why does alternating-bit stop-and-wait use sequence numbers 0 and 1?
Q_ZH: 停等式交替位协议为什么使用 0 和 1 两个序号？
A_EN: The receiver tracks which sequence number is expected. A retransmitted copy of the previous packet can be acknowledged again without delivering its payload twice. The sequence bit distinguishes the current new packet from a duplicate within the protocol's assumptions. It does not make arbitrary old packets harmless over unlimited lifetimes and wraps.
A_ZH: 接收者记录当前期望的序号。上一分组的重传副本可以再次确认，但不重复向上交付载荷。序号位在协议假设下区分当前新分组与重复副本，并不保证任意长寿命、反复回绕的旧分组都不会造成混淆。

@@ N158 | x02-transport | learn | XN3:40-44
Q_EN: Why does rdt3.0 add a timer?
Q_ZH: rdt3.0 为什么需要增加定时器？
A_EN: If either data or its acknowledgment disappears, the sender may otherwise wait forever. A timeout triggers retransmission. A slow packet can be mistaken for a lost one, so sequence numbers and duplicate handling are still needed. The timer trades waiting delay against unnecessary retransmission; a timeout is evidence of delay or loss, not proof of which occurred.
A_ZH: 数据或确认消息丢失后，发送者可能无限等待；超时会触发重传。慢分组也可能被误判为丢失，所以仍需序号和去重机制。定时器在等待时间与多余重传之间取舍；超时说明发生了延迟或丢失，不能直接证明是哪一种。

@@ N159 | x02-transport | learn | XN3:45-46
Q_EN: What is ideal stop-and-wait sender utilization?
Q_ZH: 理想停等协议的发送端利用率是多少？
A_EN: With packet serialization time L/R, propagation round trip RTT, negligible ACK transmission and no errors, $U=(L/R)/(RTT+L/R)$. The sender transmits one packet and then waits for its ACK. Throughput is $L/(RTT+L/R)$ bits/s. Be explicit about whether a problem's RTT already includes serialization or processing.
A_ZH: 设分组发送时间为 L/R、传播往返时间为 RTT，忽略 ACK 发送与差错，则 $U=(L/R)/(RTT+L/R)$。发送者发一包后等待确认，吞吐量为 $L/(RTT+L/R)$ bit/s。必须明确题目的 RTT 是否已经包含发送或处理时间。

@@ N160 | x02-transport | worked | XN3:45-46
Q_EN: In a loss-free stop-and-wait model, link rate R=1 Gbps, packet length L=8,000 bits, and round-trip propagation RTT=30 ms. Ignore ACK transmission and processing time. Find the fraction of a send–ACK cycle spent transmitting data and the resulting throughput.
Q_ZH: 无丢包停等模型中，链路速率 R=1 Gbps，分组长度 L=8000 比特，往返传播时延 RTT=30 毫秒。忽略 ACK 传输与处理时间。求一个发送—确认周期中发送数据所占比例，以及吞吐量。
A_EN: Serialization takes 8 microseconds. Utilization is $8/30008\approx0.0002666$, or 0.02666%. Throughput is about 266.6 kbit/s, despite a 1 Gbit/s link. Use consistent time units and distinguish the dimensionless fraction from its percentage.
A_ZH: 发送时间为 8 微秒，利用率为 $8/30008\approx0.0002666$，即 0.02666%。吞吐量约为 266.6 kbit/s，远低于链路的 1 Gbit/s。计算时统一时间单位，并区分无量纲比例与百分数。

@@ N161 | x02-transport | learn | XN3:47-50
Q_EN: How does pipelining improve utilization in the ideal reliable-transfer model?
Q_ZH: 理想可靠传输模型中，流水线怎样提高利用率？
A_EN: Allow several unacknowledged packets in flight. With window N, the ideal utilization is bounded by $\min(1,N(L/R)/(RTT+L/R))$. Once the path is full, enlarging the window cannot exceed link capacity. Loss, receiver limits and congestion can reduce realized performance, so this is a simplified capacity calculation.
A_ZH: 允许多个未确认分组同时在途。窗口为 N 时，理想利用率受 $\min(1,N(L/R)/(RTT+L/R))$ 限制。路径填满后，继续扩大窗口也不能超过链路容量。丢包、接收限制与拥塞会降低实际性能，因此这是简化容量计算。

@@ N162 | x02-transport | learn | XN3:50-55
Q_EN: What does Go-Back-N retransmit after a timeout?
Q_ZH: Go-Back-N 超时后会重传哪些分组？
A_EN: In the lecture's GBN sender, a timer tracks the oldest unacknowledged packet. On timeout, retransmit all outstanding packets from the window base through the most recently sent one. Cumulative ACK n confirms packets through n in this packet-number convention. Do not confuse that convention with TCP's next-byte acknowledgment.
A_ZH: 课件的 GBN 发送者为最早未确认分组计时；超时后，重传从窗口基序号到最近已发送分组之间的全部未确认分组。在该分组编号约定中，累计 ACK n 表示已收到包括 n 在内的所有前序分组，不要与 TCP 的“下一个字节”确认约定混淆。

@@ N163 | x02-transport | learn | XN3:53-55
Q_EN: How does the lecture's GBN receiver handle an out-of-order packet?
Q_ZH: 课件中的 GBN 接收者怎样处理乱序分组？
A_EN: It discards the out-of-order payload and repeats the ACK for the latest correctly received in-order packet. It only needs the next expected sequence number, rather than an out-of-order buffer. This keeps the receiver simple but can force retransmission of packets that physically arrived successfully.
A_ZH: 它丢弃乱序载荷，并重复确认最近正确按序收到的分组。接收者只需记录下一个期望序号，不需要乱序缓冲区。这使接收者简单，但也可能迫使发送者重传物理上已经成功到达过的分组。

@@ N164 | x02-transport | learn | XN3:56-59
Q_EN: How does Selective Repeat differ from GBN?
Q_ZH: Selective Repeat 与 GBN 有何区别？
A_EN: SR individually acknowledges correctly received packets, can buffer in-window out-of-order data, and retransmits specific unacknowledged packets when their timers expire. This saves retransmissions but needs more receiver state and careful window management. Delivery to the application remains ordered when that is the protocol's promised service.
A_ZH: SR 单独确认正确收到的分组，可缓存窗口内乱序数据，并在对应定时器超时后重传特定未确认分组。它减少重复发送，却需要更多接收状态和更谨慎的窗口管理。若协议承诺有序服务，向应用交付时仍需保持顺序。

@@ N165 | x02-transport | check | XN3:51-59; XNT5:2
Q_EN: Why must sender/receiver windows be limited relative to the sequence-number space?
Q_ZH: 为什么发送、接收窗口的大小要受序号空间限制？
A_EN: After sequence numbers wrap, a receiver must distinguish an old duplicate from new data. In the standard models with m-bit sequence numbers, GBN allows window size at most $2^m-1$, while equal-sized SR windows require at most $2^{m-1}$. These bounds depend on the protocol and its lifetime assumptions; “more sequence numbers than packets currently buffered” is not a complete argument.
A_ZH: 序号回绕后，接收者必须区分旧副本和新数据。在标准 m bit 序号模型中，GBN 窗口至多为 $2^m-1$，等大小的 SR 收发窗口至多为 $2^{m-1}$。这些界限依赖协议和分组寿命假设，不能只说“序号比当前缓存分组多”就算完整论证。

@@ N166 | x02-transport | worked | XN3:55-59
Q_EN: Packets 0,1,2,3 are sent and packet 1 is lost. Contrast the basic GBN and SR reactions.
Q_ZH: 发送了 0、1、2、3，分组 1 丢失，基础 GBN 和 SR 的处理有何不同？
A_EN: GBN accepts 0, discards later out-of-order 2 and 3, and eventually retransmits the outstanding sequence starting at 1. SR can acknowledge and buffer 2 and 3, then retransmit only 1 when needed. This comparison assumes no further loss and valid windows; actual timers and ACK arrival order determine the precise event timeline.
A_ZH: GBN 接收 0，丢弃随后乱序到达的 2、3，之后从 1 起重传未确认序列。SR 则可确认并缓存 2、3，在需要时只重传 1。这里假设没有额外丢包且窗口有效，实际定时器和 ACK 到达顺序决定精确事件时间线。

@@ N167 | x03-tcp | learn | XN3:61-64
Q_EN: What do TCP sequence and acknowledgment numbers count?
Q_ZH: TCP 的序号和确认号统计的是什么？
A_EN: A data segment's sequence number identifies its first byte in the stream. The acknowledgment number is the next byte expected, confirming all earlier bytes cumulatively. These are byte positions, not packet counts. SYN and FIN consume sequence space, while an ACK without data does not consume a new data byte.
A_ZH: 数据段序号标识其在字节流中的第一个字节；确认号表示下一个期望字节，对之前所有字节作累计确认。它们是字节位置，不是分组数量。SYN 和 FIN 消耗序号空间，而不带数据的 ACK 不会消耗新的数据字节。

@@ N168 | x03-tcp | worked | XN3:63-67
Q_EN: A segment starts at sequence 1,000 and carries 500 bytes. Assuming all earlier bytes arrived, what ACK follows?
Q_ZH: 数据段序号为 1,000，携带 500 byte，且之前字节均已到达，随后确认号是多少？
A_EN: The segment covers bytes 1,000 through 1,499, so the next expected byte and ACK number is 1,500. If another contiguous 200 bytes arrive, the ACK advances to 1,700. Do not add an extra one for ordinary payload beyond the payload byte count; the SYN/FIN rule is separate.
A_ZH: 该段覆盖 1,000 至 1,499 号字节，下一个期望字节、也就是 ACK 号为 1,500。若随后连续收到 200 byte，则 ACK 前进到 1,700。普通载荷按字节数累计，不要额外再加一；SYN/FIN 的规则另算。

@@ N169 | x03-tcp | worked | XN3:64,76-79
Q_EN: Bytes 0–535 and 900–1,000 have arrived, but the gap is missing. What is the cumulative TCP ACK?
Q_ZH: 已收到字节 0–535 和 900–1,000，中间缺口尚未补齐，TCP 累计 ACK 是多少？
A_EN: It remains 536, the first missing byte. Receiving a later segment does not make the gap disappear. A receiver may retain out-of-order data, and optional selective acknowledgments can describe additional received ranges, but the cumulative ACK still reports the first missing byte.
A_ZH: 仍为 536，即第一个缺失字节。收到后面的数据段不会让缺口消失。接收者可保留乱序数据，可选的选择性确认也可描述额外收到的范围，但累计 ACK 仍指出第一个缺失字节。

@@ N170 | x03-tcp | check | XN3:61,72-79
Q_EN: Can TCP deliver later application bytes while an earlier byte is still missing?
Q_ZH: TCP 的前面字节还缺失时，能先向应用交付后面的字节吗？
A_EN: The ordered stream service waits for the gap before delivering the later bytes as contiguous stream data. They may already be buffered at the receiver. This is transport-level head-of-line blocking. It differs from an input-queue packet blocking another router output, although both use the same broad phrase.
A_ZH: 有序字节流服务需要等待缺口补齐，才能把后续字节作为连续数据交给应用；这些字节可能已经缓存于接收端。这是传输层的队头阻塞，与路由器输入队列中一个分组挡住其他输出方向分组的情况不同，虽然两者使用类似名称。

@@ N171 | x03-tcp | learn | XN3:68-70
Q_EN: Why does a TCP retransmission timeout account for RTT variation as well as its average?
Q_ZH: TCP 重传超时为什么既要考虑平均 RTT，也要考虑波动？
A_EN: A timeout close to the mean can expire prematurely when delay fluctuates. The lecture model smooths samples into EstimatedRTT and adds a safety margin: RTO=EstimatedRTT+4 DevRTT. A longer timeout avoids some spurious retransmissions but slows recovery from actual loss. State the update order when computing both estimates from a new sample.
A_ZH: 延迟波动时，接近均值的超时值容易提前触发。课件模型平滑样本得到 EstimatedRTT，并加安全余量：RTO=EstimatedRTT+4 DevRTT。较长超时可减少误重传，却延缓真正丢包后的恢复。用新样本同时更新两个估计时，应说明更新顺序。

@@ N172 | x03-tcp | worked | XN3:69-70
Q_EN: TCP smooths RTT by new E=(1−alpha)old E+alpha×sample. With old E=100 ms, sample=140 ms and alpha=0.125, find new E. For this exercise keep DevRTT=10 ms fixed and use RTO=E+4DevRTT; find RTO.
Q_ZH: TCP 按新 E=(1−alpha)旧 E+alpha×样本平滑 RTT。旧 E=100 ms、样本 140 ms、alpha=0.125，求新 E。本题固定 DevRTT=10 ms，不再更新，按 RTO=E+4DevRTT 求 RTO。
A_EN: The estimate becomes $0.875(100)+0.125(140)=105$ ms. Using the separately given DevRTT=10 ms, RTO is $105+4(10)=145$ ms. This question holds DevRTT fixed at the supplied value; computing a new deviation estimate would require an additional formula and an update-order convention.
A_ZH: 新估计为 $0.875(100)+0.125(140)=105$ ms。使用题中另给的 DevRTT=10 ms，得到 RTO=$105+4(10)=145$ ms。本题直接使用给定偏差值；若要更新偏差，还需额外公式及更新顺序约定。

@@ N173 | x03-tcp | learn | XN3:78-79
Q_EN: Why can three duplicate ACKs trigger fast retransmit?
Q_ZH: 为什么三个重复 ACK 能触发快速重传？
A_EN: Later arrivals often cause repeated ACKs for a missing earlier byte. Three duplicates provide evidence that later data is getting through while a gap remains, allowing retransmission before a long timer expires. Reordering can also produce duplicates, so this is a protocol heuristic rather than certain proof of loss.
A_ZH: 后续数据到达时，接收者常重复确认同一个缺失字节。三个重复 ACK 表明后面的数据可能已通过而缺口仍在，使发送者可在较长定时器到期前重传。乱序也可能产生重复 ACK，因此这是一种协议判断规则，不是丢包的绝对证明。

@@ N174 | x03-tcp | learn | XN3:81-82,103
Q_EN: How do TCP flow control and congestion control differ?
Q_ZH: TCP 流量控制与拥塞控制有什么区别？
A_EN: Flow control protects the receiver's capacity to buffer and consume data, using its advertised receive window rwnd. Congestion control responds to network capacity and congestion, using sender state such as cwnd. A receiver can be fast while the path is congested, or slow while the path is free. Neither window can be ignored.
A_ZH: 流量控制保护接收者缓冲和消费数据的能力，使用其通告的接收窗口 rwnd。拥塞控制响应网络容量与拥塞，使用发送端的 cwnd 等状态。接收者可能很快而路径拥塞，也可能接收者很慢但路径空闲，因此不能忽略任何一个窗口。

@@ N175 | x03-tcp | worked | XN3:103-104
Q_EN: If cwnd=12 kB, rwnd=8 kB and 5 kB is unacknowledged, how much more data can the simplified window rule allow?
Q_ZH: 若 cwnd=12 kB、rwnd=8 kB，已有 5 kB 未确认，简化窗口规则还允许发送多少？
A_EN: The in-flight bound is $\min(12,8)=8$ kB, leaving 3 kB of window space. This ignores other constraints such as application availability, segment sizing and pacing. The receive window is not added to the congestion window; the tighter limit applies.
A_ZH: 在途上限为 $\min(12,8)=8$ kB，因此还剩 3 kB 窗口空间。这里忽略应用数据是否就绪、分段大小和发送节奏等限制。接收窗口不能与拥塞窗口相加，应采用较紧的限制。

@@ N176 | x03-tcp | learn | XN3:84-86
Q_EN: What does the TCP three-way handshake establish?
Q_ZH: TCP 三次握手建立哪些状态？
A_EN: It exchanges initial sequence numbers and confirms that both sides can participate in the connection. If the client sends SYN with sequence x, the server acknowledges x+1 and sends its own SYN with sequence y; the client acknowledges y+1. The SYNs consume sequence space. This handshake does not authenticate human identities.
A_ZH: 它交换初始序号，并确认双方能够参与连接。客户端以序号 x 发 SYN，服务器确认 x+1，并以序号 y 发送自己的 SYN；客户端再确认 y+1。SYN 消耗序号空间，但该握手并不认证人的身份。

@@ N177 | x03-tcp | learn | XN3:87-88
Q_EN: Why can TCP close its two directions separately, and what does TIME_WAIT help with?
Q_ZH: TCP 为什么可以分别关闭两个方向？TIME_WAIT 有什么作用？
A_EN: A FIN announces that one sender has no more stream data; the other direction can still operate until it closes too. FIN is acknowledged and consumes sequence space. TIME_WAIT allows handling a retransmitted FIN if the final ACK was lost, and helps keep old segments from interfering with a reused connection identity.
A_ZH: FIN 表示某一发送方不再发送字节流数据，另一方向在自己关闭前仍可工作。FIN 需要确认，也消耗序号空间。TIME_WAIT 使最终 ACK 丢失后仍可应对重传的 FIN，并有助于避免旧数据段干扰复用连接标识的新连接。

@@ N178 | x03-tcp | learn | XN3:105-109
Q_EN: In the lecture's classic TCP model, why is slow start called slow despite exponential window growth?
Q_ZH: 在课件的经典 TCP 模型中，窗口指数增长，为什么还称为慢启动？
A_EN: It starts from a small congestion window and probes capacity through ACKs. With one ACK per segment and no losses or limiting factors, the window roughly doubles per RTT. The lecture begins at 1 MSS for its teaching model; that is not a universal initial-window setting for every implementation.
A_ZH: 它从较小拥塞窗口开始，通过 ACK 探测容量。若每段得到一个 ACK，且没有丢包或其他限制，窗口每 RTT 近似翻倍。课件为教学模型设置初始 1 MSS，这不是所有实现统一使用的初始窗口值。

@@ N179 | x03-tcp | learn | XN3:102,108-109
Q_EN: How is additive increase different from slow-start growth?
Q_ZH: 加性增长与慢启动增长有何不同？
A_EN: Congestion avoidance increases cwnd by roughly one MSS per RTT, instead of roughly doubling it. If cwnd is measured in bytes, a common per-ACK increment is about $MSS^2/cwnd$. Losing track of units can turn that into the wrong formula. The classic AIMD picture also reduces the window multiplicatively after a congestion signal.
A_ZH: 拥塞避免阶段每 RTT 大约增加一个 MSS，而不是近似翻倍。若 cwnd 用 byte 表示，常见的逐 ACK 增量约为 $MSS^2/cwnd$，忽略单位会写错公式。经典 AIMD 图景还会在收到拥塞信号后按比例减小窗口。

@@ N180 | x03-tcp | learn | XN3:105-112
Q_EN: What main difference separates the lecture's TCP Tahoe and Reno loss reactions?
Q_ZH: 课件中 TCP Tahoe 与 Reno 遇到丢包时，主要反应差异是什么？
A_EN: In the classic model, Tahoe returns to slow start after loss detection. Reno uses fast retransmit and fast recovery after triple duplicate ACKs, avoiding a complete restart in that case. A timeout is treated more severely. These are named historical algorithms; do not label every modern TCP trace as Reno without knowing the implementation.
A_ZH: 在经典模型中，Tahoe 在检测到丢包后返回慢启动。Reno 遇到三个重复 ACK 时采用快速重传与快速恢复，避免在该情形下完全重新启动，而超时会触发更强反应。这些是特定历史算法，未确认实现前不能把所有现代 TCP 轨迹都当成 Reno。

@@ N181 | x03-tcp | learn | XN3:111-112
Q_EN: Why does classic Reno temporarily use ssthresh plus three MSS in fast recovery?
Q_ZH: 经典 Reno 快速恢复时，为什么暂时使用 ssthresh 加三个 MSS？
A_EN: Three duplicate ACKs suggest three later segments have left the network and reached the receiver. Reno accounts for them by temporarily inflating cwnd after setting a reduced threshold. Further duplicate ACKs can allow more sending; a suitable new ACK ends recovery and deflates the window. The exact transition depends on the Reno variant and ACK event.
A_ZH: 三个重复 ACK 表明可能有三个后续数据段已离开网络并到达接收者。Reno 在降低阈值后，通过暂时膨胀 cwnd 反映这些离网数据。更多重复 ACK 可允许继续发送，适当的新 ACK 则结束恢复并缩减窗口。具体转移取决于 Reno 版本与 ACK 事件。

@@ N182 | x03-tcp | worked | XN3:114
Q_EN: In an ideal AIMD model, the congestion window rises linearly from W/2 to maximum W, with constant RTT and no timeout periods. If W=64 kB and RTT=0.1 s, estimate the mean throughput using decimal units.
Q_ZH: 理想 AIMD 模型中，拥塞窗口从 W/2 线性增加到最大 W，RTT 固定且忽略超时阶段。若 W=64 kB、RTT=0.1 s，按十进制单位估计平均吞吐量。
A_EN: Average window is $(3/4)W=48$ kB, so throughput is 480 kB/s, or 3.84 Mbit/s with decimal units. This model assumes a roughly linear sawtooth between W/2 and W, fixed RTT, continuous data and negligible slow-start time. Variable delay, timeouts or application limits can invalidate the estimate.
A_ZH: 平均窗口为 $(3/4)W=48$ kB，因此吞吐量为 480 kB/s，按十进制单位即 3.84 Mbit/s。模型假设窗口在 W/2 与 W 之间近似线性变化、RTT 固定、数据持续可用且忽略慢启动时间。变动时延、超时或应用限制都可能使估计失效。

@@ N183 | x03-tcp | check | XN3:115-117
Q_EN: Why is per-connection TCP fairness not automatically per-user fairness?
Q_ZH: 为什么每条 TCP 连接公平，不自动等于每个用户公平？
A_EN: One user can open several competing connections and receive several shares. Fairness also depends on RTTs, algorithms, loss and other traffic. The equal R/K sharing picture is an idealized comparison for K similar flows, not a universal service guarantee or a rule that every application receives equal bandwidth.
A_ZH: 一个用户可开启多条竞争连接，从而获得多个份额。公平性还受 RTT、算法、丢包及其他流量影响。R/K 平分图景是 K 条相似流的理想化比较，不是通用服务保证，也不意味着每个应用必定得到相同带宽。

@@ N184 | x03-tcp | learn | XN3:90-100,113
Q_EN: How can ECN signal congestion without requiring a packet drop?
Q_ZH: ECN 怎样在不必丢弃分组的情况下指示拥塞？
A_EN: A capable network device can mark congestion in an ECN-capable packet, and endpoints communicate and respond to that signal. This can avoid waiting for loss as the only indication. Congestion still costs queueing delay and capacity, and repeated unnecessary retransmissions add load rather than creating more useful throughput.
A_ZH: 支持 ECN 的网络设备可在允许 ECN 的分组中标记拥塞，端点再传递并响应该信号，从而不必只等丢包才发现问题。拥塞仍会带来排队延迟和容量损失，反复进行不必要重传只会增加负载，不会创造更多有效吞吐量。

@@ N185 | x04-ip | learn | XN4:5-8,13-14
Q_EN: How do forwarding, routing, the data plane and control plane relate?
Q_ZH: 转发、路由、数据平面与控制平面之间是什么关系？
A_EN: Forwarding applies local rules to an arriving packet, such as choosing an output port. Routing determines paths and the information used to build those rules. Forwarding is a data-plane action; route computation and rule distribution belong to the control plane. A logically centralized SDN controller can still have a distributed physical implementation.
A_ZH: 转发对到达分组应用本地规则，例如选择输出端口；路由决定路径以及构建规则所需的信息。转发属于数据平面，路由计算和规则分发属于控制平面。SDN 控制器在逻辑上集中，并不意味着物理上只能用一台机器实现。

@@ N186 | x04-ip | learn | XN4:15-16,48
Q_EN: Why does IP forwarding use longest-prefix matching?
Q_ZH: IP 转发为什么使用最长前缀匹配？
A_EN: Several routes can match one destination. The longest matching prefix describes the most specific address range, so it wins over a broader aggregate or default route. Prefix length, not row order or smallest numerical address, is the basic selection criterion in this model. Ties and policy require additional rules.
A_ZH: 同一目的地址可能匹配多条路由，最长匹配前缀描述最具体的地址范围，因此优先于较宽的聚合路由或默认路由。在该模型中，基本标准是前缀长度，不是表格行顺序或地址数值最小；平局与策略还需要额外规则。

@@ N187 | x04-ip | worked | XN4:16,48
Q_EN: Routes are 10.0.0.0/8→A, 10.1.0.0/16→B and 10.1.2.0/24→C. Where does 10.1.2.99 go?
Q_ZH: 路由为 10.0.0.0/8→A、10.1.0.0/16→B、10.1.2.0/24→C，10.1.2.99 应走哪一条？
A_EN: It matches all three prefixes, but /24 is longest, so choose C. Destination 10.1.3.99 instead matches /8 and /16, so choose B. Compare network-prefix bits rather than just checking whether a decimal string begins with similar characters.
A_ZH: 它匹配三条前缀，其中 /24 最长，因此选择 C。若目的为 10.1.3.99，则匹配 /8 和 /16，选择 B。应比较网络前缀的二进制位，而不是只检查十进制字符串看起来是否相似。

@@ N188 | x04-ip | learn | XN4:17-20
Q_EN: What is head-of-line blocking in a router's input queue?
Q_ZH: 路由器输入队列中的队头阻塞是什么？
A_EN: The first queued packet may wait for a busy output, preventing later packets from reaching other available outputs. This can waste switching capacity even though those later packets could otherwise advance. Input buffering and output buffering create different bottlenecks; a fast external link does not eliminate internal contention.
A_ZH: 队首分组可能等待繁忙输出端口，使后面本可前往空闲输出端口的分组也无法前进，从而浪费交换能力。输入缓冲与输出缓冲存在不同瓶颈，外部链路快并不能消除内部竞争。

@@ N189 | x04-ip | learn | XN4:23
Q_EN: What are IPv4 header length, total length, TTL and protocol fields used for?
Q_ZH: IPv4 的首部长度、总长度、TTL 和 protocol 字段分别做什么？
A_EN: Header length locates where payload starts; the IHL field counts 32-bit words. Total length counts the entire IP datagram in bytes. TTL limits forwarding lifetime in hops. Protocol identifies the payload's next protocol, such as TCP or UDP. These fields describe different layers of interpretation and use different units.
A_ZH: 首部长度用于确定载荷起点，IHL 以 32 bit 字为单位；总长度按 byte 统计完整 IP 数据报。TTL 限制经过的转发跳数，protocol 标识载荷中的下一层协议，如 TCP 或 UDP。这些字段的含义与单位不同。

@@ N190 | x04-ip | worked | XN4:23-25
Q_EN: An IPv4 datagram has IHL=5 and total length 1,500 bytes. How many bytes remain after the IP header?
Q_ZH: IPv4 数据报 IHL=5，总长度 1,500 byte，IP 首部之后剩多少字节？
A_EN: The IP header is $5\times4=20$ bytes, leaving 1,480 bytes of IP payload. That payload can include a transport header, so it is not automatically 1,480 bytes of application data. If a basic 20-byte TCP header is present with no options, the application payload would be 1,460 bytes.
A_ZH: IP 首部为 $5\times4=20$ byte，剩余 IP 载荷为 1,480 byte。但其中还可包含传输层首部，不自动等于 1,480 byte 应用数据。若包含无选项的基本 20 byte TCP 首部，则应用载荷为 1,460 byte。

@@ N191 | x04-ip | learn | XN4:24-26
Q_EN: What is IPv4 fragmentation, and what does link MTU constrain?
Q_ZH: 什么是 IPv4 分片？链路 MTU 限制什么？
A_EN: When permitted, an oversized IPv4 datagram can be split into smaller IP fragments, each with its own IP header. MTU limits the IP packet carried by the link, rather than including every link-layer framing byte. Fragment offsets count units of 8 payload bytes. Reassembly occurs at the final IP destination, using identification and offset information.
A_ZH: 在允许分片时，过大的 IPv4 数据报可拆成更小的 IP 分片，每片都有自己的 IP 首部。MTU 限制链路承载的 IP 包大小，并非包含所有链路层封装字节。分片偏移以 8 个载荷字节为单位，最终 IP 目的端利用标识和偏移信息重组。

@@ N192 | x04-ip | worked | XN4:25
Q_EN: Fragment a 4,000-byte IPv4 datagram over MTU 1,500, assuming a 20-byte header and fragmentation allowed.
Q_ZH: 4,000 byte IPv4 数据报经过 MTU 1,500 的链路，假设首部 20 byte 且允许分片，结果是什么？
A_EN: Original payload is 3,980 bytes. Use payloads 1,480, 1,480 and 1,020 bytes, giving total fragment lengths 1,500, 1,500 and 1,040. Offsets are 0, 185 and 370 because offsets use 8-byte units. More-fragments flags are 1,1,0, and identification is shared. Do not divide total fragment length by 8 to compute offsets.
A_ZH: 原载荷为 3,980 byte，分成 1,480、1,480、1,020 byte，片总长度分别为 1,500、1,500、1,040。偏移按 8 byte 计，为 0、185、370；更多分片标志为 1、1、0，并共享同一标识。计算偏移时，不能用包含首部的片总长度除以 8。

@@ N193 | x04-ip | learn | XN4:28-34
Q_EN: Does an IP address identify an entire physical device in all circumstances?
Q_ZH: IP 地址在所有情况下都标识整个物理设备吗？
A_EN: More precisely, IP addresses are associated with network interfaces or logical endpoints. A router typically has addresses on multiple interfaces, and one device can have several addresses. Subnet prefixes identify address ranges. Avoid assuming a permanent one-to-one mapping among an IP address, a physical machine and a human user.
A_ZH: 更准确地说，IP 地址关联网络接口或逻辑端点。路由器通常在多个接口上有地址，同一设备也可拥有多个地址。子网前缀标识地址范围，不能假设 IP、物理机器和人之间永久一一对应。

@@ N194 | x04-ip | learn | XN4:29-34
Q_EN: What does an IPv4 prefix such as /26 mean?
Q_ZH: IPv4 中的 /26 这类前缀是什么意思？
A_EN: The first 26 bits specify the network prefix, leaving 6 host bits and $2^6=64$ addresses in the block. A matching mask has 26 leading ones. The network address is obtained by bitwise AND with the mask, not by decimal rounding. CIDR prefixes replace the fixed class A/B/C boundary assumption.
A_ZH: 前 26 bit 是网络前缀，剩余 6 bit 为主机部分，地址块包含 $2^6=64$ 个地址，对应掩码前 26 bit 为 1。网络地址通过与掩码按位 AND 得到，不能进行十进制四舍五入。CIDR 不再假设固定 A/B/C 类边界。

@@ N195 | x04-ip | worked | XN4:30-34
Q_EN: Find the network and broadcast addresses for 192.0.2.130/26 in an ordinary IPv4 subnet.
Q_ZH: 普通 IPv4 子网中的 192.0.2.130/26，其网络地址和广播地址是什么？
A_EN: /26 gives mask 255.255.255.192 and blocks of 64 last-octet addresses. The containing block is 128–191, so the network is 192.0.2.128 and broadcast is 192.0.2.191. Under ordinary subnet conventions, usable host addresses run from .129 through .190, totaling 62.
A_ZH: /26 对应 255.255.255.192，末字节每 64 个地址形成一块。130 位于 128–191 块，因此网络地址为 192.0.2.128，广播地址为 192.0.2.191。按普通子网约定，可用主机地址为 .129 至 .190，共 62 个。

@@ N196 | x04-ip | check | XN4:29-34
Q_EN: Is $2^{32-p}-2$ a universal IPv4 host-count formula?
Q_ZH: $2^{32-p}-2$ 是普遍适用的 IPv4 主机数公式吗？
A_EN: No. It describes ordinary subnets that reserve network and broadcast addresses. Special uses such as /31 point-to-point links and /32 host routes require different interpretation. First compute block size, then apply the addressing convention requested by the problem. A prefix length by itself is not a promise of that many usable interfaces.
A_ZH: 不是。该公式用于保留网络地址和广播地址的普通子网；/31 点对点链路、/32 主机路由等特殊用途需要不同解释。应先算地址块大小，再采用题目要求的地址约定，前缀长度本身不保证某个可用接口数量。

@@ N197 | x04-ip | learn | XN4:35-43
Q_EN: What configuration can DHCP supply besides an IP address?
Q_ZH: DHCP 除 IP 地址外，还能提供哪些配置？
A_EN: It can provide a subnet mask, default-router address, DNS-server information and lease timing. The familiar discover–offer–request–acknowledge exchange establishes a configuration lease. A default router is the next hop for off-subnet traffic; a DNS server resolves names. They serve different roles even if one device provides both services.
A_ZH: 它可提供子网掩码、默认路由器、DNS 服务器信息及租约时间。常见的 discover–offer–request–acknowledge 流程建立配置租约。默认路由器是外部子网流量的下一跳，DNS 服务器负责名称解析，即使同一设备提供两者，角色也不同。

@@ N198 | x04-ip | learn | XN4:44-48
Q_EN: Why does route aggregation help scalability, and when can two prefixes be aggregated exactly?
Q_ZH: 路由聚合为何有助于扩展性？两个前缀何时能精确聚合？
A_EN: An aggregate can advertise one aligned contiguous address block instead of several smaller entries. Two equal-length neighboring prefixes combine only when they share the proper parent-prefix boundary. For example, 192.0.2.0/25 and 192.0.2.128/25 combine into 192.0.2.0/24. Merely being numerically close is insufficient.
A_ZH: 聚合可用一个对齐的连续地址块替代多条较小前缀。两个等长相邻前缀只有满足共同父前缀边界时才能合并，例如 192.0.2.0/25 与 192.0.2.128/25 合成 192.0.2.0/24。仅仅地址数值接近并不充分。

@@ N199 | x04-ip | learn | XN4:50-55
Q_EN: How does the lecture's address-and-port NAT allow several internal hosts to share an external address?
Q_ZH: 课件中的地址与端口转换 NAT，如何让多个内部主机共享外部地址？
A_EN: The gateway maintains mappings between internal address/port pairs and externally used address/port information. Outbound packets are rewritten, and replies are mapped back to the appropriate internal endpoint. This common NAPT form changes transport-related fields as well as addresses. Basic address-only NAT is a different case.
A_ZH: 网关维护内部地址/端口与外部使用的地址/端口信息之间的映射，改写外发分组，并把回复映射回相应内部端点。这种常见 NAPT 形式既改地址，也改传输层相关字段；仅做地址转换的基本 NAT 是另一种情况。

@@ N200 | x04-ip | check | XN4:53-55
Q_EN: Why should the slide's “about 60,000 NAT connections” not be treated as a universal capacity guarantee?
Q_ZH: 为什么不能把课件中“约 60,000 条 NAT 连接”当作通用容量保证？
A_EN: A 16-bit port field offers a finite identifier space, but actual mappings depend on transport protocol, destination tuples, port-reuse rules, timeouts and device resources. NAT can also complicate unsolicited inbound connections and peer-to-peer reachability. Counting port values alone does not fully characterize a gateway's usable connection capacity.
A_ZH: 16 bit 端口提供有限标识空间，但实际映射取决于传输协议、目的端元组、端口复用规则、超时及设备资源。NAT 还可能增加主动入站连接与 P2P 可达性的复杂度，仅数端口值不能完整描述网关可用连接容量。

@@ N201 | x04-ip | learn | XN4:57-60; XIP6:3-5
Q_EN: What major IPv6 changes matter when comparing packet headers and fragmentation?
Q_ZH: 比较包首部与分片时，IPv6 的哪些变化最重要？
A_EN: IPv6 uses 128-bit addresses and a 40-byte base header, with extension headers when needed. Routers do not fragment forwarded IPv6 packets; the source must handle packet-size limits, potentially using fragmentation at the source. Hop Limit replaces IPv4's TTL field. Do not infer that all IPv6 packets are only 40 bytes long.
A_ZH: IPv6 使用 128 bit 地址和 40 byte 基本首部，需要时再加入扩展首部。路由器不对转发中的 IPv6 包分片，源端必须处理路径包长限制，并可在源端进行分片。Hop Limit 对应 IPv4 的 TTL 功能，不能据此认为所有 IPv6 包总长只有 40 byte。

@@ N202 | x04-ip | learn | XN4:61-63
Q_EN: What happens when an IPv6 packet crosses an IPv4 tunnel?
Q_ZH: IPv6 包穿过 IPv4 隧道时会发生什么？
A_EN: The tunnel entrance encapsulates the IPv6 packet inside an IPv4 packet. IPv4 routers forward using the outer header; the tunnel exit removes that header and continues IPv6 forwarding. Encapsulation adds overhead and can affect effective MTU. It does not mean intermediate IPv4 routers interpret the inner packet as native IPv6 traffic.
A_ZH: 隧道入口把 IPv6 包封装进 IPv4 包，IPv4 路由器根据外层首部转发，出口去掉外层首部后继续 IPv6 转发。封装会增加开销，并影响有效 MTU。这不意味着中间 IPv4 路由器把内层包当作原生 IPv6 流量处理。

@@ N203 | x05-routing | learn | XN5:9-13,19-23
Q_EN: How do link-state and distance-vector routing differ in the information exchanged?
Q_ZH: 链路状态与距离向量路由，交换的信息有什么区别？
A_EN: Link-state routers distribute information about links and build a topology view for path computation. Distance-vector routers exchange current distance estimates with neighbors and improve routes using those estimates. The distinction is about available information and update procedures, not simply “one is centralized and one never communicates.”
A_ZH: 链路状态路由传播链路信息，建立拓扑视图后计算路径；距离向量路由与邻居交换当前距离估计，并利用这些估计改善路由。区别在于掌握的信息和更新过程，不应简单理解为“一种集中，另一种不通信”。

@@ N204 | x05-routing | learn | XN5:13-17; XND:1-7
Q_EN: What is the main invariant behind Dijkstra's shortest-path algorithm?
Q_ZH: Dijkstra 最短路算法的核心不变量是什么？
A_EN: With nonnegative link costs, repeatedly finalize the unvisited node with smallest tentative distance, then relax its outgoing edges. Once finalized, that distance cannot be improved through a longer unfinished route. Maintain predecessor or next-hop information for reconstruction. Negative costs invalidate the usual finalization argument.
A_ZH: 在链路代价非负时，反复确定尚未访问节点中暂定距离最小者，再松弛它的出边。一旦确定，该距离不能再通过更长的未完成路径改善。还需保存前驱或下一跳信息以重构路径；负代价会破坏通常的确定性论证。

@@ N205 | x05-routing | worked | XN5:13-17
Q_EN: Undirected edges are A-B=2, A-C=5, B-C=1, B-D=4, C-D=1. Find shortest distances and the path from A to D.
Q_ZH: 无向边为 A-B=2、A-C=5、B-C=1、B-D=4、C-D=1，求从 A 出发的最短距离及到 D 的路径。
A_EN: Initialize B=2 and C=5. Finalizing B improves C to 3 and D to 6. Finalizing C improves D to 4. Distances to A,B,C,D are (0,2,3,4), and the path to D is A-B-C-D. The first-hop forwarding entry for D is B, not D's predecessor C.
A_ZH: 初始化 B=2、C=5；确定 B 后，C 改为 3，D 改为 6；确定 C 后，D 改为 4。到 A、B、C、D 的距离为 (0,2,3,4)，到 D 的路径为 A-B-C-D。A 转发给 D 的第一跳是 B，不是 D 的前驱 C。

@@ N206 | x05-routing | check | XN5:15-16
Q_EN: Why is a shortest-path predecessor not always the next hop in a forwarding table?
Q_ZH: 最短路径中的前驱，为什么不总是转发表中的下一跳？
A_EN: A predecessor records the node immediately before a destination on a reconstructed path. The forwarding next hop is the first neighbor after the source router. For path A-B-C-D, D's predecessor is C, but A must forward toward B. Follow the predecessor chain back to the source before extracting its first hop.
A_ZH: 前驱记录重构路径中紧邻目的节点之前的节点；转发下一跳则是源路由器之后的第一个邻居。在 A-B-C-D 中，D 的前驱是 C，但 A 应转发给 B。应沿前驱链回溯到源，再取第一跳。

@@ N207 | x05-routing | learn | XN5:19-23
Q_EN: What does the Bellman-Ford equation mean for routing from x to y?
Q_ZH: 从 x 到 y 路由时，Bellman-Ford 方程表示什么？
A_EN: It states $D_x(y)=\min_v\{c(x,v)+D_v(y)\}$ over neighbors v. A route first pays for reaching a neighbor, then adds that neighbor's estimated remaining distance. Updates are meaningful only with consistent destination and cost conventions. A neighbor's advertised distance is not the cost of the first link.
A_ZH: 方程为 $D_x(y)=\min_v\{c(x,v)+D_v(y)\}$，其中 v 遍历邻居。路径先付出到邻居的链路代价，再加该邻居估计的剩余距离。目的节点与代价约定必须一致，邻居通告的距离并不是第一条链路本身的代价。

@@ N208 | x05-routing | worked | XN5:19-20
Q_EN: Neighbor A costs 2 to reach and advertises distance 6 to Z; neighbor B costs 5 and advertises 1. Which route is cheaper?
Q_ZH: 到邻居 A 的代价为 2，A 通告到 Z 距离为 6；到 B 的代价为 5，B 通告为 1，应选哪条路线？
A_EN: Via A costs 2+6=8; via B costs 5+1=6. Choose B with total distance 6. Choosing A merely because its first link is cheaper ignores the remainder of the path. If advertisements become stale after a failure, the calculation may temporarily use incorrect information.
A_ZH: 经 A 的总代价为 2+6=8，经 B 为 5+1=6，因此选 B，总距离为 6。仅因第一条链路便宜而选 A，会忽略剩余路径。若故障后通告过期，该计算可能暂时使用错误信息。

@@ N209 | x05-routing | learn | XN5:26-28
Q_EN: What is the distance-vector count-to-infinity problem?
Q_ZH: 距离向量路由中的计数到无穷问题是什么？
A_EN: After a route fails, neighbors may incorrectly believe that each other still has a path, repeatedly increasing their advertised distances through a loop. Good news about a shorter path can propagate quickly, while bad news may converge slowly. Loop-mitigation techniques help in particular settings, but do not make all asynchronous failures disappear.
A_ZH: 某路由失效后，邻居可能误以为对方仍有路径，在循环依赖中反复提高通告距离。较短路径的好消息可能传播很快，坏消息却可能缓慢收敛。避免环路的技术可改善特定情况，但不会消除所有异步故障。

@@ N210 | x05-routing | learn | XN5:30-33
Q_EN: Why is Internet routing organized into autonomous systems?
Q_ZH: 互联网路由为什么组织为自治系统？
A_EN: An AS groups networks under a routing administration. Intra-AS routing handles internal paths, while inter-AS routing exchanges reachability and policy between administrations. Hierarchy improves scalability and allows administrative choices. A route that is attractive within one AS need not satisfy another AS's business or traffic policy.
A_ZH: AS 将网络组织在同一套路由管理之下。域内路由处理内部路径，域间路由在不同管理方之间交换可达性与策略。层级结构改善扩展性，也容纳管理决策。在某 AS 内有吸引力的路径，不一定符合其他 AS 的业务或流量策略。

@@ N211 | x05-routing | learn | XN5:33-36
Q_EN: What kind of routing protocol is OSPF?
Q_ZH: OSPF 属于哪种路由协议？
A_EN: OSPF is an intra-AS link-state protocol. Routers distribute link-state information and compute shortest paths using configured costs. Areas and a backbone provide hierarchy in larger deployments. A link's configured cost is a routing metric; it need not equal its measured propagation delay.
A_ZH: OSPF 是域内链路状态协议。路由器传播链路状态，并按配置的代价计算最短路径；较大部署可使用区域与骨干层级。链路配置代价是一种路由指标，并不必须等于测得的传播时延。

@@ N212 | x05-routing | learn | XN5:38-48
Q_EN: Why is BGP not simply “Dijkstra over the entire Internet”?
Q_ZH: 为什么 BGP 不能简单理解为“对整个互联网运行 Dijkstra”？
A_EN: BGP advertises prefix reachability with path attributes and selects routes according to policy as well as path information. A preferred route need not minimize hop count or delay. Local preference, AS path and next-hop reachability serve different purposes. Interdomain routing must respect administrative relationships, not one universally shared scalar cost.
A_ZH: BGP 通告带路径属性的前缀可达性，并结合策略与路径信息选择路由。优选路由不必使跳数或时延最小。本地优先级、AS 路径及下一跳可达性有不同作用，域间路由需要尊重管理关系，并非只优化一个全网统一的标量代价。

@@ N213 | x05-routing | learn | XN5:41-46
Q_EN: What information does the BGP AS-PATH carry, and how does it help avoid loops?
Q_ZH: BGP 的 AS-PATH 携带什么信息？怎样帮助避免环路？
A_EN: It records autonomous systems on an advertised AS-level path. An AS can reject a route containing its own AS number, detecting an AS-level loop. This is not a list of every physical router or an exact latency measurement. Path attributes influence selection, but policy can prefer a longer AS path.
A_ZH: 它记录通告路径所经过的自治系统。AS 可拒绝包含自身 AS 号的路由，从而检测 AS 层级环路。这不是每台物理路由器的列表，也不是精确时延测量。路径属性影响选择，但策略仍可能偏好更长的 AS 路径。

@@ N214 | x05-routing | learn | XN5:39-45
Q_EN: How do eBGP and iBGP differ?
Q_ZH: eBGP 与 iBGP 有什么区别？
A_EN: eBGP exchanges BGP information between autonomous systems; iBGP distributes BGP information within an AS. Internal forwarding still needs a way to reach the selected next hop, often supplied by the intra-AS routing system. Receiving a BGP advertisement is not the same event as forwarding a data packet along the final path.
A_ZH: eBGP 在自治系统之间交换 BGP 信息，iBGP 则在同一 AS 内传播 BGP 信息。内部转发仍需知道怎样到达选定下一跳，这常由域内路由提供。收到 BGP 通告，与沿最终路径转发数据分组，是不同事件。

@@ N215 | x05-routing | learn | XN5:46-48
Q_EN: What is hot-potato routing?
Q_ZH: 什么是热土豆路由？
A_EN: When suitable external routes are available through multiple exits, an AS can prefer the exit with the lowest internal cost, handing traffic off sooner. This minimizes a local cost and may not minimize total end-to-end distance or latency. Apply it only after the relevant policy comparisons, not as the entire BGP selection rule.
A_ZH: 若多个出口都有适当外部路由，AS 可以选择内部代价最低的出口，尽快交出流量。它优化本地代价，不一定优化端到端总距离或时延。应在相关策略比较之后使用，不能把它当成完整 BGP 选路规则。

@@ N216 | x05-routing | learn | XN5:50-53
Q_EN: How does the lecture's UDP traceroute use ICMP?
Q_ZH: 课件中的 UDP traceroute 如何利用 ICMP？
A_EN: Probes use increasing TTL values. A router where TTL expires can return ICMP Time Exceeded, revealing that hop. At the destination, a probe to an unused UDP port can elicit Port Unreachable. ICMP carries control/error information inside IP; it does not itself guarantee that probes or replies arrive. Other traceroute variants use different probe protocols.
A_ZH: 探测包使用逐渐增大的 TTL。TTL 到期的路由器可返回 ICMP Time Exceeded，从而显示该跳。到达目的端后，发往未使用 UDP 端口的探测可触发 Port Unreachable。ICMP 在 IP 内承载控制或错误信息，并不保证探测和回复一定到达；其他 traceroute 版本可采用不同协议。

@@ N217 | x06-link | learn | XN6:4-9
Q_EN: How is link-layer delivery different from end-to-end network-layer delivery?
Q_ZH: 链路层交付与端到端网络层交付有什么区别？
A_EN: The link layer transfers a frame across one link between adjacent nodes. An IP datagram can traverse several links using different frame formats on the way to its destination. A router removes one link's framing and applies the next link's framing. Link-local mechanisms do not automatically provide an end-to-end reliability guarantee.
A_ZH: 链路层把帧跨一个链路传给相邻节点。IP 数据报到达目的地前可经过多个链路，并采用不同帧格式。路由器移除上一链路封装，再加入下一链路封装。链路局部机制不自动构成端到端可靠性保证。

@@ N218 | x06-link | learn | XN6:6-9
Q_EN: What services may a link layer provide?
Q_ZH: 链路层可以提供哪些服务？
A_EN: Framing, medium access, error detection, and sometimes correction, local retransmission or flow control. Different link technologies provide different subsets. A frame typically encapsulates an IP datagram with link-specific header/trailer information. Always distinguish an offered link service from a service required of every possible link protocol.
A_ZH: 可包括成帧、介质访问、检错，有时还包括纠错、局部重传或流量控制。不同链路技术提供的子集不同。帧通常为 IP 数据报增加链路专用首部和尾部，必须区分某协议提供的服务与所有链路协议都必须提供的服务。

@@ N219 | x06-link | learn | XN6:11-14
Q_EN: What is the difference between detecting an error and correcting it?
Q_ZH: 检测错误与纠正错误有什么区别？
A_EN: Detection indicates that a received pattern is inconsistent with a valid codeword. Correction additionally identifies the intended data within the code's capability. More redundancy can support stronger guarantees, but no finite code corrects arbitrary corruption without assumptions. State which error patterns a scheme is designed to handle.
A_ZH: 检错表示接收模式与合法码字不一致；纠错还要在编码能力范围内确定原始数据。更多冗余可支持更强保证，但没有有限编码能在不加假设时纠正任意损坏。应说明方案要处理哪些错误模式。

@@ N220 | x06-link | worked | XN6:12
Q_EN: Data bits are 1011001. What even-parity bit is appended, and can this detect every two-bit error?
Q_ZH: 数据为 1011001，追加什么偶校验位？它能检测所有两位错误吗？
A_EN: There are four ones, already even, so append 0. A single flipped bit changes parity and is detected. Two flipped bits preserve overall parity, so ordinary single-bit parity does not detect that pattern. “Even parity” concerns the total ones count including the parity bit.
A_ZH: 数据中有四个 1，已是偶数，因此追加 0。单个位翻转会改变奇偶性并被检测，两位翻转则保持整体奇偶性，普通单校验位无法检测这种模式。“偶校验”统计的是包含校验位在内的 1 的总数。

@@ N221 | x06-link | learn | XN6:12; XNT11:1
Q_EN: How can two-dimensional parity locate one flipped data bit?
Q_ZH: 二维奇偶校验怎样定位一个翻转的数据位？
A_EN: Arrange data in rows and columns and include parity checks for both. A single data-bit error makes its row and column fail, and their intersection locates the bit. More complex patterns, such as four flipped corners of a rectangle, can preserve every row and column parity. Correction is therefore conditional on the assumed error pattern.
A_ZH: 将数据按行列排列，并分别加入行、列校验。单个数据位出错时，对应一行和一列都会失败，其交点即可定位错误。但矩形四个角同时翻转等复杂模式可使所有行列奇偶性保持不变，因此纠错能力取决于所假设的错误模式。

@@ N222 | x06-link | learn | XN6:14-16
Q_EN: How does CRC interpret a bit string and a generator?
Q_ZH: CRC 如何解释位串与生成多项式？
A_EN: Treat bits as polynomial coefficients over GF(2). Addition/subtraction is XOR, with no arithmetic carry. A generator of degree r defines r check bits. The sender chooses a remainder so the transmitted polynomial is divisible by the generator. This is polynomial division, not ordinary integer division with decimal remainders.
A_ZH: 将位串视为 GF(2) 上的多项式系数，加减法是 XOR，没有普通算术进位。r 次生成多项式对应 r 个校验位。发送者选择余数，使发送多项式可被生成多项式整除。这是多项式除法，不是带十进制余数的普通整数除法。

@@ N223 | x06-link | learn | XN6:14-16
Q_EN: What are the CRC encoding and checking steps?
Q_ZH: CRC 编码与检查的步骤是什么？
A_EN: Append r zeros to data D, divide by generator G using XOR, and append the r-bit remainder R to the original data. The transmitted word is $D2^r\oplus R$. The receiver divides the full received word by G. A nonzero remainder detects an error; a zero remainder cannot rule out all possible corruption.
A_ZH: 先给 D 追加 r 个零，用 XOR 对 G 做除法，再把 r bit 余数 R 接到原数据后，发送字为 $D2^r\oplus R$。接收者用 G 除完整接收字。余数非零表示检测到错误，余数为零则不能排除所有可能损坏。

@@ N224 | x06-link | worked | XN6:14-16
Q_EN: Encode data 1101 with CRC generator 1011.
Q_ZH: 使用 CRC 生成式 1011 对数据 1101 编码。
A_EN: G has degree 3, so divide 1101000 by 1011 using XOR. The remainder is 001, and the transmitted word is 1101001. Dividing that complete word by 1011 yields zero remainder. Preserve leading zeros in the remainder so the check field has exactly three bits.
A_ZH: G 的次数为 3，因此用 XOR 将 1101000 除以 1011，余数为 001，发送字为 1101001。完整发送字再除以 1011，余数为零。余数开头的零不能省略，校验字段必须恰好有三位。

@@ N225 | x06-link | check | XN6:11,14-16; XNA3:1
Q_EN: Does an r-bit CRC mean “any r erroneous bits can be corrected”?
Q_ZH: r bit CRC 是否意味着“任意 r 个错误位都能纠正”？
A_EN: No. CRC is primarily an error-detection scheme. Its guarantees depend on the generator and error structure, such as burst length, rather than a generic correction count equal to r. A zero syndrome can occur when the error polynomial is itself divisible by G. Detection and correction must not be conflated.
A_ZH: 不是，CRC 主要是检错方案。保证取决于生成式以及突发长度等错误结构，并不等于能纠正 r 个任意错误位。若错误多项式本身可被 G 整除，余式仍可能为零。检错与纠错不能混为一谈。

@@ N226 | x06-link | learn | XN6:18-24
Q_EN: What problem do multiple-access protocols solve on a shared link?
Q_ZH: 多路访问协议在共享链路上解决什么问题？
A_EN: They coordinate which node can transmit when several nodes share one medium. Broad approaches include partitioning resources, random access and taking turns. A collision concerns overlapping uses of that shared resource. It differs from queue overflow, which can occur even on a point-to-point link when arrivals exceed service capacity.
A_ZH: 多节点共享同一介质时，它们协调谁在何时发送。基本方法包括资源划分、随机接入和轮流访问。碰撞涉及共享资源上的重叠使用，与队列溢出不同；即使点对点链路，只要到达速度超过服务能力，也可能发生溢出。

@@ N227 | x06-link | learn | XN6:21-24
Q_EN: What tradeoff separates TDMA/FDMA from random access?
Q_ZH: TDMA/FDMA 与随机接入各有什么取舍？
A_EN: Partitioning gives nodes separate time slots or frequency bands, avoiding simultaneous interference under the model but potentially leaving allocated capacity idle. Random access lets an active node use the channel without a fixed exclusive allocation, but collisions and retries cost capacity. The better choice depends on traffic load and coordination requirements.
A_ZH: 资源划分给节点独立时隙或频带，在模型下避免同时干扰，但已分配容量可能闲置。随机接入允许活跃节点不经固定独占分配就使用信道，却会因碰撞和重传损失容量。何者更合适取决于负载与协调要求。

@@ N228 | x06-link | learn | XN6:25-27
Q_EN: Derive the success probability per slot for N independent slotted-ALOHA nodes, each transmitting with probability p.
Q_ZH: N 个节点独立地以概率 p 在时隙内发送，推导时隙 ALOHA 每槽成功概率。
A_EN: A particular node succeeds with $p(1-p)^{N-1}$. Any one of N nodes may be the sole transmitter, so $S=Np(1-p)^{N-1}$. Maximizing gives p=1/N, and the maximum tends to $1/e$ as N grows. This assumes saturated independent nodes and equal-length synchronized slots.
A_ZH: 某个节点成功的概率为 $p(1-p)^{N-1}$。N 个节点中任一个都可成为唯一发送者，因此 $S=Np(1-p)^{N-1}$。最大化得到 p=1/N，N 很大时最大值趋于 $1/e$。该模型假设节点饱和且独立，时隙同步、长度相同。

@@ N229 | x06-link | learn | XN6:28-29
Q_EN: Why is pure ALOHA less efficient than slotted ALOHA in the standard ideal model?
Q_ZH: 标准理想模型中，纯 ALOHA 为什么比时隙 ALOHA 效率低？
A_EN: Without slot alignment, a frame can collide with transmissions beginning within a vulnerable interval of roughly two frame times. Under Poisson attempts with load G per frame time, throughput is $S=Ge^{-2G}$, maximized at G=0.5 with $1/(2e)$. Slotted alignment halves the vulnerable interval in the corresponding model.
A_ZH: 没有时隙对齐时，一个帧可能与约两个帧时长的易冲突区间内开始的传输相撞。若尝试次数按 Poisson 模型、每帧时长负载为 G，则吞吐率 $S=Ge^{-2G}$，在 G=0.5 时达到 $1/(2e)$。对应模型下，时隙对齐将易冲突区间减半。

@@ N230 | x06-link | worked | XN6:25-27
Q_EN: Four slotted-ALOHA nodes each transmit with probability 1/4. Find success, idle and collision probabilities per slot.
Q_ZH: 四个时隙 ALOHA 节点各以 1/4 概率发送，求每槽成功、空闲和碰撞概率。
A_EN: Success is $4(1/4)(3/4)^3=108/256=0.421875$. Idle probability is $(3/4)^4=81/256$. The remainder, $67/256\approx0.261719$, is collision probability. These three mutually exclusive events sum to one, giving a useful check on the calculation.
A_ZH: 成功概率为 $4(1/4)(3/4)^3=108/256=0.421875$，空闲概率为 $(3/4)^4=81/256$，其余 $67/256\approx0.261719$ 为碰撞概率。三种事件互斥且和为一，可用于检查计算。

@@ N231 | x07-tutorials | historical | XNT3:1
Q_EN: A plain-HTTP request contains GET /cs453/index.html HTTP/1.1, Host: gaia.cs.umass.edu, and Connection: keep-alive. What can you infer from these lines, and can you read the client IP from them?
Q_ZH: 明文 HTTP 请求包含 GET /cs453/index.html HTTP/1.1、Host: gaia.cs.umass.edu 和 Connection: keep-alive。能从这些行推断什么？能读出客户端 IP 吗？
A_EN: The requested URL is http://gaia.cs.umass.edu/cs453/index.html, the version is HTTP/1.1, and the client asks to keep the connection open. These lines contain the server name, not the client IP. The client address must come from network-layer information or other supplied context.
A_ZH: 请求的 URL 是 http://gaia.cs.umass.edu/cs453/index.html，版本是 HTTP/1.1，客户端请求保持连接。这几行包含服务器名称，不包含客户端 IP。客户端地址须从网络层信息或其他给定上下文取得。

@@ N232 | x07-tutorials | historical | XNT3:2
Q_EN: A host-to-local-DNS exchange costs RTTL. An uncached lookup then needs three sequential upstream exchanges of RTTr each. What changes if the local resolver caches the answer?
Q_ZH: 主机到本地 DNS 的交互耗时 RTTL，未缓存查询还需依次进行三次各耗时 RTTr 的上游交互。本地解析器已有缓存时会怎样？
A_EN: Uncached delay is RTTL + 3RTTr; cached delay is RTTL, ignoring processing and transmission costs. The three upstream exchanges are sequential in this question, so add them. A DNS cache removes particular lookup steps; it does not remove the later TCP or HTTP exchanges needed to fetch the page.
A_ZH: 忽略处理与传输耗时，未缓存为 RTTL + 3RTTr，已缓存为 RTTL。本题三次上游交互依次发生，因此相加。DNS 缓存省掉的是特定查询步骤，后续获取网页需要的 TCP 或 HTTP 交互仍存在。

@@ N233 | x07-tutorials | historical | XNT3:3
Q_EN: After DNS, fetch one tiny HTML page and eight tiny objects. With server RTT R, compare serial nonpersistent HTTP, nonpersistent HTTP with five parallel connections, and one nonpipelined persistent connection.
Q_ZH: DNS 完成后获取一个很小的 HTML 页面及八个很小的对象，服务器 RTT 为 R。比较串行非持久、最多五条并行非持久，以及一条无流水线的持久连接。
A_EN: Ignoring transmission time: serial nonpersistent needs 9×2R=18R. Five parallel connections need 2R for HTML plus two object batches of 2R, totaling 6R. Persistent without pipelining needs 2R for connection+HTML, then 8R, totaling 10R. Add DNS delay to each. HTTP pipelining or HTTP/2 multiplexing would change the assumed model.
A_ZH: 忽略传输时间：串行非持久需要 9×2R=18R；五条并行连接先用 2R 获取 HTML，再分两批获取对象，每批 2R，共 6R；无流水线持久连接先用 2R 建连并取 HTML，再用 8R 取对象，共 10R。都需另加 DNS 耗时。若使用 HTTP 流水线或 HTTP/2 多路复用，模型会改变。

@@ N234 | x07-tutorials | historical | XNT4:1
Q_EN: Why can the ideal client-server file-distribution bound max(NF/us, F/dmin) be achieved in the fluid model?
Q_ZH: 为什么理想流体模型中，客户端—服务器分发下界 max(NF/us, F/dmin) 可以达到？
A_EN: Give every client rate min(us/N, dmin). Total server upload then does not exceed us, and no client's download limit is exceeded because every limit is at least dmin. Every client receives F bits in F/min(us/N,dmin), equal to the bound. This assumes divisible continuous traffic, no other bottlenecks, and simultaneous transmissions; it is not a guarantee for real TCP transfers.
A_ZH: 给每个客户端分配 min(us/N, dmin) 的速率，总上传不超过 us，而且各客户端下行上限均不小于 dmin。每个客户端接收 F 位所需时间为 F/min(us/N,dmin)，正好等于该下界。这里假设流量连续可分、无其他瓶颈且可同时发送，并非实际 TCP 传输保证。

@@ N235 | x07-tutorials | historical | XNT4:1
Q_EN: Distribute F=15 Gbit to N=100 peers. Server upload is 30 Mbps, each peer downloads at 2 Mbps and uploads at 0.7 Mbps. Compute the ideal client-server and P2P lower bounds.
Q_ZH: 将 15 Gbit 文件分发给 100 个节点，服务器上传 30 Mbps，每个节点下载 2 Mbps、上传 0.7 Mbps。求理想客户端—服务器与 P2P 分发下界。
A_EN: Client-server: max(100×15000/30,15000/2)=50000 s. P2P: max(15000/30,15000/2,100×15000/(30+100×0.7))=max(500,7500,15000)=15000 s. Use decimal units consistently. Peer upload improves aggregate supply but cannot eliminate the server's first-copy or slowest-download constraints.
A_ZH: 客户端—服务器：max(100×15000/30,15000/2)=50000 秒。P2P：max(15000/30,15000/2,100×15000/(30+100×0.7))=max(500,7500,15000)=15000 秒。统一使用十进制单位。节点上传可提高总供给，但不能消除服务器提供首份文件、最慢节点接收文件的限制。

@@ N236 | x07-tutorials | historical | XNT4:2
Q_EN: A DASH exercise has N video qualities and N audio qualities. How many files are required if every audio-video pair is precombined, if only equal-level pairs are allowed, or if tracks are separate?
Q_ZH: DASH 题目有 N 种视频质量和 N 种音频质量。若预先合并所有音视频组合、只允许同等级配对，或分开存储音视频，分别要多少文件？
A_EN: All combinations require N² combined representations. Equal-level-only pairing requires N. Separate tracks require N+N=2N and the client combines them. These counts refer to representation choices, ignoring segmentation. The historical question mixes “any combination” and “one-to-one” wording, so state the pairing assumption instead of memorizing one unexplained number.
A_ZH: 所有组合需 N² 份合并版本；只允许同等级配对需 N 份；音视频分开存储则为 N+N=2N，客户端自行组合。这里统计版本选择，忽略分段数量。往年题目混用了“任意组合”与“一一对应”，因此必须先写清配对假设，不能只背一个数字。

@@ N237 | x07-tutorials | historical | XNT5:1
Q_EN: In the toy 8-bit Internet-checksum exercise, add 00100011, 01001110 and 01010100. What checksum is sent, and can all two-bit errors be detected?
Q_ZH: 在简化的 8 位 Internet checksum 题中，将 00100011、01001110、01010100 相加。发送的校验和是多少？能检测所有两位错误吗？
A_EN: The values are 35+78+84=197=11000101, with no carry beyond eight bits. Complement to get 00111010. Adding it back gives 11111111. Single-bit corruption is detected, but two changes with cancelling weighted effects can be missed. Actual UDP/TCP checksums use 16-bit words; eight bits is this exercise's simplification.
A_ZH: 三个数为 35+78+84=197=11000101，没有超过八位的进位，按位取反得到 00111010。加回后为 11111111。单比特错误可被检测，但权重影响相互抵消的两个变化可能漏检。实际 UDP/TCP 校验和使用 16 位字，八位只是本题简化。

@@ N238 | x07-tutorials | historical | XNT5:2
Q_EN: Why can an alternating-bit protocol fail if the channel permits arbitrarily delayed duplicates and reordering?
Q_ZH: 如果信道允许重复包任意延迟和乱序，交替比特协议为什么可能失效？
A_EN: Receive data numbered 0, then 1, so the receiver expects 0 again. A very old duplicate 0 can now arrive and be mistaken for new data. A sequence number is useful only with bounds or rules that prevent old packets from surviving until that number is reused. This illustrates why the channel assumptions matter in reliability proofs.
A_ZH: 接收编号 0、再接收 1 后，接收方重新期待 0。此时很久以前的重复 0 若到达，就可能被误认为新数据。序号机制必须配合限制，避免旧包存活到序号再次使用时。这个例子说明可靠性证明必须明确信道假设。

@@ N239 | x07-tutorials | historical | XNT6:1; XNT6S:6
Q_EN: A sender transmits packets 0–7 once, packet 6 is lost, and nothing is reordered. What ACK sequence does the receiver send under GBN and under SR before retransmission?
Q_ZH: 发送者依次发送 0–7 号包，6 号丢失且没有乱序。重传之前，GBN 和 SR 接收方分别发出什么 ACK 序列？
A_EN: GBN: 0,1,2,3,4,5,5. Packet 7 is discarded and repeats cumulative ACK5. SR: 0,1,2,3,4,5,7; packet 7 is buffered and individually acknowledged. There are seven ACKs, not eight: the lost packet never reaches the receiver and generates no ACK. Here ACK numbers identify packets, unlike TCP's next-byte convention.
A_ZH: GBN 为 0,1,2,3,4,5,5：丢弃 7 号并重复累计 ACK5。SR 为 0,1,2,3,4,5,7：缓存 7 号并单独确认。共有七个 ACK，不是八个，因为丢失的包未到接收方，不会产生 ACK。此处 ACK 表示包编号，与 TCP 的下一期待字节约定不同。

@@ N240 | x07-tutorials | historical | XNT6:1; XNT6S:11-14
Q_EN: TCP receiver B has bytes through 126. A sends seq=127 with 80 bytes, then 40 bytes, using ports 302→80. Give the second sequence number and the ACK when either segment arrives first.
Q_ZH: TCP 接收方 B 已收到至 126 字节。A 用端口 302→80 先发 seq=127、长度 80 的段，再发 40 字节。第二段序号是多少？两段分别先到时 ACK 是多少？
A_EN: First data covers 127–206, so the second starts at 207 and keeps ports 302→80. If the first arrives first, B sends ACK207 with ports 80→302. If the second arrives first, the gap starts at 127, so B sends ACK127. Once both are received contiguously, ACK247 acknowledges bytes through 246.
A_ZH: 第一段覆盖 127–206，因此第二段从 207 开始，端口仍为 302→80。第一段先到时，B 从 80→302 发 ACK207。第二段先到时，缺口从 127 开始，因此发 ACK127。两段连续收齐后发 ACK247，表示已收至 246。

@@ N241 | x07-tutorials | historical | XNT6:2; XNT6S:17-20; XRTO:2
Q_EN: Start EstimatedRTT=100 ms, DevRTT=5 ms; samples are 106,120,140 ms, alpha=1/8 and beta=1/4. Update EstimatedRTT first, use its NEW value for DevRTT, then RTO=EstimatedRTT+4DevRTT, ignoring timer bounds. Find the three RTOs. Is this tutorial convention identical to RFC 6298?
Q_ZH: 初始 EstimatedRTT=100 ms、DevRTT=5 ms，样本为 106、120、140 ms，alpha=1/8、beta=1/4。先更新 EstimatedRTT，再用其新值更新 DevRTT，取 RTO=EstimatedRTT+4DevRTT，忽略定时器上下界。求三次 RTO。这一教程约定与 RFC 6298 完全相同吗？
A_EN: The tutorial updates EstimatedRTT first and uses that new value in DevRTT; RTO=EstimatedRTT+4DevRTT gives 121,135.1875,164.0234 ms. For example the final estimate/deviation are 107.7617/14.0654 ms. RFC 6298 updates variation using the OLD SRTT and also includes timer granularity and a recommended minimum. State the course convention when solving this exercise; do not call it the exact RFC algorithm.
A_ZH: 例解先更新 EstimatedRTT，再用新值更新 DevRTT；按 RTO=EstimatedRTT+4DevRTT 得到 121、135.1875、164.0234 ms。最终估计值与偏差为 107.7617、14.0654 ms。RFC 6298 用旧 SRTT 更新偏差，还考虑时钟粒度和建议的最小超时值。解本题时注明课程约定，不能称其为完全相同的 RFC 算法。

@@ N242 | x07-tutorials | historical | XNT7:1; XNT7S:5
Q_EN: In the historical Reno graph, identify slow start, congestion avoidance, and the loss signals after rounds 16 and 22.
Q_ZH: 根据往年 Reno 图，识别慢启动、拥塞避免，以及第 16、22 轮之后的丢包信号。
MEDIA_FRONT: extra-t7-reno.png
A_EN: Slow start operates over rounds 1–6 and 23–26; congestion avoidance over 6–16 and 17–22. Round 6 is the transition. After round 16 the window drops to roughly half plus the graph's recovery allowance, indicating triple duplicate ACKs. After round 22 it drops to one segment, indicating timeout in this historical model. Explain the growth/drop pattern, not only interval labels.
A_ZH: 慢启动为第 1–6、23–26 轮，拥塞避免为第 6–16、17–22 轮；第 6 轮是切换点。第 16 轮后窗口约减半并加上图中的恢复增量，表示三次重复 ACK。第 22 轮后降到一段，表示该历史模型中的超时。应说明增长或下降形态，不能只背区间。

@@ N243 | x07-tutorials | historical | XNT7:1-2; XNT7S:6-8
Q_EN: In a historical Reno model, windows are in MSS. Three duplicate ACKs follow round 16 with cwnd=42; a timeout follows round 22 with cwnd=29. At round 26 cwnd=8. Give ssthresh at rounds 18/24 and the immediate response to three duplicate ACKs after round 26, with no intervening losses.
Q_ZH: 历史 Reno 模型中窗口以 MSS 为单位：第 16 轮 cwnd=42 后出现三次重复 ACK；第 22 轮 cwnd=29 后超时；第 26 轮 cwnd=8。假设无其他丢包，求第 18/24 轮 ssthresh，以及第 26 轮后三次重复 ACK 的即时响应。
A_EN: Round 18: ssthresh=21. Round 24: 29/2=14.5, shown as 14 under the solution's whole-segment convention. After round 26: ssthresh=4 and immediate fast-recovery cwnd=4+3=7. The extra three segments describe recovery, not a permanent new threshold. Tahoe would instead reset cwnd to one; after the round-16 loss its round-19 cwnd is four in this model.
A_ZH: 第 18 轮 ssthresh=21；第 24 轮为 29/2=14.5，例解按整段约定写为 14。第 26 轮之后 ssthresh=4，快速恢复即时 cwnd=4+3=7。额外三段属于恢复阶段，不是永久阈值。Tahoe 则将 cwnd 置为一；在本题第 16 轮丢包后，第 19 轮 cwnd 为四。

@@ N244 | x07-tutorials | historical | XNT7:2; XNT7S:7
Q_EN: With windows 1,2,4,8,16,32 in the first six rounds and 33 in round seven, during which round is segment 70 first sent?
Q_ZH: 前六轮窗口依次为 1、2、4、8、16、32，第七轮为 33。第 70 个段首次在第几轮发送？
A_EN: Six rounds send 1+2+4+8+16+32=63 segments. Round seven sends segments 64–96, including 70. Therefore the answer is round seven. Count cumulative transmitted segments; cwnd is the amount allowed within a round, not the cumulative segment number.
A_ZH: 六轮共发送 1+2+4+8+16+32=63 个段。第七轮发送第 64–96 个段，包含第 70 个。因此答案是第七轮。要累计已发送段数；cwnd 是一轮内允许的数量，不是累计段号。

@@ N245 | x07-tutorials | historical | XNT7:3; XNT7S:14
Q_EN: For an ideal pipeline, R=1 Gbps, RTT=30 ms and packet length=1200 bytes. What is the smallest integer window giving sender utilization greater than 97%?
Q_ZH: 理想流水线中 R=1 Gbps、RTT=30 ms、包长 1200 字节。使发送利用率超过 97% 的最小整数窗口是多少？
A_EN: Serialization takes 1200×8/10^9=9.6 microseconds. Use $U=\min(1,NL/R\,/\,(RTT+L/R))$. Thus N>0.97×(30000+9.6)/9.6=3032.22, so choose 3033 packets. Convert bytes to bits and keep the serialization term; substituting the nearby 8000-bit illustrative figure would solve a different problem.
A_ZH: 串行化耗时 1200×8/10^9=9.6 微秒。用 $U=\min(1,NL/R\,/\,(RTT+L/R))$，得到 N>0.97×(30000+9.6)/9.6=3032.22，因此选 3033 个包。要把字节转为位并保留串行化项；若代入旁边示意图中的 8000 位，就变成另一道题了。

@@ N246 | x07-tutorials | historical | XNT8:1
Q_EN: True or false: a TCP receiver with no application data to send emits no ACKs; after seq=m the next segment must have seq=m+1; a segment with seq=38 and four bytes must itself have ACK=42.
Q_ZH: 判断：TCP 接收方没有应用数据就不发 ACK；seq=m 后下一段必为 m+1；某段 seq=38、携带四字节时，该段自身 ACK 必为 42。
A_EN: All false. ACKs can be sent without application data. For consecutive new data, sequence numbers advance by payload length, with SYN/FIN also consuming sequence space. A segment's ACK field refers to the opposite direction's byte stream, so its own seq and payload do not determine that ACK. The receiver's response could ACK42 if it has all earlier bytes.
A_ZH: 全部错误。没有应用数据也能单独发 ACK；连续新数据的序号按有效载荷长度推进，SYN/FIN 也占序号。某段的 ACK 字段对应反方向的字节流，不能用它自己的 seq 与载荷推算。接收方在此前字节已完整收到时，回复才可能是 ACK42。

@@ N247 | x07-tutorials | historical | XNT8:1
Q_EN: Why are “rwnd never changes” and “the newest RTT sample always lies below the current RTO” unsafe claims?
Q_ZH: 为什么“rwnd 始终不变”和“最新一次 RTT 样本总小于当前 RTO”都不可靠？
A_EN: The advertised receive window changes as data arrives and the application drains the buffer; it is carried in the TCP header. RTO is computed from a smoothed estimate and variation, so one unusually large newest sample need not be below the resulting RTO. Flow control limits outstanding data according to the advertised window; it does not freeze receiver-buffer occupancy.
A_ZH: 接收数据和应用读取缓冲区都会改变通告接收窗口，TCP 首部携带此信息。RTO 根据平滑估计和偏差计算，异常大的新样本不一定低于更新后的 RTO。流量控制按通告窗口限制未确认数据，并不意味着接收缓冲占用不变。

@@ N248 | x07-tutorials | historical | XNT8:1
Q_EN: Fragment an IPv4 datagram of total length 1600 bytes, ID=291, onto MTU=500, assuming a 20-byte header without options. Give each fragment's total length, offset and MF.
Q_ZH: IPv4 数据报总长 1600 字节、ID=291，经过 MTU=500 的链路，假设首部 20 字节且无选项。给出各分片总长、偏移和 MF。
A_EN: Payload is 1580 bytes. Nonfinal payloads must be multiples of eight, so use 480,480,480,140. Total lengths are 500,500,500,160; offsets in eight-byte units are 0,60,120,180; MF values are 1,1,1,0. All retain ID291. Check that payloads, not total lengths including repeated headers, sum to 1580.
A_ZH: 原载荷为 1580 字节。非末片载荷须为八的倍数，取 480、480、480、140。总长为 500、500、500、160；以八字节为单位的偏移为 0、60、120、180；MF 为 1、1、1、0，ID 均为 291。校验时应让各片载荷相加为 1580，而非含重复首部的总长相加。

@@ N249 | x07-tutorials | historical | XNT9:1; XNT9S:3
Q_EN: Run Dijkstra from x on the original Tutorial 9 graph. Give final distances and one shortest-path tree; explain ties in the selection order.
Q_ZH: 在 Tutorial 9 原图上从 x 运行 Dijkstra。给出最终距离和一棵最短路径树，并解释选点顺序的平局。
MEDIA_FRONT: extra-t9-dijkstra.png
A_EN: Distances are x:0,v:3,u:6,w:6,y:6,t:7,z:8. One tree uses x-v, v-u, x-w, x-y, v-t, x-z. After selecting v, u/w/y tie at six and may be settled in any order without changing final distances. At each step settle a minimum tentative distance and relax only through that settled node; do not confuse predecessor with the first hop.
A_ZH: 距离为 x:0、v:3、u:6、w:6、y:6、t:7、z:8。一棵树包含 x-v、v-u、x-w、x-y、v-t、x-z。选定 v 后，u/w/y 的距离同为六，可按任意顺序确定而不改变最终距离。每步选最小暂定距离，并经该节点松弛；前驱节点与第一跳不是同一概念。

@@ N250 | x07-tutorials | historical | XNT9:1; XNT9S:10
Q_EN: In a triangle with costs xy=3, yz=6 and zx=4, do synchronous distance-vector exchanges improve any direct route?
Q_ZH: 三角网络边权 xy=3、yz=6、zx=4。同步距离向量交换会改善任何直接路由吗？
A_EN: No. Alternatives cost 4+6=10 for xy, 3+4=7 for yz, and 3+6=9 for zx, all worse than the direct edges. Final vectors in order x,y,z are (0,3,4), (3,0,6), (4,6,0). Initially a router knows its own vector, while stored neighbor vectors may be unknown; the first exchange fills that knowledge even when its best distances do not change.
A_ZH: 不会。xy 的绕行代价为 4+6=10，yz 为 3+4=7，zx 为 3+6=9，均高于直达。按 x,y,z 顺序，最终向量为 (0,3,4)、(3,0,6)、(4,6,0)。初始节点知道自身向量，但保存的邻居向量可能未知；第一次交换仍补充了信息，即使最短距离没有改变。

@@ N251 | x07-tutorials | historical | XNT9:2; XNT9S:11
Q_EN: In the shown graph, xw=2, xy=5, wy=2. Neighbors w and y advertise distances to u of 5 and 6. What is x's updated vector to w,y,u?
Q_ZH: 图中 xw=2、xy=5、wy=2，邻居 w、y 通告到 u 的距离分别为 5、6。x 更新后到 w、y、u 的向量是多少？
MEDIA_FRONT: extra-t9-distance-vector.png
A_EN: To w: min(2,5+2)=2. To y: min(5,2+2)=4. To u: min(2+5,5+6)=7. Thus (2,4,7), all via w where that is best. In the Bellman-Ford update use the direct cost to a neighbor plus that neighbor's advertised distance; do not substitute a newly computed indirect route as if it were a direct link.
A_ZH: 到 w：min(2,5+2)=2；到 y：min(5,2+2)=4；到 u：min(2+5,5+6)=7。因此为 (2,4,7)，最优第一跳均为 w。Bellman-Ford 更新应使用到邻居的直接边权加其通告距离，不能把刚算出的间接路径误作直接链路。

@@ N252 | x07-tutorials | historical | XNT10:1; XNT10S:6
Q_EN: Within 223.1.17.0/24, subnet 1 already uses 223.1.17.0/26. Allocate disjoint subnets for 106 and 14 hosts using ordinary IPv4 host-address rules.
Q_ZH: 在 223.1.17.0/24 内，子网 1 已使用 223.1.17.0/26。按普通 IPv4 主机地址规则，为 106 和 14 台主机分配互不重叠的子网。
A_EN: Use 223.1.17.128/25 for 106 hosts: 128 addresses, 126 usable. Use 223.1.17.64/28 for 14 hosts: 16 addresses, 14 usable. Existing /26 occupies .0–.63; the new ranges are .128–.255 and .64–.79. Other aligned /28 blocks in .64–.127 also work. Writing .64/25 does not create a valid independent /25 network; check alignment and overlap.
A_ZH: 106 台可分配 223.1.17.128/25，共 128 地址、126 可用；14 台可分配 223.1.17.64/28，共 16 地址、14 可用。原 /26 占 .0–.63，新范围分别是 .128–.255 与 .64–.79。在 .64–.127 内其他对齐的 /28 也可。写 .64/25 并不会得到独立有效的 /25 网络，必须检查边界对齐和重叠。

@@ N253 | x07-tutorials | historical | XNT10:2; XNT10S:14
Q_EN: In the original four-AS graph, ignore the dashed AS2–AS4 link. By which protocol do 3c,3a,1c,1d learn external prefix x: OSPF, RIP, eBGP or iBGP?
Q_ZH: 在原四 AS 图中忽略虚线 AS2–AS4 链路。3c、3a、1c、1d 分别通过 OSPF、RIP、eBGP、iBGP 中哪一种获知外部前缀 x？
MEDIA_FRONT: extra-t10-bgp.png
A_EN: In order: eBGP, iBGP, eBGP, iBGP. Information crosses AS4→AS3 at 3c, spreads within AS3 to 3a, crosses AS3→AS1 at 1c, then spreads within AS1 to 1d. OSPF/RIP support internal routing and next-hop reachability; they are not the BGP advertisement sessions asked about here.
A_ZH: 依次为 eBGP、iBGP、eBGP、iBGP。信息从 AS4 跨入 AS3 到达 3c，在 AS3 内传播到 3a；再从 AS3 跨入 AS1 到达 1c，在 AS1 内传播到 1d。OSPF/RIP 负责内部路由及下一跳可达性，本题问的前缀通告会话由 BGP 完成。

@@ N254 | x07-tutorials | historical | XNT11:1; XNT11S:3; XPARITY:9
Q_EN: Place data 1110 0110 1001 1101 row by row in a 4×4 grid. Extend it to 5×5 so every row and column, including the parity row/column, has even parity. Fill the missing bits. Why does this specified format transmit nine extra bits?
Q_ZH: 把 1110 0110 1001 1101 逐行放入 4×4 数据格，再扩成 5×5，使每行每列（包括校验行/列）都满足偶校验。补齐空位，并解释为何此指定格式发送九个额外位。
A_EN: Row parity is 1,0,0,1 and column parity is 1,1,0,0. The full 5×5 format also transmits corner parity 0, totaling 4+4+1=9 check bits. The corner makes the parity row and column even too. Although its value is determined by other parity values, it is part of this code: omitting it changes the format and lowers minimum Hamming distance from 4 to 3. Do not replace the course's nine-bit answer with eight by calling the corner redundant.
A_ZH: 行校验为 1,0,0,1，列校验为 1,1,0,0。完整 5×5 格式还发送角落校验 0，共 4+4+1=9 个校验位，使校验行和校验列也满足偶校验。角落位虽可由其他校验值算出，却是此编码的一部分；省略它会改变格式，使最小汉明距离从 4 降为 3。不能因它可被推算，就把课程要求的九位答案改成八位。
MEDIA_FRONT: parity-grid-question.png

@@ N255 | x07-tutorials | historical | XNT11:1; XNT11S:5
Q_EN: Two saturated slotted-ALOHA nodes transmit independently with probabilities pA and pB. Does pA=2pB give A twice B's throughput? How should pA be chosen for that target?
Q_ZH: 两个饱和时隙 ALOHA 节点独立地以 pA、pB 发送。令 pA=2pB 就能让 A 吞吐量为 B 两倍吗？应如何设置 pA？
A_EN: Throughputs are $S_A=p_A(1-p_B)$ and $S_B=p_B(1-p_A)$. Doubling attempt probability also changes collision probabilities, so it does not generally double successful throughput. Solve $p_A(1-p_B)=2p_B(1-p_A)$ to obtain $p_A=2p_B/(1+p_B)$. At pB=0.2, choose pA=1/3; then SA=4/15 and SB=2/15.
A_ZH: 吞吐量为 $S_A=p_A(1-p_B)$、$S_B=p_B(1-p_A)$。尝试发送概率加倍也会改变碰撞概率，因此通常不等于成功吞吐加倍。解 $p_A(1-p_B)=2p_B(1-p_A)$ 得 $p_A=2p_B/(1+p_B)$。当 pB=0.2 时取 pA=1/3，得到 SA=4/15、SB=2/15。

@@ N256 | x07-tutorials | historical | XNT11:1-2; XNT11S:5
Q_EN: In N-node slotted ALOHA, A attempts with probability 2p and every other node with p. Give the individual throughputs and the valid range of p.
Q_ZH: N 节点时隙 ALOHA 中，A 以 2p 尝试发送，其余节点均以 p 发送。求各节点吞吐量及 p 的有效范围。
A_EN: A succeeds when it transmits and all N−1 others remain silent: $S_A=2p(1-p)^{N-1}$. Another named node succeeds when it transmits, A is silent, and the remaining N−2 nodes are silent: $S_B=p(1-2p)(1-p)^{N-2}$. Valid probabilities require $0\le p\le1/2$. Count the silent competitors explicitly to avoid wrong exponents.
A_ZH: A 成功要求它发送且其余 N−1 个节点静默：$S_A=2p(1-p)^{N-1}$。某个其他节点成功要求它发送、A 静默且余下 N−2 个节点静默：$S_B=p(1-2p)(1-p)^{N-2}$。概率有效要求 $0\le p\le1/2$。逐一数清必须静默的竞争者，就不易写错指数。

@@ N257 | x07-tutorials | historical | XNT11:2; XNT11S:6-10
Q_EN: If CSMA listens before transmitting, why can collisions still occur? What additional behavior does CSMA/CD provide?
Q_ZH: CSMA 在发送前监听信道，为什么还会碰撞？CSMA/CD 又增加了什么行为？
A_EN: Signals take time to propagate. B may sense idle and start before A's earlier signal reaches B, so both transmit. Collision detection lets a sender detect overlap during transmission and abort, reducing wasted time. This is the historical shared-medium Ethernet model; ordinary full-duplex switched Ethernet does not operate as a shared collision channel. These topics appear in Tutorial 11 even though the supplied Chapter 6 lecture ends at ALOHA.
A_ZH: 信号传播需要时间；A 已发送但信号尚未到 B 时，B 仍可能认为空闲并开始发送。碰撞检测使发送者在传输期间发现冲突并中止，减少浪费。这属于历史共享介质以太网模型，普通全双工交换式以太网不是共享碰撞信道。虽然现有 Chapter 6 课件止于 ALOHA，Tutorial 11 确实包含这些内容。

@@ N258 | x07-tutorials | historical | XNT11:2; XNT11S:11
Q_EN: In the pictured tree, S4 connects S1,S2,S3; A/B/C attach to S1, D/E/F to S2, G/H/I to S3. All switch tables start empty. A sends a frame to G. Which switches learn A, and why does S2 receive a flooded copy?
Q_ZH: 图中 S4 连接 S1、S2、S3；A/B/C 接 S1，D/E/F 接 S2，G/H/I 接 S3。所有交换表初始为空，A 向 G 发帧。哪些交换机会学到 A？为什么 S2 也收到泛洪副本？
MEDIA_FRONT: extra-t11-switches.png
A_EN: Every switch learns a source-MAC→incoming-port entry. S1 learns A on its A-facing port; S4 learns A toward S1; S2 and S3 learn A toward S4. Unknown-destination flooding goes through S1→S4 and onward to both S2 and S3, excluding each incoming port. S2 floods toward D/E/F; those hosts discard the frame. The provided solution's short path summary omits this flooded branch, but its S2 table confirms A was learned.
A_ZH: 每台交换机记录“源 MAC→入端口”。S1 学到 A 朝 A，S4 学到 A 朝 S1，S2 和 S3 学到 A 朝 S4。目的未知时，泛洪经 S1→S4 后同时进入 S2、S3，各交换机均不向入端口回发。S2 向 D/E/F 泛洪，这些主机丢弃该帧。例解的简短路径描述漏写了该分支，但其 S2 表确实记录了 A。

@@ N259 | x07-tutorials | historical | XNT11:2; XNT11S:11
Q_EN: S4 connects S1,S2,S3; A attaches to S1 and G to S3. Initially empty tables have just learned A from A’s flooded frame to G. Using the pictured tree, G now replies to A. Give the path and the switches that learn G; does S2 learn G from this reply?
Q_ZH: S4 连接 S1、S2、S3，A 接 S1、G 接 S3。初始空表刚通过 A 向 G 的泛洪帧学到 A。现在 G 按图回复 A：经过哪条路径？哪些交换机会学到 G？S2 会由这次回复学到 G 吗？
MEDIA_FRONT: extra-t11-switches.png
A_EN: The reply follows G→S3→S4→S1→A because A's location has been learned. S3 learns G on its G-facing port; S4 learns G toward S3; S1 learns G toward S4. S2 does not receive this known-destination unicast and therefore does not learn G from it. Switches learn from the source of frames they receive, not from every destination appearing anywhere in the network.
A_ZH: 回复沿 G→S3→S4→S1→A，因为各沿途交换机已学到 A。S3 学到 G 朝 G，S4 学到 G 朝 S3，S1 学到 G 朝 S4。S2 不接收这次已知目的单播，因此不会由此学到 G。交换机根据自己实际接收帧的源地址学习，而不是看到全网任何目的地址就能学习。

@@ N260 | x08-assignments | historical | XNA1:1; XNA1S:1
Q_EN: Assignment 1: a link has rate R, length m and propagation speed s. At t=L/R after transmission begins, where are the first and last bits? For L=120 bits, R=56 kbps, s=2.5×10^8 m/s, find m when propagation and transmission delays are equal.
Q_ZH: Assignment 1：链路速率 R、长度 m、传播速度 s。开始发送后 t=L/R 时，首位和末位在哪里？若 L=120 位、R=56 kbps、s=2.5×10^8 m/s，求传播与发送时延相等时的 m。
A_EN: The last bit is just leaving the sender. If m/s>L/R, the first bit is still on the link; if m/s<L/R, it has reached the receiver. Equality requires m=sL/R=535714.3 m≈535.7 km. End-to-end delivery of the last bit takes L/R+m/s, ignoring processing/queueing. Finishing serialization does not mean the whole packet has arrived.
A_ZH: 末位刚离开发送端。若 m/s>L/R，首位仍在链路上；若 m/s<L/R，首位已到接收端。相等条件为 m=sL/R=535714.3 米，约 535.7 千米。忽略处理和排队，末位到达总耗时 L/R+m/s。完成串行发送并不代表整个包已到达。

@@ N261 | x08-assignments | historical | XNA1:2; XNA1S:3
Q_EN: Send 8×10^6 bits across three equal 2 Mbps store-and-forward links. Compare one whole message with 800 packets of 10000 bits each, ignoring headers, propagation and queueing.
Q_ZH: 经三条等速 2 Mbps、存储转发链路发送 8×10^6 位。比较整报文发送与分成 800 个、每个 10000 位的包，忽略首部、传播和排队。
A_EN: Whole message: 4 s per link, so 12 s. Packet serialization is 5 ms. The first packet arrives after 3×5=15 ms; the last after 15+799×5=4010 ms=4.01 s. The formula is (P+H−1)L/R with P=800 packets, H=3 links and L=10000 bits per packet. Segmentation enables pipelining and smaller retransmissions, but adds headers and reassembly work when those are included.
A_ZH: 整报文每条链路耗时四秒，共 12 秒。单包串行化五毫秒，首包在 3×5=15 毫秒到达，末包在 15+799×5=4010 毫秒，即 4.01 秒到达。公式 (P+H−1)L/R 中，P=800 个包、H=3 条链路、L=每包 10000 位。分段可实现流水线并减小重传单位，但实际还会增加首部和重组工作。

@@ N262 | x08-assignments | historical | XNA1:3; XNA1S:5
Q_EN: After POP3 LIST shows messages 1 and 2 and RETR 1 has completed, how do download-and-delete and download-and-keep command sequences differ?
Q_ZH: POP3 的 LIST 显示邮件 1、2，并已完成 RETR 1 后，下载删除和下载保留模式接下来的命令有何不同？
A_EN: For delete mode, issue DELE 1, RETR 2, DELE 2, then QUIT after the relevant replies. For keep mode, issue RETR 2 and QUIT without DELE. On the next session with no new messages, keep mode can still list and retrieve both stored messages. DELE requests deletion; the normal session's update phase commits it, so RETR by itself does not delete mail.
A_ZH: 删除模式在收到相应回复后依次 DELE 1、RETR 2、DELE 2、QUIT；保留模式则 RETR 2、QUIT，不发 DELE。若无新邮件，下次保留模式会话仍可列出和下载原来两封。DELE 请求删除，正常结束会话的更新阶段才提交；RETR 本身不会删除邮件。

@@ N263 | x08-assignments | historical | XNA1:3; XNA1S:6-8; XUDP:Format
Q_EN: A student claims: “Video conferencing using UDP has no error detection, and media packets must be sent directly to the teacher’s computer.” What is wrong with these claims, and what deployment evidence would be needed?
Q_ZH: 有人声称：“视频会议用 UDP，所以没有差错检测，而且媒体分组一定直接发往老师的电脑。”这两句话哪里有问题？还需要什么部署证据？
A_EN: Protocol names, media relay versus P2P choices, and fallback behavior need dated official evidence for the client/mode studied. A cloud-relayed call need not use the lecturer's IP as the student's media destination. UDP has a checksum; it lacks built-in reliable retransmission and ordering. The old solution confuses error checking with reliable delivery. Record observations and deployment assumptions instead of treating every old vendor claim as universal.
A_ZH: 协议名称、媒体中继或 P2P 选择、回退行为都需与所研究客户端和模式对应的有日期官方证据。云中继通话中，学生的媒体目的地址不必是教师电脑 IP。UDP 有校验和，缺少的是内建可靠重传和排序；旧例解混淆了差错检测与可靠交付。应记录观测及部署假设，不把旧产品描述当作普遍定律。

@@ N264 | x08-assignments | historical | XNA2:1; XNA2S:1
Q_EN: Why can rdt3.0 reuse the alternating-bit receiver logic of rdt2.2 even though the sender adds a timeout?
Q_ZH: rdt3.0 的发送方增加超时机制，为什么接收方仍能复用 rdt2.2 的交替比特逻辑？
A_EN: The receiver already distinguishes the expected bit from a duplicate. In state “expect 0”, accept uncorrupted 0, deliver it, ACK0 and move to “expect 1”; a duplicate 1 or corrupted arrival causes the last valid ACK to be repeated without delivery. The other state is symmetric. Timeouts change when the sender retransmits, not the receiver's rule for suppressing duplicates under the assumed channel model.
A_ZH: 接收方本来就能区分期待序号与重复包。在“期待 0”状态，收到未损坏的 0 后交付、回 ACK0 并转为“期待 1”；重复 1 或损坏包则不交付，重复上次有效 ACK。另一状态对称。超时改变发送方重传时机，但在题设信道模型下，不改变接收方去重规则。

@@ N265 | x08-assignments | historical | XNA2:1; XNA2S:1-2
Q_EN: GBN has window N=4 and sequence space 1024. With no reordering, the receiver next expects k. What sender-window positions and in-flight ACK values are possible?
Q_ZH: GBN 窗口 N=4、序号空间 1024，信道无乱序，接收方下一期待 k。发送窗口可能位于哪里？在途 ACK 可能有哪些值？
A_EN: The sender base can range from k−4 through k; each window contains four consecutive sequence numbers. The receiver has accepted through k−1, but ACKs may lag. In-flight cumulative ACK values can range from k−5 through k−1: an earlier copy of ACK(k−5) may already have reached the sender while a later duplicate is still in transit. This respects the no-reordering assumption. Interpret indices modulo 1024 near wraparound.
A_ZH: 发送基序号可为 k−4 至 k，各窗口包含从该基序号开始的连续四个编号。接收方已接受至 k−1，但 ACK 可能滞后。在途累计 ACK 可为 k−5 至 k−1：较早一份 ACK(k−5) 已到发送方，较晚的重复 ACK 仍在途中，这与无乱序假设一致。序号环绕时按模 1024 理解。

@@ N266 | x08-assignments | historical | XNA2:1; XNA2S:2
Q_EN: A router's table maps destination H3 to interface 3. Can this destination-only table send H1→H3 via interface 3 but H2→H3 via interface 4?
Q_ZH: 路由器转发表将目的 H3 映射到接口 3。只按目的地址查表时，能让 H1→H3 走接口 3、H2→H3 走接口 4 吗？
A_EN: No: both packets have the same lookup key H3 and therefore match the same forwarding action. To distinguish them, the rule would need additional information such as source address or another policy field. The answer is about the destination-only model in the question, not a claim that all real routers lack policy routing or multipath features.
A_ZH: 不能，两种包的查找键都是 H3，因此匹配同一动作。若要区分，规则需要源地址或其他策略字段。这个结论针对题设“仅按目的地址”的模型，并不是说所有实际路由器都没有策略路由或多路径能力。

@@ N267 | x08-assignments | historical | XNA2:2; XNA2S:3-4; XDETOUR:2-4
Q_EN: In the 1999 Detour reading, what can make an available route inefficient, and why do measured better alternatives not prove universal improvement after rerouting?
Q_ZH: 在 1999 年 Detour 阅读题中，可达的路径为什么仍可能低效？测得更好的替代路径，为什么不能证明重路由后必然普遍改善？
A_EN: The paper discusses weak performance metrics, restrictive policies, manual balancing and unused alternative paths. Rerouting changes traffic load, so measurements of an alternative under the old load do not establish performance after everyone switches. Separate the measured inefficiency from the proposed routing policy, and retain the study's historical setting.
A_ZH: 论文讨论了性能指标不足、策略限制、人工均衡和替代路径未被利用。重路由会改变负载，旧负载下测得的优势不能证明所有流量迁移后的性能。应区分已观测到的低效与提出的路由策略，并保留研究的历史背景。

@@ N268 | x08-assignments | historical | XNA2:2; XNA2S:3-4; XDETOUR:5-9
Q_EN: What information limitation motivates Detour's “informed transport,” especially for short TCP flows?
Q_ZH: 哪种信息局限促使 Detour 提出“知情传输”，尤其针对短 TCP 流？
A_EN: A new flow has little path information; feedback takes RTTs and the flow may finish before learning useful capacity estimates. Detour proposes sharing observations across flows at network edges to inform startup and congestion decisions. This is a design proposal with tradeoffs, not proof that bypassing congestion control improves the network.
A_ZH: 新流缺少路径信息，反馈需经历 RTT，短流可能在学到有效容量估计前已结束。Detour 提议由网络边缘汇总跨流观测，辅助启动和拥塞决策。这是带权衡的设计提议，并不证明绕过拥塞控制就能改善网络。

@@ N269 | x08-assignments | historical | XNA3:1; XNA3S:1
Q_EN: Compute CRC for D=1010101010 and generator G=10011. How many remainder bits are needed and what is the transmitted codeword?
Q_ZH: 数据 D=1010101010、生成多项式 G=10011，求 CRC 余数位数和最终发送码字。
A_EN: G has degree four, so append four zeros to D before modulo-2 division. The remainder is 0100, with the leading zero retained. Send 10101010100100. Dividing that codeword by 10011 gives zero remainder. A five-bit generator produces four check bits; generator length and degree differ by one.
A_ZH: G 为四次，因此先在 D 后补四个零再作模二除法。余数是 0100，保留前导零，发送 10101010100100。将该码字除以 10011 余数为零。五位生成多项式产生四个校验位，位数与次数相差一。

@@ N270 | x08-assignments | historical | XNA3:1; XNA3S:3
Q_EN: In the pictured topology, E and F share a subnet and B is remote. For this question replace the left router by switch S1 and call the right router R1; assume no NAT. On E’s first link, give source/destination IP and MAC roles for E→F and E→B.
Q_ZH: 图中 E、F 在同一子网，B 在远端。本题把左路由器替换为交换机 S1，右路由器称 R1，并假设无 NAT。E→F、E→B 时，E 首段链路上的源/目的 IP 与 MAC 各指向谁？
MEDIA_FRONT: extra-a3-subnets.png
A_EN: E→F: source/destination IPs are E/F and MACs are E/F; no router is needed. E→B: IPs are E/B but the Ethernet MAC destination is R1's interface on E's subnet, with source MAC E. E resolves the next-hop gateway's MAC, not remote B's MAC. IP identifies the remote endpoint; link-layer addressing reaches the next hop. Assume no NAT in this exercise.
A_ZH: E→F 时，源/目的 IP 是 E/F，MAC 也是 E/F，不需路由器。E→B 时，IP 是 E/B，但以太网目的 MAC 是 R1 在 E 子网的接口，源 MAC 仍为 E。E 解析下一跳网关的 MAC，而非远端 B 的 MAC。IP 指向远端端点，链路层地址负责抵达下一跳；本题不含 NAT。

@@ N271 | x08-assignments | historical | XNA3:1-2; XNA3S:3
Q_EN: Use the diagram with its left router replaced by switch S1 and right router named R1. A broadcasts an ARP request for B. Why can R1 receive it without forwarding it to subnet 3, and why can B reply without querying A? Does S1 see B's reply?
Q_ZH: 按图将左路由器替换为交换机 S1，右路由器命名为 R1。A 广播 ARP 请求寻找 B。为什么 R1 能收到却不转发到子网 3？B 为什么无需另查 A 就能回复？S1 会收到 B 的回复吗？
A_EN: Switches flood the broadcast within the LAN and learn A's incoming direction. R1 receives it on that LAN interface, but ordinary routers do not propagate the Ethernet broadcast to other subnets. ARP carries A's protocol and hardware addresses, allowing B's unicast reply. The left access switch has just learned A and forwards the reply directly to A, so S1 need not see B's reply in this topology.
A_ZH: 交换机在 LAN 内泛洪广播，并学习 A 的入端口方向。R1 的该 LAN 接口能收到，但普通路由器不把以太网广播传播到其他子网。ARP 请求携带 A 的协议地址和硬件地址，B 因而能单播回复。左侧接入交换机刚学到 A，会将回复直接发给 A，因此本拓扑中的 S1 不必收到 B 的回复。
MEDIA_FRONT: extra-a3-subnets.png

@@ N272 | x08-assignments | historical | XNA3:2; XNA3S:4
Q_EN: Historical CSMA/CD exercise: A transmits for 576 bit-times; one-way propagation to B is 325 bit-times. If B starts at time 324, can A finish before detecting B? What design condition does this illustrate?
Q_ZH: 历史 CSMA/CD 题：A 的发送持续 576 比特时间，到 B 单程传播为 325 比特时间。若 B 在 324 时刻开始，A 会在检测到 B 前发完吗？这说明什么设计条件？
A_EN: B's first bit reaches A at 324+325=649, after A finishes at 576. Thus A can incorrectly conclude no collision occurred. Collision detection requires the sender to remain transmitting long enough for the worst-case round-trip propagation effect, approximately 2τ. This hypothetical span violates that timing requirement; it is not a claim that a correctly dimensioned shared Ethernet permits undetected ordinary collisions this way.
A_ZH: B 的首位在 324+325=649 到达 A，晚于 A 在 576 发完，因此 A 可能误以为没有碰撞。要检测碰撞，发送持续时间须覆盖最坏情况下约 2τ 的往返传播影响。题设链路跨度违反了该时序要求，并不是说尺寸符合要求的共享以太网也必然以这种方式漏检。

@@ N273 | x08-assignments | historical | XNA3:2; XNA3S:5-6
Q_EN: Starting with empty caches on an IPv4 Ethernet host using DHCP, explain the protocol chain to fetch a remote plain-HTTP page. How are the gateway's IP and MAC obtained?
Q_ZH: IPv4 以太网主机使用 DHCP、缓存为空，如何逐步获取远端明文 HTTP 网页？网关的 IP 和 MAC 分别如何获得？
A_EN: DHCP supplies the host address, subnet mask, gateway IP and DNS configuration. Use ARP for a local next hop: the DNS server if on-link, otherwise the gateway. DNS resolves the web name. ARP obtains the gateway MAC if still unknown; TCP establishes a connection, HTTP requests the page, and replies traverse IP routing and link frames. Each router replaces link headers. The gateway IP comes from configuration/DHCP, its MAC from local ARP.
A_ZH: DHCP 提供主机地址、掩码、网关 IP 和 DNS 配置。对本地下一跳使用 ARP：DNS 服务器在同链路则查它，否则查网关。DNS 解析网站名称；网关 MAC 若仍未知，再用 ARP 获取；随后 TCP 建连、HTTP 请求页面，回复通过 IP 路由及链路帧返回。每个路由器重建链路首部。网关 IP 来自配置/DHCP，MAC 来自本地 ARP。

@@ N274 | x08-assignments | historical | XW:3-5
Q_EN: In the historical HTTP capture lab, what evidence supports an answer about request language, destination endpoint, matching response and conditional caching?
Q_ZH: 在历史 HTTP 抓包实验中，回答请求语言、目的端点、对应响应和条件缓存问题时，需要哪些证据？
A_EN: Read Accept-Language when present, IP destination and TCP destination port, then match request/response within the same connection and transaction using packet numbers and timestamps. For caching, inspect the actual conditional header, status and body presence. A repeat request need not always produce 304. Save the trace and exact packet references; do not invent values from a sample screenshot or assume encrypted traffic exposes plaintext HTTP.
A_ZH: 若存在则读取 Accept-Language，查看目的 IP 与 TCP 端口，再用包号、时间戳在同一连接和事务内匹配请求回复。缓存问题要检查实际条件首部、状态码和是否有正文。重复请求并不总返回 304。保存抓包文件和精确包号，不照抄示例截图数值，也不假设加密流量暴露明文 HTTP。

@@ N275 | x08-assignments | historical | XW:6-7
Q_EN: What should a DNS lab record besides the domain's returned IP, and how do you distinguish the responding resolver from the authoritative server?
Q_ZH: DNS 实验除了域名返回的 IP，还应记录什么？如何区分回复解析器与权威服务器？
A_EN: Record query name/type, transaction ID, query/response endpoints, answer records, flags and timing. The server that replies to your host may be a recursive resolver answering from cache, not the authoritative server named by an NS record. Match each response to its query. DNS answers and TTLs depend on time and cache state; learn the method instead of memorizing an old site's numeric address.
A_ZH: 记录查询名/类型、事务 ID、查询与回复端点、答案记录、标志和耗时。向主机回复的可能是从缓存回答的递归解析器，并非 NS 记录所指的权威服务器。应把每个回复对应到查询。DNS 答案及 TTL 随时间和缓存状态变化，应学习分析方法而非背旧网站数字地址。

@@ N276 | x08-assignments | historical | XW:8
Q_EN: In a captured TLS-over-TCP connection, a student treats each Ethernet frame as exactly one TLS handshake message. Why is this unsafe, and what version, reassembly and encryption information must be checked before interpreting ClientHello/ServerHello?
Q_ZH: 抓到一条 TLS-over-TCP 连接后，有人把每个以太网帧都当成恰好一条 TLS 握手消息。为什么不可靠？解释 ClientHello/ServerHello 前，应检查哪些版本、重组和加密信息？
A_EN: A TCP segment, TLS record and handshake message are different units: one may span or contain another. Inspect the negotiated version and the actual trace before describing cipher suites, certificates or session behavior. Packet loss/reassembly and encryption can hide details. Report “not visible in this capture” when appropriate; do not force every TLS version to match the old SSL example or equate one Ethernet frame with one handshake record.
A_ZH: TCP 段、TLS 记录、握手消息是不同单位，可能跨越或包含彼此。先看协商版本和实际抓包，再描述密码套件、证书或会话行为。丢包、重组和加密可能使细节不可见，必要时明确写“本抓包不可见”。不能强行让所有 TLS 版本匹配旧 SSL 示例，也不能把一个以太网帧当作一条握手记录。

@@ N277 | x08-assignments | historical | XW:9; XRTO:3
Q_EN: For the TCP capture exercise, how do you measure an RTT and avoid confusing frame length, TCP header length and TCP payload length?
Q_ZH: TCP 抓包题如何测量 RTT，并避免混淆帧长度、TCP 首部长度与有效载荷长度？
A_EN: Identify a transmitted segment and the ACK that acknowledges its data; subtract their capture timestamps at the same observation point. Retransmissions can make the ACK's correspondence ambiguous, so choose an unambiguous sample and state delayed-ACK effects. Record the exact field used for each length: captured frame, TCP header or tcp.len payload. The lab's trace-specific numeric answers must come from that capture, not a generic handshake diagram.
A_ZH: 找到某次发送及确认其数据的 ACK，在同一观察点用时间戳相减。重传会让 ACK 对应关系不明确，应选无歧义样本并说明延迟 ACK 影响。长度要写清采用的是捕获帧长度、TCP 首部还是 tcp.len 载荷。实验的具体数值必须来自指定抓包，不能从通用握手图猜测。

@@ N278 | x08-assignments | historical | XPROJ:1-2; XPROJ:5
Q_EN: A TCP message-board protocol uses POST/DELETE followed by lines ending with a line containing only #; GET/QUIT are single-line commands, and QUIT requires an OK reply before closing. What client states and receive-buffer behavior implement these rules?
Q_ZH: 一个 TCP 留言板协议规定：POST/DELETE 后接多行，单独一行 # 结束；GET/QUIT 是单行命令，QUIT 要等 OK 回复后关闭。客户端应怎样组织状态与接收缓冲？
A_EN: Connect, await user command, assemble/send that command, receive a complete response, then return to the command state. POST/DELETE collect lines until a line containing only #; GET/QUIT send only the command. After QUIT, wait for the specified OK reply and close. Keep a receive buffer because TCP is a byte stream. These are historical protocol requirements; future Canvas specifications decide any changed terminator or response format.
A_ZH: 先连接，等待用户命令，组装并发送命令，接收完整回复，再回到命令状态。POST/DELETE 收集多行直至仅含 # 的行；GET/QUIT 只发命令。QUIT 后等待规定的 OK 回复再关闭。TCP 是字节流，因此需要接收缓冲。以上是历史协议要求，终止符或回复格式若有变化，以后续 Canvas 说明为准。

@@ N279 | x08-assignments | historical | XPROJ:5-6
Q_EN: What tests reveal a message-board client's protocol bugs before running it against the course server?
Q_ZH: 在对接课程服务器前，哪些测试能发现留言板客户端的协议错误？
A_EN: With a local mock server, split one response across several reads, combine multiple lines in one read, and test empty messages, invalid commands/IDs, unexpected disconnects and QUIT acknowledgement. Verify exact newline/terminator handling and that partial data stays buffered. Handle error replies explicitly; success in one send/one recv example does not establish correct framing. These are AI-added test cases derived from the historical project's error-handling requirements.
A_ZH: 用本地模拟服务器将一个回复拆成多次读取、把多行合并进一次读取，并测试空消息、非法命令/ID、意外断开和 QUIT 确认。核对换行与终止符，确保不完整数据保留在缓冲中，并显式处理错误回复。一次 send/一次 recv 的演示成功不代表分帧正确。这些是根据历史项目错误处理要求补充的 AI 测试思路。

@@ N280 | x01-applications | learn | XW:5; HTTPSEM:15.3.1,15.4.5,15.5.5,15.6.1
Q_EN: What do HTTP status codes 200, 304, 404 and 500 tell you?
Q_ZH: HTTP 状态码 200、304、404、500 分别告诉你什么？
A_EN: 200 indicates success; 304 validates a stored representation after a conditional GET/HEAD without sending its content again; 404 says the server cannot find the target or will not disclose its existence; 500 indicates an unexpected server condition preventing fulfillment. A status describes HTTP processing, not whether the page is scientifically correct or every embedded object loaded successfully.
A_ZH: 200 表示成功；304 在条件 GET/HEAD 后验证已有副本，无须再次发送其内容；404 表示找不到目标或不愿透露其存在；500 表示服务器遇到意外情况而无法完成请求。状态码描述 HTTP 处理结果，不保证网页知识正确，也不证明其中所有嵌入对象都已成功加载。

@@ N281 | x01-applications | worked | XW:5; HTTPSEM:13.1.2-13.1.3,15.4.5
Q_EN: A cached response has ETag "v1". How can a conditional GET avoid downloading unchanged content?
Q_ZH: 缓存响应的 ETag 为 "v1"。条件 GET 怎样避免重复下载未变化的内容？
A_EN: Send `If-None-Match: "v1"`. If the selected representation still matches, the server returns 304 and no content; reuse the validated stored content. Otherwise an ordinary successful GET can return 200 with the new representation. `If-Modified-Since` instead uses a modification date. A repeated URL alone does not guarantee 304: a conditional request and the relevant server-side comparison are required.
A_ZH: 发送 `If-None-Match: "v1"`。若选定表示仍匹配，服务器返回不带内容的 304，可复用经验证的缓存内容；否则普通成功 GET 可返回带新表示的 200。`If-Modified-Since` 则使用修改日期。仅重复访问同一 URL 不保证出现 304，还要有条件请求及服务端相应比较。

@@ N282 | x06-link | learn | XNA3:1-2; ARP:Packet Generation,Packet Reception
Q_EN: What does ARP resolve, and whose MAC address is needed for an off-subnet IPv4 destination?
Q_ZH: ARP 解析什么？IPv4 目的地在子网外时，需要谁的 MAC 地址？
A_EN: On an Ethernet IPv4 LAN, ARP maps a local next-hop IP address to its MAC address. Routing first chooses that next hop: the destination itself if on-link, otherwise a gateway. If the mapping is absent, broadcast an ARP request on that LAN; the target normally replies directly. The IP destination remains the remote host, while the frame destination is the gateway's local MAC. ARP is neither DNS nor an Internet-wide search.
A_ZH: 在以太网 IPv4 局域网中，ARP 把本地下一跳 IP 映射到 MAC 地址。先由路由确定下一跳：同链路时为目标主机，跨子网时为网关。若缺少映射，就在本 LAN 广播 ARP 请求，目标通常直接回复。IP 目的地址仍是远端主机，帧的目的 MAC 却是网关的本地接口。ARP 既不是 DNS，也不是全互联网搜索。

@@ N283 | x06-link | learn | XNT11:2; XNT11S:11
Q_EN: How does a basic Ethernet switch learn addresses and decide whether to forward or flood?
Q_ZH: 基本以太网交换机怎样学习地址、决定转发还是泛洪？
A_EN: In a loop-free LAN, learn source MAC→arrival port from received frames. Look up the destination: a known different port gets a single forwarded copy; the same arrival port needs no forwarding; an unknown destination is flooded to the other eligible ports in that LAN/VLAN. Entries age out. Learning uses the source, forwarding uses the destination. The switch does not learn a host's location merely because another host names it as a destination.
A_ZH: 在无环 LAN 中，从收到的帧学习“源 MAC→入端口”。再查询目的地址：已知且在其他端口就定向转发；在同一入端口则不必转发；未知则向该 LAN/VLAN 的其他可用端口泛洪。表项会老化。学习看源地址，转发看目的地址；别人把某主机写成目的地，并不能让交换机直接学到它的位置。

@@ N284 | x04-ip | learn | XN4:13-20
Q_EN: What does a router's switching fabric do, and why can a router queue packets even when its external links are fast?
Q_ZH: 路由器的交换结构做什么？外部链路很快时，为什么内部仍可能排队？
A_EN: The fabric transfers packets from input ports to selected output ports. Memory, a shared bus and crossbar interconnection are basic designs with different internal contention. If aggregate input exceeds fabric capacity, input queues grow; if many inputs target one slower output, that output queues even with a fast fabric. Distinguish internal transfer capacity from each external link's transmission rate.
A_ZH: 交换结构把分组从输入端口送到选定输出端口。内存、共享总线、交叉互连是基本实现，它们面临不同内部争用。总输入超过交换能力时，输入队列积累；即使内部很快，多路输入集中到较慢的一个出口时，输出仍要排队。内部搬运能力与各条外部链路发送速率是不同瓶颈。

@@ N285 | x04-ip | worked | XN4:19-21
Q_EN: What does the historical buffer-sizing rule B≈C×RTT mean, and why is a larger buffer not automatically better?
Q_ZH: 往年缓冲区经验式 B≈C×RTT 是什么意思？为什么缓冲区越大不一定越好？
A_EN: C in bit/s times RTT in seconds gives a buffer size in bits: 10 Gbit/s×0.25 s=2.5 Gbit. It is a historical sizing heuristic, not a universal requirement; traffic and congestion-control assumptions matter. If Q bits already await service on an R-bit/s FIFO output, their service adds Q/R seconds of waiting. More buffer can absorb bursts but also sustain longer queues; it does not increase link capacity.
A_ZH: C 用 bit/s、RTT 用秒，相乘得到以 bit 计的容量：10 Gbit/s×0.25 s=2.5 Gbit。这是历史经验式，不能当作普遍要求，流量和拥塞控制假设会影响适用性。若 FIFO 出口已有 Q bit 等待，速率为 R bit/s，它们的服务会增加 Q/R 秒等待。更多缓冲能吸收突发，也能维持更长队列，却不增加链路容量。
