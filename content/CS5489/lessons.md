# CS5489 连续微课主稿

本稿是 AI 编写的串讲与教学例题，来源通过 CARDS 关联到原课件页/单元。卡片范围表示复习入口，不表示一节短课穷尽了这些卡片的所有细节。PREREQ 是概念先修；BRIDGE 解释联系。题答的 ` || ` 分隔中文与英文。

@@ ml01 | 学习的对象：从短信到可检验的预测 | From messages to testable predictions
CARDS: M001-M006
PREREQ:
GOAL: 能区分特征、标签、参数和超参数，并画出一次可信的训练流程。
EXPLAIN: 想让计算机识别垃圾短信，先把每条短信变成特征 x，例如长度和 free 出现次数；训练时还知道标签 y，例如 spam 或 ham。模型 f 把 x 映射为预测。学习不是记住文件名，而是用训练样本决定 f 的参数，使新短信也能被正确处理。

把模型比作一套待调整的评分规则：每个词的权重是参数；采用哪种模型、正则化强度多大是超参数。训练集用于拟合参数，验证集用于比较方案，最后的测试集用于评估已选定方案。反复看测试成绩再修改方案，会把测试集变成实际的验证集。

分类预测类别；回归预测连续量。两者都应先说明输入、输出、损失和评价指标。准确率高不等于方法在所有场景可靠，还要看类别比例、错误代价和新数据是否变化。
RECAP_EN: Define the prediction task before choosing an algorithm. Fit parameters on training data, choose settings using validation data, and evaluate the selected procedure on held-out test data.
WORKED_Q: 100 条短信中 95 条正常。模型永远预测正常，准确率是多少？它学会识别垃圾短信了吗？ || Of 100 messages, 95 are legitimate. What accuracy does an always-legitimate classifier achieve, and does it detect spam?
WORKED_A: 正常短信判对 95 条，准确率 95%；5 条垃圾短信全漏掉，垃圾类召回率为 0。一个好看的总分可能掩盖目标类别完全失败。 || It gets 95/100 = 95% accuracy, but spam recall is zero. Overall accuracy hides complete failure on the target class.
PRACTICE_Q: 训练权重、比较三个 C、报告最终成绩，分别该用哪个数据划分？ || Which split is used to fit weights, compare three C values, and report final performance?
HINT: 区分拟合、选择与最终评价。 || Separate fitting, selection, and final evaluation.
PRACTICE_A: 依次为训练集、验证集或训练内部交叉验证、保留测试集。 || Training data, validation data or cross-validation within training data, and the held-out test set, respectively.
TRANSFER_Q: 测试集不用标签，只拿它参与建立词表，这是否仍可能泄漏？ || Can building the vocabulary using unlabeled test messages still leak information?
TRANSFER_A: 会。词表已适应测试分布；严格归纳评估应在训练数据上拟合词表，再变换验证和测试数据。若任务明确采用传导设置，应单独声明。 || Yes. The vocabulary adapts to the test distribution. Under an inductive protocol, fit it on training data only; explicitly declare any transductive setting.
BRIDGE: 下一步先把这条流程写成能够从干净状态运行的程序，之后再讨论模型公式。

@@ ml02 | 让代码忠实执行你的想法 | Python and reproducible notebooks
CARDS: M007-M020
PREREQ: ml01
GOAL: 能跟踪变量、函数返回值与 Notebook 状态，而不是靠反复点击运行。
EXPLAIN: Notebook 的单元是界面顺序，内存中的变量却取决于实际执行顺序。先运行后面的单元，再改前面的变量，屏幕上可能同时保留不属于同一次运行的结果。重启内核并从头运行，才是在检查流程是否完整。

先掌握三个动作：用变量保存值，用循环逐个处理对象，用函数把输入变成输出。print 是给人看，return 才把结果交给后续计算。列表保存有序对象；字典把词映射到计数；集合帮助去重。类把一组状态和相关方法放在一起，后面分类器的 fit 会存参数，predict 再使用这些参数。

注意对象共享：b = a 通常让两个名字指向同一个可变列表，修改 b 也会影响 a。复制、视图和随机数状态都可能让“公式没错”的实验产生错误结果。
RECAP_EN: A notebook is a stateful program. Track data flow, distinguish printing from returning, and verify the complete workflow by restarting and running all cells in order.
WORKED_Q: a=[1,2]；b=a；b[0]=9；a 是什么？ || After a=[1,2], b=a, and b[0]=9, what is a?
WORKED_A: a 也是 [9,2]，因为两个名字引用同一个列表。若先 b=a.copy()，这次修改才不会改变 a 中的整数元素。浅复制嵌套容器时仍要检查内部共享。 || a becomes [9,2] because both names reference the same list. With b=a.copy(), this integer replacement would not change a; nested objects may still be shared by a shallow copy.
PRACTICE_Q: 函数只执行 print(x*2)，调用后把返回值赋给 y，y 是什么？ || A function only calls print(x*2). What is y when assigned its return value?
HINT: 屏幕输出和函数输出不是同一件事。 || Printed output and a returned value are different.
PRACTICE_A: 没有显式 return 时返回 None；要继续计算，应 return x*2。 || It returns None. Use return x*2 to pass the computed value to later calculations.
TRANSFER_Q: 一个单元在当前内核能运行，重启后报变量未定义，优先怎样排查？ || A cell works now but fails after a restart with an undefined variable. What should you check first?
TRANSFER_A: 查该变量的赋值或导入是否在前面的实际执行路径中；去掉对旧内存的依赖，再完整重跑。随机种子不能修复缺失的数据流。 || Check whether the variable is assigned or imported earlier on the actual execution path. Remove reliance on stale state and rerun everything; a random seed cannot repair missing data flow.
BRIDGE: 列表适合组织对象，机器学习计算则需要具有明确形状的数组。

@@ ml03 | 先看形状，再看矩阵公式 | Shapes before matrix formulas
CARDS: M021-M034
PREREQ: ml02
GOAL: 能给矩阵乘法、广播和按轴统计逐步标出形状。
EXPLAIN: 约定一行是一条样本，一列是一种特征。X 有 N 行 d 列，权重 w 有 d 个数；一条样本的预测是各特征乘对应权重后求和，全部样本一起写成 Xw。矩阵式只是把重复的标量运算打包，并没有增加新规则。

axis=0 的均值把样本轴压掉，得到每个特征的均值；axis=1 则得到每条样本内部的平均值。转置把行列交换，reshape 只是按元素顺序重新安排形状，两者通常不同。NumPy 的 * 是逐元素乘，@ 才是矩阵乘。

广播从末尾维度对齐：相等或有一个为 1 才兼容。因此 (N,1) 减 (N,) 会被当作列向量减行向量，得到 N×N 个两两差，而不是 N 个样本残差。每一步先写预期 shape，再运行确认。
SYMBOLS: X | 数据矩阵，N×d；w | 权重向量，d；Xw | 预测，N；X^T X | d×d 特征内积矩阵
RECAP_EN: Matrix notation packages scalar operations. With samples in rows, X has shape N by d and Xw contains N predictions. Broadcasting compatibility does not guarantee the intended meaning.
WORKED_Q: X 的两行为 (1,2)、(3,4)，w=(2,-1)，求 Xw。 || X has rows (1,2) and (3,4), and w=(2,-1). Compute Xw.
WORKED_A: 第一行为 1×2+2×(-1)=0，第二行为 3×2+4×(-1)=2，结果 (0,2)，形状 (2,)。每个输出对应一条样本。 || The row-wise dot products are 0 and 2. The result is (0,2), of shape (2,), with one prediction per sample.
PRACTICE_Q: X 为 (100,4)，计算每列均值后得到什么形状？ || For X of shape (100,4), what is the shape of its column means?
HINT: 对 100 条样本求平均，保留 4 种特征。 || Average over the 100 samples while retaining the four features.
PRACTICE_A: mean(axis=0) 得 (4,)；keepdims=True 时得 (1,4)，两者都可用于按列中心化。 || mean(axis=0) gives (4,), or (1,4) with keepdims=True; either can support column centering.
TRANSFER_Q: 预测形状 (3,1)、标签形状 (3,)，相减前该做什么？ || Predictions have shape (3,1) and labels (3,). What should you do before subtraction?
TRANSFER_A: 统一成 (3,) 或都成 (3,1)，并断言一致；否则广播会产生 (3,3)，损失可能照样输出一个数字却代表错误任务。 || Make both shapes (3,) or both (3,1), and assert equality. Otherwise the (3,3) broadcast result can produce a plausible but incorrect loss.
BRIDGE: 内积不仅用于预测，也能衡量方向对齐程度；这就连接到投影、正交化和后来的 PCA。

@@ ml04 | 投影：把一个向量拆成已有部分和新信息 | Projection and orthogonalization
CARDS: M035-M041
PREREQ: ml03
GOAL: 能解释 Gram–Schmidt 每次减掉什么，并手算两维例子。
EXPLAIN: 想知道 v 中有多少已经沿着 u 的方向，可把投影写成 a u。选择 a 使剩余 r=v-au 与 u 垂直，即 u^T r=0。代入得到 a=(u^T v)/(u^T u)。分母是在校正 u 本身的长度；只有 u 已是单位向量时才能省掉。

Gram–Schmidt 先把第一个非零向量归一化，再从后续向量中减掉它们沿已建立正交方向的投影。余下的部分代表尚未被这些方向表示的新信息；最后把余量除以长度。零余量意味着线性相关，不能继续除以零。

这也解释了为什么用 E^T E 检查结果：对角线是每列长度的平方，非对角线是方向间内积。得到单位矩阵说明列向量正交归一，但仍应确认这些列张成了原目标空间。
RECAP_EN: Projection removes the component already explained by a direction. Gram–Schmidt repeatedly subtracts projections, then normalizes the remaining independent component.
WORKED_Q: 对 v1=(1,1)、v2=(1,0) 做正交归一化。 || Orthonormalize v1=(1,1) and v2=(1,0).
WORKED_A: e1=(1,1)/√2。v2 在 e1 上的投影为 (1/√2)e1=(1/2,1/2)，余量 (1/2,-1/2)，长度 1/√2，所以 e2=(1,-1)/√2。两向量内积为 0。 || e1=(1,1)/√2. Subtract the projection (1/2,1/2) from v2, leaving (1/2,-1/2). Normalization gives e2=(1,-1)/√2, orthogonal to e1.
PRACTICE_Q: v=(3,4)，投到 u=(2,0) 上得到什么？ || Project v=(3,4) onto u=(2,0).
HINT: 先求系数，再乘回 u；不要把系数当向量。 || Compute the coefficient, then multiply u by it.
PRACTICE_A: a=6/4=1.5，投影为 (3,0)，余量 (0,4)。 || a=6/4=1.5, so the projection is (3,0) and the residual is (0,4).
TRANSFER_Q: 如果第二个向量变成 (2,2)，余量为零说明什么？ || If the second vector is (2,2), what does a zero residual mean?
TRANSFER_A: 它已在第一方向张成的直线上，没有第二个独立方向。应报告秩不足或跳过该列，不能假造一个归一化结果。 || It lies in the span of the first vector. Report rank deficiency or skip that column rather than normalizing zero.
BRIDGE: 投影最小化剩余距离的思想会在最小二乘和 PCA 中再次出现。

