# 零基础入口：每节先走一个小场景，再进入正式讲解

@@ ml01
START: 想做一个短信分拣员：看到“free prize”时，是放进收件箱，还是垃圾箱？计算机不能凭生活经验判断，我们先给它可计算的描述，再用带答案的例子教它。 || Imagine sorting messages into an inbox or a spam folder. A computer needs measurable descriptions and examples with known answers before it can learn a decision rule.
STEP1: 一条短信就是一个样本。长度、free 出现次数等可测量属性叫特征；“正常/垃圾”这个训练答案叫标签。 || One message is one sample. Measurable properties are features; its known category is the training label.
STEP2: 把 100 条短信中的 80 条用于学习规则，10 条用于挑方案，另 10 条留到最后检查。这里的数量仅作流程示例。 || For illustration, use 80 messages to fit a rule, 10 to choose a setup, and 10 for final evaluation.
STEP3: 学习的目标是处理未见短信。像做练习、订正方法、再做闭卷测验：三个环节有不同职责。 || The goal is performance on unseen messages: practice, choose an approach, then take a held-out test.
TRAP: “模型”是学到的计算规则，并不一定是神经网络；“准确率高”也不等于能找出少数类。 || A model need not be a neural network, and high accuracy can hide failure on a minority class.

@@ ml02
START: 先把 Python 当成一位只按指令办事的助手。我们要它计算 12 除了 1 和自身之外有几个因数，就必须把“试除—判断—计数”说清楚。 || Treat Python as an assistant following explicit instructions. Counting divisors of 12 means trying candidates, checking remainders, and counting successes.
STEP1: `n = 12` 保存数字；`12 % 3 == 0` 得到 True，表示除以 3 没有余数。赋值 = 与比较 == 是不同动作。 || `n = 12` stores a value; `12 % 3 == 0` tests divisibility. Assignment and comparison are different operations.
STEP2: `range(2,12)` 依次给出 2 到 11；循环逐个检查，命中 2、3、4、6，共四个。终点 12 不包含在 range 中。 || Loop over 2 through 11. The successful candidates are 2, 3, 4 and 6; the range stop is excluded.
STEP3: 把这段过程装成函数：输入 n，`return` 计数。以后换成 n=7，同一规则返回 0；函数是可复用的步骤，不是只服务于 12。 || Package the steps as a function returning a count. The same procedure returns zero for 7.
TRAP: Notebook 像一张共享草稿纸，变量会留下来。读到的“第一个单元”未必是实际最后执行的操作。 || Notebook variables persist. Display order does not tell you the actual execution history.

@@ ml03
START: 把数组想成一张小表：两行是两条短信，两列是“free 次数”和“长度分数”。先问每个数代表什么，再写矩阵符号。 || Think of an array as a table: two messages in rows, with free-count and a length score in columns. Give entries meaning before using matrix notation.
STEP1: 设两行为 (1,2)、(3,4)，权重为 (2,-1)。第一条短信得分是 1×2−2=0，第二条是 3×2−4=2。 || Rows (1,2) and (3,4), weighted by (2,-1), produce scores 0 and 2.
STEP2: `X @ w` 把这两次同样的计算一起做完：输入形状 (2,2)，权重 (2,)，输出 (2,)。一个输出对应一个样本。 || Matrix multiplication batches the two calculations. A (2,2) matrix times a (2,) vector returns one score per row.
STEP3: 绘图也要先认清“一个点是什么”。散点图保留每对坐标；直方图把数值分组计数。Tutorial 1 的因数图就在练这个区别。 || A scatter plot retains coordinate pairs; a histogram counts values in bins. The divisor exercise practices this distinction.
TRAP: 行列不是装饰。把列向量和一维数组相减，可能产生所有样本的两两差，而不是每条样本自己的误差。 || Shape changes meaning: a column minus a one-dimensional array can produce pairwise differences instead of matched errors.

@@ ml04
START: 想象把一支斜向箭头照到水平地面上。影子表示“沿水平方向能解释多少”，箭头尖到影子尖的竖直部分是剩余信息。这个垂直投影的直觉会贯穿最小二乘和 PCA。 || Project a tilted arrow onto a horizontal line. Its shadow is the horizontal component; the perpendicular remainder is what that direction cannot explain.
STEP1: 向量 v=(3,4) 表示横向走 3、纵向走 4。沿水平轴的投影是 (3,0)，不是一个没有方向的数字 3。 || For v=(3,4), the horizontal projection is the vector (3,0), not merely the number 3.
STEP2: 用 u=(2,0) 当方向尺，需要系数 1.5 才有 1.5u=(3,0)。尺子变长，系数会变，实际影子不变。 || Using u=(2,0) requires coefficient 1.5. Rescaling the direction changes the coefficient, not the projection vector.
STEP3: Gram–Schmidt 对每个新箭头减掉已有方向的影子，再把剩余箭头缩成长度 1。这就是“正交”加“归一”。 || Gram–Schmidt removes projections onto earlier directions, then scales the remaining vector to unit length.
TRAP: 残差为零说明没有新方向，不能再除以它的长度。正交是垂直，归一是长度为 1，两者要分别检查。 || A zero remainder contains no new direction. Orthogonality and unit length are separate requirements.

@@ ml05
START: “垃圾短信常含 free”不等于“含 free 的短信大多是垃圾”。像“猫常有四条腿”不能倒推“四条腿的动物大多是猫”：筛选的人群变了。 || “Spam often contains free” does not imply “most messages containing free are spam.” Reversing the condition changes the population being counted.
STEP1: 从 1,000 条短信出发：垃圾 200 条，正常 800 条。先验就是看到关键词之前的这份比例。 || Start with 200 spam and 800 legitimate messages. These proportions are the prior.
STEP2: free 留下垃圾中的 60%，即 120 条；同时留下正常中的 10%，即 80 条。观察词语像一道筛子。 || The word keeps 120 spam and 80 legitimate messages. Think of the observation as a filter.
STEP3: 现在只在留下的 200 条中数：垃圾占 120/200=60%。贝叶斯公式就是把这次重新计数写成通用形式。 || Recount within the 200 retained messages: 120/200=60% are spam. Bayes' rule expresses this calculation generally.
TRAP: 分母必须包含所有能产生该证据的类别，不能只看目标类别的数量。 || The denominator includes every class that can produce the evidence, not only the class of interest.

@@ ml06
START: 有一枚不知道是否公平的硬币，抛四次得到“正、正、反、正”。最大似然问：哪一个正面概率 p 最能解释这串已发生的结果？ || A coin produces heads, heads, tails, heads. Maximum likelihood asks which heads probability best explains that observed sequence.
STEP1: 假设各次独立，这串顺序在 p=0.5 下的概率是 0.5⁴=0.0625。 || Under independence, the sequence probability at p=0.5 is 0.0625.
STEP2: 若 p=0.75，概率是 0.75³×0.25≈0.1055，更大。导数进一步告诉我们，这个例子的最佳 p 正好是 3/4。 || At p=0.75 it is about 0.1055. Differentiation confirms that 3/4 is the maximizer here.
STEP3: 数据始终没变，变化的是待选参数。换成高斯数据时，同样选择最能解释观测的中心和散布。 || The data stay fixed while the candidate parameter varies. A Gaussian model similarly selects its center and spread.
TRAP: 这不表示“p=0.75 的概率是 0.1055”。似然评价参数怎样解释数据，不是直接给参数分配概率。 || A likelihood is not the probability that the parameter itself equals 0.75.

