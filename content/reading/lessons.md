# 参考书补充 / Reading companion

这些段落、图示与自测是依据所列章节重新编写的教学辅助，不是书中原题或本学期新增考试范围。主课仍从两门课程各自的 learning/authoring.md 构建。OPTIONAL 表示可跳过的书本拓展。

@@ ml01 | 先写一张“任务说明书” | Write a task specification
REFS: mla@§1.4–1.5，印刷页 11–12 / PDF 38–39
FIGURE: ml-workflow
BODY_ZH: 想做一个“识别危险场景”的模型，先别急着挑算法。输入是一帧图像、一个视频片段，还是传感器序列？输出是类别、风险分数，还是未来轨迹？同一句需求会变成不同任务。先在纸上写出输入 x、目标 y、何时预测、错误怎样计分，再选模型。

书中的“收集→准备→分析→训练→测试→使用”适合搭骨架；实际评估还要把划分提前。例如同一次行车的视频帧很相似，随机拆帧可能让训练和测试共享近重复场景。按行程或时间划分，才更接近对新行程的检验。这是将书中流程应用到研究场景的例子。
BODY_EN: Before selecting an algorithm, specify the input, target, prediction time, and error measure. A scene label, risk score, and future trajectory define different tasks.

The book's collect–prepare–analyze–train–test–use workflow is a useful skeleton. Add an explicit split protocol: adjacent frames from one drive may be near duplicates, so splitting by drive or time can better test transfer to unseen trips. This is an original application of the workflow, not a reported experiment.
CHECK_Q: 为什么“测试集没有参与梯度更新”还不足以证明评估独立？ || Why is excluding test data from gradient updates insufficient to establish independent evaluation?
CHECK_A: 测试数据仍可能影响词表、归一化、调参，或与训练样本近重复。需检查整条数据与选择流程。 || Test data can still influence vocabulary, scaling, tuning, or appear as near duplicates. Audit the full data and selection procedure.

@@ ml03 | 把旧书代码翻译成数组语言 | Read legacy code by its operations
REFS: mla@§1.7，印刷页 15–16 / PDF 42–43；§8.3.1，印刷页 165 / PDF 192
BODY_ZH: 旧书大量使用 `numpy.matrix`，其中 `*` 表示矩阵乘；当前课程常用 `ndarray`，其中 `*` 是逐元素乘。把对象换成数组却原样保留 `*`，程序有时仍能运行，但算的东西已变。先写形状，再确认这里要的是内积、矩阵乘还是逐元素操作。

例如两行样本 X=((1,2),(3,4))、w=(2,-1)。要的预测是 `X @ w`=(0,2)；`X * w` 会把每一列分别缩放成 ((2,-2),(6,-4))。书中 `.I` 是逆矩阵写法；解最小二乘时，理解目标和秩条件，比逐字照搬求逆更重要。
BODY_EN: The book frequently uses `numpy.matrix`, whose `*` means matrix multiplication. With `ndarray`, `*` is elementwise multiplication. Replacing the container without checking operators can silently change the computation.

For X with rows (1,2),(3,4) and w=(2,-1), `X @ w` gives predictions (0,2), while `X * w` gives ((2,-2),(6,-4)). Interpret operations and dimensions before translating legacy code; an explicit inverse is not the preferred way to solve least squares.
CHECK_Q: 想把每条样本的特征加权求和，应该检查输出形状是什么？ || What output shape should you expect when taking one weighted feature sum per sample?
CHECK_A: N 条样本应得到 N 个预测，通常形状 (N,) 或 (N,1)，不是 (N,d)。 || Expect N predictions, usually shape (N,) or (N,1), not (N,d).

@@ ml08 | 从一条短信算到一个分类分数 | From tokens to a class score
REFS: mla@§4.5.3–4.5.4，印刷页 71–73 / PDF 98–100 || mlzh@§4.5.3–4.5.4，印刷页 62–64 / PDF 81–83
FIGURE: ml-tokens
BODY_ZH: 固定词表 free、meeting、win，`free free win` 变成 (2,0,1)。若垃圾类词概率为 (4/7,2/7,1/7)，先验 0.4，则去掉跨类相同项后的分数为 $\log 0.4+2\log(4/7)+\log(1/7)$。三次出现贡献三份证据；分数仍须与另一类比较，不能直接叫后验概率。

读书时留意一个实现差异：书中示例将每个词的计数加 1，却把分母初值设为 2。标准 Multinomial 的加一平滑应把分母增加词表大小 V，保证词概率之和为 1；Bernoulli 才是每个词的两种结果使分母加 2，而且要计算未出现词。微课沿用正文的明确模型，不把该简化实现当成两者通用公式。
BODY_EN: With vocabulary (free, meeting, win), `free free win` becomes (2,0,1). For spam token probabilities (4/7,2/7,1/7) and prior 0.4, the class score is $\log 0.4+2\log(4/7)+\log(1/7)$ after dropping class-independent terms. Compare scores before interpreting the prediction.

The book's example adds one to each word count but initializes the denominator to two. Standard add-one multinomial smoothing adds V to the total token count. Bernoulli smoothing adds two per feature and includes absence terms. Keep these observation models distinct.
CHECK_Q: 三词计数 (3,1,0)，每词加一但分母只加二，概率和是多少？ || For counts (3,1,0), what is the probability sum if each count gets one but the denominator gets only two?
CHECK_A: (4+2+1)/(4+2)=7/6，不是 1；标准多项式分母应为 7。 || It is 7/6, not one; the standard multinomial denominator is seven.