@@ ml05 | 贝叶斯公式就是重新数一遍可能的人群 | Bayes through concrete counts
CARDS: M042-M049
PREREQ: ml01
GOAL: 能从人数表推回条件概率与后验公式。
EXPLAIN: P(free|spam) 问的是“已经知道是垃圾短信，其中多少有 free”；P(spam|free) 问的是“已经看到 free，其中多少是垃圾”。它们筛选的分母人群不同，不能交换。

想象 1,000 条短信，其中 20% 是垃圾。若垃圾中 60% 有 free，正常中 10% 有 free，那么看见 free 的人群包括 120 条垃圾和 80 条正常。后验就是在这 200 条中再数垃圾比例。贝叶斯公式中的分子是目标类别贡献的人数比例，分母是所有类别贡献之和。

把人数换成比例就是 $P(c\mid x)=P(x\mid c)P(c)/\sum_k P(x\mid k)P(k)$，分母须大于零。先验像筛选前的底数，似然决定每类留下多少，后验才是筛选后的占比。连续特征将似然换成密度；密度可以大于 1，区间下的面积才是概率。
SYMBOLS: $P(c)$ | 先验 prior；$P(x\mid c)$ | 似然 likelihood；$P(x)$ | 证据 evidence；$P(c\mid x)$ | 后验 posterior
RECAP_EN: Bayes' rule changes the conditioning population. Multiply the prior by the likelihood, then normalize over all possible classes.
DEMO: bayes
WORKED_Q: 上述 1,000 条短信中，看到 free 后垃圾概率是多少？ || In the 1,000-message population above, what is the probability of spam given free?
WORKED_A: 垃圾且有 free：1000×0.2×0.6=120；正常且有 free：1000×0.8×0.1=80。后验为 120/(120+80)=0.6。 || There are 120 spam messages and 80 legitimate messages containing free. The posterior is 120/200=0.6.
PRACTICE_Q: 其他条件不变，垃圾先验变为 0.1，后验是多少？ || Keeping both likelihoods unchanged, what is the posterior if the spam prior becomes 0.1?
HINT: 在新的人群比例下重新计算两个分子贡献。 || Recompute both class contributions under the new prior.
PRACTICE_A: 后验为 0.1×0.6/(0.1×0.6+0.9×0.1)=0.4。 || The posterior is 0.06/(0.06+0.09)=0.4.
TRANSFER_Q: 某词在垃圾邮件中出现频率很高，能否直接认定它有很强区分力？ || Does a word's high frequency in spam alone imply strong discriminative power?
TRANSFER_A: 不能，还要比较正常邮件中的概率，以及先验。若两类概率相同，观察该词不会改变类别优势比。 || No. Compare its probability in legitimate mail and account for priors. Equal class-conditional probabilities leave the prior odds unchanged.
BRIDGE: 概率表通常未知，下一节用训练样本估计它们。

@@ ml06 | MLE：选择最能解释已见数据的参数 | Maximum likelihood and generative classification
CARDS: M050-M060
PREREQ: ml05
GOAL: 能从样本似然推导伯努利均值，并解释高斯均值与方差估计。
EXPLAIN: 生成式分类器分别学习类别比例和每类会生成什么样的特征，然后用贝叶斯公式做判断。最大似然把数据固定、参数视作待选量：哪个参数使这批观测联合出现的概率或密度最大，就选哪个。它不是“给参数直接求概率”，后者需要先验。

这里 log 指自然对数，是指数函数 exp 的反函数。它严格递增，所以不会改变最大值的位置；log(ab)=log(a)+log(b) 把乘积变成和。导数描述参数微小增加时函数怎样变化，例如 log p 的导数是 1/p。寻找内部最优点时令导数为零，但还要检查边界和它是否真是最大值。

若 n>0 次独立同分布的伯努利观测中有 k 次成功，这串观测的似然为 $p^k(1-p)^{n-k}$。取对数得到 $k\log p+(n-k)\log(1-p)$。对 p 求导并令零，得到 $k/p-(n-k)/(1-p)=0$，解为 p=k/n；k=0 或 n 时最优位于边界。若只记录成功总数，还会多一个与 p 无关的组合系数，不改变这个估计。

高斯模型中，对数似然含平方偏差和；均值 MLE 是平均数，方差 MLE 用 n 作分母。统计学常见的 n-1 是估计总体方差时的无偏修正，二者目标不同。分类时比较 log prior+log likelihood，避免小概率连乘下溢。
RECAP_EN: Maximum likelihood chooses parameters that best explain fixed observations under a specified model. Taking logs preserves the maximizer and turns products into sums.
WORKED_Q: 观测为 (1,2,3)，一维高斯均值和方差 MLE 是多少？ || For observations (1,2,3), compute the Gaussian mean and variance MLEs.
WORKED_A: 均值为 2；残差为 (-1,0,1)，平方和为 2；方差 MLE 为 2/3。用 n-1 得到 1，那是另一种方差估计约定。 || The mean is 2. The squared deviations sum to 2, giving an MLE variance of 2/3. Dividing by n-1 instead gives 1.
PRACTICE_Q: 10 次伯努利观测有 7 次成功，MLE 是多少？ || Seven of ten Bernoulli observations are successes. What is the MLE?
HINT: 将通式中的成功次数和总次数代入。 || Substitute the success count and sample size.
PRACTICE_A: p=7/10=0.7。它描述这组数据的拟合，不意味着未来恰好每十次成功七次。 || p=0.7. This fitted probability does not require exactly seven successes in every future batch of ten.
TRANSFER_Q: A 类似然 0.4、先验 0.2；B 类似然 0.2、先验 0.8。为何不选似然更大的 A？ || Why not choose A when its likelihood is 0.4 versus B's 0.2, with priors 0.2 and 0.8?
TRANSFER_A: 应比较加权分数：A 为 0.08，B 为 0.16，选 B。归一化后 B 后验为 2/3。仅比较似然相当于忽略不相等的先验。 || The weighted scores are 0.08 and 0.16, so choose B, whose posterior is 2/3. Likelihood-only comparison ignores unequal priors.
BRIDGE: 多特征数据还需要说明特征之间如何一起变化，这决定使用对角还是完整协方差。

@@ ml07 | 协方差：椭圆的方向也是信息 | Gaussian models and covariance
CARDS: M061-M074
PREREQ: ml03,ml06
GOAL: 能区分完整逐类协方差、对角 Gaussian NB 和共享协方差。
EXPLAIN: 一维高斯描述围绕均值的散布；二维高斯还要描述两个特征是一起变大、反向变化，还是缺少线性关联。协方差矩阵的对角线是各自方差，非对角线描述共同变化，等密度线可形成倾斜椭圆。

当协方差 $\Sigma$ 正定时，高斯密度中的 $(x-\mu)^T\Sigma^{-1}(x-\mu)$ 是按散布方向校正的平方距离。以 $\Sigma=\operatorname{diag}(4,1)$ 为例，偏移 (2,0) 与 (0,1) 的该距离都为 1：前一方向本来更分散，偏移两格才相当于后一方向偏移一格。行列式项校正密度占据的体积，比较不同协方差的类别时不能随意删掉。

Gaussian NB 假设给定类别后特征独立，因此采用对角协方差。当前 GaussianBayes 每类拟合完整协方差；LDA 使用共享协方差。课堂代码的 `cov(Xc, rowvar=False)` 默认用每类样本数 Nc-1 作分母，不是上一节用 Nc 的 MLE。少量样本会使估计不稳；加正的 alpha I 可抬高各方向方差，避免奇异矩阵。
RECAP_EN: Covariance describes both scale and joint variation. Gaussian NB uses diagonal class-conditional covariance; the current full Gaussian classifier estimates a separate full covariance for each class.
WORKED_Q: 两个特征时，一类完整协方差有几个独立参数？对角模型呢？ || With two features, how many independent covariance parameters does one full model need, compared with a diagonal model?
WORKED_A: 完整对称矩阵有两个方差和一个协方差，共 3 个；对角模型为 2 个。这还没计入均值和类别先验。 || A symmetric full covariance needs two variances and one covariance: three parameters. A diagonal covariance needs two, excluding means and class priors.
PRACTICE_Q: d=4 时两种协方差分别需要几个参数？ || How many covariance parameters are needed when d=4?
HINT: 对角 d 个，非对角只计上三角。 || Count d diagonal entries and only the upper triangle off the diagonal.
PRACTICE_A: 完整为 d(d+1)/2=10，对角为 4。 || The full covariance needs 10 parameters and the diagonal covariance needs 4.
TRANSFER_Q: 两类共享同一个正定协方差时，对数后验比中的二次 x 项会怎样？ || What happens to quadratic terms in x in the log posterior odds when two classes share the same positive-definite covariance?
TRANSFER_A: 相同的二次项抵消，留下线性分数，连接到 LDA 与逻辑形式。逐类协方差不同时通常不会抵消；不能把共享假设套到当前 GaussianBayes。 || They cancel, leaving linear log odds, connecting LDA to a logistic form. Different class covariances generally retain quadratic terms.
BRIDGE: 对文本词频而言，高斯未必是合适的观测模型；先决定“出现”还是“出现次数”。

@@ ml08 | 同一条短信，为什么有不同的 NB 模型 | Text representation and naive Bayes
CARDS: M075-M089
PREREQ: ml02,ml06
GOAL: 能从数据表示选择 Bernoulli 或 Multinomial NB，并算出平滑概率。
EXPLAIN: 固定词表为 free、meeting、win。短信 free free win 的词频向量是 (2,0,1)，出现标记则是 (1,0,1)。这两种表示问的问题不同：Bernoulli NB 关注每个词是否出现，Multinomial NB 关注文档中各词元分配了多少次。

“朴素”把给定类别后的证据作简化分解，不是说词在现实中从不相关。Bernoulli NB 假设各词是否出现条件独立，还计入未出现词的贡献；Multinomial NB 将词元按同一类的词概率分配，类分数是次数乘 log 词概率再求和。给定总词数时，各词的计数本身并不彼此独立。平滑给未见事件留一点质量：伯努利分母加 2alpha，多项式分母加 alpha 乘词表大小。