@@ ml07
START: 同班学生的身高和臂展可能一起增大。分别记录“身高有多分散”和“臂展有多分散”，还没记录两者怎样一起变化；这正是协方差补上的信息。 || Height and arm span may increase together. Their separate variances omit this joint pattern; covariance adds it.
STEP1: 看一个点离均值多远之前，先问该方向平时有多分散。标准差为 2 的方向偏离 2，与标准差为 1 的方向偏离 1，都偏离一个标准差。 || A deviation of 2 along a standard-deviation-2 axis equals a deviation of 1 along a standard-deviation-1 axis in standardized units.
STEP2: 对角协方差只保留各轴散布；非零的交叉协方差还能让二维密度椭圆倾斜。 || A diagonal covariance keeps axis-wise spread; cross-covariance can tilt density contours.
STEP3: 每个类别可以有自己的椭圆，也可以被要求共用同一种形状。不同限制改变参数量和分类边界。 || Classes may have separate covariance shapes or share one. The restriction changes parameter count and decision boundaries.
TRAP: 零协方差只排除线性共同变化；需要联合高斯等附加条件，才能由它推出独立。 || Zero covariance rules out linear association, not all dependence, unless additional assumptions apply.

@@ ml08
START: “free free win”有三次词元，但只有两种词出现过。先决定你要记录次数，还是只记录有没有，才能决定用哪种概率模型。 || “free free win” contains three tokens but two distinct present words. Choose the representation before choosing the probability model.
STEP1: 词表按 free、meeting、win 排列。计数是 (2,0,1)，是否出现是 (1,0,1)。顺序必须固定。 || With vocabulary free, meeting, win, counts are (2,0,1) and presence flags are (1,0,1).
STEP2: Bernoulli 像逐个打勾的清单；Multinomial 像把三张词元票分给词表中的格子。它们统计的对象不同。 || Bernoulli uses a checklist; multinomial modeling allocates token occurrences among vocabulary entries.
STEP3: 未见过 win 不等于 win 永远不可能出现。平滑预留一点概率，使单个未见词不把整类分数直接压成零。 || Smoothing reserves probability for unseen events so one unseen word does not force a class likelihood to zero.
TRAP: “free free”不能在二元出现表示中变成两次独立的出现证据；表示决定模型能看到什么。 || A binary indicator cannot retain repeated-word counts. Representation determines which evidence remains available.

@@ ml09
START: 把每篇等暴露量文档当作一个观察窗口，数单词出现了几次。Poisson 模型像数每个窗口里的来客数：0、1、2……都是合法结果。 || Treat each equal-exposure document as an observation window and count occurrences. A Poisson variable models nonnegative counts within such a window.
STEP1: 某类四篇文档的计数为 (0,1,3,0)，平均每篇一次，估计率为 1。这个率不是“该词至少出现一次的概率”。 || Counts (0,1,3,0) yield an estimated rate of 1, not a probability of at least one occurrence.
STEP2: 率为 1 时，零次的概率为 exp(−1)≈0.368；一次也约为 0.368。一个均值对应整套计数概率。 || With rate 1, both zero and one occurrence have probability about 0.368. A mean determines the whole count distribution.
STEP3: 分类时，看观测次数在每个类别的率下有多合理，再加入类别先验；多个词的证据在对数空间累加。 || Compare the observed counts under each class's rates, add the prior, and accumulate evidence in log space.
TRAP: 不同文档长度会影响计数。独立 Poisson 的建模假设与固定总词数的 Multinomial 不同。 || Document exposure matters. Independent Poisson counts differ from a multinomial model conditioned on total length.

@@ ml10
START: 假设一个评分器给短信打分：分数越高越像垃圾，但分数 2 不能解释成 200% 概率。逻辑回归先打分，再把分数压到 0 与 1 之间。 || A classifier may give a message score 2, but that is not 200% probability. Logistic regression converts a score into a probability.
STEP1: 初始分数 z=0，sigmoid 给 p=0.5。这个转换像一把刻度弯曲的尺，不是简单截断。 || Score zero maps to probability 0.5 through a smooth sigmoid, rather than clipping.
STEP2: 若真实标签 t=1，预测 p=0.5 还不够肯定。交叉熵会鼓励提高这个真实类别的概率。 || For target t=1, cross-entropy encourages the model to raise the true-class probability.
STEP3: 对 x=2，梯度为 (0.5−1)×2=−1。学习率 0.1 时减去梯度，w 从 0 变为 0.1，正类概率随之上升。 || For x=2 the gradient is −1. A learning-rate-0.1 update moves w from 0 to 0.1 and raises the positive probability.
TRAP: 梯度是“损失向哪里增大”，所以最小化时反向走；负梯度不等于权重必须减小。 || A gradient points toward increasing loss. Subtracting a negative gradient increases the weight.

@@ ml11
START: 选超参数像选学习方法：不能只用它练过的题打分，也不能反复偷看最终考试来改方法。交叉验证让不同训练子集轮流担任小测验。 || Hyperparameter selection needs unseen practice tests. Cross-validation rotates held-out subsets while preserving a final untouched test set.
STEP1: 每个候选在相同的折上比较，先完成该折训练，再看该折验证分数；预处理也随折重新拟合。 || Compare candidates on the same folds, fitting preprocessing only within each training portion.
STEP2: 从二类变成三类时，可给三类各打一个分数。分数 (log 2,0,0) 指数化后为 (2,1,1)。 || For three classes, logits (log 2,0,0) exponentiate to weights (2,1,1).
STEP3: Softmax 将总共四份权重归一化为 (1/2,1/4,1/4)。它比较相对分数，所以一起加同一个常数不会改变结果。 || Normalize the four weight units to probabilities (1/2,1/4,1/4). A common logit shift leaves them unchanged.
TRAP: 三个独立二分类器的原始概率不会天然构成同一套和为 1 的多类概率。 || Separate binary classifier outputs do not automatically form one normalized multiclass distribution.

@@ ml12
START: 在红点和蓝点之间放一道隔离线。只要求分对，可以有很多条线；SVM 进一步寻找离两边最近样本都尽量远的那条线。 || Many lines may separate red and blue points. An SVM favors a separator with a wide margin to the nearest examples.
STEP1: 在一维上，负类点为 −1，正类点为 +1。中间 x=0 是边界，两侧最近点各距它 1。 || For negative point −1 and positive point +1, the midpoint boundary is zero and both points are one unit away.
STEP2: 两侧间隔线之间宽度是 2，但单侧到边界的距离是 1。先说明自己在量哪种距离。 || The full corridor is two units wide; each side's margin is one unit.
STEP3: 若点重叠，软间隔允许付出代价进入走廊甚至分错。C 决定违约代价的权重。 || With overlap, soft margins permit violations at a cost weighted by C.
TRAP: 把分数整体放大，并不会把实际几何距离变大；距离必须除以权重向量的长度。 || Multiplying every score does not widen the geometric margin; normalize by the weight-vector length.