@@ ml10 | 书里上升，这里下降，矛盾吗？ | Ascent and descent agree on the objective
REFS: mla@§5.2.1–5.2.2，印刷页 86–89 / PDF 113–116
BODY_ZH: 书中最大化对数似然，用梯度上升；正文最小化负对数似然，用梯度下降。若 L 是对数似然、J=-L，那么 $w+\eta\nabla L=w-\eta\nabla J$，两条更新完全相同。读不同讲义时先看“目标是什么、求最大还是最小”，再判断符号。

把爬山类比说完整：梯度给当前位置的局部方向，不保证迈出任意大的一步都更好。对 J(w)=w²，从 w=1 出发，梯度为 2。学习率 0.1 得 w=0.8、J=0.64；学习率 2 得 w=-3、J=9，跨过谷底太远，反而更差。
BODY_EN: The book maximizes log likelihood by ascent; this lesson minimizes its negative by descent. If J=-L, then $w+\eta\nabla L=w-\eta\nabla J$. Compare objectives before comparing signs.

A gradient is local information, not a guarantee for any step size. For J(w)=w² at w=1, a step size of 0.1 gives w=0.8 and J=0.64; a step size of 2 gives w=-3 and J=9. Overshooting can increase the loss.
CHECK_Q: 将总损失换成平均损失，保持学习率不变，梯度是否一般不变？ || Does replacing summed loss by mean loss generally leave the gradient unchanged at fixed learning rate?
CHECK_A: 不变的是最优点（在相同相对正则约定下），数据梯度缩小为原来的 1/N；每步幅度会改变。 || With compatible regularization scaling, the optimum is unchanged, but the data gradient becomes 1/N as large, changing the update size.

@@ ml12 | 走廊的宽度由最近的点限制 | The nearest points constrain the corridor
REFS: mla@§6.1–6.2，印刷页 102–105 / PDF 129–132
FIGURE: ml-margin
BODY_ZH: 看图中的 x₁=-1 与 x₁=1 两排点。决策线 x₁=0 正好居中，离两边最近点各 1；把线挪到 x₁=0.5，虽然仍然分对，较窄一侧却只剩 0.5。硬间隔优化关心最窄的安全余量，不是所有距离的平均数。

图中 w=(1,0)、b=0，间隔线是 f=-1 和 f=1，总宽度为 2/||w||。远处再添一个已满足间隔的同类点，可以完全不改变这个解；软间隔中则要同时看 C 与违约代价。离边界远是几何证据，不直接等于校准后的正确概率。
BODY_EN: For points at x₁=-1 and x₁=1, the centered boundary x₁=0 has one unit of margin on each side. Moving it to x₁=0.5 preserves correct classification but reduces the smaller margin to 0.5. Hard-margin SVM maximizes the worst clearance.

Here w=(1,0), b=0, and total margin width is 2/||w||. Adding a distant same-class point can leave the solution unchanged. Soft-margin fitting additionally trades violations against C; geometric distance is not a calibrated probability.
CHECK_Q: 对本图把 w 变为 (2,0)、b 仍为 0，原来 x₁=1 点的几何距离是多少？ || If w becomes (2,0) and b stays zero, what is the distance of x₁=1 from the boundary?
CHECK_A: |2|/2=1。分数从 1 变为 2，但直线和距离都没变。 || The distance is |2|/2=1. The score doubles but the boundary and distance do not change.

@@ ml13 | SMO 为什么一次改两个乘子 | Why SMO updates two multipliers
REFS: mla@§6.3.1–6.3.2，印刷页 106–107 / PDF 133–134
BODY_ZH: SVM 对偶要求 $\sum_i\alpha_i y_i=0$。只改一个非零标签对应的乘子，通常立刻破坏这个平衡。SMO 固定其余乘子，选择两个一起调，把大问题拆成可处理的小问题；这不是随意换两个数，还要满足上下界并改善目标。

若两点标签相反，例如 y₁=-1、y₂=+1，那么 -Δα₁+Δα₂=0，二者必须同增或同减；若标签相同，则变化量一增一减。书中“一增一减”的直觉不能脱离标签套用。这里解释约束几何，完整求解器还需选对、裁剪和停止条件。
BODY_EN: The equality constraint $\sum_i\alpha_i y_i=0$ usually prevents changing just one multiplier. SMO holds the others fixed and optimizes a pair while preserving feasibility.

For opposite labels, -Δα₁+Δα₂=0, so the two changes have the same sign. For equal labels, they have opposite signs. The book's increase/decrease intuition must be interpreted with the labels. Pair selection, clipping, and stopping rules are additional implementation steps.
CHECK_Q: 标签 (-1,+1)，从乘子 (0.2,0.2) 改成 (0.3,0.1) 还满足等式约束吗？ || For labels (-1,+1), does changing multipliers from (0.2,0.2) to (0.3,0.1) preserve the equality constraint?
CHECK_A: 不满足，-0.3+0.1=-0.2。若两者都变成 0.3 则仍满足等式，但还须检查 C 上界。 || No: the sum is -0.2. Changing both to 0.3 preserves equality, subject also to the C bounds.

@@ ml15 | 选读：决策树怎样选第一个问题 | Optional: choosing a decision-tree split
OPTIONAL: true
REFS: mla@§3.1，印刷页 39–43 / PDF 66–70 || mlzh@§3.1.1，印刷页 34–36 / PDF 53–55
FIGURE: ml-tree
BODY_ZH: 这是书本拓展，帮助对照线性模型。决策树像连续问“是否满足某条件”。若节点中两类各半，标签最难猜；若全是同一类，就已经很纯。熵 $H=-\sum_c p_c\log_2p_c$ 衡量这种不确定性，约定 0log0=0。选择划分时比较信息增益：父节点熵减去按样本比例加权的子节点熵。