词表和 IDF 都应只在训练部分拟合。TF-IDF 降低普遍常见词的影响，但它是加权特征，不是严格的整数多项式计数；有效的经验组合与严格生成假设应区分。稀疏矩阵只存非零词项，让大词表计算更省空间。
RECAP_EN: Choose the observation model after choosing the representation. Bernoulli NB models presence and absence; Multinomial NB models token counts. Fit text transformations on training data only.
WORKED_Q: 某类三词总计数 (3,1,0)，alpha=1，多项式平滑概率是多少？ || A class has token counts (3,1,0). With alpha=1, what are the smoothed multinomial probabilities?
WORKED_A: 原总词元数 4，加入 3 个伪计数后分母为 7；分子为 (4,2,1)，概率为 (4/7,2/7,1/7)，和为 1。 || The denominator is 4+3=7 and the numerators are (4,2,1), giving probabilities (4/7,2/7,1/7), which sum to one.
PRACTICE_Q: 10 篇某类文档中，一个词出现过 0 篇。Bernoulli alpha=1 时概率是多少？ || A word occurs in none of ten documents in a class. What is its Bernoulli estimate with alpha=1?
HINT: 两种事件是出现与不出现。 || There are two outcomes: presence and absence.
PRACTICE_A: (0+1)/(10+2)=1/12；未出现概率为 11/12。 || The presence probability is 1/12 and absence probability is 11/12.
TRANSFER_Q: 文档没有出现某词，Bernoulli 和 Multinomial 的该词贡献是否都为零？ || If a word is absent, is its contribution zero in both Bernoulli and Multinomial scoring?
TRANSFER_A: 不是。Bernoulli 贡献 log(1-p)；多项式的该词次数项为 0×log p=0。前者的“不出现”本身是建模的证据。 || No. Bernoulli contributes log(1-p), while the multinomial count term is zero. Absence itself is evidence in the Bernoulli model.
BRIDGE: 当每个词的出现次数被视为独立计数，Poisson NB 提供第三种建模思路。

@@ ml09 | Poisson NB：把次数变成证据 | Count evidence with Poisson NB
CARDS: M107-M118
PREREQ: ml08
GOAL: 能从 Poisson 概率写出类分数，并解释文档长度与独立性假设。
EXPLAIN: Poisson 分布以 lambda 表示计数的均值。对某类别的某个词，先统计每篇文档中出现几次，再求平均作为 MLE。它和多项式的差别是：多项式在给定总次数下分配词元，独立 Poisson 则对每个计数单独建模，也隐含了文档长度的结构。

单词概率为 $e^{-\lambda}\lambda^x/x!$。多个词取对数相加，类分数为 $\log\pi_c+\sum_j[x_j\log\lambda_{cj}-\lambda_{cj}-\log(x_j!)]$。对于同一文档，各类的阶乘项相同，比较类别时可以去掉；负 lambda 项依赖类别，不能漏。

当前 Tutorial 2 模板带 alpha，却未规定其数学定义，不能自行加一个平滑公式又称为老师原式。先说明采用的约定，再检查零计数、类别标签顺序、特征形状与训练/测试隔离。实际 AGNews 文件为训练 2000、测试 1000；教学小例子不是实验成绩。
RECAP_EN: Poisson NB scores independent counts using log priors, count-weighted log rates, and negative rates. Drop only terms that are identical across classes for the same observation.
WORKED_Q: 等先验，A 的均值 (2,1)，B 为 (1,2)，x=(2,0)，哪个分数大？ || With equal priors, rates (2,1) for A and (1,2) for B, which class scores higher for x=(2,0)?
WORKED_A: 忽略共同项，A 为 2log2-3，B 为 -3；差为 2log2>0，选 A。两个类别的总均值恰好相同，这一次负 lambda 和才抵消。 || A scores 2log2-3 and B scores -3, so A wins by 2log2. The negative-rate sums cancel here only because their totals match.
PRACTICE_Q: 某词在三篇同类文档的计数为 0、1、5，lambda 的 MLE 是多少？ || Counts for a word in three same-class documents are 0,1,5. What is the rate MLE?
HINT: 是每篇文档的平均次数，不是出现文档比例。 || Use mean count per document, not the fraction of documents containing it.
PRACTICE_A: lambda=(0+1+5)/3=2；出现比例 2/3 属于另一个统计量。 || The rate estimate is 2; the presence fraction 2/3 is a different statistic.
TRANSFER_Q: 两类单词均值为 1 和 10，空计数 x=0、更支持哪类？ || With one feature, equal priors, and rates 1 and 10, which class does x=0 support?
TRANSFER_A: 分数为 -1 和 -10，支持均值 1 的类别。若错删负 lambda 项，就会把这两类误判为平局。 || The scores are -1 and -10, favoring rate 1. Dropping the negative-rate term incorrectly creates a tie.
BRIDGE: 前面先建模“数据怎样生成”；下一节直接建模“给定数据属于哪类”。

@@ ml10 | 逻辑回归：分数、概率、损失怎样连起来 | Logistic regression from score to update
CARDS: M119-M132
PREREQ: ml03,ml06
GOAL: 能说出一次参数更新为什么朝这个方向，并手算梯度。
EXPLAIN: 线性分数 z=w^T x+b 可以是任何实数，不能直接叫概率。sigmoid 将它映射为 $p=1/(1+e^{-z})$：z=0 对应 0.5，正分数更支持正类。反过来 $\log[p/(1-p)]=z$，所以加一单位分数是在给优势比乘 e。

标签 t 取 0 或 1。模型给真实标签的概率是 $p^t(1-p)^{1-t}$，取负对数得到交叉熵 $\ell=-t\log p-(1-t)\log(1-p)$。真实类别越被低估，损失越大。链式法则是将一条计算路径上的局部变化率相乘。这里先对 p 求导，得到 -t/p+(1-t)/(1-p)；再乘 sigmoid 的导数 p(1-p)，化简为 p-t。再由 z 对 w 的各偏导组成向量 x，得到 $\nabla_w\ell=(p-t)x$。

梯度告诉我们局部增大损失最快的方向，所以减去学习率乘梯度。这里先讲单样本、无正则；多样本取和还是均值会改变系数，L2 正则还会增加拉回权重的项。学习率控制每步幅度，正则强度改变目标，二者不能互相替代。
SYMBOLS: x | d 维特征；w | d 维权重；b | 标量偏置；t | 0/1 标签；p | 预测正类概率；eta | 学习率
RECAP_EN: Logistic regression maps a linear score to a probability. Bernoulli negative log likelihood gives cross-entropy; its single-sample weight gradient is (p-t)x.
DEMO: gradient
WORKED_Q: x=2、t=1、w=0，固定 b=0，无正则，eta=0.1，做一步更新。 || For x=2, t=1, w=0, fixed b=0, no regularization, and eta=0.1, perform one update.
WORKED_A: z=0，p=0.5；梯度 (0.5-1)×2=-1。新 w=0-0.1×(-1)=0.1，新 z=0.2，新 p≈0.5498。正类概率上升，符合这条正样本的要求。 || z=0 and p=0.5, so the gradient is -1. The new weight is 0.1, giving z=0.2 and p≈0.5498, increasing the true-class probability.
PRACTICE_Q: 同样 x=2、w=0，但标签 t=0，一步后的 w 是多少？ || With x=2 and w=0 but t=0, what is w after one step at eta=0.1?
HINT: 只改变 p-t 的符号。 || Check the sign of p-t.
PRACTICE_A: 梯度为 1，新 w=-0.1，正类概率下降到约 0.4502。 || The gradient is 1, so w=-0.1 and the positive-class probability falls to about 0.4502.
TRANSFER_Q: 如果同时训练偏置，本例第一题的偏置梯度和更新是什么？ || If the bias is also trained in the worked example, what are its gradient and update?
TRANSFER_A: b 的梯度为 p-t=-0.5，新 b=0.05。两者应在同一组旧参数上计算；此时新 z=0.25，不是固定偏置版本的 0.2。 || The bias gradient is -0.5 and b becomes 0.05. Both gradients use the old parameters; the new score is 0.25.
BRIDGE: 梯度能拟合一个模型；选择模型和推广到多类别，还需要交叉验证与 softmax。

@@ ml11 | 模型选择与多类别概率 | Cross-validation and multiclass probabilities
CARDS: M133-M142
PREREQ: ml10
GOAL: 能区分训练一个模型、选择超参数、定义多类别概率这三件事。
EXPLAIN: 比较两个 C 时，应在相同数据划分上公平比较。每一折中，词表、缩放和模型参数都只能用该折训练部分拟合；验证部分负责评分。选定设置后可以用全部开发数据重新拟合，最后只评一次保留测试集。C 与惩罚强度的具体换算依赖库的目标系数约定。

多类别可以训练 K 个 one-vs-rest 二分类器，每个回答“是不是这一类”；也可以让一个模型给所有类别打分，再用 softmax 一起归一化。后者是 $p_k=e^{z_k}/\sum_j e^{z_j}$，每行概率和为 1。数值实现先减去最大分数，避免 exp 溢出，这不改变概率比。

交叉熵只取真实类别概率的负对数，因此前节的“提高真实标签概率”依然成立。权重符号的含义还受特征尺度、类别编码和其他特征固定条件影响，不能把正权重直接解释成因果作用。
RECAP_EN: Cross-validation selects settings; it does not define the multiclass model. Softmax normalizes class scores jointly and is invariant to adding the same constant to every score.
WORKED_Q: 三类分数为 (log2,0,0)，概率是多少？ || What are the probabilities for class scores (log2,0,0)?
WORKED_A: 指数为 (2,1,1)，总和 4，因此 (1/2,1/4,1/4)。所有分数加 1000，理论概率不变；实现时应先减最大值。 || Exponentials are (2,1,1), so probabilities are (1/2,1/4,1/4). Adding 1000 leaves them unchanged mathematically; subtract the maximum for numerical stability.
PRACTICE_Q: 三折均分分别为 (0.82,0.86,0.84) 和 (0.90,0.74,0.79)，按均分选谁？ || Which setting wins by mean score: (0.82,0.86,0.84) or (0.90,0.74,0.79)?
HINT: 不要只挑某一折的最大成绩。 || Compare averages, not the highest individual fold.
PRACTICE_A: 第一组均分 0.84，第二组 0.81，选第一组；这不是泛化必然更好的证明。 || Their means are 0.84 and 0.81. Choose the first under this rule; it is not a guarantee of better population performance.
TRANSFER_Q: 全数据先标准化再交叉验证，为什么即使分类器每折重训也不够？ || Why is refitting the classifier insufficient if standardization was fitted before cross-validation on all data?
TRANSFER_A: 验证折已影响均值和尺度，评估过程提前看到了验证分布。应把变换和分类器一同放进每折训练流程。 || Validation observations have already affected means and scales. Fit the transformation and classifier together within each training fold.
BRIDGE: 逻辑回归惩罚概率判断，SVM 则把“离边界多远”放到学习目标里。