@@ ml13
START: 先用一维问题理解约束的“价格”：最小化 x²，但必须 x≥1。若没有限制会选 x=0；限制把最优点推到 x=1。 || Minimize x² subject to x≥1. Without the constraint choose zero; the constraint pushes the optimum to one.
STEP1: 写 L=x²+λ(1−x)，其中 λ≥0。驻点条件 2x−λ=0，在 x=1 得 λ=2。 || Use L=x²+λ(1−x). Stationarity gives λ=2 at x=1.
STEP2: 此时限制刚好卡住解，称为活跃约束。互补松弛 λ(1−x)=0 在这里成立。 || The constraint is active at the optimum, and complementary slackness holds.
STEP3: SVM 为每个样本配一个这样的乘子。再消去 w、b，问题就变成选择各样本影响力的对偶问题。 || SVMs attach a multiplier to each sample constraint; eliminating w and b produces the dual problem.
TRAP: “价格”只是帮助理解敏感性的类比，乘子仍由数学条件决定；约束取等号也可能配零乘子。 || The price analogy is not a separate rule: an active constraint can still have a zero multiplier.

@@ ml14
START: 一条直线分不开“靠近原点”和“远离原点”的点，但若多测量一个平方距离特征，原来的弯曲边界可能变成直的。核方法利用这种换表示的想法。 || Measuring squared distance can make an origin-centered curved boundary linear in a richer feature representation. Kernels exploit such changes of representation.
STEP1: 对二维 x，加入 x₁²、x₁x₂、x₂²，相当于给每条样本增加“组合测量”。 || Squared and cross-product features add new measurements to each sample.
STEP2: 若算法只需要新特征之间的内积，就可直接计算这个内积，而不显式保存所有新坐标。 || If only feature inner products are needed, compute them without explicitly storing every new coordinate.
STEP3: 例如二次核先算原内积 11，再平方得 121；下面会逐项验证它与显式映射完全相同。 || A quadratic kernel squares an inner product of 11 to get 121; the formal example verifies the explicit map.
TRAP: 相似度不是越花哨越好。合法核要满足半正定条件，模型仍需验证，数据规模仍会带来计算成本。 || A valid kernel needs positive semidefiniteness, and kernel models still need validation and computation.

@@ ml15
START: 比较两个邻居，一个人的身高差 0.1 米，收入差 1,000 元。若直接把两项数值平方相加，收入几乎完全决定“距离”，只是因为单位不同。 || A height difference of 0.1 meters and an income difference of 1,000 currency units have incomparable raw scales. Units can dominate distance.
STEP1: 标准化先问“离训练均值有几个训练标准差”，把各列放到更可比的刻度上。 || Standardization measures deviations in training-standard-deviation units.
STEP2: 把红、绿、蓝写成 0、1、2 又暗示了顺序和等距；one-hot 用独立指示格避免这种人为顺序。 || Integer color codes imply order and spacing; one-hot indicators avoid that invented ordering.
STEP3: 每次改变表示，只改一个因素，再用相同验证集比较。这样才能知道改进来自哪里。 || Change one representation choice at a time and compare on the same validation data.
TRAP: 尺度相同不表示信息同样重要；标准化也不应提前利用测试集统计量。 || Equal scale does not mean equal relevance. Test statistics must not be used to fit preprocessing.

@@ ml16
START: 一个垃圾短信过滤器总分很好，你仍可能每天收到诈骗信息。先把错误拆开，才能知道它是在漏掉危险短信，还是误封正常通知。 || A high overall score can coexist with missed scam messages. Separate types of errors before deciding what to improve.
STEP1: 真实垃圾共 10 条，找出 6 条，召回率为 6/10=60%：问的是危险信息找回多少。 || Finding 6 of 10 actual spam messages gives 60% recall.
STEP2: 总共拦了 8 条，其中 6 条真是垃圾，精确率为 6/8=75%：问的是拦下来的结果有多可靠。 || If 6 of 8 blocked messages are spam, precision is 75%.
STEP3: 查看漏掉和误拦的原文，提出一项可检验改动，例如保留否定词，然后重新做相同验证比较。 || Read false negatives and false positives, propose one testable change, and repeat the same validation protocol.
TRAP: 指标方向不能靠分母猜。先用一句话说清楚“我现在数的是哪一群短信”。 || State which population forms the denominator before calculating a metric.

@@ ml17
START: 当被追问“为什么选这个模型”，只报模型名字很难继续。把解释组织成一条因果链：数据长什么样，假设是什么，预测怎样得到，哪里会失败。 || To explain a model choice, connect the data, assumptions, prediction rule, and possible failures rather than listing model names.
STEP1: 先用具体任务开头：“我根据单词出现情况分类短信”，而不是从一串公式开始。 || Start with the task: classify messages from word-occurrence features.
STEP2: 再解释“条件独立让类分数能分解、容易估计”，并指出词语相关时这是假设近似。 || Explain how conditional independence simplifies class scoring, then acknowledge correlated words.
STEP3: 最后换一个条件：若误封正常短信代价更高，应提高拦截门槛，而非直接声称概率模型更准确。 || Change one condition: more costly false positives call for a higher decision threshold, not an accuracy claim.
TRAP: 流利背诵与理解不同。能说明一个反例，或解释一个条件变化后的结果，才说明论证能经受追问。 || Fluent recall is different from explaining a counterexample or a changed-condition result.

@@ ml18
START: 不先训练一条复杂分界线，而是问：“附近几个已知样本怎么分类？”k-NN 像向最相似的已知案例借经验。关键是相似的定义。 || k-NN asks nearby known examples for a vote instead of first fitting a global boundary. The definition of nearby is crucial.
STEP1: 三个近邻标签为 A、B、B，普通投票给 B 两票，预测 B。 || Labels A, B, B produce a majority vote for B.
STEP2: 若 A 距离仅 0.1，两个 B 距离均为 1，按距离倒数加权时，票重变为 10 对 2，预测反而是 A。 || At distances 0.1, 1 and 1, inverse-distance weights give A ten units and B two.
STEP3: 所以先规定特征尺度、距离、k 和投票规则，才能复现“最近邻”的答案。 || Specify scaling, distance, k, and the voting rule to make the prediction reproducible.
TRAP: 更近的案例未必标签更可靠；小 k 也更容易被噪声或异常样本影响。 || Nearby labels can be noisy, and small k is particularly sensitive to individual examples.