四条样本有两正两负，父熵为 1 bit。某个问题将它们恰好拆成两个纯组，子熵都为 0，增益为 1。若拆完两组仍各含一正一负，增益为 0。一次划分很纯不保证泛化；给每条训练样本一个独特编号也能记住标签，却未必帮助预测新样本。树深和叶子大小仍要验证。
BODY_EN: This optional book extension contrasts trees with linear models. A decision tree asks successive feature questions. Label entropy $H=-\sum_c p_c\log_2p_c$ measures uncertainty, with 0log0=0. Information gain subtracts the size-weighted child entropy from the parent entropy.

Two positive and two negative samples have entropy one bit. Splitting them into two pure groups yields gain one; two equally mixed groups yield gain zero. Training purity alone does not ensure generalization: unique identifiers can memorize labels. Validate depth and leaf size.
CHECK_Q: 90 个样本的子节点熵为 0，10 个样本的子节点熵为 1，加权子熵是多少？ || A split has 90 samples in a child of entropy zero and 10 in a child of entropy one. What is the weighted child entropy?
CHECK_A: 0.9×0+0.1×1=0.1 bit，不能简单平均成 0.5。 || It is 0.1 bit, not the unweighted average 0.5.

@@ ml16 | 分词是一个可检查的实验假设 | Tokenization is a testable modeling choice
REFS: mla@§4.6，印刷页 74–76 / PDF 101–103 || mlzh@§4.6，印刷页 65–67 / PDF 84–86
BODY_ZH: 书中的邮件例子把文本切词、转小写并过滤短词，让分类管线更具体。但“删掉短词”不天然合理：`not`、`no`、货币符号、网址片段可能正是有用证据。先拿五条真实训练短信打印分词前后结果，检查你想保留的意思有没有被删掉。

一个最小实验：`not free` 与 `free` 在仅含 free 的词表中都会变成 (1)。若目标标签不同，任何只看这一向量的分类器都无法区分它们。可以在训练内部比较保留否定词、加入二元词组等方案。书中示范代码先建全体文档词表再划分；严格归纳评估应改成先划分，再只由训练文本建立词表。
BODY_EN: The book makes the spam pipeline concrete through tokenization, lowercasing, and short-word filtering. These choices can remove useful negation, currency symbols, or URL cues. Inspect before/after tokens for actual training examples.

With a vocabulary containing only free, both `not free` and `free` map to (1). No classifier receiving only that vector can distinguish them. Compare retained negation or bigrams within training. Unlike the illustrative book code that builds vocabulary before splitting, an inductive evaluation fits vocabulary after the split using training text alone.
CHECK_Q: 两条语义不同的短信被映射成同一个向量，单纯加深分类器能恢复丢掉的信息吗？ || Can a deeper classifier recover information when two different messages are mapped to the same feature vector?
CHECK_A: 不能从这个向量本身恢复区别；需要改变表示或提供额外信息。 || Not from that vector alone. Change the representation or supply additional information.

@@ ml17 | 选读：AdaBoost 的两套权重 | Optional: two kinds of weights in AdaBoost
OPTIONAL: true
REFS: mla@§7.1–7.2，印刷页 130–133 / PDF 157–160
BODY_ZH: 先学完分类评估，再选读这段。AdaBoost 有两套权重：Dᵢ 决定本轮训练更关注哪些样本；αₜ 决定第 t 个弱分类器在最终投票中的话语权。对 ±1 二分类，令加权错误率 $\epsilon=\sum_iD_i\mathbf{1}[h(x_i)\ne y_i]$，其中 Dᵢ 总和为 1。标准系数为 $\alpha=\frac12\log((1-\epsilon)/\epsilon)$。

当 ε=0.25，α≈0.5493。更新样本权重时乘 $e^{-\alpha y_ih(x_i)}$ 再归一化，分错样本相对分对样本的权重倍率是 e^(2α)=3。注意是加权错误率，并且获得正投票系数需 0<ε<0.5；书中“错误率大于 50% 仍优于随机”的文字不能照记。ε=0 或 0.5 需另行处理，反复追逐错标样本也可能伤害泛化。
BODY_EN: Read this after classification evaluation. AdaBoost's Dᵢ weights training examples; αₜ weights each weak learner in the final vote. For binary labels ±1 and normalized D, use weighted error $\epsilon=\sum_iD_i\mathbf{1}[h(x_i)\ne y_i]$ and $\alpha=\frac12\log((1-\epsilon)/\epsilon)$.

At ε=0.25, α≈0.5493. Updating by $e^{-\alpha y_ih(x_i)}$ and normalizing makes a misclassified example gain a factor of three relative to a correct one. Positive voting weight requires 0<ε<0.5, correcting the book's greater-than-50% wording. Handle boundary cases separately; mislabeled samples can attract excessive attention.
CHECK_Q: 均匀权重的四个样本错一个，更新后该错例和每个对例的权重分别是多少？ || With four equally weighted samples and one error, what are the updated weights of the error and each correct example?
CHECK_A: 权重比例变为 3:1:1:1，归一化后错例 1/2，每个对例 1/6。 || The ratio becomes 3:1:1:1, so the error has weight 1/2 and each correct example 1/6.

@@ ml18 | 归一化真的会换掉最近邻 | Scaling can change the nearest neighbor
REFS: mla@§2.2.3，印刷页 29–30 / PDF 56–57 || mlzh@§2.2.3，印刷页 25–26 / PDF 44–45
FIGURE: ml-neighbors
BODY_ZH: 查询点 q=(0,0)，训练点 A=(1,100)、B=(4,0)。未经缩放，距离约为 100.005 和 4，B 最近。若按训练阶段确定的尺度，将第一维除以 10、第二维除以 1000，A 变成 (0.1,0.1)、B 变成 (0.4,0)，距离变为约 0.141 和 0.4，A 反而最近。