@@ ml12 | SVM：先看距离，再看优化式 | Margins and soft-margin SVM
CARDS: M143-M146,M154-M156,M159-M164
PREREQ: ml04,ml10
GOAL: 能用几何距离解释间隔，并判断松弛变量的含义。
EXPLAIN: 设标签 y 为 -1 或 +1，决策边界是 $w^Tx+b=0$，w 非零。把 w 和 b 同乘正数不会移动边界，所以分数大小不是距离；点到边界的距离为 $|w^Tx+b|/\|w\|$。硬间隔要求两类可被线性完全分开，并规范分数使 $y_i(w^Tx_i+b)\ge1$。再最小化 $\frac12\|w\|^2$，相当于把两类之间最窄的“走廊”拓宽，单侧间隔是 $1/\|w\|$。

若数据有重叠，软间隔改为最小化 $\frac12\|w\|^2+C\sum_i\xi_i$，约束是 $y_i f(x_i)\ge1-\xi_i$ 和 $\xi_i\ge0$，这里 C>0。固定模型后，最小松弛为 $\max(0,1-yf)$，即 hinge loss。此时 0<xi<1 表示分类正确但进入走廊；xi=1 在决策边界上；xi>1 才表示误分类。

C 大表示在给定系数约定下更重视违约代价，不是学习率。SVM 分数也不是概率；若需要概率应另有校准过程。
RECAP_EN: SVM controls geometric margin after fixing score scale. Soft-margin slack allows margin violations, and minimizing slack yields hinge loss. Decision scores are not probabilities.
WORKED_Q: 一维样本 (-1,-1)、(1,+1)，求硬间隔解。 || Find the hard-margin solution for one-dimensional samples (-1,-1) and (1,+1).
WORKED_A: 约束为 w-b≥1、w+b≥1，相加得 w≥1。取最小范数 w=1 时 b=0，单侧间隔 1，两条间隔边界之间宽度 2。 || Constraints are w-b≥1 and w+b≥1, implying w≥1. The minimum norm solution is w=1, b=0; the one-sided margin is 1 and total width is 2.
PRACTICE_Q: 带标签分数 yf=0.4，最小松弛和分类正误是什么？ || For yf=0.4, what is the minimum slack and is the prediction correct?
HINT: 分类看零，满足间隔看一。 || Classification uses zero; the margin requirement uses one.
PRACTICE_A: xi=0.6，分类正确但进入间隔。 || The slack is 0.6. The point is correctly classified but lies inside the margin.
TRANSFER_Q: 把 w、b 同乘 10，距离会扩大 10 倍吗？ || Does scaling w and b by 10 multiply point-to-boundary distances by 10?
TRANSFER_A: 不会，距离分子和分母同时乘 10，抵消。分数改变不意味着几何边界或距离改变。 || No. The numerator and denominator both scale by 10, so the geometric distance stays unchanged.
BRIDGE: 原始问题看 w 与 b；对偶从样本贡献出发，解释哪些点真正支撑边界。

@@ ml13 | 对偶与 KKT：给约束配上价格 | Duality, multipliers, and support vectors
CARDS: M147-M153,M157-M158
PREREQ: ml12
GOAL: 能从拉格朗日函数推出 w 的样本展开，并避免 KKT 逆命题错误。
EXPLAIN: 把硬间隔约束写成 $g_i=1-y_i(w^Tx_i+b)\le0$。最小化问题的拉格朗日函数为 $L=\frac12\|w\|^2+\sum_i\alpha_i g_i$，其中 alpha_i≥0。对任一可行 w,b，乘子项非正，所以先对 w,b 求下确界得到原问题最优值的下界；再最大化这个下界就是对偶。

对 w 求导得 $w=\sum_i\alpha_i y_i x_i$，对 b 求导得 $\sum_i\alpha_i y_i=0$。代回后，对偶目标是最大化 $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_j y_i y_j x_i^Tx_j$，同时满足这些约束。乘子像约束的“价格”；不挤压最优解的约束不必付价。互补松弛 $\alpha_i g_i=0$ 表示：g_i<0 时 alpha_i=0；反向却不一定成立。

软间隔加上线性松弛惩罚后得到 0≤alpha_i≤C。0<alpha_i<C 的点落在间隔边界，可用于求 b；alpha_i=C 也可能仍正确分类。硬间隔在线性可分时可放大分离超平面，使约束严格满足；结合凸性可用强对偶说明最优值相等。这是本问题的条件，不能推广为任意优化问题都成立。
RECAP_EN: The dual maximizes a lower bound on the primal objective. Stationarity expresses w as a weighted sample sum; complementary slackness is an implication, not a reversible test for every constraint.
WORKED_Q: 前节两点的最优 w=1、b=0，求两个硬间隔乘子。 || For the previous two-point optimum w=1, b=0, find the hard-margin multipliers.
WORKED_A: sum alpha_i y_i=0 得 alpha1=alpha2=a；w=sum alpha_i y_i x_i=2a=1，因此两者都是 1/2。代入对偶目标为 1-1/2=1/2，与原始目标相同。 || The bias condition gives equal multipliers a. Since w=2a=1, both equal 1/2. The dual and primal objectives both equal 1/2.
PRACTICE_Q: 若某约束 g_i=-2，互补松弛要求 alpha_i 是多少？ || If g_i=-2, what must alpha_i be under complementary slackness?
HINT: alpha_i g_i 必须为零。 || Their product must be zero.
PRACTICE_A: 乘子必须为 alpha_i=0。 || alpha_i must be zero.
TRANSFER_Q: 若 alpha_i=0，能推出 g_i<0 吗？ || Does alpha_i=0 imply g_i<0?
TRANSFER_A: 不能；g_i=0 也满足乘积为零。应区分必要条件、充分条件以及反向推理。 || No. g_i=0 also satisfies complementary slackness. The reverse implication does not follow.
BRIDGE: 对偶只通过样本内积计算，这为核方法提供了入口。

@@ ml14 | 核：换一种比较样本的方式 | Kernels as implicit feature comparisons
CARDS: M165-M172
PREREQ: ml03,ml13
GOAL: 能展开一个二次核，并解释 C 与 gamma 控制不同事情。
EXPLAIN: 在原空间画不直的边界，变成更丰富的特征后可能是线性的。例如加入平方与交叉项，可以表达弯曲关系。如果算法只需要新特征的内积，就不一定要真正存出这些特征：用 k(x,z)=phi(x)^T phi(z) 直接计算即可。

对二维齐次二次核，$(x^Tz)^2=x_1^2z_1^2+2x_1x_2z_1z_2+x_2^2z_2^2$，所以 phi(x)=(x1²,√2 x1x2,x2²)。中间的 √2 保证内积系数正确。RBF 核根据平方距离给相似度，gamma 大时相似度随距离下降更快，边界可以更局部。

不是所有“相似度”都能当实值标准核：函数应对称，任意有限样本的 Gram 矩阵 K 都须半正定，即任意系数 a 满足 $a^TKa\ge0$。只在一批数据上通过检查还不是对所有输入的证明。核方法还可能需要 N×N 的矩阵，避免显式高维特征不等于免除大样本成本。
RECAP_EN: A kernel computes an inner product in a feature space without explicitly constructing every feature. Validity requires positive semidefinite Gram matrices, and computational costs still depend on sample count.
WORKED_Q: x=(1,2)、z=(3,4)，二次核是多少？ || Compute the homogeneous quadratic kernel for x=(1,2) and z=(3,4).
WORKED_A: 原内积 11，平方为 121。映射后内积为 1×9+(2√2)(12√2)+4×16=9+48+64=121。 || The original dot product is 11, so the kernel is 121. The feature-space dot product is 9+48+64=121 as well.
PRACTICE_Q: 平方距离 4，gamma=0.25 时 RBF 相似度是多少？ || For squared distance 4 and gamma=0.25, what is the RBF similarity?
HINT: 指数里是负 gamma 乘平方距离。 || The exponent is negative gamma times squared distance.
PRACTICE_A: 相似度为 exp(-1)≈0.3679。 || The similarity is exp(-1)≈0.3679.
TRANSFER_Q: 增大 C 和增大 gamma 是否是同一种“复杂化”？ || Do increasing C and increasing gamma change an RBF SVM in the same way?
TRANSFER_A: 不是。C 改变间隔违约的惩罚权重；gamma 改变样本间的相似度范围。应在训练内部联合验证，并先检查尺度。 || No. C weights margin violations; gamma changes the similarity length scale. Tune them jointly inside the training protocol after considering feature scale.
BRIDGE: 模型看到的几何结构来自特征表示，因此缩放和编码也是模型的一部分。

@@ ml15 | 特征与评估：别让表示偷偷改变问题 | Features, scale, and fair comparison
CARDS: M173-M182
PREREQ: ml11,ml14
GOAL: 能解释变换如何影响距离和惩罚，并建立公平比较流程。
EXPLAIN: 假设两个特征是身高和收入，数值单位不同。依赖欧氏距离或 L2 权重惩罚的模型会受单位影响；标准化用训练均值和标准差构造可比尺度。但标准化不是删除信息，也不意味着每个特征都一定应被等权对待。

类别编码同样在表达假设。给红、绿、蓝编码 0、1、2，线性模型会看到大小与等距关系；one-hot 可避免这种无序类别的伪几何。多项式项增加交互，分箱牺牲连续细节，对数变换则需要合法定义域。每个变换都应先问：它保留了什么、丢掉了什么？

类别权重改变训练错误的相对代价。样本少与漏判代价高不是同一概念，决策阈值也会影响最终结果。比较不同模型时固定划分、指标和调参预算，才能分清表示改进与分类器改进。
RECAP_EN: Representation shapes geometry and regularization. Fit transformations within training folds, distinguish class imbalance from decision costs, and compare models under a shared evaluation protocol.
WORKED_Q: 训练最小值 2、最大值 6，映射到 [-1,1] 后，4 与新值 8 分别是多少？ || With training minimum 2 and maximum 6, map 4 and a new value 8 to [-1,1].
WORKED_A: z=2(x-2)/(6-2)-1。4 变成 0；8 变成 2。新数据可以落在训练目标区间外，除非另行截断。 || Using z=2(x-2)/4-1, 4 maps to 0 and 8 maps to 2. New observations can lie outside the training range unless clipping is explicitly applied.
PRACTICE_Q: 两类数量为 200、20，平衡权重 N/(K Nc) 各是多少？ || For class counts 200 and 20, compute balanced weights N/(K Nc).
HINT: 总样本数 N=220，类别数 K=2。 || Use N=220 and K=2.
PRACTICE_A: 两类分别 0.55 和 5.5，少数类每个样本权重是多数类的 10 倍。 || The weights are 0.55 and 5.5; each minority-class observation receives ten times the weight.
TRANSFER_Q: 新特征加上后成绩上升，怎样判断是否仅因为多调了很多次参数？ || How can you assess whether improvement after adding features mainly came from extra tuning?
TRANSFER_A: 在相同划分和调参预算下比较旧特征与新特征，固定模型或做表示×模型组合；保留最终测试，报告变化和不确定性。 || Compare representations using the same splits and tuning budget, with a fixed model or a representation-by-model design, and reserve final testing.
BRIDGE: 将这一流程落实到短信作业，比先尝试很多复杂模型更容易定位问题。