@@ ml19
START: 根据房屋面积预测价格，通常不能让每个样本都落在同一条直线上。最小二乘是在所有候选直线中，选择总体偏差较小的一条。 || A price-versus-area line rarely passes through every observation. Least squares chooses a line by its total squared prediction errors.
STEP1: 每个点都有“预测−真实”的残差。残差 1 和 −1 不能相加抵消，因此先平方再累加。 || Squaring prevents positive and negative residuals from canceling.
STEP2: 对 (0,1)、(1,3)、(2,5)，直线 y=1+2x 恰好通过三个点，平方残差总和为 0。 || The line y=1+2x fits (0,1), (1,3), (2,5) with zero squared residual.
STEP3: 有噪声时通常做不到零误差；正规方程寻找让任何微小系数调整都不能继续降低目标的位置。 || With noise, normal equations identify a stationary fit even when zero error is impossible.
TRAP: 矩阵求逆形式需要可逆条件；样本很多也可能包含重复或共线特征。 || An inverse formula needs invertibility. Many samples do not rule out collinear features.

@@ ml20
START: 多数点靠近一条趋势线，但传感器偶尔报出极离谱的数。平方损失把大偏差放大，单个异常点就可能拉动整条线。 || A faulty sensor can produce an extreme outlier. Squared loss magnifies its influence on an otherwise reasonable trend.
STEP1: 残差从 1 变为 10，平方损失由 1 变为 100；它不是只严重十倍。 || Increasing a residual from 1 to 10 increases squared loss from 1 to 100.
STEP2: RANSAC 先用很少的点拟合候选，再问有多少其他点落在允许误差内，寻找彼此一致的一组。 || RANSAC fits a small sample, then counts other points consistent with that candidate.
STEP3: 若各次独立抽到内点的概率为 0.5，用两点拟合时一次抽到全内点的概率仅 0.25，所以要多次尝试。 || With independent inlier probability 0.5, a two-point sample is all-inlier with probability 0.25.
TRAP: “远离模型”不自动等于“坏数据”。阈值和模型本身也可能不适合真实结构。 || A model outlier is not automatically bad data; the model or tolerance can be wrong.

@@ ml21
START: 给几家住得分散的住户设置两个取件点。住户想选近的点，管理者又想把取件点放在服务住户的中心；这两个决定相互依赖。 || Place two pickup centers for several homes. Homes choose nearby centers, while center locations depend on which homes they serve.
STEP1: 一维住址为 0、2、8、10，取件点先放在 0 和 10。按最近距离分为 {0,2} 和 {8,10}。 || With initial centers 0 and 10, homes split into {0,2} and {8,10}.
STEP2: 将取件点移到各组平均位置 1、9。总平方距离由 8 降为 4。 || Moving centers to means 1 and 9 reduces total squared distance from 8 to 4.
STEP3: 再分组、再移动，直到按所用停止规则结束。现实取件点可能有道路或容量限制，基础 k-means 暂不包含它们。 || Repeat assignment and updates. Basic k-means omits real-world road and capacity constraints.
TRAP: 这个类比对应的是平方距离目标，不能把“中心取平均”直接套到所有距离度量。 || The mean update belongs to squared Euclidean distance, not every possible distance measure.

@@ ml22
START: 两台机器都生产同类零件，但记录丢了“来自哪台”的标签。观察一个零件尺寸，只能说它更像哪台机器的产物，不能立即确定归属。 || Two machines produce parts, but origin labels are missing. A measured size may support one machine more strongly without determining its origin.
STEP1: 某零件对两个成分的加权密度为 0.12 和 0.08，除以总和 0.20，得到责任度 0.6 和 0.4。 || Weighted component densities 0.12 and 0.08 normalize to responsibilities 0.6 and 0.4.
STEP2: 重估机器平均尺寸时，这个零件分别贡献 0.6 份和 0.4 份，而不是硬塞给其中一台。 || The part contributes fractional weights of 0.6 and 0.4 to the component updates.
STEP3: 用新参数重新估计归属，再重新统计。EM 就这样在隐含归属与模型参数之间交替。 || Recompute responsibilities with the new parameters and repeat the updates.
TRAP: 责任度是当前模型给出的解释，不是重新发现了真实标签；似然上升也不证明找到了全局最优。 || Responsibilities are model-based assignments, and increasing likelihood does not imply a global optimum.

@@ ml23
START: 一群点排成斜长的云。用水平尺或垂直尺各看一次，不如把尺子转到云延伸的方向：一个坐标就能保留大部分变化。 || For an elongated diagonal point cloud, rotating a ruler along the cloud can preserve much of the variation in one coordinate.
STEP1: 先移到数据中心，把“整体偏在哪里”与“围绕中心怎样变化”分开。 || Center the data to separate its location from its variation.
STEP2: 沿候选单位方向投影，比较投影坐标的方差。第一主成分选择方差最大的方向。 || Compare variance along unit projection directions; the first component maximizes it.
STEP3: 两个方向方差为 9 和 1 时，只留第一个保留 90% 总方差，但丢掉了第二个方向的信息。 || Keeping the variance-9 direction out of variances 9 and 1 retains 90% of total variance.
TRAP: 方差大不等于对分类有用；一个变化很小的方向，也可能恰好区分两个类别。 || High variance does not guarantee predictive relevance; a low-variance direction can separate classes.

@@ ml24
START: 一条生产线先混合 x 和 y，再乘一个放大系数 z。想知道最终输出变坏是谁造成的，就沿着每一步的影响往回算，而不是猜责任。 || A small computation first adds x and y, then multiplies by z. Backpropagation traces how each local change affects the output.
STEP1: 对 f=(x+y)z，x=−2、y=5、z=−4，先得到中间值 3，再得到输出 −12。 || The forward pass computes x+y=3 and f=−12.
STEP2: 中间值增加一点，输出变化率为 z=−4；x 或 y 各增加一点，都会把中间值增加同样多。 || The local derivative through multiplication is −4; each input changes the sum at rate one.
STEP3: 因此对 x、y 的偏导均为 −4，对 z 为 3。神经网络把同样的链式法则应用到更大的计算图。 || The derivatives are −4, −4 and 3. Neural networks apply the same chain rule to larger graphs.
TRAP: 反向传播算梯度，优化器才更新参数。这两个动作不能混为一谈。 || Backpropagation computes gradients; the optimizer uses them to update parameters.

@@ ml25
START: 用一个小窗口寻找图像里的边缘：同一套局部检测规则在左上角有用，通常也希望它能移到右下角使用。这就是卷积权重共享的动机。 || A local edge detector should work at many image locations. Convolution shares the same local weights across positions.
STEP1: 先看一维简例：数据 (1,2,4)，窗口权重 (1,−1)。不翻核的互相关在两个位置给出 −1、−2，检测相邻变化。 || For (1,2,4), cross-correlation with (1,−1) returns −1 and −2 at two positions.
STEP2: 输入长度 3、窗口长 2、步长 1，没有填充时只放得下两个完整窗口。输出尺寸是在数合法起点。 || A length-2 window fits at two starts in a length-3 input without padding.
STEP3: 二维图像按高和宽分别数；RGB 再将三个通道的贡献相加。换一个滤波器，就得到另一张特征图。 || Count starts along both image axes, sum input-channel contributions, and use additional filters for additional output maps.
TRAP: 这里的小例子是互相关。数学卷积要翻转核，原题要求哪种运算就用哪种。 || This example is cross-correlation; mathematical convolution reverses the kernel.