这不是模型“算错”，而是你改变了相似性的定义。书中的归一化例子想说明的正是单位不能偷偷替你决定重要性。这里的尺度为教学给定值；真实流程应只在训练数据拟合。若某维训练最大值等于最小值，还须处理零分母，而不是硬除。
BODY_EN: Let q=(0,0), A=(1,100), and B=(4,0). Raw distances are about 100.005 and 4, so B is nearest. Dividing feature one by 10 and feature two by 1000 gives distances about 0.141 and 0.4, making A nearest.

Scaling changes the definition of similarity. These scales are specified for the example; estimate real preprocessing parameters on training data alone. Constant training features require explicit handling of a zero range.
CHECK_Q: 所有特征一起乘同一个正数，普通欧氏 k-NN 的邻居排序会改变吗？ || Does multiplying every feature by the same positive constant change ordinary Euclidean k-NN rankings?
CHECK_A: 不会，所有距离同乘该常数；不同特征用不同倍率才可能改变排序（忽略数值舍入与平局）。 || No. All distances scale equally. Different feature-wise factors can change rankings, apart from numerical and tie issues.

@@ ml19 | Ridge 给不稳定方向加一点约束 | Ridge stabilizes weakly constrained directions
REFS: mla@§8.3.1，印刷页 164–166 / PDF 191–193
BODY_ZH: 设两列特征完全相同。OLS 只知道两列权重的和应是多少，却分不清功劳属于谁，所以可能有无穷多个权重给出同样预测。L2 惩罚会在这些方案中偏爱较小的平方范数：固定 w₁+w₂=2 时，(1,1) 的范数平方是 2，(2,0) 则是 4。

Ridge 不是免费消除错误，而是用偏差换稳定性。λ 太大可能把真实信号也压小；用验证选择 λ，最终测试留到方案选定后。书中 ridgeTest 将特征除以方差，这是该实现的缩放约定；常用 z-score 除以标准差，两者并不相同。
BODY_EN: With identical feature columns, OLS identifies their weight sum but not the individual contributions. Among coefficients summing to two, (1,1) has squared norm two, versus four for (2,0), illustrating the preference induced by L2 regularization.

Ridge trades bias for stability; excessive λ can suppress real signal. Select λ with validation and reserve the final test. The book's ridgeTest divides by variance, whereas z-score scaling divides by standard deviation. Do not silently equate these conventions.
CHECK_Q: 特征均值 2、方差 4，原值 6；除以方差和除以标准差分别得到多少？ || For mean 2, variance 4, and value 6, compare centering then dividing by variance versus standard deviation.
CHECK_A: 分别为 (6-2)/4=1 和 (6-2)/2=2。 || The results are one and two, respectively.

@@ ml21 | 距离换了，中心更新也可能要换 | Match the center update to the loss
REFS: mla@§10.1，印刷页 208–209 / PDF 235–236
BODY_ZH: 标准 k-means 的均值更新依赖平方欧氏距离。用一组数 (0,0,9) 看得最清楚：平方损失在均值 3 时为 9+9+36=54，在中位数 0 时为 81；如果改成绝对距离和，中心 0 的损失是 9，中心 3 却是 12。

因此“换任意距离仍照样取均值”不能保留原来的下降证明。绝对距离对应中位数；要求中心必须是实际样本时，可考虑 medoid 等不同目标。书中的距离函数接口方便实验，但数学目标、分配规则与中心更新必须配套。聚类也有拟合步骤，只是没有监督标签。
BODY_EN: The mean update in standard k-means depends on squared Euclidean loss. For (0,0,9), center 3 yields squared loss 54, versus 81 at center zero. For absolute loss, center zero yields 9, versus 12 at center 3.

An arbitrary distance change does not preserve the mean update or its descent proof. Absolute loss suggests a median; requiring a center to be an observed sample gives a different optimization problem. Match the objective, assignment, and center update. Clustering still fits a model despite having no labels.
CHECK_Q: “没有标签，所以 k-means 没有训练”准确吗？ || Is it accurate to say that k-means has no training because it has no labels?
CHECK_A: 不准确。中心与分组仍由数据拟合；无监督指缺少监督目标标签，并非不学习参数。 || No. Centers and assignments are fitted from data; unsupervised means no supplied target labels, not no fitting.

@@ ml23 | PCA 的坐标、重构与压缩成本 | Coordinates, reconstruction, and storage
REFS: mla@§13.1–13.2，印刷页 270–274 / PDF 297–301；§14.6，印刷页 295–297 / PDF 322–324
FIGURE: ml-pca
BODY_ZH: 点 (1,1) 投到单位方向 v=(1,1)/√2，得分是 √2，重构为 √2v=(1,1)。点 (1,-1) 的得分为 0，重构到原点，两个坐标的信息全丢了。图中的长轴适合保留大方差，却不能保证保住区分类别的方向；标签可能恰好藏在短轴上。书中的分类改善是例子，不是 PCA 的保证。

SVD 压缩则给出更直观的账本。m×n 矩阵原有 mn 个数，秩 k 因子可用 Uₖ、k 个奇异值和 Vₖ 共 k(m+n+1) 个数存储。100×80、k=5 时为 905 个，而不是 8000 个。这个比较忽略元数据、精度与编码；真正图像压缩还要看码率和重构质量，不能只数维度。
BODY_EN: Projecting (1,1) onto v=(1,1)/√2 gives score √2 and exact reconstruction. Projecting (1,-1) gives zero and loses that point's displacement. Large variance need not mean strong class discrimination; useful labels may lie along a low-variance direction.