@@ ml16 | 从基线到可解释的短信实验 | A reproducible assignment workflow
CARDS: M090-M100
PREREQ: ml08,ml11
GOAL: 能独立建立短信分类基线，并用混淆矩阵解释失败。
EXPLAIN: 作业先拆为数据、特征、训练、选择、评价、交付六步。先让简单词袋加 NB 的基线端到端运行，再改变一个因素。记录训练样本数、标签映射、随机种子、词表拟合位置和评价函数，才能确定两个成绩来自可比较的实验。

混淆矩阵把“错了”细分为哪一类被判成哪一类。Recall 看该真实类别中找回多少；precision 看预测为该类的结果中多少正确。Balanced accuracy 对各类 recall 做算术平均，使多数类不能仅靠数量掩盖少数类失败。

错误分析应回到具体短信：是否分词错误、否定词缺失、稀有词未覆盖、内容本就模糊？提出可检验改动，而不是只抄一个更高分。提交要求和评分细节以当前 Assignment 1 卡片链接的原 Notebook 为准；这里的小例子不是代做实验或报告实际成绩。
RECAP_EN: Build a complete baseline before optimizing components. Use per-class errors to formulate testable improvements and preserve the distinction between validation choices and final evaluation.
WORKED_Q: 三类召回率 0.95、0.60、0.40，balanced accuracy 是多少？ || What is balanced accuracy for recalls 0.95,0.60,0.40?
WORKED_A: (0.95+0.60+0.40)/3=0.65。它给三个类别相同权重，不是把正确样本数直接除总数。 || The mean recall is 0.65. Each class receives equal weight, unlike ordinary accuracy based on total sample counts.
PRACTICE_Q: 某类 TP=8、FN=2、FP=4，recall 和 precision 各多少？ || For TP=8, FN=2, FP=4, compute recall and precision.
HINT: Recall 的分母来自真实类别，precision 的分母来自预测类别。 || Recall conditions on the true class; precision conditions on the predicted class.
PRACTICE_A: 召回率 recall=8/10=0.8；精确率 precision=8/12≈0.6667。 || Recall is 0.8 and precision is approximately 0.6667.
TRANSFER_Q: 一次实验同时换词表、分类器和数据划分，成绩上升能说明哪个部分有效吗？ || If vocabulary, classifier, and data split all change together, can an improved score identify the useful component?
TRANSFER_A: 不能。固定划分，分开比较改动，保留可复现配置；有必要时重复不同随机划分评估波动。 || No. Hold the split fixed, compare controlled changes, record configurations, and assess variation when appropriate.
BRIDGE: QE 需要从实验与公式上升到“为什么、何时成立、何时失败”的解释。

@@ ml17 | QE 口述：把模型讲成可追问的论证 | Explaining assumptions and decisions
CARDS: M101-M106
PREREQ: ml07,ml08,ml10,ml16
GOAL: 能用英文连续解释任务、模型、假设、决策规则和局限。
EXPLAIN: 一个完整解释可以按五句话展开：解决什么任务；用什么表示；模型假设什么；怎样训练和预测；什么情况下会失败。公式应嵌在这条论证中，而不是突然背出来。比如朴素贝叶斯的 fast 来自可分解的统计量，局限也正来自条件独立等建模假设。

预测概率和决策要分开。设 p 是垃圾短信后验，误封正常短信的代价为 C_FP，漏掉垃圾的代价为 C_FN；两者非负、和为正，正确判断代价均为零。预测垃圾的风险为 $C_{FP}(1-p)$，预测正常为 $C_{FN}p$。比较得阈值 $p>C_{FP}/(C_{FP}+C_{FN})$。换代价是在换决策规则，不是在重新证明 p 已校准。

高置信度不自动表示校准良好；零协方差也不自动表示独立。遇到追问时给出假设或反例，比用“通常都这样”更可靠。这里是表达练习，未宣称学校 QE 采用某个固定问答模板。
RECAP_EN: Naive Bayes combines class priors with factorized class-conditional evidence. It is efficient, but dependence violations and poor probability calibration can affect decisions. A decision threshold should reflect the costs of errors.
WORKED_Q: C_FP=9、C_FN=1，预测垃圾的概率阈值是多少？ || If C_FP=9 and C_FN=1, what posterior threshold selects spam?
WORKED_A: 阈值 9/(9+1)=0.9；误封正常邮件很贵，所以要求更强证据。等号时两种动作期望损失相同，需说明平局规则。 || The threshold is 0.9 because false positives are costly. At equality both actions have equal expected loss, so specify a tie rule.
PRACTICE_Q: 若代价交换，阈值是多少？ || What is the threshold if the costs are swapped?
HINT: 重新比较两个动作的期望损失。 || Compare the two expected losses again.
PRACTICE_A: 1/(1+9)=0.1，更重视避免漏掉垃圾。 || It becomes 0.1, prioritizing avoidance of false negatives.
TRANSFER_Q: 用英文解释为什么 NB 后验 0.99 不等于已经证明 99% 正确。 || Explain in English why a Naive Bayes posterior of 0.99 does not establish 99% empirical correctness.
TRANSFER_A: 概率依赖模型与数据分布，独立假设错误或分布变化可能导致过度自信；需用独立数据检查校准。 || The probability is conditional on a model and its assumptions. Dependence violations or distribution shift can cause overconfidence, so calibration must be checked on independent data.
BRIDGE: 后续 Extra Resources 可用于预习新模型；始终将它们映射回任务、假设、目标与验证这四个问题。

@@ ml18 | k-NN：先用附近的例子回答 | Nearest-neighbor reasoning
CARDS: M183-M186
PREREQ: ml03,ml15
GOAL: 能手算多数投票，并解释为什么尺度会改变邻居。
EXPLAIN: k-NN 在预测时找离查询点最近的 k 条训练样本，再用标签投票。它把复杂的全局边界变成局部问题，但“最近”完全依赖距离与表示：若一个特征的单位变大，它就可能主导欧氏距离。

k 小时边界更受个别样本影响；k 大时更平滑，却可能抹掉小区域的类别差异。距离加权是另一条规则，近点的票更重。两种规则都要说明平局和零距离处理，不能看到三个标签就默认所有实现必定给同一答案。
RECAP_EN: k-NN predicts from nearby training examples. The metric, feature scale, neighborhood size, and voting rule jointly determine the result.
WORKED_Q: 最近三点标签 A、B、B，距离 0.1、1、1。普通投票与 1/距离加权各选什么？ || The nearest labels are A,B,B at distances 0.1,1,1. Compare ordinary and inverse-distance voting.
WORKED_A: 普通投票 B 为两票，选 B；加权时 A 为 10，B 总共 2，选 A。 || Ordinary voting chooses B by two votes to one. Inverse-distance voting gives A weight 10 and B total weight 2, choosing A.
PRACTICE_Q: 若三点距离都相等，两种规则还会不同吗？ || Would the two rules differ if all three distances were equal and nonzero?
HINT: 每张票被乘上同一个系数。 || Every vote receives the same multiplier.
PRACTICE_A: 这个例子都选 B。 || Both choose B in this example.
TRANSFER_Q: 把距离特征从米改成毫米，模型不重做尺度处理会怎样？ || What can happen if a distance feature changes from meters to millimeters without rescaling?
TRANSFER_A: 它的平方距离贡献放大一百万倍，邻居可能改变。模型学到的“相似”不应无意地依赖单位。 || Its squared-distance contribution grows by a million, potentially changing neighbors. Similarity should not unintentionally depend on measurement units.
BRIDGE: k-NN 直接查例子；回归则用参数概括输入与连续输出的关系。

@@ ml19 | 最小二乘：从每个误差推到正规方程 | Least squares without skipping the derivative
CARDS: M187-M202
PREREQ: ml03,ml04,ml10
GOAL: 能逐项求导得到正规方程，说明何时唯一以及正则化改了什么。
EXPLAIN: 约定 X 的每行是一条样本，包含常数列时也可学习截距。令 $J(w)=\frac12\sum_i(\sum_jX_{ij}w_j-y_i)^2$。先只对第 k 个系数求导：第 i 个残差的导数为 X_ik，所以 $\partial J/\partial w_k=\sum_iX_{ik}(X_iw-y_i)$。把所有 k 的结果排列起来，恰好就是 $X^T(Xw-y)$。

令梯度为零得到 $X^TXw=X^Ty$。这表示残差与每个特征列正交，也就是投影思想。Hessian 是所有二阶偏导组成的矩阵，用来描述局部曲率；此处为 X^TX，因任意 v 都有 $v^TX^TXv=\|Xv\|^2\ge0$，目标是凸的。只有列满秩时它才正定，解才唯一；样本数够多本身不保证满秩。

加 $\frac\lambda2\|w\|^2$ 后，梯度增加 lambda w，得到 $(X^TX+\lambda I)w=X^Ty$。lambda>0 且所有系数都被惩罚时可得到唯一解；不惩罚截距时要按实际惩罚矩阵讨论。L1 则可能将部分系数压成零。数值上通常解方程或用 QR/SVD，不直接显式求逆。
SYMBOLS: X | N×d 设计矩阵；w | d 维系数；r=Xw-y | N 维残差；X^T r | d 维梯度；lambda | 非负惩罚强度，系数约定见正文
RECAP_EN: Differentiate one residual at a time to obtain X-transpose times the residual. The normal equations express orthogonality; uniqueness requires full column rank, unless an appropriate strictly convex penalty supplies it.
WORKED_Q: 拟合 (0,1)、(1,3)、(2,5) 的直线 y=b+ax，写出正规方程并解。 || Fit y=b+ax to (0,1),(1,3),(2,5) using the normal equations.
WORKED_A: X 的行为 (1,0)、(1,1)、(1,2)。X^TX=[[3,3],[3,5]]，X^Ty=(9,13)。方程 3b+3a=9、3b+5a=13，相减得 a=2，再得 b=1，残差全为零。 || X has rows (1,0),(1,1),(1,2). The equations are 3b+3a=9 and 3b+5a=13, giving a=2 and b=1, with zero residuals.
PRACTICE_Q: 一维 X^TX=1、X^Ty=3，lambda=1，按正文 Ridge 约定求 w。 || With X-transpose-X=1, X-transpose-y=3, and lambda=1, find the ridge coefficient under the stated convention.
HINT: 方程左边的系数变成 1+lambda。 || The coefficient on the left becomes 1+lambda.
PRACTICE_A: 系数 w=3/(1+1)=1.5。 || The coefficient is w=1.5.
TRANSFER_Q: X 两列完全相同，但有 1000 行，OLS 一定唯一吗？ || If X has two identical columns and 1,000 rows, must OLS have a unique solution?
TRANSFER_A: 不唯一；两列的权重可一增一减而不改变预测。列数不等于秩，更多重复样本无法恢复这个不可识别方向。 || No. Increasing one coefficient and decreasing the other equally leaves predictions unchanged. Sample count does not repair column dependence.
BRIDGE: 平方残差惩罚大错误特别重，因此下一节讨论异常点和不同损失。