@@ ml26
START: 训练像不断根据练习反馈调整策略：一次看多少题、每次改多少、何时停，是三个不同决定。先把这些旋钮分开，才能定位训练为什么失败。 || Batch size, update size, and stopping time control different aspects of training. Separate these choices when debugging.
STEP1: 1,000 个样本，每批 100 个、每批更新一次，走完一个 epoch 要更新 10 次。 || One epoch contains ten updates for 1,000 samples and batch size 100.
STEP2: 学习率决定每步走多远；momentum 还记住之前的方向；正则化则改变偏好的模型。 || Learning rate controls step size, momentum retains past direction, and regularization changes model preference.
STEP3: 用保留率 0.8 的 inverted dropout，保留时把激活乘 1.25，平均值才与原激活一致。 || Inverted dropout with keep probability 0.8 scales retained activations by 1.25.
TRAP: 关闭梯度记录不等于进入评估模式；dropout 和 BatchNorm 的训练/评估行为仍需正确切换。 || Disabling gradient recording does not switch dropout or BatchNorm into evaluation behavior.

@@ ml27
START: 看一张有两个人的街景：问“有人吗”、问“人在哪里”、问“哪些像素是人”、问“哪一块属于第一个人”，是四个不同任务。 || A street image can be classified, localized, semantically segmented, or separated into individual instances. These are different output tasks.
STEP1: 分类输出类别；检测给框；语义分割给像素类别；实例分割还给每个对象不同身份。 || Classification gives labels, detection gives boxes, semantic segmentation gives pixel classes, and instance segmentation separates objects.
STEP2: 模型输出形式改变，标注、损失和评价规则也必须跟着改变。不能拿整图准确率评价边界是否画得准。 || Changing the output requires matching annotations, losses, and metrics.
STEP3: 恢复模糊图像又是另一类任务：输出是一幅图，像素误差只是评价它的一种角度。 || Image restoration outputs an image; pixel error measures only one aspect of its quality.
TRAP: 一张看起来漂亮的重构可能添加不存在的细节。视觉好看与忠实恢复需要分别检查。 || An attractive reconstruction may invent details; perceptual quality and fidelity are different criteria.

@@ ml28
START: 分类器问“这像什么”，生成模型问“怎样产生这样的样本”。会画出一张像猫的图，并不等于能计算任意图片的精确概率。 || Classification assigns a label; generation produces samples. Sampling a plausible cat does not require evaluating every image's exact density.
STEP1: GAN 让生成器和判别器交替学习：一方改变样本，另一方改变判断，双方目标都受对方影响。 || GAN training alternates a generator and discriminator, each changing the other's learning problem.
STEP2: 扩散先规定加噪过程，再训练模型从带噪输入估计去噪所需的信息。 || Diffusion specifies a forward noising process and learns information for reversing it.
STEP3: 若信号保留系数为 0.6、噪声系数为 0.8，x₀=2、噪声=1，则带噪值为 2；结果碰巧相同，过程仍然加了噪声。 || With coefficients 0.6 and 0.8, signal 2 and noise 1 produce 2. Equal numerical values do not mean no noise was added.
TRAP: 去噪模型并不知道新生成样本的“真实原图”。生成是在学到的分布下逐步采样。 || A generative denoiser does not know a hidden ground-truth original for each new sample.

@@ ml29
START: 查询资料时，你先提出需求，再比较索引，最后取回内容。注意力的 query、key、value 分别承担相似角色，但实际都是学习到的向量。 || Attention resembles querying an index and combining retrieved content: queries, keys and values are learned vectors, not literal text fields.
STEP1: 一个 query 对两个 key 的分数为 (log 3,0)，softmax 给它们 3/4 和 1/4 的权重。 || Scores (log 3,0) produce weights 3/4 and 1/4.
STEP2: 若两个 value 是 2、10，组合结果为 3/4×2+1/4×10=4。分数决定取多少，value 决定取什么。 || Values 2 and 10 combine to 4. Scores decide how much; values supply the content.
STEP3: 每个 query 都各做一次这样的选择，所以会产生一个“谁关注谁”的矩阵。 || Repeating this for each query creates a matrix of pairwise attention weights.
TRAP: 权重加起来为 1，不代表输出是分类概率，也不保证注意力权重就是可靠的因果解释。 || Normalized attention weights do not make the output a class probability or a causal explanation.

@@ ml30
START: 长题往往不是新公式，而是把几个熟悉动作串在一起。先给中间量起名，就像把一段难读的长代码拆成小函数。 || Long problems often compose familiar operations. Naming intermediate quantities makes a derivation easier to track.
STEP1: 若损失是“一个括号的平方”，先把括号写成 q，外层变化率就是 2q。 || For a squared expression q², the outer derivative contributes 2q.
STEP2: 再分别计算 q 对各变量的导数，把两段变化率相乘；不要同时在脑中展开所有项。 || Differentiate q with respect to each input, then apply the chain rule.
STEP3: 算完用极简单输入或有限差分检查方向和数量级；证明题则逐一检查可逆、独立、正定等前提。 || Check simple inputs or finite differences; for proofs, audit assumptions such as invertibility or independence.
TRAP: 同时梯度更新要使用同一份旧参数。先改一个变量再计算另一个导数，会变成另一种算法。 || Simultaneous gradient updates use the same old parameters, not partially updated ones.

@@ net01
START: 打开一个远端网页，电脑并不是把整张网页沿一根直达网线搬回来。它与服务器交换消息，消息被分成网络可以逐段转送的数据。 || Opening a remote page involves exchanging messages through several networks, not moving a whole page over one direct cable.
STEP1: 浏览器和服务器应用在两端主机上运行。Wi-Fi 或网线首先把你的设备接入附近网络。 || Browser and server applications run on endpoint hosts; Wi-Fi or Ethernet provides local access.
STEP2: 路由器像路口，逐包决定下一段出口；链路负责把比特送过这一段。 || Routers choose the next output for packets; links carry bits across individual segments.
STEP3: 协议是双方约定的说话规则：什么格式算请求、什么回复算成功、没有回复时怎么办。 || A protocol specifies message formats, responses, and actions when events occur.
TRAP: Web 是互联网承载的应用之一；连上 Wi-Fi 也只说明本地接入成立，不证明远端服务可达。 || The Web is one Internet application. A Wi-Fi connection alone does not prove remote reachability.