A rank-k SVD representation stores k(m+n+1) values rather than mn when storing Uₖ, k singular values, and Vₖ. For a 100×80 matrix and k=5, that is 905 rather than 8000. This excludes metadata and coding precision; compression quality also matters.
CHECK_Q: 均值不是零时，低维得分乘回方向就完成重构了吗？ || If the data mean is nonzero, is multiplying scores by directions sufficient for reconstruction?
CHECK_A: 还要加回训练均值：$\hat x=\mu+V_kV_k^T(x-\mu)$。 || Add back the training mean: $\hat x=\mu+V_kV_k^T(x-\mu)$.

@@ net03 | 把流水线画成三条工作日程 | A packet pipeline as a schedule
REFS: kuro@§1.3.1，印刷页 23–26 / PDF 34–37；§1.4.1，印刷页 35–39 / PDF 46–50
FIGURE: net-pipeline
BODY_ZH: 三条等速链路像三道工序：每道处理一包需 2 ms，下一道必须收到整包才开始。包 1 占用三道的时段分别为 0–2、2–4、4–6 ms；与此同时，包 2 已能在第一条链路的 2–4 ms 时段发送。流水线节省的是不同包的工作重叠，并没让单包少过任何一跳。

图中四个包在 12 ms 全部完成。若第二条链路变慢，后续包会等它空闲，等速公式就失效。可逐格使用“本包到齐时间与本链路空闲时间取较大值，再加发送时间”；有传播时延时，再把它加到下一节点的到达时间。
BODY_EN: Three equal-rate links act as three stages, each serializing a packet in 2 ms. Packet 1 uses intervals 0–2, 2–4, and 4–6 ms, while packet 2 can already use the first link during 2–4 ms. Different packets overlap; an individual packet still traverses every hop.

Four packets finish in 12 ms. With unequal rates, compute each transmission start as the later of packet availability and link availability, then add serialization; add propagation to obtain arrival at the next node.
CHECK_Q: 图中 t=4 到 6 ms，三条链路分别发送哪个包？ || Which packet occupies each link from t=4 to 6 ms in the diagram?
CHECK_A: 第一条发包 3，第二条发包 2，第三条发包 1。 || Link 1 sends packet 3, link 2 packet 2, and link 3 packet 1.

@@ net04 | 同样的平均负载，排队可以完全不同 | Equal mean load, different queues
REFS: kuro@§1.4.2，印刷页 39–40 / PDF 50–51
FIGURE: net-queue
BODY_ZH: 设每包发送需 1 ms，队列初始为空。四个包在 0、2、4、6 ms 到达，各自无需排队；若四个包都在 0 ms 到达，就分别等待 0、1、2、3 ms，平均 1.5 ms。两种模式都每 8 ms 重复一次时，平均到达率和负载都一样，ρ=0.5。

区别在“何时到达”，不是总共有多少包。书中的突发例子补上了只背 ρ=La/R 容易漏掉的机制：平均速率没有告诉你突发性、包长分布或缓冲大小，所以不能单凭 ρ 算出唯一平均等待时间。
BODY_EN: Suppose each packet takes 1 ms to serialize and the queue starts empty. Arrivals at 0,2,4,6 ms incur zero waiting. Four arrivals at time zero wait 0,1,2,3 ms, averaging 1.5 ms. Repeating either pattern every 8 ms gives the same mean load, ρ=0.5.

Arrival timing differs despite equal average work. Mean load alone omits burstiness, length distribution, and buffer size, so it does not uniquely determine average queueing delay.
CHECK_Q: 同时到达的 n 个等长包，每包发送需 s 秒，平均排队时间是多少？ || For n equal packets arriving simultaneously at an idle link, each taking s seconds to transmit, what is mean queueing delay?
CHECK_A: 等待为 0,s,…,(n-1)s，平均为 (n-1)s/2；不含自身发送时间。 || Waiting times are 0,s,…,(n-1)s, averaging (n-1)s/2, excluding each packet's own serialization.

@@ net05 | HTTPS 保护什么，又不证明什么 | What HTTPS protects
REFS: http@§7.1–7.2，PDF 135–155 || tls13@§1.2、§2、Appendix E.8
BODY_ZH: 将 HTTPS 分成三个问题更容易记：怎样确认服务器身份，怎样协商通信密钥，怎样保护后续数据。证书把名称与公钥等信息绑定，并需验证信任链、名称等条件；对称密钥用于高效保护通信内容。这不等于网站内容一定真实，也不自动证明登录用户的身份。

《图解 HTTP》中的 SSL 与握手图用于理解历史背景。TLS 1.3 不再使用静态 RSA 密钥传输；常见证书认证握手结合临时密钥协商与签名，不能照搬“用服务器公钥加密一个会话密钥”描述所有 HTTPS。HTTP/1.x 的明文报文练习和现代加密连接应分开理解。
BODY_EN: Separate server authentication, key agreement, and protection of subsequent data. A certificate binds an identity to public-key information and requires validation; symmetric keys efficiently protect traffic. HTTPS does not establish that a website's claims are true or automatically authenticate its users.

The illustrated book's SSL diagrams are historical. TLS 1.3 removes static RSA key transport; common certificate-authenticated handshakes combine ephemeral key agreement and signatures. Do not describe every HTTPS connection as encrypting a session key with the server's public key.
CHECK_Q: 有效 HTTPS 证书能证明网页中的一篇文章没有事实错误吗？ || Does a valid HTTPS certificate prove an article on that site is factually correct?
CHECK_A: 不能。通信身份与通道保护，不等于内容事实核验。 || No. Authentication and channel protection are distinct from factual verification of content.

@@ net06 | 同一个服务器端口怎样接待多个连接 | Many connections can share one server port
REFS: kuro@§3.2，印刷页 187–193 / PDF 198–204
BODY_ZH: 端口像服务入口，但一台服务器的 443 端口可以同时服务许多客户端。普通 TCP 连接用源 IP、源端口、目的 IP、目的端口这个四元组区分。例如同一客户端用端口 51000 和 51001 分别连向同一服务器 443，就是两个不同连接。