@@ ml20 | 鲁棒回归：一个异常点为什么能拉走直线 | Outliers and robust fitting
CARDS: M203-M210
PREREQ: ml19
GOAL: 能比较平方损失、epsilon 不敏感损失与 RANSAC 的假设。
EXPLAIN: 残差从 1 增到 10，平方损失从 1 增到 100，梯度幅度也变大。一个远离主体的数据点可能明显拉动拟合结果。换损失是在改变错误代价；RANSAC 则先反复用小子集拟合候选模型，再寻找符合容差的内点集合。

先把“抽到全内点”与“拟合出好模型”分开。理想模型假设样本内每次取点独立、内点概率为 w，于是 s 个点全为内点的概率是 $w^s$；K 次独立尝试全失败的概率为 $(1-w^s)^K$。实际从有限数据中无放回取子集时，单次概率应为 $\binom{I}{s}/\binom{N}{s}$，I 是内点数，$w^s$ 是常用近似。全内点也可能几何退化，阈值仍须合理。

模型对输入非线性不代表对参数非线性，例如 b+a1 x+a2 x² 仍可线性求系数。核岭回归与 SVR 延续了这些区别；SVR 的 epsilon 不敏感损失是 max(0,|r|-epsilon)。
RECAP_EN: Robust fitting changes how residuals or consensus sets influence a model. RANSAC's success calculation depends on an idealized sampling model, not merely on running many iterations.
WORKED_Q: 按独立取点的理想模型，w=0.5、s=2，至少一次抽到全内点的概率要达到 0.99，需几次尝试？ || Under the independent-draw model, with w=0.5 and s=2, how many trials give at least 0.99 probability of drawing an all-inlier sample?
WORKED_A: 每次成功概率 0.25；要求 0.75^K≤0.01，K≥log(0.01)/log(0.75)≈16.008，向上取整为 17。 || Each trial succeeds with probability 0.25. Solving 0.75^K≤0.01 gives K≥16.008, hence 17 trials.
PRACTICE_Q: epsilon=0.2，残差 -0.5 的不敏感损失是多少？ || What is epsilon-insensitive loss for residual -0.5 and epsilon=0.2?
HINT: 先取绝对值再扣容差。 || Take the absolute value, then subtract the tolerance.
PRACTICE_A: 损失为 max(0,0.5-0.2)=0.3。 || The loss is 0.3.
TRANSFER_Q: y=a x²+b 为什么仍叫对参数线性？ || Why is y=a x²+b still linear in the parameters?
TRANSFER_A: 将 x² 视为已知特征后，未知 a、b 只以一次线性组合出现；输入曲线可以弯，参数优化仍是线性回归形式。 || Treat x² as a fixed feature: the unknown a and b enter linearly, even though the curve is nonlinear in x.
BRIDGE: 聚类同样用距离，但没有标签告诉我们哪条预测对错。

@@ ml21 | k-means：分组与代表点为什么交替更新 | Why k-means alternates
CARDS: M211-M216
PREREQ: ml03,ml19
GOAL: 能从平方距离目标推导均值更新，解释下降与全局最优的区别。
EXPLAIN: 分类有标签，聚类需要自己定义怎样算“同一组”。k-means 让每个点只属于一个组，并选择组中心，使点到自己中心的平方距离总和尽量小：$J=\sum_i\|x_i-\mu_{z_i}\|^2$。

同时选所有分组和中心很难，但固定其中一半后问题简单。中心固定时，每个点选最近中心；分组固定时，对非空组中心求导，中心就是组内平均值。因此两步都不会增大同一目标。距离平局要有固定规则；空簇没有均值，需保留旧中心或按明确规则重置，不能除以零。

以 0、2 这一组为例，中心 c 的损失是 $c^2+(2-c)^2=2(c-1)^2+2$，显然 c=1 最好。这个等式把“取均值”从口令变成可见的最小化理由。算法仍受初始化影响，可能停在局部解；增加 k 往往降低训练损失，不能据此无限增加簇数。
SYMBOLS: x_i | 第 i 个点；z_i | 它的簇编号；mu_k | 第 k 个簇的中心；J | 簇内平方距离总和，不是概率
RECAP_EN: Assignment minimizes the objective with centers fixed; taking means minimizes it with assignments fixed. This gives non-increasing loss, not a guarantee of the globally best clustering.
DEMO: kmeans
WORKED_Q: 数据 0、2、8、10，中心先取 0、10，完成一次分配和更新。 || For data 0,2,8,10 and initial centers 0,10, perform one assignment and update.
WORKED_A: 分为 {0,2} 与 {8,10}；更新中心为 1 和 9。平方距离和由 0+4+4+0=8 变为 1+1+1+1=4；再次分配不变。 || Assign {0,2} and {8,10}; update centers to 1 and 9. The objective falls from 8 to 4, and the next assignments are unchanged.
PRACTICE_Q: 若第一组是 0、2、4，它的中心应该是多少？ || What center minimizes squared distances for the group {0,2,4}?
HINT: 用均值更新，或对三个平方项求导。 || Take the mean or differentiate the three squared terms.
PRACTICE_A: 中心为 2，平方距离和 4+0+4=8。 || The center is 2, with squared-distance sum 8.
TRANSFER_Q: 每次迭代损失都下降，为什么仍要尝试多个初始化？ || Why try multiple initializations if every iteration reduces or preserves the loss?
TRANSFER_A: 不同起点可进入不同局部解；单次下降只比较同一轨迹的前后，不比较所有可能分组。 || Different starts can reach different local solutions. Monotonic descent compares successive iterates, not all possible clusterings.
BRIDGE: 点在两组边缘时，硬分配太绝对；GMM 用责任度表示软归属。

@@ ml22 | EM：先估计归属，再重估模型 | Soft clustering and EM
CARDS: M217-M226
PREREQ: ml07,ml21
GOAL: 能计算责任度与加权均值，并区分密度值和归属概率。
EXPLAIN: 想象两台机器都生产零件，但记录里没写每件来自哪台。GMM 假设先按混合权重选择成分，再从该成分的高斯分布生成观测；不知道成分标签，就不能直接按组统计。E 步计算“这一件有多大可能来自每台机器”：$r_{ik}=\pi_k\mathcal N(x_i;\mu_k,\Sigma_k)/\sum_j\pi_j\mathcal N(x_i;\mu_j,\Sigma_j)$。这叫责任度，对每个点跨成分求和为一。

M 步把责任度当分数权重重新统计：$N_k=\sum_i r_{ik}$，$\pi_k=N_k/N$，$\mu_k=\sum_i r_{ik}x_i/N_k$；协方差围绕新均值计算加权偏差的外积。若 N_k 为零或太小，需要处理失效成分。一个点可部分影响多个成分，有点像软分组，但 GMM 还学习方差与混合比例，不等同于直接把 k-means 的标签变软。

精确 EM 的单调性来自对似然下界的交替处理，不等于全局最优。无约束高斯成分可能压到某个数据点并令方差趋零，使似然异常增大；正则、初始化和有效样本量检查都很重要。
RECAP_EN: EM alternates posterior responsibilities and weighted parameter estimation. Responsibilities sum to one per observation; mixture densities themselves are not class probabilities.
WORKED_Q: 某点的两个加权密度为 0.12、0.08，责任度是多少？ || An observation has weighted component densities 0.12 and 0.08. Find its responsibilities.
WORKED_A: 总和 0.20，归一化后为 0.6、0.4。 || Normalizing by 0.20 gives responsibilities 0.6 and 0.4.
PRACTICE_Q: 点 0、10 对某成分的责任度为 0.8、0.2，更新均值与混合权重。 || Points 0 and 10 have responsibilities 0.8 and 0.2 for a component. Update its mean and mixture weight.
HINT: 先求有效样本数，再用它归一化均值；混合权重还要除总样本数。 || Compute effective count, then the weighted mean; divide that count by total N for the mixture weight.
PRACTICE_A: Nk=1，均值为 (0.8×0+0.2×10)/1=2，混合权重为 1/2。 || Nk=1, the mean is 2, and the mixture weight is 1/2.
TRANSFER_Q: 为何不能把每个成分的责任度在所有点上强制归一化为一？ || Why shouldn't responsibilities be normalized to one across observations for each component?
TRANSFER_A: 责任度回答的是某一个点来自哪一成分，应在成分维度归一化。跨点求和是有效样本数，大小反映该成分占比。 || A responsibility distribution concerns which component generated a given point. Summing across observations instead produces effective component size.
BRIDGE: 聚类找组，PCA 找能保留主要变化的坐标方向；两者都不直接等于分类目标。

@@ ml23 | PCA：用少数方向保留数据的变化 | PCA, projection, and SVD
CARDS: M227-M240
PREREQ: ml04,ml19
GOAL: 能解释中心化、最大方差方向和低秩重构之间的联系。
EXPLAIN: 先把每列减去训练均值，PCA 才是在解释围绕数据中心的变化。选择单位方向 v 后，每个点的投影是 x_i^T v，投影方差为 $v^T S v$，其中 S 是中心化样本协方差。限制 ||v||=1，避免仅靠把方向放大就增加方差。

特征向量满足 $Sv=\lambda v$：S 作用后仍沿原方向，lambda 表示该方向的方差。可以把 PCA 想成旋转坐标尺，先沿数据云最舒展的方向读数。实对称 S 有正交特征向量基；任意单位方向的方差是特征值的加权平均，因此最大方差取最大特征值对应方向，再依次取与前面正交的方向。单点得分是 $v^T(x-\mu)$，是新坐标，不是挑出某一原始特征。