@@ net02
START: 想象十条固定预约车道与一条大家轮流使用的大车道。电路交换预留份额，分组交换按当前需求共享；共享省下空闲份额，也带来竞争。 || Circuit switching reserves capacity like fixed appointments; packet switching shares capacity among current demand, saving idle allocations but creating contention.
STEP1: 总速率 1 Mbps，每个连接固定预留 100 kbps，只能预留十份，用户此刻不说话也占着份额。 || A 1 Mbps link supports ten reserved shares of 100 kbps, even when a reservation is idle.
STEP2: 分组方式让正在发送的人使用链路。但同时需求超过容量时，包只能排队或被丢弃。 || Packet sharing uses capacity on demand; simultaneous excess demand queues or drops packets.
STEP3: 经过存储转发设备时，一个包要先收齐再发下一跳。不同包则可以在不同链路同时工作。 || Store-and-forward waits for a complete packet at each hop, while different packets can occupy different links simultaneously.
TRAP: 共享提高利用效率，没有创造额外物理带宽。对所有用户同时满速的保证仍受容量限制。 || Sharing improves utilization without creating capacity or guaranteeing full rate to everyone simultaneously.

@@ net03
START: 把一个包想成一列进入长桥的小车。把整列车放上桥要时间，第一辆车开到桥对岸也要时间；两种时间可以重叠。 || Think of a packet as vehicles entering a long bridge: injecting the whole convoy and crossing the bridge take different, overlapping amounts of time.
STEP1: 包长 L 比特，速率 R 比特/秒。L/R 是把所有比特送入链路的时间。 || L/R is the time needed to inject all L bits at rate R.
STEP2: 链路长 d，信号速度 s。d/s 是某个已发出比特到另一端的传播时间。 || d/s is the travel time of an already transmitted bit.
STEP3: 若发送需 6 ms、传播需 5 ms，首位约 5 ms 到达，末位在 11 ms 到达；不是每一位各再加一次 6 ms。 || With 6 ms serialization and 5 ms propagation, the first bit arrives around 5 ms and the last at 11 ms.
TRAP: 车队类比只帮助区分时间，不表示信号真是一辆辆有间距的汽车。计算仍按题目的比特模型。 || The convoy is an analogy; use the stated bit-transmission model for calculations.

@@ net04
START: 三段水管串联，中间最细的一段限制长期出水速度；再把其他两段加粗，出水也未必变快。网络瓶颈有类似的容量限制。 || In a series of pipes, the narrowest section limits sustained flow. Increasing capacity elsewhere may not improve throughput.
STEP1: 路径速率为 20、5、10 Mbps，理想单流持续吞吐量最多 5 Mbps，不是把三段相加。 || A 20/5/10 Mbps path has ideal sustained single-flow throughput at most 5 Mbps.
STEP2: 即使长期平均不超载，一群包同时到达也会排队。平均值没有描述突发时刻。 || A low long-run load can still produce queues when packets arrive in bursts.
STEP3: 当前包还剩 3 ms 服务，前方另有四个各需 6 ms 的包，新包要等 3+4×6=27 ms 才能开始。 || A 3 ms remainder plus four queued 6 ms packets creates a 27 ms wait before service starts.
TRAP: 吞吐量问“每秒交付多少”，时延问“这一件等多久”，两者不能互相替代。 || Throughput measures delivery rate; delay measures completion time for a particular item.

@@ net05
START: 寄一件包裹时，物品说明、收件人、运输单和当前运输车辆各有职责。网络分层同样让每一层解决一个范围明确的问题。 || Network layers divide communication responsibilities, much like item instructions, recipient information, transport labels, and a local carrier serve different roles.
STEP1: 应用消息说“要哪个网页”；传输端口帮助找到服务端应用；IP 地址说明跨网络要到哪里。 || Application messages name the request, ports identify application endpoints, and IP addresses guide inter-network delivery.
STEP2: 每一跳的链路层再回答“当前这段交给谁”，物理层把信息编码成可传播信号。 || Link addressing selects the local next hop, while the physical layer carries signals.
STEP3: 封装是在载荷外加本层说明，不是修改网页内容；中间路由器通常重建链路封装再转发。 || Encapsulation adds control information; routers normally replace link framing as they forward packets.
TRAP: 比喻里的“地址”不全是同一种地址：应用名字、端口、IP、MAC 分别解决不同定位问题。 || Names, ports, IP addresses, and MAC addresses identify different aspects of communication.

@@ net06
START: 同一栋楼里有很多办公室。知道楼的位置还不够，还要找到接待业务的窗口；IP 与端口的组合有类似作用。 || Reaching a building is not enough to locate a particular office. IP addresses and ports similarly identify a network endpoint more precisely.
STEP1: Socket 是程序访问通信服务的接口。服务器监听一个端口，客户端主动联系它。 || A socket is a program's communication interface; a client contacts a listening service.
STEP2: TCP 像保证顺序的连续字节传送带，但不替应用划分消息；UDP 保留每个数据报的边界，却不自带可靠重传。 || TCP provides ordered bytes without message boundaries; UDP preserves datagrams without built-in reliable retransmission.
STEP3: 下载文件可以等迟到的数据，实时语音可能已经错过播放时刻。先看应用需要什么，再选服务。 || A download may wait for late bytes, while real-time audio can miss its playback deadline.
TRAP: 端口不是用户身份，TCP 可靠也不表示加密；定位、交付、安全是不同问题。 || Ports do not authenticate users, and TCP reliability does not encrypt data.

@@ net07
START: 浏览器先拿到一份“购物清单”般的 HTML，才知道还要哪些图片。算网页完成时间，要尊重这份依赖顺序。 || The base HTML reveals which additional objects are needed, like a shopping list. Completion time follows those dependencies.
STEP1: 简化非持久 HTTP 模型中，一个 RTT 建 TCP，一个 RTT 请求到响应开头，再加正文传输。 || The simplified non-persistent model uses one RTT to connect, one for request/response start, then body transfer.
STEP2: 三个很小对象串行取回需 6 RTT；一条无流水线持久连接只建一次，需 1+3=4 RTT。 || Three tiny sequential objects take 6 RTTs with separate connections or 4 RTTs with one persistent connection.
STEP3: 缓存像已有副本。ETag 是副本的版本标记；询问版本是否仍匹配后，304 可省正文，验证往返仍要花时间。 || An ETag identifies a representation version. A 304 validation saves body transfer but still involves communication.
TRAP: 这些 RTT 计算明确忽略 DNS、TLS 和 TCP 动态行为；不能把它当作所有网页的精确计时公式。 || These RTT counts omit DNS, TLS, and TCP dynamics; they are not universal page-load timing formulas.