服务器的监听入口负责接新连接，已建立的连接各有状态。于是“目的端口一样”既不意味着同一连接，也不意味着应用消息可以随意混在一起。再往上一层，消息如何定界仍由应用协议决定，TCP 四元组不会告诉你 HTTP 正文在哪里结束。
BODY_EN: A server can handle many TCP connections on port 443. A conventional TCP connection is identified by source IP, source port, destination IP, and destination port. Two source ports, 51000 and 51001, distinguish two connections to the same server endpoint.

The listening endpoint accepts connections; established connections maintain separate state. A shared destination port does not imply a shared byte stream. Application framing still determines message boundaries.
CHECK_Q: 两个不同客户端都使用源端口 51000 连接同一服务器 443，一定冲突吗？ || Must two clients using source port 51000 conflict when connecting to the same server port 443?
CHECK_A: 不一定；源 IP 不同则四元组不同。此处讨论普通 TCP 端点模型，NAT 映射是另一层处理。 || No. Different source IPs give different four-tuples. NAT mapping is a separate consideration.

@@ net07 | 缓存的三个结局：直接用、问一下、重新拿 | Three cache outcomes
REFS: kuro@§2.2.4–2.2.5，印刷页 105–113 / PDF 116–124 || http@§2.8、§6.3.1，PDF 45–47、85–89 || cache@§4.2–4.3、§5.2.2.4–5.2.2.6
FIGURE: net-cache
BODY_ZH: 把缓存当作带版本号的课件副本：仍新鲜且允许直接复用，就从本地拿；需要验证且有 ETag，就带 `If-None-Match` 问版本是否改变。未改可返回 304，沿用旧正文；已改则通常返回 200 和新正文。图中的三条路分别省下不同成本。

两个名字尤其容易误解：响应 `Cache-Control: no-cache`（不带字段参数）允许存储，但每次复用前必须成功验证；`no-store` 要求缓存不存储。这里按 RFC 9111 澄清书中正文与译注的混淆。Cookie 又是另一件事：请求里的状态标记可让应用关联会话，“HTTP 无状态”并不禁止服务器维护会话数据库。
BODY_EN: Treat a cache as a versioned copy. A fresh response may be reused when policy permits. If validation is required and an ETag is available, send `If-None-Match`: an unchanged representation can produce 304 and reuse the body; a changed one normally produces 200 with new content.

An unqualified response `no-cache` allows storage but requires successful validation before reuse; `no-store` forbids cache storage. This follows RFC 9111 and resolves confusing wording in the illustrated book. Cookies address session association instead: HTTP statelessness does not forbid an application's session database.
CHECK_Q: 已缓存的响应带 no-cache，但年龄只有 1 秒，能否仅因“很新”直接复用？ || May a cached response with no-cache be reused without validation just because it is only one second old?
CHECK_A: 不可，仍需成功验证；这条指令不只针对已经过期的响应。 || No. Successful validation is required; the directive is not limited to stale responses.

@@ net09 | DNS 缓存和网页缓存装的是不同东西 | DNS and web caches store different answers
REFS: kuro@§2.4.2，印刷页 125–131 / PDF 136–142
BODY_ZH: DNS 缓存回答“这个名字对应哪个记录”；HTTP 缓存回答“这个资源的哪个响应还能复用”。DNS 命中不会自动得到 HTML；HTTP 命中也不等于 DNS 所有记录都有效。把两种缓存画成不同抽屉，比统称“浏览器有缓存”更容易算时延。

例如解析器最终 A 记录命中，主机只等 2 ms 的本地解析交互；随后仍可能需要 TCP 建连和 HTTP 请求。反过来，页面副本可直接本地复用时，某次访问可能根本不需要发起新的 DNS 查询。每道题先列出这次实际走了哪些步骤，再累加。
BODY_EN: DNS caches name records; HTTP caches reusable resource responses. A DNS hit does not provide HTML, and an HTTP hit does not establish DNS freshness.

A cached final A record may reduce resolution to a 2 ms local exchange while TCP and HTTP still remain. Conversely, a directly reusable local response may avoid a new DNS lookup entirely. Count the operations actually required by the stated cache conditions.
CHECK_Q: 权威服务器更新记录后，已有有效 TTL 的递归缓存一定立即更新吗？ || Must a recursive cache update immediately after an authoritative record changes if its cached TTL remains valid?
CHECK_A: 不一定；缓存可能继续使用旧记录直到到期或刷新，TTL 不是全球同步刷新时钟。 || No. It can retain the prior record until expiry or refresh; TTL is not a global synchronization clock.

@@ net12 | DASH：下载速度与播放速度在赛跑 | DASH: downloads race the playback clock
REFS: kuro@§2.6.2–2.6.3，印刷页 144–149 / PDF 155–160
BODY_ZH: 视频不是等全部下载完才播放，而是边下载片段边消耗缓冲。假设一个片段代表 2 秒视频，编码码率 3 Mbps，大小约 6 Mbit。可用吞吐量若为 4 Mbps，下载需 1.5 秒；稳态下这段时间播放消耗 1.5 秒，下载完成后增加 2 秒，缓冲净增约 0.5 秒。

若吞吐量降为 2 Mbps，同一片段需 3 秒，缓冲净少约 1 秒，持续下去会卡顿。DASH 在可选码率与缓冲状态之间权衡；CDN 则改变内容从哪里来。这个例子忽略请求开销和码率波动，不表示播放器只按一次测速立即切换。
BODY_EN: Streaming downloads segments while playback consumes buffered time. A two-second segment at 3 Mbps contains about 6 Mbit. At 4 Mbps throughput it downloads in 1.5 seconds, adding roughly 0.5 seconds to the buffer in steady playback.