中心化 X 的 SVD 为 UΣV^T，V 的列就是 PCA 方向，协方差特征值与奇异值平方相差样本分母因子。保留前 k 项给出平方重构误差意义下的低秩近似。去相关不保证独立，也不保证保留了对标签最有用的信息。
RECAP_EN: PCA selects orthogonal directions maximizing centered variance, equivalently minimizing squared reconstruction error. SVD computes these directions; explained variance is not predictive accuracy.
WORKED_Q: 协方差为 diag(9,1)，只保留一个方向，选哪个、保留多少方差？ || For covariance diag(9,1), which one-dimensional direction is selected and what variance fraction is retained?
WORKED_A: 选第一坐标方向 (1,0)，保留 9/(9+1)=90%。第二方向的变化被舍弃，但它仍可能携带标签信息。 || Select (1,0), retaining 90% of total variance. The discarded second direction could still contain label information.
PRACTICE_Q: 特征值 9、3、2、1，达到至少 90% 方差需要几维？ || For eigenvalues 9,3,2,1, how many dimensions retain at least 90% variance?
HINT: 总方差为 15，累计到阈值 13.5。 || Total variance is 15; the threshold is 13.5.
PRACTICE_A: 前两维为 12，不够；前三维为 14，需要 3 维。 || Two dimensions retain 12, insufficient; three retain 14, so use three.
TRANSFER_Q: 某特征从米变成毫米，未经标准化的 PCA 方向可能改变吗？ || Can unstandardized PCA change when one feature switches from meters to millimeters?
TRANSFER_A: 会，该特征方差放大一百万倍，并改变协方差结构。是否标准化应根据特征单位与任务含义决定。 || Yes. Its variance scales by a million and the covariance structure changes. Decide on standardization based on units and task meaning.
BRIDGE: PCA 通过线性投影提取特征；神经网络通过多层可学习变换得到更丰富的表示。

@@ ml24 | 反向传播：沿计算图分配责任 | Backpropagation through a computation graph
CARDS: M241-M254
PREREQ: ml03,ml10
GOAL: 能区分前向、反向、更新，并手算局部导数如何相乘与相加。
EXPLAIN: 常叫“线性层”的 $XW+b$ 严格说是仿射变换，因为含偏置。若中间没有非线性，连续两层仍可合并：$(XW_1+b_1)W_2+b_2=X(W_1W_2)+(b_1W_2+b_2)$。加层并未跳出仿射函数族；加入 ReLU，即 $\max(0,z)$ 这样的非线性，才改变表达能力。输出还需匹配任务：分类常用交叉熵，回归可用平方损失。

前向传播计算中间值与最终损失；反向传播应用链式法则，计算每个参数如何影响损失；优化器再使用这些梯度更新参数。这三步各司其职，反向传播本身不是一种学习率策略。

把大公式拆成小节点。对标量节点 u=g(v)，已知损失对节点输出的梯度 dL/du，乘 du/dv 才得到它对输入的贡献 dL/dv；这沿前向计算的反方向传递。同一变量有多条影响路径时，贡献相加。矩阵层中若 G=dL/dY，Y=XW+b，则 $dW=X^TG$、$dX=GW^T$，db 按样本行求和；G 应已含损失取和或均值的系数。
RECAP_EN: Backpropagation applies the chain rule efficiently on a computation graph. Multiply along each path and sum contributions at shared variables; the optimizer performs a separate parameter update.
WORKED_Q: f=(x+y)z，x=-2、y=5、z=-4，求 f 与三个偏导。 || For f=(x+y)z at x=-2,y=5,z=-4, compute f and its three partial derivatives.
WORKED_A: 先 u=x+y=3，f=uz=-12。df/du=z=-4，du/dx=du/dy=1，所以 df/dx=df/dy=-4；df/dz=u=3。 || u=3 and f=-12. The gradient through u is -4, giving df/dx=df/dy=-4; df/dz=3.
PRACTICE_Q: f=x×x，x=3，为什么导数是 6 而不是 3？ || For f=x*x at x=3, why is the derivative 6 rather than 3?
HINT: x 出现在乘法的两个输入位置。 || x appears on both inputs to the multiplication.
PRACTICE_A: 两条路径各贡献 3，总梯度 6。 || Each path contributes 3; their sum is 6.
TRANSFER_Q: 4 输入、3 输出的全连接层，每个输出有偏置，需要几个参数？ || How many parameters are in a dense layer with four inputs, three outputs, and one bias per output?
TRANSFER_A: W 有 4×3=12 个，b 有 3 个，总计 15。样本批量大小不改变共享参数数量。 || There are 12 weights and 3 biases, totaling 15. Batch size does not change the shared parameter count.
BRIDGE: CNN 在局部空间位置共享同一组参数，把图像结构融入网络。

@@ ml25 | CNN：同一个小检测器在图上滑动 | Convolution, shape, and receptive field
CARDS: M255-M264
PREREQ: ml24
GOAL: 能手算滑动内积、输出尺寸和参数数目。
EXPLAIN: 卷积层在一个小窗口内，将像素与滤波器权重逐项相乘再求和，然后把同一滤波器移动到别的位置。一个滤波器产生一个输出通道；多个输入通道的贡献在该输出通道内相加。空间位置共享权重，参数数目通常不随图像宽高增长。

沿一个轴，若输入长度 n、核宽 k、两侧填充 p、步长 s、膨胀为 1，则输出长度为 $\lfloor(n+2p-k)/s\rfloor+1$。这是数“窗口能从哪些起点完整放下”，而不是背一个尺寸口令。池化也做局部汇聚，但不一定有可学习权重。

数学卷积会翻转核，很多深度学习层实际做互相关；手算序列题时要遵守原定义。平移等变指输入移动导致输出相应移动，平移不变指输出不变；边界、步长与采样还会限制严格等变性。
RECAP_EN: A convolutional layer shares local filters across spatial positions. Count valid window placements for output size and distinguish mathematical convolution from the cross-correlation used by many neural layers.
WORKED_Q: 32×32 RGB 输入，6 个 5×5 核，步长 1、无填充，求输出形状及含偏置参数量。 || For 32×32 RGB input and six 5×5 filters with stride 1 and no padding, find output shape and parameter count including biases.
WORKED_A: 每轴 32-5+1=28，输出 28×28×6。每核 5×5×3=75 个权重加 1 偏置，总参数 6×76=456。 || Output shape is 28×28×6. Each filter has 75 weights and one bias, giving 456 parameters.
PRACTICE_Q: 输入序列 (1,2,3)，互相关核 (1,-1)，步长 1、无填充，输出是什么？ || Cross-correlate (1,2,3) with (1,-1), stride 1 and no padding.
HINT: 不翻转核，依次计算两个窗口。 || Do not flip the kernel; evaluate both windows.
PRACTICE_A: 两个窗口的输出为 (1-2,2-3)=(-1,-1)。 || The output is (-1,-1).
TRANSFER_Q: 两个连续 3×3 卷积，步长 1、无膨胀，第二层一个输出理论上依赖多大输入区域？ || What input receptive field supports one output after two 3×3 stride-one, undilated convolutions?
TRANSFER_A: 5×5。第二层汇聚第一层相邻三格，各自看三格，最远范围每轴扩为 3+2=5；不是 9×9。 || A 5×5 region. Combining three neighboring first-layer positions expands each axis from 3 to 5, not to 9.
BRIDGE: 网络结构定义能表示什么；优化与训练模式决定如何学到参数。

@@ ml26 | 训练网络：梯度、状态和正则化分别做什么 | Optimization and training state
CARDS: M265-M276
PREREQ: ml24,ml25
GOAL: 能区分优化器状态、数据统计与训练/评估模式。
EXPLAIN: mini-batch SGD 每步用一部分样本估计梯度；一个 epoch 表示看完一遍训练集，不等于一次更新。Momentum 累积方向，Adam 还维护梯度及平方梯度的移动平均，并做初期偏差修正。它们改变更新规则，不会自动消除数据泄漏或错误标签。

正则化控制学习偏好。Inverted dropout 以保留概率 q>0 留下激活，保留时除以 q，使这一激活的期望不变；经过后续非线性，整网输出的期望不一定不变。评估时不再随机丢弃。常见 BatchNorm 训练时按通道汇集批内统计，评估时用运行统计；LayerNorm 通常对每个样本/token 的指定特征维归一化，不依赖其他样本的批统计。

先用小子集检查是否能过拟合，再扩大实验。检查学习率、梯度、模式切换和增强是否保留标签含义。Early stopping 根据验证表现决定何时停，学习率计划决定怎样迈步，职责不同。AdamW 的衰减与在 Adam 损失中加入 L2 也不应机械等同。
RECAP_EN: Optimizers maintain update state; normalization layers and dropout maintain or use different training behavior. Debug a small subset and keep evaluation separate from parameter fitting and model selection.
WORKED_Q: N=1000、batch size=100，每批执行一次参数更新、不做梯度累积，一 epoch 更新几次？ || With N=1000, batch size 100, and one optimizer update per batch without gradient accumulation, how many updates occur per epoch?
WORKED_A: 1000/100=10 次。训练 5 epoch 则为 50 次更新，不是 5 次。 || Ten updates per epoch, hence fifty updates over five epochs.
PRACTICE_Q: 激活 3，dropout 保留概率 q=0.75，保留时输出多少，期望多少？ || For activation 3 and retention probability 0.75, what is the retained output and its expectation?
HINT: 保留时除以 q，丢弃时为零。 || Divide by q when retained, otherwise output zero.
PRACTICE_A: 保留时为 4，期望 0.75×4+0.25×0=3。 || The retained output is 4; its expectation is 3.
TRANSFER_Q: 固定权重后重复预测还不稳定，是否一定是优化器没收敛？ || If repeated predictions vary with fixed weights, must the optimizer have failed to converge?
TRANSFER_A: 不一定；先检查是否仍开着训练模式的 dropout、随机增强或其他随机处理，以及归一化模式。 || No. Check training-mode dropout, random augmentation or other stochastic processing, and normalization behavior first.
BRIDGE: 视觉任务的输出与评价标准不同，不能只按网络名称判断方法优劣。

@@ ml27 | 视觉任务：输出决定损失与评价 | Vision tasks and evaluation
CARDS: M277-M284
PREREQ: ml25,ml26
GOAL: 能区分类别、框、像素与实例输出，并解释重构指标的局限。
EXPLAIN: 分类给整图标签；检测还要给对象位置；语义分割给每个像素语义类别；实例分割还分开同类的不同对象。输出结构不同，所以头部、损失和评价标准不能直接混用。残差连接把变换结果与输入相加，需要形状兼容，目的是提供额外的信息和梯度路径。