@@ net08
START: 发邮件像把信交给邮局：对方邮局收到了，不表示收件人已经拆信。投递与读取是两段不同流程。 || Email delivery resembles handing a letter to a postal service. Acceptance by the recipient's server does not mean the person has read it.
STEP1: 用户代理把邮件交给服务器；服务器之间使用 SMTP 传递邮件。 || A user agent submits mail, and SMTP transfers it between mail servers.
STEP2: 接收者之后用 IMAP、POP3 或网页邮箱访问已存邮件。Webmail 的浏览器一段使用 HTTP/HTTPS。 || The recipient accesses stored mail through IMAP, POP3, or HTTP/HTTPS webmail.
STEP3: SMTP 的信封地址用于投递；正文前显示的 From/To 是消息内容字段。信封与信纸上的地址可以不同。 || SMTP envelope addresses guide delivery; visible From/To headers belong to the message and can differ.
TRAP: RETR 是取邮件，DELE 是标记删除；下载一封邮件本身并不必然把服务器副本删掉。 || Retrieving mail does not itself delete the server copy; deletion is a separate operation.

@@ net09
START: 你知道网站名字，但通信还需要地址。DNS 像分层查找的名录：先找负责范围，再找管理具体记录的人。 || DNS resolves names through delegated responsibility, like a directory that points to the organization holding the relevant record.
STEP1: 主机把问题交给本地递归解析器；它可能已有有效缓存，直接回答。 || The host asks a recursive resolver, which may answer from a valid cache.
STEP2: 冷缓存简化模型中，解析器依次询问根、TLD、权威服务器；这些请求是三组问答，不是主机自己到处询问。 || In a simplified cold-cache lookup, the resolver makes three upstream exchanges with root, TLD, and authoritative servers.
STEP3: 加上主机与解析器一组问答，共八条消息。计时则把每个串行问答的 RTT 各加一次。 || Including the host–resolver exchange yields eight messages; sum one RTT per serial exchange for timing.
TRAP: 根服务器通常给下一步的线索，不是亲自保存或查询所有网站的最终地址。 || A root server normally provides delegation information rather than resolving every hostname to its final address.

@@ net10
START: 一道题写“传输完成”，先别急着找公式：它可能问第一位到达、最后一位到达，或一整个文件到齐。先把终点事件说清楚。 || Before selecting a formula, determine whether completion means first-bit arrival, last-bit arrival, or arrival of an entire file.
STEP1: 两条等速链路、三个等长包，每包发送时间 t。第一包先在链路 1 用一格，再在链路 2 用一格。 || With two equal-rate links, the first packet uses one transmission slot on each link.
STEP2: 第一包进入链路 2 时，第二包可同时进入链路 1。两个设备能同时处理不同包。 || Once packet 1 uses link 2, packet 2 can use link 1 concurrently.
STEP3: 三个包分别在 2t、3t、4t 到达，不是各走两格后再启动下一包。画时间轴就能看见重叠。 || The packets arrive at 2t, 3t, and 4t. A timeline reveals the overlap.
TRAP: 流水线公式不能无条件搬到不同链路速率或不同包长；那时要重新排事件时间。 || Unequal link rates or packet sizes require a new event timeline rather than the simplest pipeline formula.

@@ net11
START: “网页慢”只是一条现象，像“门口排长队”可能因为窗口少、单人业务慢，也可能突然来了很多人。需要能区分原因的证据。 || A slow page is an observation, not a cause. Like a queue, it may reflect limited capacity, slow service, or a burst of demand.
STEP1: 把总时间拆成 DNS、连接、等待首字节、正文传输等阶段，先找时间花在哪里。 || Separate DNS, connection setup, first-byte waiting, and transfer time.
STEP2: 若只记录“总共 2 秒”，还不能说明带宽是瓶颈；服务器处理也可能占掉大部分时间。 || A two-second total alone cannot establish a bandwidth bottleneck; server processing may dominate.
STEP3: 固定资源与实验条件，比较冷缓存和热缓存等明确变化，并保留多次测量。 || Compare controlled changes such as cold versus warm caches and retain repeated measurements.
TRAP: 机制解释是可能原因，测量才帮助区分它；单次观测也不自动成为普遍规律。 || A plausible mechanism needs distinguishing evidence, and one observation is not a universal rule.

@@ net12
START: 老师要给十个人分发同一份文件。如果只能老师上传十份，老师的出口可能最忙；允许学生转发收到的块，上传能力也会随参与者增加。 || Distributing a file to ten peers can bottleneck at one server. Peers that forward received chunks contribute upload capacity.
STEP1: 客户端—服务器方式至少上传 N 份文件，所以总上传工作量是 NF。 || A client–server system uploads N copies, totaling NF bits.
STEP2: P2P 仍需服务器把原文件引入群体，也仍需最慢客户端下载一份；共享没有消除这些约束。 || P2P still needs the server to inject the file and the slowest peer to receive a copy.
STEP3: 写客户端时，再把“容量够不够”与“消息怎样解析”分开。TCP 收到半条回复时，要缓存等待剩余部分。 || Capacity and message parsing are separate concerns. Buffer a partial TCP reply until a complete message is available.
TRAP: 每次 recv 的边界不是一次 send 的边界，不能把偶然跑通的小演示当作正确协议实现。 || Receive-call boundaries need not match send-call boundaries; a successful toy run does not prove correct framing.

@@ net13
START: 发一份材料给同事，没收到“已收”的回复：是材料丢了，还是回复丢了？可靠传输必须同时处理这两种可能。 || If an acknowledgment never arrives, either the data or the acknowledgment may have been lost. Reliability must handle both cases.
STEP1: 校验和检查某些损坏，ACK 报告接收进展，定时器让发送者在等太久后重试。 || Checksums detect some corruption, acknowledgments report progress, and timers trigger retries.
STEP2: 若材料已经到过，重发会产生重复。给数据编号，接收者才能再次确认而不重复交付。 || Sequence numbers let the receiver acknowledge a duplicate without delivering it again.
STEP3: 停等一次只允许一包在途；窗口允许先发多包，把等待回复的时间利用起来。 || Stop-and-wait allows one outstanding packet; a window allows multiple packets to overlap feedback delay.
TRAP: 超时不是“证明丢包”，也可能只是包或回复特别慢。协议需要容忍由此造成的多余重传。 || A timeout can result from delay rather than loss, so duplicates must remain safe.

@@ net14
START: 把 TCP 字节流想成一本有连续页码的书。拿到后面的页，不能填补前面缺失的那一页；累计 ACK 报告的是第一个缺口。 || Think of a TCP byte stream as consecutively numbered pages. Later arrivals do not fill an earlier gap; the cumulative ACK points to that gap.
STEP1: 已收到至字节 999，接着收到 1000–1499，则下一期待字节为 1500，回复 ACK1500。 || Receiving bytes through 1499 advances the next-expected-byte acknowledgment to 1500.
STEP2: 若只收到 1600–1699，中间 1500–1599 还缺着，累计 ACK 仍是 1500。 || Receiving bytes 1600–1699 leaves ACK1500 unchanged while the earlier gap remains.
STEP3: cwnd 限制网络中的未确认数据，rwnd 限制接收端可接受的数据；发送量受较小者约束。 || cwnd limits outstanding data for congestion control; rwnd reflects receiver capacity. The tighter limit applies.
TRAP: 页码只是直觉，TCP 实际按字节编号；一个含 500 字节的段会推进 500，而不是推进 1。 || TCP counts bytes, not packets: 500 new contiguous payload bytes advance the acknowledgment by 500.