At 2 Mbps it takes three seconds, reducing buffered time by about one second. DASH adapts among representations using throughput and buffer information; a CDN changes content location. This example omits request overhead and variable segment sizes, not a complete adaptation algorithm.
CHECK_Q: 已有 4 秒缓冲，随后两个片段都按上述 2 Mbps 下载且不中断播放，缓冲约剩多少？ || Starting with four seconds buffered, after two such segments download at 2 Mbps without playback interruption, how much buffer remains?
CHECK_A: 每片净少 1 秒，两片后约 2 秒；按给定简化条件计算。 || About two seconds, losing one second per segment under the stated model.

@@ net13 | 窗口要大到足以填满等待时间 | Size a window to cover feedback delay
REFS: kuro@§3.4.2–3.4.4，印刷页 211–223 / PDF 222–234
FIGURE: net-recovery
BODY_ZH: 停等的问题是“发完后还没等到反馈”。沿用正文 1 Gbps、8000 bit、传播 RTT=30 ms，每包发送 8 μs，第一次 ACK 在 30.008 ms 返回。要让发送方连续工作到该时刻，窗口至少为 ceil(30.008/0.008)=3751 包。带宽时延积 R×RTT 约为 30 Mbit，说明高速长路径需要较多在途数据。

图中 0、1、2、3 已发，1 丢失。若 ACK 正常到达、2 和 3 已被接收，基础 GBN 仍丢弃这两包，超时后重发 1、2、3；SR 缓存并分别确认 2、3，只需补 1。节省重传的代价是更多接收状态与序号管理；TCP 的具体行为不能简单等同基础 GBN。
BODY_EN: At 1 Gbps with 8000-bit packets and 30 ms propagation RTT, serialization takes 8 μs and the first ACK returns after 30.008 ms. Continuous sending until that feedback needs at least ceil(30.008/0.008)=3751 packets. The bandwidth-delay product is about 30 Mbit.

For packets 0–3 with packet 1 lost, basic GBN discards 2 and 3 and retransmits 1–3 on timeout. With successful ACK delivery, SR buffers and acknowledges 2 and 3, retransmitting only 1. Saving transmissions requires extra receiver state; TCP is not simply basic GBN.
CHECK_Q: 为什么按 R×RTT/L 得到 3750，而精确到这个停等反馈周期时需要 3751？ || Why does R×RTT/L give 3750 while this exact feedback-cycle calculation needs 3751?
CHECK_A: 这里 RTT 只含往返传播，还须把第一个包的发送时间 L/R 计入首次 ACK 返回时刻。 || Here RTT contains propagation only; the first packet's serialization time must also be included before its ACK returns.

@@ net14 | ACK 说明到货，不说明应用已消费 | Arrival and application consumption differ
REFS: kuro@§3.5.5，印刷页 246–248 / PDF 257–259
FIGURE: net-window
BODY_ZH: 接收端像有容量限制的收件柜：网络把字节放进去，应用稍后取走。简化模型中缓冲总量 8 kB，已有 5 kB 未被应用读取，则剩余接收窗口约 3 kB。即便数据已经被 TCP 确认，它仍可能占着柜子，应用慢读会令 rwnd 变小。

发送端还有另一笔账：有多少字节已发但未确认。正文的 min(cwnd,rwnd)-在途量用于给定当前窗口的发送额度估计；不要把接收缓冲的已占用量再当作发送在途量扣第二次。窗口是字节量，除以 RTT 才得到受窗口限制的速率估计。
BODY_EN: Think of the receive buffer as a delivery locker. TCP can acknowledge bytes while the application has not yet read them. In a simplified 8 kB buffer containing 5 kB of unread data, about 3 kB remains available for flow control.

The sender separately tracks sent-but-unacknowledged bytes. The lesson's min(cwnd,rwnd)-in-flight calculation estimates additional sending allowance; do not subtract receiver occupancy again as if it were sender in-flight data. Windows measure bytes, not bytes per second.
CHECK_Q: 应用再读走 2 kB、期间没有新数据进入，图中可用缓冲变为多少？ || If the application reads 2 kB with no new arrivals, how much free buffer remains in the diagram?
CHECK_A: 已占用从 5 降到 3 kB，可用从 3 升到 5 kB。 || Occupancy falls to 3 kB and free space rises to 5 kB.

@@ net16 | 最长前缀像地址从城市细化到街道 | Longest prefix chooses the most specific match
REFS: kuro@§4.2.1，印刷页 314–316 / PDF 325–327；§4.3.2，印刷页 333–344 / PDF 344–355
FIGURE: net-prefix
BODY_ZH: 目的 10.1.2.99 同时属于 10.0.0.0/8、10.1.0.0/16 和 10.1.2.0/24。它们不是三条相互矛盾的指令，而是由粗到细的覆盖范围；/24 更具体，因此优先。默认路由 /0 是没有更具体匹配时的后备。

“/26 有 64 个地址”还需配合对齐：最后一个字节的块从 0、64、128、192 开始。192.0.2.130/26 落在 128–191，不能随意选 130–193 当作它的子网。图中嵌套关系用于解释前缀，不按真实地址数量比例绘制。
BODY_EN: Destination 10.1.2.99 matches /8, /16, and /24 entries shown in the figure. These describe nested scopes; /24 is most specific. A default /0 route applies when no more specific match exists.