图像恢复可写成 y=Ax+noise：y 是观测，x 是希望恢复的图，A 表示模糊、下采样等退化。多个不同 x 可能解释同一 y，因此恢复依赖先验。像素平方误差衡量数值接近，不能完整表达视觉感受或语义正确。

压缩还需同时考虑码率与失真。模型比较应先固定任务、数据、度量与测试协议；好看的样例不证明所有场景都可靠，反复针对同一测试集调参也会削弱它的独立性。
RECAP_EN: Output structure determines the task and evaluation. Pixelwise reconstruction error, perceptual quality, and semantic correctness measure different aspects of a result.
WORKED_Q: 真值像素为 (0,2)，预测 A=(1,1)，B=(0,0)，两者 MSE 各多少？ || For target pixels (0,2), compute MSE for A=(1,1) and B=(0,0).
WORKED_A: A 为 (1+1)/2=1，B 为 (0+4)/2=2。该指标偏好 A，但这个两像素计算不能单独代表人类对完整图像的感知。 || A has MSE 1 and B has MSE 2. The metric prefers A, but this toy calculation alone does not establish perceptual quality for full images.
PRACTICE_Q: 两辆相邻汽车只被标成一片 car 区域，语义分割和实例分割要求有何不同？ || Two adjacent cars are labeled as one car region. How do semantic and instance segmentation requirements differ?
HINT: 问是否需要区分对象身份。 || Ask whether separate object identities are required.
PRACTICE_A: 语义分割只需像素类别；实例分割需再区分两个对象。 || Semantic segmentation assigns pixel classes; instance segmentation must additionally separate the two objects.
TRANSFER_Q: 降低图像压缩 MSE 就一定得到更好的压缩系统吗？ || Does lowering MSE necessarily produce a better compression system?
TRANSFER_A: 不一定，还要看用了多少码率、视觉质量、任务需求和比较条件。应比较给定码率下的失真或完整率失真曲线。 || No. Consider bitrate, perceptual quality, task needs, and comparable conditions; compare distortion at a fixed rate or rate-distortion curves.
BRIDGE: 恢复试图解释观测，生成模型则尝试从随机变量采样新的数据。

@@ ml28 | 生成模型：采样不等于计算密度 | GANs and diffusion models
CARDS: M285-M294
PREREQ: ml06,ml24,ml26
GOAL: 能分别说明 GAN 的对抗训练与扩散的加噪/去噪过程。
EXPLAIN: 生成器可以把简单随机 z 映射为图像 G(z)，因此能采样，却未必能高效给某张图计算精确概率密度。GAN 训练判别器区分真实与生成样本，再训练生成器改变这种判断；双方改变彼此面对的目标，所以不能把两个损失都当作固定函数的普通下降。

标准高斯扩散训练可直接采样 $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$，其中 $\epsilon\sim\mathcal N(0,I)$ 与 x0 独立，bar-alpha 是各步 alpha 的乘积。可以理解为逐渐让信号被噪声淹没；两个系数的平方相加为 1，这是加噪的尺度安排，不是将两幅图按普通百分比混合。网络常学习预测 epsilon；生成时从噪声出发反复使用预测，不是掌握了新图的真实噪声再直接相减。

在这个前向模型中，给定 x0、xt 的一步后验可为高斯；只给 xt 的真实反向分布一般不能据此断言精确高斯。文字等条件可影响去噪预测：无条件预测 epsilon_u 与条件预测 epsilon_c 的差表示条件带来的调整，引导强度控制采用多少调整。质量、多样性与条件符合度须分别评价。
RECAP_EN: Sampling and density evaluation are distinct. GANs learn through a changing adversarial objective; diffusion trains a denoising-related model under a specified forward noise process and uses a learned reverse process for sampling.
WORKED_Q: bar-alpha=0.36，x0=2，epsilon=1，xt 是多少？ || For bar-alpha=0.36, x0=2, and epsilon=1, compute xt.
WORKED_A: 信号系数 √0.36=0.6，噪声系数 √0.64=0.8，所以 xt=0.6×2+0.8×1=2。数值恰好相同不意味着没有噪声。 || xt=0.6*2+0.8*1=2. Its accidental equality to x0 does not mean that no noise was added.
PRACTICE_Q: 引导式 epsilon_u+s(epsilon_c-epsilon_u) 中，s=0、1 分别是什么？ || In epsilon_u+s(epsilon_c-epsilon_u), what do s=0 and s=1 produce?
HINT: 直接代入，注意这一公式的系数约定。 || Substitute into this specific convention.
PRACTICE_A: s=0 为无条件预测，s=1 为条件预测。 || They give the unconditional and conditional predictions, respectively.
TRANSFER_Q: 生成器反复生成几张很逼真的图，为什么还可能有严重问题？ || Why can a generator producing a few highly realistic images still have a serious problem?
TRANSFER_A: 它可能只覆盖少数模式，缺少多样性；需检验分布覆盖与条件一致性，不能只展示精选样例。 || It may suffer mode collapse and poor diversity. Evaluate coverage and conditioning, not only selected attractive samples.
BRIDGE: Transformer 的注意力是一种信息组合运算，可用于判别或生成，并不由任务名称决定。

@@ ml29 | 注意力：每个位置向其他位置取信息 | Attention, dimensions, and robustness
CARDS: M295-M302
PREREQ: ml03,ml11,ml24
GOAL: 能区分 query/key/value，手算注意力加权，并核对矩阵维度。
EXPLAIN: 把 token 暂时看作一个词块或图像小块。像查资料一样，query 是查询条件，key 是可匹配的索引，value 是取回后要组合的内容；它们都是学出来的向量，不是人工填写的文字。标准注意力为 $\operatorname{softmax}(QK^T/\sqrt{d_k})V$：对每个 query 的行归一化，再加权组合 values。权重和为一，输出仍通常是特征，不是类别概率。

若 X 为 n×D，WQ、WK 为 D×dk，WV 为 D×dv，则 QK^T 为 n×n，输出为 n×dv。投影处理特征维，不是 token 数。在独立、单位方差分量的直观模型下，内积分数方差随 dk 增长；除以 √dk 可抑制分数过大导致 softmax 过于尖锐。位置机制再补充顺序；自回归生成还需因果遮罩，阻止读取未来位置。

多头让模型在不同投影下组合关系；前馈块处理各 token 的特征。稠密注意力仍有两两交互成本。鲁棒性问题则问输入小改动是否改变决策：随机噪声与为了诱发错误而优化的扰动不同，任何结论都需说明威胁模型。
RECAP_EN: Queries and keys produce matching weights; values supply the mixed information. Normalize over keys for each query and check feature dimensions separately from token count.
WORKED_Q: 一个 query 的缩放后分数 (log3,0)，values=(2,10)，输出多少？ || For scaled scores (log3,0) and scalar values (2,10), what is the attention output?
WORKED_A: softmax 权重 (3/4,1/4)，输出为 3/4×2+1/4×10=4。 || Weights are (3/4,1/4), giving output 4.
PRACTICE_Q: 两个分数相等、values=(2,10)，输出多少？ || With equal scores and values (2,10), what is the output?
HINT: 两个权重相同且和为一。 || The two weights are equal and sum to one.
PRACTICE_A: 权重各 1/2，输出 6。 || Each weight is 1/2, so the output is 6.
TRANSFER_Q: token 数翻倍、特征宽度固定，稠密分数矩阵有多少倍元素？ || If token count doubles with feature width fixed, how does the dense score matrix size change?
TRANSFER_A: 从 n² 变成 (2n)²=4n²，为 4 倍；不能据此断言整网运行时间恰好四倍。 || It has four times as many entries. This alone does not imply exactly four times the end-to-end runtime.
BRIDGE: 进入往年综合题时，先识别需要哪条知识链，再开始推导。

@@ ml30 | 综合题诊所：拆条件、补中间式、找反例 | A clinic for historical derivations
CARDS: M303-M326
PREREQ: ml04,ml06,ml19,ml24
RELATED: ml13,ml23,ml25
GOAL: 能给长题列出条件和小步骤，并识别数值答案依赖的隐含约定。
EXPLAIN: 往年题跨越概率、熵、高斯条件分布、优化、线性代数、SVM、PCA、卷积与 DTFT，不应一口气按编号背完。按题回到相应微课：概率题回贝叶斯与 MLE；约束题回 KKT；秩与正规方程回最小二乘；PCA 回投影；卷积题回核翻转和索引。图题先打开卡片原图，保留原始下标。

推导时先写变量与成立条件，再给中间量命名。例如对 ell=(u exp(v)-2v exp(-u))²，先令 q 为括号项，然后写 2q 乘 q 的各偏导。同时梯度更新必须都使用旧的 u,v；先更新一个再算另一个，已经是另一种算法。

对“总成立”的命题优先找边界与反例：方阵也可能秩不足；零乘子不保证约束不活跃；线性不代表时不变。对历史解答的分组计数 4+ 也不能默认为 4。这里提供解题入口和代表性练习，24 张原题仍应分主题闭卷重做。
RECAP_EN: For a long derivation, state assumptions, introduce intermediate variables, and verify dimensions and boundary cases. A numerical answer is meaningful only under its data interpretation and update convention.
WORKED_Q: 对 ell=q²，q=u exp(v)-2v exp(-u)，写出两个偏导。 || For ell=q² and q=u exp(v)-2v exp(-u), derive both partial derivatives.
WORKED_A: dq/du=exp(v)+2v exp(-u)，dq/dv=u exp(v)-2 exp(-u)；分别再乘 2q。负号与 exp(-u) 的导数负号在第一式中相消。 || dq/du=exp(v)+2v exp(-u) and dq/dv=u exp(v)-2 exp(-u). Multiply each by 2q; the two negative signs cancel in the first derivative.
PRACTICE_Q: X 以概率 0.2 取 8，其余情况取其他值，E[I(X=8)] 是多少？ || If P(X=8)=0.2, what is E[I(X=8)]?
HINT: 指示变量只能是零或一。 || The indicator is either zero or one.
PRACTICE_A: 1×0.2+0×0.8=0.2；不是把 E[X] 代入指示函数。 || It is 0.2, not the indicator evaluated at E[X].
TRANSFER_Q: 一个计数表将尾部记为 4+，为什么精确样本均值通常不能只从表中恢复？ || Why can't the exact sample mean generally be recovered when a count table groups its tail as 4+?
TRANSFER_A: 组内实际次数未知。将每个 4+ 当成 4 只给出下界或额外假设下的值；删失模型需要把尾部概率写入似然。 || The actual tail counts are unknown. Replacing each with 4 gives a lower bound or an assumption-dependent value; a censored model must use the tail probability in its likelihood.
BRIDGE: 复习顺序是先讲通一条推导，再拆成几张检索卡，最后用未见变式检查能否迁移。