@@ net15
START: 不知道前面道路有多拥堵时，发送者先试探，再根据反馈调整。拥塞窗口是“允许多少未确认数据在路上”的旋钮。 || A sender probes an unknown path and adapts from feedback. Its congestion window limits outstanding data.
STEP1: 经典教学慢启动中，窗口可按 RTT 从 1、2、4、8 增长，前提是相应 ACK 到达且没有其他限制。 || In the idealized classic model, windows can grow 1,2,4,8 across RTTs when acknowledgments permit.
STEP2: 到阈值后改为较温和的加性增长；重复 ACK 与超时可能触发不同反应。 || Growth becomes additive after a threshold, and duplicate ACKs and timeouts can cause different responses.
STEP3: 在 W/2 到 W 的理想锯齿中，平均窗口是 3W/4；再除以 RTT，才得到窗口限制下的速率近似。 || A sawtooth from W/2 to W averages 3W/4; dividing by RTT approximates a window-limited rate.
TRAP: 算图题先确认 Tahoe、Reno 等模型，不能只凭一段下降曲线套用所有 TCP 实现。 || Identify the specified congestion-control model before interpreting a trace.

@@ net16
START: 地址查找像逐级细化位置：同一个地点既属于城市，也属于更具体的街区。多个路由匹配时，最长前缀选最具体的那条。 || An address can match both a broad region and a narrower district. Longest-prefix matching chooses the more specific routing entry.
STEP1: 10.1.2.99 同时匹配 10/8、10.1/16、10.1.2/24，选择 /24。这里比较的是二进制前缀长度。 || Destination 10.1.2.99 matches /8, /16 and /24 entries; select the /24 match.
STEP2: /26 留下六个主机位，地址块共 64 个。192.0.2.130 落在末字节 128–191 的块中。 || A /26 block contains 64 addresses; 192.0.2.130 lies in the .128–.191 block.
STEP3: MTU 又问另一件事：“这一跳装得下多大 IP 包？”分片切的是载荷，每片还要自己的首部。 || MTU limits packet size on a link. Fragmentation divides the payload and adds a header to each fragment.
TRAP: 地址范围与分组大小没有直接换算关系；子网划分和 IP 分片是两类不同问题。 || Subnetting divides address space; fragmentation divides packet payload. They are different operations.

@@ net17
START: 去目的地有多条路，“第一段便宜”不代表整条最便宜。最短路要把到邻居的代价和后续代价一起比较。 || The cheapest first hop need not give the cheapest complete route. Compare the first-hop cost plus the remaining path.
STEP1: 经邻居 A 要先付 2，再付 6，共 8；经 B 要先付 5，再付 1，共 6，所以选 B。 || A route costing 2+6 loses to one costing 5+1; choose the latter's first hop.
STEP2: Dijkstra 用已知拓扑逐步确定最短距离；距离向量则使用邻居通告的后续距离更新。 || Dijkstra works with topology information; distance-vector updates use neighbors' advertised distances.
STEP3: 跨自治系统时还要考虑策略。一个管理域愿意转送什么流量，与数学上最短是不同条件。 || Inter-domain routing also follows policy; willingness to carry traffic is distinct from shortest distance.
TRAP: A–B–C–D 路径中，D 的前驱是 C，但 A 的下一跳是 B。不要把两张不同含义的表混在一起。 || On A–B–C–D, D's predecessor is C, but A's forwarding next hop is B.

@@ net18
START: 共享链路同时面对两个问题：传来的比特有没有被改坏，以及多个人何时可以一起使用信道。前者是检错，后者是接入协调。 || A shared link must detect corrupted bits and coordinate access. Error detection and medium access solve different problems.
STEP1: 1011001 有四个 1，偶校验追加 0。翻转一位会改变奇偶性，翻转两位却可能漏检。 || The even-parity bit for 1011001 is zero. One flip changes parity; two can escape detection.
STEP2: CRC 用 XOR 多项式除法加入更有结构的冗余。余数为零表示“没有检出”，不等于“绝不可能出错”。 || CRC uses polynomial redundancy; a zero remainder means no error was detected, not certainty of correctness.
STEP3: ALOHA 像抢答：没人说话是空闲，一人说话可成功，多人同时说则碰撞。选择发送概率是在两端浪费之间取舍。 || In the ALOHA model, silence is idle, one sender succeeds, and simultaneous senders collide.
TRAP: 以太网交换机的 MAC 学习、IPv4 的 ARP 解析，也属于本地交付的问题；它们不负责跨全网选路。 || MAC learning and ARP support local delivery rather than selecting end-to-end Internet routes.

@@ net19
START: 协议题最容易错在“脑中跳过了一个事件”。像记账一样，每收到一个包就记录状态变化，后面的答案自然跟着出来。 || Protocol mistakes often come from skipping events. Record the state change after each packet or acknowledgment.
STEP1: 假设依次发送 0、1、2、3，1 丢失。先记录接收者期待 1，不急着猜重传结果。 || If packet 1 is lost from 0,1,2,3, first record that the receiver still expects 1.
STEP2: 基础 GBN 丢弃后来的 2、3；SR 可缓存并确认它们。相同丢包事件因接收规则不同而产生不同状态。 || GBN discards later out-of-order packets; SR may buffer and acknowledge them.
STEP3: 交换机题也一样：每次只从实际收到的帧源地址学习，不能把未来回复的信息提前写进表。 || Switch learning likewise uses only the source addresses of frames actually received so far.
TRAP: 图题中的原图和起始状态都是题目条件，不能只记“某轮减半”或某个选项字母。 || A diagram and its initial state are part of the question, not optional background.

@@ net20
START: 从空缓存打开网页，需要先回答四个不同问题：我是谁、网站 IP 是什么、本地下一跳是谁、怎样请求页面。把四张信息卡片串起来，就能看清整条链。 || Fetching a page from empty caches requires local configuration, the site's IP address, a next-hop link address, and an application request.
STEP1: DHCP 提供本机 IP、掩码、网关和 DNS 配置；DNS 再把网站名称解析成 IP。DNS 查询本身也要先有本地下一跳可用。 || DHCP supplies configuration and DNS resolves the site name. Sending DNS queries also requires a usable local next hop.
STEP2: 若网站在远端，ARP 查网关在本 LAN 的 MAC。目的 IP 写网站，当前帧目的 MAC 写网关。 || For a remote site, resolve the gateway's local MAC: the IP destination is the site, while the first frame targets the gateway.
STEP3: 然后按题设建立 TCP、发送 HTTP 请求；各路由器在每一跳重建链路封装。 || Under the stated model, establish TCP and send HTTP; routers replace link framing at each hop.
TRAP: 这个场景限定 IPv4 以太网、空缓存和明文 HTTP。HTTPS、IPv6 或已有连接会改变部分步骤。 || This scenario assumes IPv4 Ethernet, empty caches, and plaintext HTTP; other configurations change some steps.