A /26 contains 64 addresses but must also align to its prefix boundary. Last-octet blocks start at 0,64,128,192, so 192.0.2.130/26 lies in 128–191, not 130–193. The diagram shows nesting, not address-space area to scale.
CHECK_Q: 若删除图中的 /24，但保留 /16 和 /8，目的 10.1.2.99 选哪个？ || If the /24 entry is removed but /16 and /8 remain, which entry is selected for 10.1.2.99?
CHECK_A: 选择仍匹配且最长的 /16。 || Select the still-matching /16 entry.

@@ net17 | 路径长度与第一跳分别存什么 | Distance, predecessor, and next hop
REFS: kuro@§5.2.1–5.2.2，印刷页 383–395 / PDF 394–406
FIGURE: net-routing
BODY_ZH: 跟着图中的原例子走：从 A 出发，先确定 B=2；经 B 改善 C=3、D=6；再确定 C，把 D 改到 4。最终 D 的前驱是 C，但 A 发往 D 的下一跳是 B。前驱像倒着追踪来路，下一跳才是当前路由器马上执行的动作。

距离向量的坏消息则可能让邻居互相相信对方仍有路：A 以为“B 能到”，B 的旧估计却本来就依赖 A。Poisoned reverse 把经某邻居到达的目的，向该邻居通告为无穷，能避免这一类二节点循环；它并不保证消除三节点以上的所有环路。
BODY_EN: Starting at A, fix B at cost 2, improve C to 3 and D to 6, then fix C and improve D to 4. D's predecessor is C, but A's next hop toward D is B. Predecessors reconstruct a path; next hops drive forwarding.

Distance-vector failures can involve neighbors relying on each other's stale routes. Poisoned reverse advertises infinity back to a neighbor used as the next hop for that destination, preventing this two-node dependency. It does not eliminate all larger loops.
CHECK_Q: 将原图 AC 的代价从 5 降为 1，其余不变，从 A 到 D 的路径和代价变成什么？ || If edge AC falls from 5 to 1 with all other costs unchanged, what is A's shortest path and cost to D?
CHECK_A: A-C-D，代价 1+1=2，下一跳为 C。 || A-C-D at cost two, with next hop C.

@@ net18 | CRC 检查通过，为什么仍不是绝对无错 | Passing CRC does not prove no error
REFS: kuro@§6.2.3，印刷页 459–461 / PDF 470–472
BODY_ZH: 合法码字 C 可被生成多项式 G 整除。若传输翻转形成错误模式 E，接收串为 C XOR E。由于模二运算的线性关系，若 E 也可被 G 整除，接收串仍会通过检查。这解释了“余数为零”表示没有检出的错误，而不是已经证明没有任何错误。

沿用正文码字 1101001、生成式 1011。在其上 XOR 错误模式 0001011，收到 1100010。该错误模式恰好就是 G 的对齐副本，因此仍可整除。不要由这一反例推断 CRC 无用：具体生成式可保证检出指定类别的错误，但检测并不等于纠错或恶意篡改认证。
BODY_EN: A valid codeword C is divisible by generator G. After an error pattern E, the received word is C XOR E. If E is also divisible by G, the received word still passes the modulo-two check.

Using codeword 1101001 and generator 1011, XOR with 0001011 yields 1100010, which also passes. This shows that zero remainder means no detected error, not proof of perfect delivery. A specified generator detects important error classes; CRC is neither arbitrary error correction nor cryptographic authentication.
CHECK_Q: 发送方与接收方使用不同的生成式，是否还能套用同一个 CRC 余数判断？ || Can sender and receiver use different generators and still apply the same CRC divisibility check?
CHECK_A: 不行。必须先约定相同生成式及编码约定，否则合法性判断没有共同基础。 || No. They must agree on the generator and encoding conventions.

@@ net20 | 用四张“小纸条”串起网页访问 | Four pieces of information connect the fetch
REFS: kuro@§6.7，印刷页 512–517 / PDF 523–528 || http@§1.4–1.6，PDF 19–24 || http3@§2、§3.1
FIGURE: net-addresses
BODY_ZH: 先把四张纸条分开：DHCP 配置告诉主机“我是谁、网关和 DNS 在哪”；ARP 告诉它“本地下一跳的 MAC 是什么”；DNS 给出“网站名字对应的地址记录”；HTTP 描述“我要哪个资源”。缺哪张纸条就补哪一步，已知或缓存有效时不必每次全部重来。

图采用远端 DNS、远端网站、IPv4 以太网、无 NAT、明文 HTTP/1.x 的教学场景，所以先 ARP 网关，再发 DNS 查询，之后 TCP 和 HTTP。若是 HTTPS over TCP，还需 TLS；HTTP/3 则在 QUIC 上运行，不能机械套三次 TCP 握手。QUIC 的独立流减少了因一个流缺数据而阻塞其他流交付的问题，但不消除拥塞或应用依赖。
BODY_EN: Keep four answers separate: DHCP supplies host and service configuration; ARP resolves a local next-hop MAC; DNS resolves name records; HTTP requests a resource. Reuse valid known information rather than assuming every fetch starts empty.

The figure assumes remote DNS and web servers, IPv4 Ethernet, no NAT, and cleartext HTTP/1.x: ARP for the gateway precedes DNS, then TCP and HTTP. HTTPS over TCP adds TLS; HTTP/3 uses QUIC, not a TCP handshake. Independent QUIC streams reduce cross-stream delivery blocking, not congestion or application dependencies.
CHECK_Q: 网站和 DNS 都在远端且网关 MAC 已有效缓存，换一个新网站一定要再发 ARP 吗？ || If both DNS and the website are remote and the gateway MAC is validly cached, must visiting a new website trigger another ARP?
CHECK_A: 不必。若本地下一跳仍是同一网关，就可以复用该 MAC；新网站可能仍需 DNS 查询。 || No. The same next-hop MAC can be reused; the new name may still require DNS resolution.
