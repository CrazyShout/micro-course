# CS5489 连续微课主稿

本稿是 AI 编写的串讲与教学例题，来源通过 CARDS 关联到原课件页/单元。卡片范围表示复习入口，不表示一节短课穷尽了这些卡片的所有细节。PREREQ 是概念先修；BRIDGE 解释联系。题答的 ` || ` 分隔中文与英文。

@@ ml01 | 学习的对象：从短信到可检验的预测 | From messages to testable predictions
CARDS: M001,M002,M003,M004,M327,M328
PREREQ:
GOAL: 能把一个预测任务写成特征、标签、参数、超参数与训练—验证—测试流程，并识别信息泄漏。
EXPLAIN: 想让计算机识别垃圾短信，先把每条短信变成特征 x，例如长度和 free 出现次数；训练时还知道标签 y，例如 spam 或 ham。模型 f 把 x 映射为预测。学习不是记住文件名，而是用训练样本决定 f 的参数，使新短信也能被正确处理。

把模型比作一套待调整的评分规则：每个词的权重是参数；采用哪种模型、正则化强度多大是超参数。训练集用于拟合参数，验证集用于比较方案，最后的测试集用于评估已选定方案。反复看测试成绩再修改方案，会把测试集变成实际的验证集。

分类预测类别；回归预测连续量。两者都应先说明输入、输出、损失和评价指标。准确率高不等于方法在所有场景可靠，还要看类别比例、错误代价和新数据是否变化。
RECAP_EN: Define the prediction task before choosing an algorithm. Fit parameters on training data, choose settings using validation data, and evaluate the selected procedure on held-out test data.
WORKED_Q: 短信用 free 次数 x 预测标签 y（垃圾=1、正常=0）。规则为分数 wx，w 从数据学得；候选模型设置有简单版和复杂版。100 条已标注短信按 80/10/10 划分。每组分别做什么，w 和模型设置分别叫什么？ || A spam task uses free-count x to predict y (spam=1, legitimate=0), with score wx and learned w. Choose between simple and complex model settings using an 80/10/10 split of 100 labeled messages. What is each split for, and which quantity is a parameter versus a hyperparameter?
WORKED_A: x 是特征，y 是标签；w 是训练得到的参数，预先比较的模型设置是超参数。80 条拟合每个候选的 w；10 条验证比较候选；选定方案后，用最后 10 条报告成绩。测试结果不能再反过来挑方案。 || x is the feature, y the label, w a fitted parameter, and the candidate setting a hyperparameter. Fit each candidate on 80 messages, compare them on 10 validation messages, then evaluate the selected procedure on the final 10. Do not choose the procedure using its test result.
PRACTICE_Q: 200 条短信按 160/20/20 划分。要学习词的权重、从两个平滑强度中选一个、报告最后成绩，分别使用哪组？ || For a 160/20/20 split of 200 messages, which split fits word weights, selects between two smoothing strengths, and reports final performance?
HINT: 把“拟合数值”“比较设置”“最后检验”分别对应到三组。 || Match fitting values, choosing settings, and final evaluation to the three splits.
PRACTICE_A: 160 条训练拟合权重；20 条验证选平滑强度；最后 20 条测试只用于评价已选流程。每个候选的词表等预处理也只从训练组学习。 || Use 160 training messages for fitting, 20 validation messages for smoothing selection, and the final 20 for evaluation. Fit each candidate’s vocabulary and preprocessing using training data only.
TRANSFER_Q: 另一位同学不读测试标签，却先用全部 200 条短信建立词表，再按 160/20/20 训练与评价。指出泄漏位置，并写出修正后的先后顺序。 || A student builds the vocabulary from all 200 messages without reading test labels, then trains and evaluates on the split. Identify the leakage and give the corrected order.
TRANSFER_A: 词表已看到验证和测试文本的分布。先划分；只用 160 条训练文本拟合词表和模型；用固定词表变换验证、测试文本；验证选方案，测试评价。这里采用普通归纳评估，特殊传导设置须另行声明。 || Vocabulary fitting has already used validation and test distributions. Split first; fit vocabulary and models on training text; transform other splits with that fixed vocabulary; select on validation and evaluate on test. This is the ordinary inductive protocol; a transductive setting must be declared separately.
BRIDGE: 下一步先把这条流程写成能够从干净状态运行的程序，之后再讨论模型公式。

@@ ml02 | 让代码忠实执行你的想法 | Python and reproducible notebooks
CARDS: M007,M008,M009,M010,M011,M012,M013,M014,M015,M016,M017,M018,M019,M020,M334,M335,M336,M337
PREREQ: ml01
GOAL: 能逐行跟踪一个含循环、判断和 return 的函数，并在干净 Notebook 中独立复现。
EXPLAIN: Notebook 的单元是界面顺序，内存中的变量却取决于实际执行顺序。先运行后面的单元，再改前面的变量，屏幕上可能同时保留不属于同一次运行的结果。重启内核并从头运行，才是在检查流程是否完整。

先掌握三个动作：用变量保存值，用循环逐个处理对象，用函数把输入变成输出。print 是给人看，return 才把结果交给后续计算。列表保存有序对象；字典把词映射到计数；集合帮助去重。类把一组状态和相关方法放在一起，后面分类器的 fit 会存参数，predict 再使用这些参数。

先把可跟做的完整函数写出来。本例假设 n 是至少 2 的整数；缩进表示哪些语句属于循环或判断。定义单元只建立规则，后面的调用才实际计算。

```python
def count_factors(n):
    count = 0
    for d in range(2, n):
        if n % d == 0:
            count = count + 1
    return count

answer = count_factors(12)
print(answer)  # 4
```

range 依次提供候选；% 求余；== 比较；仅余数为 0 才加 1。return 位于循环外，因此先检查完全部候选再交回计数。掌握逐行过程后，才可把它压缩为 `def count_factors(n): return sum(n % d == 0 for d in range(2,n))`；sum 把每个 True 当作 1，这不是新的数学规则。

注意对象共享：b = a 通常让两个名字指向同一个可变列表，修改 b 也会影响 a。复制、视图和随机数状态都可能让“公式没错”的实验产生错误结果。
RECAP_EN: A notebook is a stateful program. Track data flow, distinguish printing from returning, and verify the complete workflow by restarting and running all cells in order. The complete function below assumes an integer n≥2. The return statement is outside the loop, so every candidate is checked before returning the count.

```python
def count_factors(n):
    count = 0
    for d in range(2, n):
        if n % d == 0:
            count = count + 1
    return count

print(count_factors(12))  # 4
```
WORKED_Q: 使用正文多行 count_factors 函数计算 n=6。依次列出 d、6 % d、count 的变化和最后的返回值。 || Trace the multiline count_factors function above for n=6. List each d, remainder, count change, and returned value.
WORKED_A: count 从 0 开始。d=2：余数 0，count=1；d=3：余数 0，count=2；d=4：余数 2，不加；d=5：余数 1，不加。循环结束 return 2；2、3 是除 1 和 6 外的正因数。 || Start count at zero. For d=2, remainder 0 makes count 1; d=3 makes it 2; d=4 gives remainder 2 and d=5 remainder 1, so neither increments it. Return 2: the eligible divisors are 2 and 3.
PRACTICE_Q: 同一函数输入 n=8，候选 d 为 2 到 7。先找能整除的 d，再补出 return 的结果。 || Run the same function for n=8 with candidates 2 through 7. Find the divisors and complete the returned count.
HINT: 依次检查 8 % d 是否等于 0；不要计入 1 与 8。 || Check whether 8 % d equals zero; exclude 1 and 8.
PRACTICE_A: d=2、4 时余数为 0，其余候选不是因数，count 依次为 1、2，最后 return 2。 || Only 2 and 4 divide 8, so the counter becomes 1, then 2, and the function returns 2.
TRANSFER_Q: 在重启后的 Notebook 中调用 count_factors(7)，应先运行什么单元、得到什么值？若把函数最后的 return count 改为 print(count)，y=count_factors(7) 的 y 又是什么？ || After restarting a notebook, what must run before count_factors(7), and what value should it return? If return count is replaced by print(count), what does y=count_factors(7) assign to y?
TRANSFER_A: 先运行函数定义单元，再运行调用；7 没有符合条件的因数，因此返回 0。改为 print 后屏幕仍显示 0，但没有 return 的函数返回 None，所以 y 是 None。 || Run the function-definition cell before the call. Seven has no eligible divisors, so it returns zero. Replacing return with print displays zero but makes the function return None; y is None.
BRIDGE: 列表适合组织对象，机器学习计算则需要具有明确形状的数组。

@@ ml03 | 先看形状，再看矩阵公式 | Shapes before matrix formulas
CARDS: M021,M022,M023,M024,M025,M026,M027,M028,M029,M030,M031,M032,M033,M034,M329,M330,M035,M036
PREREQ: ml02
GOAL: 能把每行样本的加权求和写成矩阵乘法，并逐步检查预测与残差的形状。
EXPLAIN: 约定一行是一条样本，一列是一种特征。X 有 N 行 d 列，权重 w 有 d 个数；一条样本的预测是各特征乘对应权重后求和，全部样本一起写成 Xw。矩阵式只是把重复的标量运算打包，并没有增加新规则。

axis=0 的均值把样本轴压掉，得到每个特征的均值；axis=1 则得到每条样本内部的平均值。转置把行列交换，reshape 只是按元素顺序重新安排形状，两者通常不同。NumPy 的 * 是逐元素乘，@ 才是矩阵乘。

广播从末尾维度对齐：相等或有一个为 1 才兼容。因此 (N,1) 减 (N,) 会被当作列向量减行向量，得到 N×N 个两两差，而不是 N 个样本残差。每一步先写预期 shape，再运行确认。

把 Tutorial 1 的绘图任务也放在这里：对每个 n=2,…,100，计算不含 1 和 n 的正因数个数 f(n)。散点图用 (n,f(n))，一个点对应一个整数；直方图对 f(n) 分组，一个柱的高度表示有多少整数具有该计数。例如 12 的非平凡因数为 2、3、4、6，因此散点含 (12,4)，直方图中“4 个因数”这一组多计一个。因为一共有 99 个整数，各箱频数之和应为 99。

另一个绘图练习给出形状 (120,2) 的数组，每行就是一个二维点。`mydata[:,0]` 取全部横坐标，`mydata[:,1]` 取全部纵坐标，再交给 scatter。这里要学的是“数组的行怎样对应观察对象”，不需要先读其他文件才能理解问题。
SYMBOLS: X | 数据矩阵，N×d；w | 权重向量，d；Xw | 预测，N；X^T X | d×d 特征内积矩阵
RECAP_EN: Matrix notation packages scalar operations. With samples in rows, X has shape N by d and Xw contains N predictions. Broadcasting compatibility does not guarantee the intended meaning.
WORKED_Q: X 的两行为 (1,2)、(3,4)，w=(2,-1)，标签 y=(1,1)。求 Xw、预测减标签的残差，并给出形状。 || X has rows (1,2),(3,4), w=(2,-1), and labels y=(1,1). Compute Xw and prediction-minus-label residuals, giving each shape.
WORKED_A: 第一行得 1×2+2×(-1)=0；第二行得 3×2+4×(-1)=2。X 为 (2,2)、w 为 (2,)，预测为 (0,2)、形状 (2,)；减去同形状 y，残差 (-1,1)，仍为 (2,)。 || Row sums are 0 and 2. X has shape (2,2), w (2,), and predictions (0,2) shape (2,). Subtract same-shaped labels to get residuals (-1,1), also shape (2,).
PRACTICE_Q: X 的行为 (2,1)、(0,3)、(1,1)，w=(1,2)，y=(3,5,3)。先算第一行 2×1+1×2，再补出全部预测与残差形状。 || Use rows (2,1),(0,3),(1,1), weights (1,2), and labels (3,5,3). Start with 2×1+1×2, then compute all predictions and residual shapes.
HINT: 一行产生一个预测；三行应产生三个数。 || One prediction per row means three output numbers.
PRACTICE_A: 预测 (4,6,3)，残差 (1,1,0)。X 为 (3,2)，w 为 (2,)，预测和 y 都是 (3,)。 || Predictions are (4,6,3), residuals (1,1,0). Shapes are X=(3,2), w=(2,), and predictions and labels=(3,).
TRANSFER_Q: 三条样本的预测被存为形状 (3,1)，标签为 (3,)。直接相减得到什么形状？怎样改成逐样本残差，并解释原因？ || Three predictions are stored as (3,1), with labels (3,). What shape does subtraction produce, and how should you obtain matched per-sample residuals?
TRANSFER_A: 广播将 (3,) 视为末轴有 3 个数，和三行的 (3,1) 组合出 (3,3)。应先把双方统一为 (3,) 或都为 (3,1)，再相减并检查形状；这样每个预测只减自己的标签。 || Broadcasting combines three rows with three columns, producing (3,3). Convert both to (3,) or both to (3,1) before subtraction, then assert equal shapes so each prediction subtracts its own label.
BRIDGE: 内积不仅用于预测，也能衡量方向对齐程度；这就连接到投影、正交化和后来的 PCA。

@@ ml04 | 投影：把一个向量拆成已有部分和新信息 | Projection and orthogonalization
CARDS: M037,M038,M039,M040,M041
PREREQ: ml03
GOAL: 能解释 Gram–Schmidt 每次减掉什么，并手算两维例子。
EXPLAIN: 想知道 v 中有多少已经沿着 u 的方向，可把投影写成 a u。选择 a 使剩余 r=v-au 与 u 垂直，即 u^T r=0。代入得到 a=(u^T v)/(u^T u)。分母是在校正 u 本身的长度；只有 u 已是单位向量时才能省掉。

Gram–Schmidt 先把第一个非零向量归一化，再从后续向量中减掉它们沿已建立正交方向的投影。余下的部分代表尚未被这些方向表示的新信息；最后把余量除以长度。零余量意味着线性相关，不能继续除以零。

这也解释了为什么用 E^T E 检查结果：对角线是每列长度的平方，非对角线是方向间内积。得到单位矩阵说明列向量正交归一，但仍应确认这些列张成了原目标空间。
RECAP_EN: Projection removes the component already explained by a direction. Gram–Schmidt repeatedly subtracts projections, then normalizes the remaining independent component.
WORKED_Q: 对 v1=(1,1)、v2=(1,0) 做正交归一化。 || Orthonormalize v1=(1,1) and v2=(1,0).
WORKED_A: e1=(1,1)/√2。v2 在 e1 上的投影为 (1/√2)e1=(1/2,1/2)，余量 (1/2,-1/2)，长度 1/√2，所以 e2=(1,-1)/√2。两向量内积为 0。 || e1=(1,1)/√2. Subtract the projection (1/2,1/2) from v2, leaving (1/2,-1/2). Normalization gives e2=(1,-1)/√2, orthogonal to e1.
PRACTICE_Q: 对v₁=(2,0)、v₂=(3,4)做Gram–Schmidt。先把v₁归一化，再给v₂投影、余量与第二单位向量。 || Apply Gram–Schmidt to v₁=(2,0),v₂=(3,4). Normalize the first vector, then find projection, residual and second unit vector.
HINT: e₁=(1,0)，投影为(e₁ᵀv₂)e₁，最后把余量除以长度。 || Use e₁=(1,0), projection (e₁ᵀv₂)e₁, then normalize the residual.
PRACTICE_A: e₁=(1,0)，投影3e₁=(3,0)，余量(0,4)，长度4，e₂=(0,1)。两者单位长度且内积0。 || e₁=(1,0); projection (3,0); residual (0,4) of length4; e₂=(0,1). Both have unit length and zero inner product.
TRANSFER_Q: 对v₁=(1,1)、v₂=(2,2)正交归一化。独立算第二余量，说明能否得到两个独立单位方向。 || Orthonormalize v₁=(1,1),v₂=(2,2). Compute the second residual and determine whether two independent unit directions exist.
TRANSFER_A: e₁=(1,1)/√2，e₁ᵀv₂=2√2，投影=(2,2)，余量为0。两向量线性相关，不能除以零归一化；只提供一个独立方向。 || The first unit vector is (1,1)/√2. Projection coefficient 2√2 reproduces v₂, leaving zero residual. Only one independent direction exists; do not normalize zero.
BRIDGE: 投影最小化剩余距离的思想会在最小二乘和 PCA 中再次出现。

@@ ml05 | 贝叶斯公式就是重新数一遍可能的人群 | Bayes through concrete counts
CARDS: M042,M043,M044,M045,M046,M047,M048,M049
PREREQ: ml01
GOAL: 能从人数表推回条件概率与后验公式。
EXPLAIN: P(free|spam) 问的是“已经知道是垃圾短信，其中多少有 free”；P(spam|free) 问的是“已经看到 free，其中多少是垃圾”。它们筛选的分母人群不同，不能交换。

想象 1,000 条短信，其中 20% 是垃圾。若垃圾中 60% 有 free，正常中 10% 有 free，那么看见 free 的人群包括 120 条垃圾和 80 条正常。后验就是在这 200 条中再数垃圾比例。贝叶斯公式中的分子是目标类别贡献的人数比例，分母是所有类别贡献之和。

把人数换成比例就是 $P(c\mid x)=P(x\mid c)P(c)/\sum_k P(x\mid k)P(k)$，分母须大于零。先验像筛选前的底数，似然决定每类留下多少，后验才是筛选后的占比。连续特征将似然换成密度；密度可以大于 1，区间下的面积才是概率。
SYMBOLS: $P(c)$ | 先验 prior；$P(x\mid c)$ | 似然 likelihood；$P(x)$ | 证据 evidence；$P(c\mid x)$ | 后验 posterior
RECAP_EN: Bayes' rule changes the conditioning population. Multiply the prior by the likelihood, then normalize over all possible classes.
DEMO: bayes
WORKED_Q: 1,000 条短信中 20% 为垃圾；垃圾中 60% 含 free，正常中 10% 含 free。看到 free 后垃圾概率是多少？ || Of 1,000 messages, 20% are spam; 60% of spam and 10% of legitimate messages contain free. What is the spam probability given free?
WORKED_A: 垃圾且有 free：1000×0.2×0.6=120；正常且有 free：1000×0.8×0.1=80。后验为 120/(120+80)=0.6。 || There are 120 spam messages and 80 legitimate messages containing free. The posterior is 120/200=0.6.
PRACTICE_Q: 垃圾先验改为 0.1，P(free|spam)=0.6、P(free|ham)=0.1 保持不变。看到 free 后垃圾概率是多少？ || With spam prior 0.1, P(free|spam)=0.6 and P(free|ham)=0.1, what is the spam posterior given free?
HINT: 在新的人群比例下重新计算两个分子贡献。 || Recompute both class contributions under the new prior.
PRACTICE_A: 后验为 0.1×0.6/(0.1×0.6+0.9×0.1)=0.4。 || The posterior is 0.06/(0.06+0.09)=0.4.
TRANSFER_Q: 若垃圾先验为 0.2，两类中 free 出现概率都为 0.6，看到 free 后垃圾概率是多少？解释这个词有没有改变判断。 || If the spam prior is 0.2 and free appears with probability 0.6 in both classes, what is the spam posterior, and does the word change the evidence?
TRANSFER_A: 分子为 0.2×0.6=0.12，分母为 0.12+0.8×0.6=0.60，后验仍为 0.2。两类同样容易产生该证据，所以它不改变先验优势比。 || The numerator is 0.12 and denominator 0.60, so the posterior remains 0.2. Equal class-conditional probabilities leave the prior odds unchanged.
BRIDGE: 概率表通常未知，下一节用训练样本估计它们。

@@ ml06 | MLE：选择最能解释已见数据的参数 | Maximum likelihood and generative classification
CARDS: M050,M051,M052,M053,M054,M055,M056,M057,M058,M059,M060
PREREQ: ml05
GOAL: 能从独立伯努利观测写出似然、求出 MLE，并检查内部解与边界；高斯估计见补充单元。
EXPLAIN: 生成式分类器分别学习类别比例和每类会生成什么样的特征，然后用贝叶斯公式做判断。最大似然把数据固定、参数视作待选量：哪个参数使这批观测联合出现的概率或密度最大，就选哪个。它不是“给参数直接求概率”，后者需要先验。

这里 log 指自然对数，是指数函数 exp 的反函数。它严格递增，所以不会改变最大值的位置；log(ab)=log(a)+log(b) 把乘积变成和。导数描述参数微小增加时函数怎样变化，例如 log p 的导数是 1/p。寻找内部最优点时令导数为零，但还要检查边界和它是否真是最大值。

若 n>0 次独立同分布的伯努利观测中有 k 次成功，这串观测的似然为 $p^k(1-p)^{n-k}$。取对数得到 $k\log p+(n-k)\log(1-p)$。对 p 求导并令零，得到 $k/p-(n-k)/(1-p)=0$，解为 p=k/n；k=0 或 n 时最优位于边界。若只记录成功总数，还会多一个与 p 无关的组合系数，不改变这个估计。

高斯模型中，对数似然含平方偏差和；均值 MLE 是平均数，方差 MLE 用 n 作分母。统计学常见的 n-1 是估计总体方差时的无偏修正，二者目标不同。分类时比较 log prior+log likelihood，避免小概率连乘下溢。
RECAP_EN: Maximum likelihood chooses parameters that best explain fixed observations under a specified model. Taking logs preserves the maximizer and turns products into sums.
WORKED_Q: 四次独立的同分布硬币观测为正、正、反、正，正面概率为 p。写出似然，求使它最大的 p。 || Four independent identically distributed coin outcomes are heads, heads, tails, heads with heads probability p. Write the likelihood and maximize it.
WORKED_A: 顺序观测的似然 L=p³(1−p)。在 0<p<1 内，log L=3 log p+log(1−p)，导数 3/p−1/(1−p)。令零：3(1−p)=p，得 p=3/4。二阶导数 −3/p²−1/(1−p)²<0；两端似然为零，所以这是最大值。 || The ordered-sequence likelihood is p³(1−p). Inside (0,1), its log derivative is 3/p−1/(1−p). Setting it to zero gives 3(1−p)=p, hence p=3/4. The second derivative is negative, and endpoint likelihoods are zero, so this is the maximum.
PRACTICE_Q: 五次独立同分布伯努利观测中有两次成功。补出 log L 的两个系数，再用导数求 p。 || Five IID Bernoulli observations include two successes. Complete the two coefficients in log L and solve for p using its derivative.
HINT: 成功给 log p，失败给 log(1−p)。把分母乘过去再解一元方程。 || Successes contribute log p and failures log(1−p). Clear denominators in the derivative equation.
PRACTICE_A: log L=2 log p+3 log(1−p)；2/p−3/(1−p)=0，得 2−2p=3p，所以 p=2/5=0.4。 || log L=2 log p+3 log(1−p). Its derivative equation gives 2(1−p)=3p, hence p=2/5=0.4.
TRANSFER_Q: 四次观测全部成功。写出似然并求 MLE；为什么这里不能机械要求导数等于零？ || All four observations are successes. Find the likelihood and MLE, explaining why a zero derivative is not required here.
TRANSFER_A: L=p⁴，在 0≤p≤1 上随 p 增大，最大值在边界 p=1。log L=4 log p 在内部的导数 4/p 不为零；内部驻点条件不包括边界最优。估计 p=1 不证明未来永不失败。 || L=p⁴ increases on [0,1], so the maximum is at the boundary p=1. The interior log derivative 4/p never vanishes; an interior stationary-point condition does not cover boundary optima. The estimate does not prove future failures impossible.
BRIDGE: 多特征数据还需要说明特征之间如何一起变化，这决定使用对角还是完整协方差。

@@ ml07 | 协方差：椭圆的方向也是信息 | Gaussian models and covariance
CARDS: M061,M062,M063,M064,M065,M066,M067,M068,M069,M070,M071,M072,M073,M074
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
TRANSFER_Q: K=3 类、d=2 特征，只统计协方差参数：每类完整、每类对角、三类共享一个完整协方差，各需要几个独立数？共享会带来什么限制？ || For three classes and two features, count covariance parameters for separate full, separate diagonal, and one shared full covariance. What does sharing restrict?
TRANSFER_A: 单个完整对称矩阵有 2×3/2=3 个数，因此分别为 9、6、3。共享要求三类采用相同协方差形状和尺度；均值仍可不同。正定共享协方差使类别对数分数的相同二次项抵消。 || One full symmetric matrix has three independent entries, giving totals 9, 6, and 3. Sharing constrains class covariance shapes and scales to be equal while means may differ. A shared positive-definite covariance makes common quadratic score terms cancel.
BRIDGE: 对文本词频而言，高斯未必是合适的观测模型；先决定“出现”还是“出现次数”。

@@ ml08 | 同一条短信，为什么有不同的 NB 模型 | Text representation and naive Bayes
CARDS: M075,M076,M077,M078,M079,M080,M081,M082,M083,M084,M085,M086,M087,M088,M089,M331,M332,M333
PREREQ: ml02,ml06
GOAL: 能从数据表示选择 Bernoulli 或 Multinomial NB，并算出平滑概率。
EXPLAIN: 固定词表为 free、meeting、win。短信 free free win 的词频向量是 (2,0,1)，出现标记则是 (1,0,1)。这两种表示问的问题不同：Bernoulli NB 关注每个词是否出现，Multinomial NB 关注文档中各词元分配了多少次。

“朴素”把给定类别后的证据作简化分解，不是说词在现实中从不相关。Bernoulli NB 假设各词是否出现条件独立，还计入未出现词的贡献；Multinomial NB 将词元按同一类的词概率分配，类分数是次数乘 log 词概率再求和。给定总词数时，各词的计数本身并不彼此独立。平滑给未见事件留一点质量：伯努利分母加 2alpha，多项式分母加 alpha 乘词表大小。

词表和 IDF 都应只在训练部分拟合。TF-IDF 降低普遍常见词的影响，但它是加权特征，不是严格的整数多项式计数；有效的经验组合与严格生成假设应区分。稀疏矩阵只存非零词项，让大词表计算更省空间。
RECAP_EN: Choose the observation model after choosing the representation. Bernoulli NB models presence and absence; Multinomial NB models token counts. Fit text transformations on training data only.
WORKED_Q: 某类三词总计数 (3,1,0)，alpha=1，多项式平滑概率是多少？ || A class has token counts (3,1,0). With alpha=1, what are the smoothed multinomial probabilities?
WORKED_A: 原总词元数 4，加入 3 个伪计数后分母为 7；分子为 (4,2,1)，概率为 (4/7,2/7,1/7)，和为 1。 || The denominator is 4+3=7 and the numerators are (4,2,1), giving probabilities (4/7,2/7,1/7), which sum to one.
PRACTICE_Q: 某类三词总计数 (0,2,2)，采用 Multinomial NB、每词 alpha=1。补出分母与三个平滑概率。 || For class token counts (0,2,2), use multinomial NB with alpha=1 per word. Compute the denominator and smoothed probabilities.
HINT: 总词元数加 alpha×词表大小；每个分子都加 alpha。 || Add alpha times vocabulary size to the total, and alpha to each word count.
PRACTICE_A: 分母 4+3=7，概率 (1/7,3/7,3/7)，和为 1。这里按词元计数，不是按出现过该词的文档数。 || The denominator is 7 and probabilities are (1/7,3/7,3/7), summing to one. These are token counts, not document-presence counts.
TRANSFER_Q: 某类词表只有 free、meeting，词元计数为 (3,1)，alpha=1。一条新文档含两个 free、零个 meeting。求平滑词概率和忽略类别共同系数后的文档似然；为什么不能把 Bernoulli 的缺词项直接加进来？ || A class has counts (3,1) for free and meeting with alpha=1. A new document contains two free tokens and no meeting tokens. Find smoothed probabilities and document likelihood up to class-common factors. Why not add a Bernoulli absence term?
TRANSFER_A: 概率为 (4/6,2/6)=(2/3,1/3)；似然为 (2/3)²(1/3)⁰=4/9。Multinomial 记录次数；零次的次数项为 1。Bernoulli 是另一个“有/无”表示与模型，不能混搭。 || Probabilities are (2/3,1/3) and the likelihood is (2/3)²(1/3)⁰=4/9. A zero count contributes one here. Bernoulli uses a different presence/absence representation and model; its absence factor cannot be mixed into this likelihood.
BRIDGE: 当每个词的出现次数被视为独立计数，Poisson NB 提供第三种建模思路。

@@ ml09 | Poisson NB：把次数变成证据 | Count evidence with Poisson NB
CARDS: M108,M109,M110,M111,M112,M113,M114,M115,M116,M117,M118
PREREQ: ml08
GOAL: 能从 Poisson 概率写出类分数，并解释文档长度与独立性假设。
EXPLAIN: Poisson 分布以 lambda 表示计数的均值。对某类别的某个词，先统计每篇文档中出现几次，再求平均作为 MLE。它和多项式的差别是：多项式在给定总次数下分配词元，独立 Poisson 则对每个计数单独建模，也隐含了文档长度的结构。

单词概率为 $e^{-\lambda}\lambda^x/x!$。多个词取对数相加，类分数为 $\log\pi_c+\sum_j[x_j\log\lambda_{cj}-\lambda_{cj}-\log(x_j!)]$。对于同一文档，各类的阶乘项相同，比较类别时可以去掉；负 lambda 项依赖类别，不能漏。

若训练中某词总计数为零，直接估出的率也是零，新的正计数会被判为不可能。平滑的直觉是补一点伪事件和观察量；怎样补必须先定义模型，不能照搬伯努利分母。实现时还要检查类别标签顺序、特征形状和训练/测试隔离。模板参数与文件规模等具体提醒已放在课程信息栏。
RECAP_EN: Poisson NB scores independent counts using log priors, count-weighted log rates, and negative rates. Drop only terms that are identical across classes for the same observation.
WORKED_Q: 等先验，A 的均值 (2,1)，B 为 (1,2)，x=(2,0)，哪个分数大？ || With equal priors, rates (2,1) for A and (1,2) for B, which class scores higher for x=(2,0)?
WORKED_A: 忽略共同项，A 为 2log2-3，B 为 -3；差为 2log2>0，选 A。两个类别的总均值恰好相同，这一次负 lambda 和才抵消。 || A scores 2log2-3 and B scores -3, so A wins by 2log2. The negative-rate sums cancel here only because their totals match.
PRACTICE_Q: 等先验独立 Poisson 模型：A 的率为 (2,1)，B 为 (1,2)，新文档计数 x=(0,2)。使用 sum[xj log(lambda_j)−lambda_j] 比较分数。 || For equal-prior independent Poisson models with rates A=(2,1), B=(1,2), score x=(0,2) using sum[xj log(lambda_j)−lambda_j].
HINT: 分别代入两个词的次数；log 1=0。 || Substitute both counts; log 1 is zero.
PRACTICE_A: A 为 −2+(2 log1−1)=−3；B 为 −1+(2 log2−2)=2 log2−3；B 更大 2 log2，所以选 B。 || A scores −3 and B scores 2 log2−3, so B wins by 2 log2.
TRANSFER_Q: 两类单词均值为 1 和 10，空计数 x=0、更支持哪类？ || With one feature, equal priors, and rates 1 and 10, which class does x=0 support?
TRANSFER_A: 分数为 -1 和 -10，支持均值 1 的类别。若错删负 lambda 项，就会把这两类误判为平局。 || The scores are -1 and -10, favoring rate 1. Dropping the negative-rate term incorrectly creates a tie.
BRIDGE: 前面先建模“数据怎样生成”；下一节直接建模“给定数据属于哪类”。

@@ ml10 | 逻辑回归：分数、概率、损失怎样连起来 | Logistic regression from score to update
CARDS: M119,M120,M121,M122,M123,M124,M125,M126,M127,M128,M129,M130,M131,M132
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
PRACTICE_Q: x=2、w=0、固定 b=0、标签 t=0、学习率 eta=0.1，无正则。做一次单样本梯度更新后 w 是多少？ || With x=2, w=0, fixed b=0, target t=0, learning rate 0.1, and no regularization, find w after one single-sample gradient update.
HINT: 只改变 p-t 的符号。 || Check the sign of p-t.
PRACTICE_A: 梯度为 1，新 w=-0.1，正类概率下降到约 0.4502。 || The gradient is 1, so w=-0.1 and the positive-class probability falls to about 0.4502.
TRANSFER_Q: x=2、t=1、初始 w=b=0、eta=0.1，无正则，同时训练权重与偏置。分别求两个梯度、新参数与新分数。 || With x=2, t=1, initial w=b=0, eta=0.1, and no regularization, train both weight and bias. Find both gradients, new parameters, and new score.
TRANSFER_A: b 的梯度为 p-t=-0.5，新 b=0.05。两者应在同一组旧参数上计算；此时新 z=0.25，不是固定偏置版本的 0.2。 || The bias gradient is -0.5 and b becomes 0.05. Both gradients use the old parameters; the new score is 0.25.
BRIDGE: 梯度能拟合一个模型；选择模型和推广到多类别，还需要交叉验证与 softmax。

@@ ml11 | 模型选择与多类别概率 | Cross-validation and multiclass probabilities
CARDS: M133,M134,M135,M136,M137,M138,M139,M140,M141
PREREQ: ml10
GOAL: 能按相同折比较超参数并检查预处理泄漏；多类别 softmax 用独立补充单元练习。
EXPLAIN: 比较两个 C 时，应在相同数据划分上公平比较。每一折中，词表、缩放和模型参数都只能用该折训练部分拟合；验证部分负责评分。选定设置后可以用全部开发数据重新拟合，最后只评一次保留测试集。C 与惩罚强度的具体换算依赖库的目标系数约定。

多类别可以训练 K 个 one-vs-rest 二分类器，每个回答“是不是这一类”；也可以让一个模型给所有类别打分，再用 softmax 一起归一化。后者是 $p_k=e^{z_k}/\sum_j e^{z_j}$，每行概率和为 1。数值实现先减去最大分数，避免 exp 溢出，这不改变概率比。

交叉熵只取真实类别概率的负对数，因此前节的“提高真实标签概率”依然成立。权重符号的含义还受特征尺度、类别编码和其他特征固定条件影响，不能把正权重直接解释成因果作用。
RECAP_EN: Cross-validation selects settings; it does not define the multiclass model. Softmax normalizes class scores jointly and is invariant to adding the same constant to every score.
WORKED_Q: 设置 A 的三折验证准确率为 (0.82,0.86,0.84)，B 为 (0.90,0.74,0.79)。各折样本数相同，按算术平均选方案。选谁，并说明每折词表在哪里拟合。 || Settings A and B obtain equal-sized-fold validation accuracies (0.82,0.86,0.84) and (0.90,0.74,0.79). Select by arithmetic mean and state where each fold’s vocabulary is fitted.
WORKED_A: A 总和 2.52，均分 0.84；B 总和 2.43，均分 0.81，选择 A。每折词表和模型都仅在该折训练部分拟合，验证部分只评分。选完后在开发数据重新拟合，再做保留测试。 || A averages 2.52/3=0.84; B averages 2.43/3=0.81, so choose A. Fit vocabulary and model within each training fold and only score its validation fold. Refit on development data after selection, then evaluate the untouched test set.
PRACTICE_Q: 同样规则下，A=(0.8,0.8,0.8)，B=(0.9,0.7,0.7)。先求和，再选均分较大的设置。 || Under the same rule, A=(0.8,0.8,0.8) and B=(0.9,0.7,0.7). Sum the scores and select the larger mean.
HINT: 最高的一折不能替代平均；每组三个分数都要计入。 || Use all three scores rather than the highest single fold.
PRACTICE_A: A=2.4/3=0.8；B=2.3/3≈0.7667，选择 A。这个选择规则不证明它在所有未来数据上都更好。 || A averages 0.8 and B about 0.7667, so choose A; this does not guarantee better performance on every future dataset.
TRANSFER_Q: A 的平均分 0.84 来自在每折内拟合缩放；B 的 0.85 来自先用全部开发数据拟合缩放、再三折验证。可以直接选 B 吗？写出公平重比的流程。 || A scores 0.84 with scaling fitted inside each fold; B scores 0.85 after scaling all development data before cross-validation. May B be selected directly? Give a fair comparison procedure.
TRANSFER_A: 不能，B 的验证折已影响缩放统计。固定相同折；对每个候选、每折只用训练部分拟合缩放和模型，再变换并评分验证部分；重新比较均分。测试集不参与这次修正和选择。 || No. B’s validation folds influenced scaling. Fix identical folds; fit scaling and model only on each training portion, transform and score its validation portion, then compare the recomputed means. Keep the test set out of this correction and selection.
BRIDGE: 逻辑回归惩罚概率判断，SVM 则把“离边界多远”放到学习目标里。

@@ ml12 | SVM：先看距离，再看优化式 | Margins and soft-margin SVM
CARDS: M143,M144,M145,M146,M154,M155,M156,M159,M160,M161,M162,M163,M164
PREREQ: ml04,ml10
GOAL: 能用几何距离解释间隔，并判断松弛变量的含义。
EXPLAIN: 设标签 y 为 -1 或 +1，决策边界是 $w^Tx+b=0$，w 非零。把 w 和 b 同乘正数不会移动边界，所以分数大小不是距离；点到边界的距离为 $|w^Tx+b|/\|w\|$。硬间隔要求两类可被线性完全分开，并规范分数使 $y_i(w^Tx_i+b)\ge1$。再最小化 $\frac12\|w\|^2$，相当于把两类之间最窄的“走廊”拓宽，单侧间隔是 $1/\|w\|$。

若数据有重叠，软间隔改为最小化 $\frac12\|w\|^2+C\sum_i\xi_i$，约束是 $y_i f(x_i)\ge1-\xi_i$ 和 $\xi_i\ge0$，这里 C>0。固定模型后，最小松弛为 $\max(0,1-yf)$，即 hinge loss。此时 0<xi<1 表示分类正确但进入走廊；xi=1 在决策边界上；xi>1 才表示误分类。

C 大表示在给定系数约定下更重视违约代价，不是学习率。SVM 分数也不是概率；若需要概率应另有校准过程。
RECAP_EN: SVM controls geometric margin after fixing score scale. Soft-margin slack allows margin violations, and minimizing slack yields hinge loss. Decision scores are not probabilities.
WORKED_Q: 一维样本 (-1,-1)、(1,+1)，求硬间隔解。 || Find the hard-margin solution for one-dimensional samples (-1,-1) and (1,+1).
WORKED_A: 约束为 w-b≥1、w+b≥1，相加得 w≥1。取最小范数 w=1 时 b=0，单侧间隔 1，两条间隔边界之间宽度 2。 || Constraints are w-b≥1 and w+b≥1, implying w≥1. The minimum norm solution is w=1, b=0; the one-sided margin is 1 and total width is 2.
PRACTICE_Q: 一维负样本 x=−2、y=−1，正样本 x=2、y=+1。硬间隔约束为 y(wx+b)≥1。求最小范数的 w、b 和单侧几何间隔。 || For points (x,y)=(−2,−1),(2,+1), use hard-margin constraints y(wx+b)≥1. Find minimum-norm w,b and the one-sided margin.
HINT: 写出 2w−b≥1 与 2w+b≥1，相加；最后算 1/|w|。 || Add 2w−b≥1 and 2w+b≥1, then compute 1/|w|.
PRACTICE_A: 相加得 w≥1/2，最小范数取 w=1/2，两个约束要求 b=0；单侧间隔 1/|w|=2，全宽为 4。 || The constraints imply w≥1/2. Minimum norm gives w=1/2,b=0; the one-sided margin is 2 and full width is 4.
TRANSFER_Q: 分界面 w=2、b=0，点 x=3 到边界的距离是多少？把 w、b 同乘 10 后重算，并解释分数和距离的区别。 || For boundary w=2,b=0, find the distance of x=3. Recompute after multiplying w,b by 10, and distinguish score from distance.
TRANSFER_A: 原距离 |2×3|/|2|=3；缩放后 |20×3|/|20|=3。原分数 6 变为 60，但边界和距离不变。硬间隔的 1/||w|| 还要求采用 y f≥1 的规范化表示。 || The distances are |6|/2=3 and |60|/20=3. Scores change, but the boundary and distance do not. The hard-margin expression 1/||w|| additionally uses the canonical y f≥1 scaling.
BRIDGE: 原始问题看 w 与 b；对偶从样本贡献出发，解释哪些点真正支撑边界。

@@ ml13 | 对偶与 KKT：给约束配上价格 | Duality, multipliers, and support vectors
CARDS: M147,M148,M149,M150,M151,M152,M153,M157,M158
PREREQ: ml12
GOAL: 能逐项求拉格朗日函数的导数、求两点硬间隔乘子，并正确使用互补松弛。
EXPLAIN: 把硬间隔约束写成 $g_i=1-y_i(w^Tx_i+b)\le0$。最小化问题的拉格朗日函数为 $L=\frac12\|w\|^2+\sum_i\alpha_i g_i$，其中 alpha_i≥0。对任一可行 w,b，乘子项非正，所以先对 w,b 求下确界得到原问题最优值的下界；再最大化这个下界就是对偶。

符号约定先对齐：这里写 g≤0、L=f+αg；若基础补课写 h=−g≥0，则 L=f−αh 完全相同，乘子仍非负。只可把不等式与拉格朗日项的符号一起转换。

对 w 求导得 $w=\sum_i\alpha_i y_i x_i$，对 b 求导得 $\sum_i\alpha_i y_i=0$。代回后，对偶目标是最大化 $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_j y_i y_j x_i^Tx_j$，同时满足这些约束。乘子像约束的“价格”；不挤压最优解的约束不必付价。互补松弛 $\alpha_i g_i=0$ 表示：g_i<0 时 alpha_i=0；反向却不一定成立。

软间隔加上线性松弛惩罚后得到 0≤alpha_i≤C。0<alpha_i<C 的点落在间隔边界，可用于求 b；alpha_i=C 也可能仍正确分类。硬间隔在线性可分时可放大分离超平面，使约束严格满足；结合凸性可用强对偶说明最优值相等。这是本问题的条件，不能推广为任意优化问题都成立。

边界补充（C>0）：若没有 0<αᵢ<C 的自由支持向量，不能随便选点套 b=yᵢ−wᵀxᵢ。由 KKT 求可行区间：αᵢ=0 时，正类给 b≥1−wᵀxᵢ、负类给 b≤−1−wᵀxᵢ；αᵢ=C 时方向反过来。取满足所有上下界的 b；若数值解出现冲突，应检查容差和优化结果。比如 w=0.5，(x,y)=(1,1)、(−1,−1)，两点乘子均为 C=0.25，则 −0.5≤b≤0.5，b=0 可用。
RECAP_EN: The dual maximizes a lower bound on the primal objective. Stationarity expresses w as a weighted sample sum; complementary slackness is an implication, not a reversible test for every constraint.

For C>0 with no free support vector, derive bounds from KKT instead of treating any point as a margin point. At α=0, positive labels give b≥1−wᵀx and negative labels b≤−1−wᵀx; at α=C the bounds reverse. With w=0.5, points (1,1),(−1,−1), and both multipliers C=0.25, the feasible interval is −0.5≤b≤0.5.

WORKED_Q: 一维样本 (x₁,y₁)=(−1,−1)、(x₂,y₂)=(1,+1)。写 L=½w²+α₁(1−w+b)+α₂(1−w−b)。先对 w、b 求导，再由最优 w=1、b=0 求乘子。 || For (x₁,y₁)=(−1,−1),(x₂,y₂)=(1,+1), use L=½w²+α₁(1−w+b)+α₂(1−w−b). Differentiate in w,b and find multipliers at the optimum w=1,b=0.
WORKED_A: 对 w：½w² 给 w，两个约束项分别给 −α₁、−α₂，所以 ∂L/∂w=w−α₁−α₂=0。对 b：∂L/∂b=α₁−α₂=0。故 α₁=α₂=a，1=2a，得到各 1/2。两约束均为零，互补松弛成立；原始与对偶目标都为 1/2。 || The w derivative is w−α₁−α₂=0; the b derivative is α₁−α₂=0. Thus both multipliers equal a and 1=2a, giving a=1/2. Both constraints are active, so complementary slackness holds; primal and dual objectives equal 1/2.
PRACTICE_Q: 将样本改成 (−2,−1)、(2,+1)，其最优 w=1/2、b=0。L=½w²+α₁(1−2w+b)+α₂(1−2w−b)。补出两个驻点方程并求乘子。 || For points (−2,−1),(2,+1), the optimum is w=1/2,b=0. Using L=½w²+α₁(1−2w+b)+α₂(1−2w−b), derive both stationarity equations and multipliers.
HINT: w 的两个约束导数现在各带系数 −2；b 条件仍使两个乘子相等。 || Each constraint now contributes −2 to its w derivative; the b condition still equates the multipliers.
PRACTICE_A: ∂L/∂w=w−2α₁−2α₂=0，∂L/∂b=α₁−α₂=0。令二者为 a，1/2=4a，因此 α₁=α₂=1/8。 || Stationarity gives w−2α₁−2α₂=0 and α₁−α₂=0. With both equal to a, 1/2=4a, so each is 1/8.
TRANSFER_Q: 从一般 L=½||w||²+Σᵢαᵢ[1−yᵢ(wᵀxᵢ+b)] 独立写出 ∂L/∂w 和 ∂L/∂b，推出 w 的展开。再判断：gᵢ<0 能推出 αᵢ=0 吗？αᵢ=0 能推出 gᵢ<0 吗？ || For general L=½||w||²+Σᵢαᵢ[1−yᵢ(wᵀxᵢ+b)], derive both derivatives and the expansion of w. Under complementary slackness, does gᵢ<0 imply αᵢ=0, and does αᵢ=0 imply gᵢ<0?
TRANSFER_A: ∂L/∂w=w−Σᵢαᵢyᵢxᵢ=0，故 w=Σᵢαᵢyᵢxᵢ；∂L/∂b=−Σᵢαᵢyᵢ=0。因 αᵢgᵢ=0，gᵢ<0 必使 αᵢ=0；逆向不成立，因为 αᵢ=0、gᵢ=0 也满足条件。 || The derivatives are w−Σᵢαᵢyᵢxᵢ=0 and −Σᵢαᵢyᵢ=0. Hence w is the weighted sample sum. Complementary slackness forces αᵢ=0 when gᵢ<0, but αᵢ=0 permits either an inactive or an active constraint.
BRIDGE: 对偶只通过样本内积计算，这为核方法提供了入口。

@@ ml14 | 核：换一种比较样本的方式 | Kernels as implicit feature comparisons
CARDS: M165,M166,M167,M168,M169,M170,M171,M172
PREREQ: ml03,ml13
GOAL: 能通过显式特征映射验证二次核；RBF 与超参数区别见补充单元。
EXPLAIN: 在原空间画不直的边界，变成更丰富的特征后可能是线性的。例如加入平方与交叉项，可以表达弯曲关系。如果算法只需要新特征的内积，就不一定要真正存出这些特征：用 k(x,z)=phi(x)^T phi(z) 直接计算即可。

对二维齐次二次核，$(x^Tz)^2=x_1^2z_1^2+2x_1x_2z_1z_2+x_2^2z_2^2$，所以 phi(x)=(x1²,√2 x1x2,x2²)。中间的 √2 保证内积系数正确。RBF 核根据平方距离给相似度，gamma 大时相似度随距离下降更快，边界可以更局部。

不是所有“相似度”都能当实值标准核：函数应对称，任意有限样本的 Gram 矩阵 K 都须半正定，即任意系数 a 满足 $a^TKa\ge0$。只在一批数据上通过检查还不是对所有输入的证明。核方法还可能需要 N×N 的矩阵，避免显式高维特征不等于免除大样本成本。
RECAP_EN: A kernel computes an inner product in a feature space without explicitly constructing every feature. Validity requires positive semidefinite Gram matrices, and computational costs still depend on sample count.
WORKED_Q: x=(1,2)、z=(3,4)，二次核是多少？ || Compute the homogeneous quadratic kernel for x=(1,2) and z=(3,4).
WORKED_A: 原内积 11，平方为 121。映射后内积为 1×9+(2√2)(12√2)+4×16=9+48+64=121。 || The original dot product is 11, so the kernel is 121. The feature-space dot product is 9+48+64=121 as well.
PRACTICE_Q: 对二次核 k(x,z)=(xᵀz)²，取 x=(1,1)、z=(2,0)。分别直接计算，以及用 φ(a,b)=(a²,√2ab,b²) 计算。 || For k(x,z)=(xᵀz)², use x=(1,1),z=(2,0). Compute it directly and through φ(a,b)=(a²,√2ab,b²).
HINT: 先求原空间内积，再求映射后的两个三维向量。 || Compute the original dot product and then the two three-dimensional mapped vectors.
PRACTICE_A: 原内积为 2，平方为 4。映射为 (1,√2,1)、(4,0,0)，其内积也是 4。 || The original dot product is 2, giving 4. Mapped vectors (1,√2,1) and (4,0,0) also have dot product 4.
TRANSFER_Q: 将映射错误地写成 ψ(a,b)=(a²,ab,b²)。对 x=z=(1,1)，比较 ψ(x)ᵀψ(z) 与 (xᵀz)²，并指出少了什么。 || Suppose ψ(a,b)=(a²,ab,b²) is used instead. For x=z=(1,1), compare its dot product with (xᵀz)² and identify the missing factor.
TRANSFER_A: 错误映射得 1+1+1=3，目标核为 (1+1)²=4。展开 (ac+bd)² 有 2abcd 交叉项，因此两个向量的中间坐标各需要 √2，乘起来才是系数 2。 || The incorrect map gives 3 versus the target kernel value 4. The expansion has cross-term 2abcd, so each mapped middle coordinate needs √2 to produce the factor 2.
BRIDGE: 模型看到的几何结构来自特征表示，因此缩放和编码也是模型的一部分。

@@ ml15 | 特征与评估：别让表示偷偷改变问题 | Features, scale, and fair comparison
CARDS: M173,M174,M175,M176,M177,M178,M179,M180,M181,M182
PREREQ: ml11,ml14
GOAL: 能用训练统计完成特征缩放，解释尺度含义，并识别预处理泄漏。
EXPLAIN: 假设两个特征是身高和收入，数值单位不同。依赖欧氏距离或 L2 权重惩罚的模型会受单位影响；标准化用训练均值和标准差构造可比尺度。但标准化不是删除信息，也不意味着每个特征都一定应被等权对待。

类别编码同样在表达假设。给红、绿、蓝编码 0、1、2，线性模型会看到大小与等距关系；one-hot 可避免这种无序类别的伪几何。多项式项增加交互，分箱牺牲连续细节，对数变换则需要合法定义域。每个变换都应先问：它保留了什么、丢掉了什么？

类别权重改变训练错误的相对代价。样本少与漏判代价高不是同一概念，决策阈值也会影响最终结果。比较不同模型时固定划分、指标和调参预算，才能分清表示改进与分类器改进。
RECAP_EN: Representation shapes geometry and regularization. Fit transformations within training folds, distinguish class imbalance from decision costs, and compare models under a shared evaluation protocol.
WORKED_Q: 训练最小值 2、最大值 6，映射到 [-1,1] 后，4 与新值 8 分别是多少？ || With training minimum 2 and maximum 6, map 4 and a new value 8 to [-1,1].
WORKED_A: z=2(x-2)/(6-2)-1。4 变成 0；8 变成 2。新数据可以落在训练目标区间外，除非另行截断。 || Using z=2(x-2)/4-1, 4 maps to 0 and 8 maps to 2. New observations can lie outside the training range unless clipping is explicitly applied.
PRACTICE_Q: 仅用训练数据得到 min=10、max=20，映射到 [−1,1]。补出公式，并求训练值 15 与新值 25 的结果。 || Training min and max are 10 and 20. Map to [−1,1], then transform training value 15 and new value 25.
HINT: 用 z=2(x−min)/(max−min)−1；新数据继续用训练的 min、max。 || Use z=2(x−min)/(max−min)−1, retaining training min and max for new data.
PRACTICE_A: z=2(x−10)/10−1。15→0，25→2。新值越界不代表公式错，也不能为让它回到区间而重新拟合测试范围。 || The rule is z=2(x−10)/10−1. It maps 15 to 0 and 25 to 2. Going out of range is possible; do not refit the scaler on test data merely to force it back inside.
TRANSFER_Q: 训练特征为 (2,4,6)，新测试值 8。正确按训练范围映射到 [−1,1] 后 4、8 各是什么？若误用全体 (2,4,6,8) 的范围，两个结果怎样变，为什么评估有问题？ || Training values are (2,4,6) and the new test value is 8. Map 4 and 8 to [−1,1] using training statistics; compare with fitting the range on all four values. Why is the latter invalid evaluation?
TRANSFER_A: 训练范围 [2,6] 给 4→0、8→2。加入测试后范围变 [2,8]，给 4→−1/3、8→1。测试数据已改变训练样本的表示和随后的模型；应固定训练变换。 || Training range [2,6] gives 0 and 2. Including the test value changes the range to [2,8], giving −1/3 and 1. Test data has changed the training representation and thus the model; keep the training-fitted transform fixed.
BRIDGE: 将这一流程落实到短信作业，比先尝试很多复杂模型更容易定位问题。

@@ ml16 | 从基线到可解释的短信实验 | A reproducible assignment workflow
CARDS: M091,M092,M093,M094,M095,M096,M099
PREREQ: ml08,ml11
GOAL: 能从混淆矩阵计算 precision、recall、balanced accuracy，并用错误类型选择下一步检查。
EXPLAIN: 作业先拆为数据、特征、训练、选择、评价、交付六步。先让简单词袋加 NB 的基线端到端运行，再改变一个因素。记录训练样本数、标签映射、随机种子、词表拟合位置和评价函数，才能确定两个成绩来自可比较的实验。

混淆矩阵把“错了”细分为哪一类被判成哪一类。Recall 看该真实类别中找回多少；precision 看预测为该类的结果中多少正确。Balanced accuracy 对各类 recall 做算术平均，使多数类不能仅靠数量掩盖少数类失败。

错误分析应回到具体短信：是否分词错误、否定词缺失、稀有词未覆盖、内容本就模糊？提出可检验改动，而不是只抄一个更高分。提交要求和评分细节见网页“课程信息”中的 Assignment 1 说明，并以最新 Canvas 原 Notebook 为准；这里的小例子不是代做实验或报告实际成绩。
RECAP_EN: Build a complete baseline before optimizing components. Use per-class errors to formulate testable improvements and preserve the distinction between validation choices and final evaluation.
WORKED_Q: 二分类垃圾邮件任务：TP=6、FN=4、FP=2、TN=8，垃圾为正类。计算精确率、召回率和两类 balanced accuracy。 || For spam-positive binary classification with TP=6,FN=4,FP=2,TN=8, compute precision, recall, and two-class balanced accuracy.
WORKED_A: 拦下 8 条中 6 条真垃圾，precision=6/(6+2)=0.75；10 条真垃圾找回 6 条，recall=6/(6+4)=0.6。正常类召回率=8/(8+2)=0.8；balanced accuracy=(0.6+0.8)/2=0.7。 || Precision is 6/8=0.75; spam recall is 6/10=0.6. Legitimate recall is 8/10=0.8, so balanced accuracy is (0.6+0.8)/2=0.7.
PRACTICE_Q: TP=8、FN=2、FP=4、TN=6。先写 precision 和 recall 的分母，再算 balanced accuracy。 || For TP=8,FN=2,FP=4,TN=6, identify precision and recall denominators, then compute balanced accuracy.
HINT: precision 在“被预测为垃圾”中数；recall 在“真的垃圾”中数；再求正常类召回率。 || Precision conditions on predicted spam; recall on actual spam. Also compute legitimate-class recall.
PRACTICE_A: precision=8/12=2/3；recall=8/10=0.8；正常类召回率=6/10=0.6；balanced accuracy=0.7。 || Precision is 2/3, spam recall 0.8, legitimate recall 0.6, and balanced accuracy 0.7.
TRANSFER_Q: 数据有 10 条垃圾、90 条正常。模型一律预测正常。独立写出 TP/FN/FP/TN，并算 accuracy 与 balanced accuracy；下一步优先看哪类错误？ || A dataset has 10 spam and 90 legitimate messages. An always-legitimate model predicts all normal. Derive TP/FN/FP/TN, accuracy and balanced accuracy, then identify the errors to investigate.
TRANSFER_A: TP=0、FN=10、FP=0、TN=90。accuracy=90/100=0.9；两类召回率为 0 与 1，balanced accuracy=0.5。先检查漏掉的垃圾、类别不平衡和阈值；90% 总准确率不能说明过滤器有效。 || TP=0,FN=10,FP=0,TN=90. Accuracy is 0.9 but balanced accuracy is (0+1)/2=0.5. Inspect missed spam, imbalance, and the decision threshold; 90% overall accuracy does not establish useful filtering.
BRIDGE: QE 需要从实验与公式上升到“为什么、何时成立、何时失败”的解释。

@@ ml17 | QE 口述：把模型讲成可追问的论证 | Explaining assumptions and decisions
CARDS: M101,M102,M103,M104,M105,M106
PREREQ: ml07,ml08,ml10,ml16
GOAL: 能用四句英文连接任务、模型假设、决策规则和局限，并迁移到另一模型。
EXPLAIN: 一个完整解释可以按五句话展开：解决什么任务；用什么表示；模型假设什么；怎样训练和预测；什么情况下会失败。公式应嵌在这条论证中，而不是突然背出来。比如朴素贝叶斯的 fast 来自可分解的统计量，局限也正来自条件独立等建模假设。

预测概率和决策要分开。设 p 是垃圾短信后验，误封正常短信的代价为 C_FP，漏掉垃圾的代价为 C_FN；两者非负、和为正，正确判断代价均为零。预测垃圾的风险为 $C_{FP}(1-p)$，预测正常为 $C_{FN}p$。比较得阈值 $p>C_{FP}/(C_{FP}+C_{FN})$。换代价是在换决策规则，不是在重新证明 p 已校准。

高置信度不自动表示校准良好；零协方差也不自动表示独立。遇到追问时给出假设或反例，比用“通常都这样”更可靠。这里是表达练习，未宣称学校 QE 采用某个固定问答模板。
RECAP_EN: Naive Bayes combines class priors with factorized class-conditional evidence. It is efficient, but dependence violations and poor probability calibration can affect decisions. A decision threshold should reflect the costs of errors.
WORKED_Q: 用四句英文介绍词元计数 Multinomial NB：说明输入/输出、给定类别的词元模型、如何预测以及一个局限。 || Give a four-sentence English explanation of token-count multinomial NB: input/output, class-conditional token model, prediction rule, and one limitation.
WORKED_A: 示范：“I classify messages as spam or legitimate using token counts. Given a class and document length, the model treats token positions as independent draws from a class-specific vocabulary distribution. I choose the class with the largest log prior plus count-weighted log word probabilities. Correlated language and distribution shift can make its probability estimates unreliable.” 四句依次回答任务、假设、决策、边界。 || I classify messages as spam or legitimate using token counts. Given a class and document length, the model treats token positions as independent draws from a class-specific vocabulary distribution. I choose the class with the largest log prior plus count-weighted log word probabilities. Correlated language and distribution shift can make its probability estimates unreliable.
PRACTICE_Q: 改成 Bernoulli NB，输入改为每个词是否出现。补完四句框架：I classify …; given a class …; I score each class using …; a limitation is …。 || Switch to Bernoulli NB with word-presence indicators. Complete: I classify …; given a class …; I score each class using …; a limitation is … .
HINT: 提到有/无表示、条件独立、先验与出现和缺失项、假设可能不成立。 || Mention binary representation, conditional independence, prior plus presence and absence terms, and a limitation.
PRACTICE_A: “I classify messages using word-presence indicators. Given a class, the indicators are modeled as independent Bernoulli variables. I add the log prior and the log probabilities of both present and absent words. Correlated words can violate the assumption and produce overconfident predictions.” 不要求逐字背诵，四个意思一致即可。 || I classify messages using word-presence indicators. Given a class, the indicators are modeled as independent Bernoulli variables. I add the log prior and the log probabilities of both present and absent words. Correlated words can violate the assumption and produce overconfident predictions. Equivalent wording is acceptable.
TRANSFER_Q: 独立用四句英文解释二分类逻辑回归。必须包含：线性分数、sigmoid、交叉熵训练、概率或泛化的一个限制。 || Independently explain binary logistic regression in four English sentences, including linear score, sigmoid, cross-entropy training, and one probability or generalization limitation.
TRANSFER_A: 可答：“I predict a binary label from a feature vector. A linear score is mapped through a sigmoid to a class probability. I fit the parameters by minimizing binary cross-entropy on training data. A linear decision boundary or distribution shift may limit performance, so I validate the model on held-out data.” 检查四项内容，不按句型是否相同评分。 || I predict a binary label from a feature vector. A linear score is mapped through a sigmoid to a class probability. I fit parameters by minimizing binary cross-entropy on training data. A linear decision boundary or distribution shift may limit performance, so I validate the model on held-out data. Judge these four ideas rather than exact wording.
BRIDGE: 后续 Extra Resources 可用于预习新模型；始终将它们映射回任务、假设、目标与验证这四个问题。

@@ ml18 | k-NN：先用附近的例子回答 | Nearest-neighbor reasoning
CARDS: M183,M184,M185,M186
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
TRANSFER_Q: 查询点 (0,0)，A 类邻居 (0.1,2)，B 类邻居 (1,0)；普通欧氏 1-NN 先选谁？若只把第一坐标单位改成原来的 10 倍，查询和邻居同时换单位、不标准化，又选谁？ || For query (0,0), neighbor A=(0.1,2) and B=(1,0), which class does Euclidean 1-NN choose? If the first coordinate is multiplied by 10 for all points without standardization, which is chosen?
TRANSFER_A: 原平方距离 A=0.01+4=4.01，B=1，选 B。改单位后 A=(1,2)、B=(10,0)，平方距离为 5 与 100，改选 A。只是单位变化就改变了邻居，因此尺度必须作为模型规则的一部分。 || Squared distances are 4.01 and 1, so choose B. After rescaling, they are 5 and 100, so choose A. A unit change alone alters the prediction unless scaling is handled as part of the model.
BRIDGE: k-NN 直接查例子；回归则用参数概括输入与连续输出的关系。

@@ ml19 | 最小二乘：从每个误差推到正规方程 | Least squares without skipping the derivative
CARDS: M187,M188,M189,M190,M191,M192,M193,M194,M195,M196,M197,M198,M199,M200,M201,M202
PREREQ: ml03,ml04,ml10
GOAL: 能逐项求导得到正规方程，说明何时唯一以及正则化改了什么。
EXPLAIN: 约定 X 的每行是一条样本，包含常数列时也可学习截距。令 $J(w)=\frac12\sum_i(\sum_jX_{ij}w_j-y_i)^2$。先只对第 k 个系数求导：第 i 个残差的导数为 X_ik，所以 $\partial J/\partial w_k=\sum_iX_{ik}(X_iw-y_i)$。把所有 k 的结果排列起来，恰好就是 $X^T(Xw-y)$。

令梯度为零得到 $X^TXw=X^Ty$。这表示残差与每个特征列正交，也就是投影思想。Hessian 是所有二阶偏导组成的矩阵，用来描述局部曲率；此处为 X^TX，因任意 v 都有 $v^TX^TXv=\|Xv\|^2\ge0$，目标是凸的。只有列满秩时它才正定，解才唯一；样本数够多本身不保证满秩。

加 $\frac\lambda2\|w\|^2$ 后，梯度增加 lambda w，得到 $(X^TX+\lambda I)w=X^Ty$。lambda>0 且所有系数都被惩罚时可得到唯一解；不惩罚截距时要按实际惩罚矩阵讨论。L1 则可能将部分系数压成零。数值上通常解方程或用 QR/SVD，不直接显式求逆。
SYMBOLS: X | N×d 设计矩阵；w | d 维系数；r=Xw-y | N 维残差；X^T r | d 维梯度；lambda | 非负惩罚强度，系数约定见正文
RECAP_EN: Differentiate one residual at a time to obtain X-transpose times the residual. The normal equations express orthogonality; uniqueness requires full column rank, unless an appropriate strictly convex penalty supplies it.
WORKED_Q: 拟合 (0,1)、(1,3)、(2,5) 的直线 y=b+ax，写出正规方程并解。 || Fit y=b+ax to (0,1),(1,3),(2,5) using the normal equations.
WORKED_A: X 的行为 (1,0)、(1,1)、(1,2)，残差为 b−1、b+a−3、b+2a−5。对 b 求导相加得 3b+3a−9=0；对 a 求导按 x 加权得 3b+5a−13=0。这就是 XᵀX=[[3,3],[3,5]]、Xᵀy=(9,13)。两式相减得 a=2，再得 b=1，残差全为零。 || Rows of X are (1,0),(1,1),(1,2), giving residuals b−1,b+a−3,b+2a−5. Summing residuals gives the b derivative 3b+3a−9; weighting them by x gives the a derivative 3b+5a−13. Set both to zero, subtract to obtain a=2, then b=1. All residuals are zero.
PRACTICE_Q: 无截距直线预测 y=wx，数据 (x,y)=(1,2),(2,4)。写 J=½[(w−2)²+(2w−4)²]，逐项求导并解最小二乘 w。 || Fit y=wx without an intercept to (1,2),(2,4). Differentiate J=½[(w−2)²+(2w−4)²] term by term and solve for w.
HINT: 第一项导数 w−2；第二项要再乘内部导数 2。 || The first derivative term is w−2; the second also multiplies by the inner derivative 2.
PRACTICE_A: dJ/dw=(w−2)+2(2w−4)=5w−10，令零得 w=2。二阶导数为 5>0，因此是唯一最小值；对应 XᵀX=5、Xᵀy=10。 || dJ/dw=(w−2)+2(2w−4)=5w−10, giving w=2. The second derivative is 5>0, so the minimum is unique; equivalently XᵀX=5 and Xᵀy=10.
TRANSFER_Q: X 两列完全相同，但有 1000 行，OLS 一定唯一吗？ || If X has two identical columns and 1,000 rows, must OLS have a unique solution?
TRANSFER_A: 不唯一；两列的权重可一增一减而不改变预测。列数不等于秩，更多重复样本无法恢复这个不可识别方向。 || No. Increasing one coefficient and decreasing the other equally leaves predictions unchanged. Sample count does not repair column dependence.
BRIDGE: 平方残差惩罚大错误特别重，因此下一节讨论异常点和不同损失。

@@ ml20 | 鲁棒回归：一个异常点为什么能拉走直线 | Outliers and robust fitting
CARDS: M203,M204,M205,M206,M207,M208,M209,M210
PREREQ: ml19
GOAL: 能计算 RANSAC 的成功概率和尝试次数，并区分独立近似与有限无放回抽样；损失比较见补充单元。
EXPLAIN: 残差从 1 增到 10，平方损失从 1 增到 100，梯度幅度也变大。一个远离主体的数据点可能明显拉动拟合结果。换损失是在改变错误代价；RANSAC 则先反复用小子集拟合候选模型，再寻找符合容差的内点集合。

先把“抽到全内点”与“拟合出好模型”分开。理想模型假设样本内每次取点独立、内点概率为 w，于是 s 个点全为内点的概率是 $w^s$；K 次独立尝试全失败的概率为 $(1-w^s)^K$。实际从有限数据中无放回取子集时，单次概率应为 $\binom{I}{s}/\binom{N}{s}$，I 是内点数，$w^s$ 是常用近似。全内点也可能几何退化，阈值仍须合理。

模型对输入非线性不代表对参数非线性，例如 b+a1 x+a2 x² 仍可线性求系数。核岭回归与 SVR 延续了这些区别；SVR 的 epsilon 不敏感损失是 max(0,|r|-epsilon)。
RECAP_EN: Robust fitting changes how residuals or consensus sets influence a model. RANSAC's success calculation depends on an idealized sampling model, not merely on running many iterations.
WORKED_Q: 按独立取点的理想模型，w=0.5、s=2，至少一次抽到全内点的概率要达到 0.99，需几次尝试？ || Under the independent-draw model, with w=0.5 and s=2, how many trials give at least 0.99 probability of drawing an all-inlier sample?
WORKED_A: 每次成功概率 0.25；要求 0.75^K≤0.01，K≥log(0.01)/log(0.75)≈16.008，向上取整为 17。 || Each trial succeeds with probability 0.25. Solving 0.75^K≤0.01 gives K≥16.008, hence 17 trials.
PRACTICE_Q: RANSAC 的理想独立取点模型中，内点率 w=0.8，每次取 s=2 点，要求至少一次全内点的概率≥0.95。先算单次成功率，再求最少尝试数 K。 || Under RANSAC’s independent-draw model, inlier rate is 0.8 and sample size 2. Find the minimum K for at least 0.95 probability of one all-inlier sample.
HINT: 单次失败率 1−w²；令其 K 次方≤0.05，并向上取整。 || Raise the single-trial failure probability 1−w² to K, require at most 0.05, and round upward.
PRACTICE_A: 单次成功率 0.64，失败率 0.36。0.36²=0.1296>0.05，0.36³=0.046656≤0.05，所以至少 3 次，成功率 0.953344。 || Single-trial success is 0.64. Two trials leave failure probability 0.1296; three leave 0.046656, so K=3 gives success 0.953344.
TRANSFER_Q: 只有 N=4 个点，其中 I=2 个内点，每次从中无放回取 s=2。单次全内点概率是否仍为 (I/N)²=1/4？若每次重新独立抽子集，要至少 50% 成功率需几次？ || Among four points, two are inliers. Each trial samples two distinct points without replacement. Is all-inlier probability still 1/4? If subsets are resampled independently between trials, how many trials reach 50% success?
TRANSFER_A: 单次为 C(2,2)/C(4,2)=1/6，而非 1/4。K 次失败为 (5/6)^K；K=3 约 0.5787，K=4 约 0.4823，所以最少 4 次。独立近似的使用条件会改变答案。 || Single-trial probability is C(2,2)/C(4,2)=1/6. Failure after K independent trials is (5/6)^K: about 0.5787 at K=3 and 0.4823 at K=4. Thus four trials are needed, illustrating why sampling assumptions matter.
BRIDGE: 聚类同样用距离，但没有标签告诉我们哪条预测对错。

@@ ml21 | k-means：分组与代表点为什么交替更新 | Why k-means alternates
CARDS: M211,M212,M213,M214,M215,M216
PREREQ: ml03,ml19
GOAL: 能执行k-means的一次分配与均值更新，检查目标下降，并说明不保证全局最优。
EXPLAIN: 分类有标签，聚类需要自己定义怎样算“同一组”。k-means 让每个点只属于一个组，并选择组中心，使点到自己中心的平方距离总和尽量小：$J=\sum_i\|x_i-\mu_{z_i}\|^2$。

同时选所有分组和中心很难，但固定其中一半后问题简单。中心固定时，每个点选最近中心；分组固定时，对非空组中心求导，中心就是组内平均值。因此两步都不会增大同一目标。距离平局要有固定规则；空簇没有均值，需保留旧中心或按明确规则重置，不能除以零。

以 0、2 这一组为例，中心 c 的损失是 $c^2+(2-c)^2=2(c-1)^2+2$，显然 c=1 最好。这个等式把“取均值”从口令变成可见的最小化理由。算法仍受初始化影响，可能停在局部解；增加 k 往往降低训练损失，不能据此无限增加簇数。
SYMBOLS: x_i | 第 i 个点；z_i | 它的簇编号；mu_k | 第 k 个簇的中心；J | 簇内平方距离总和，不是概率
RECAP_EN: Assignment minimizes the objective with centers fixed; taking means minimizes it with assignments fixed. This gives non-increasing loss, not a guarantee of the globally best clustering.
DEMO: kmeans
WORKED_Q: 数据 0、2、8、10，中心先取 0、10，完成一次分配和更新。 || For data 0,2,8,10 and initial centers 0,10, perform one assignment and update.
WORKED_A: 分为 {0,2} 与 {8,10}；更新中心为 1 和 9。平方距离和由 0+4+4+0=8 变为 1+1+1+1=4；再次分配不变。 || Assign {0,2} and {8,10}; update centers to 1 and 9. The objective falls from 8 to 4, and the next assignments are unchanged.
PRACTICE_Q: 数据 (0,2,4,10)，初始中心 0、10，平方欧氏距离、无平局。完成一次分配和均值更新，并比较更新前后的目标值。 || For data (0,2,4,10), centers 0 and 10, squared Euclidean distance, and no ties, perform one assignment and mean update, then compare objectives.
HINT: 先比较每点到两中心的距离，再分别求组内均值。 || Assign to the nearer center, then take each group mean.
PRACTICE_A: 分组 {0,2,4}、{10}，新中心 2、10。更新前目标 0+4+16+0=20；更新后 4+0+4+0=8。 || Groups are {0,2,4} and {10}, with updated centers 2 and 10. The objective falls from 20 to 8.
TRANSFER_Q: 每次迭代损失都下降，为什么仍要尝试多个初始化？ || Why try multiple initializations if every iteration reduces or preserves the loss?
TRANSFER_A: 不同起点可进入不同局部解；单次下降只比较同一轨迹的前后，不比较所有可能分组。 || Different starts can reach different local solutions. Monotonic descent compares successive iterates, not all possible clusterings.
BRIDGE: 点在两组边缘时，硬分配太绝对；GMM 用责任度表示软归属。

@@ ml22 | EM：先估计归属，再重估模型 | Soft clustering and EM
CARDS: M217,M218,M219,M220,M221,M222,M223,M224,M225,M226
PREREQ: ml07,ml21
GOAL: 能在固定方差的一维双高斯模型中完成一次 E 步和 M 步，更新责任度、混合权重和均值。
EXPLAIN: 想象两台机器都生产零件，但记录里没写每件来自哪台。GMM 假设先按混合权重选择成分，再从该成分的高斯分布生成观测；不知道成分标签，就不能直接按组统计。E 步计算“这一件有多大可能来自每台机器”：$r_{ik}=\pi_k\mathcal N(x_i;\mu_k,\Sigma_k)/\sum_j\pi_j\mathcal N(x_i;\mu_j,\Sigma_j)$。这叫责任度，对每个点跨成分求和为一。

M 步把责任度当分数权重重新统计：$N_k=\sum_i r_{ik}$，$\pi_k=N_k/N$，$\mu_k=\sum_i r_{ik}x_i/N_k$；协方差围绕新均值计算加权偏差的外积。若 N_k 为零或太小，需要处理失效成分。一个点可部分影响多个成分，有点像软分组，但 GMM 还学习方差与混合比例，不等同于直接把 k-means 的标签变软。

精确 EM 的单调性来自对似然下界的交替处理，不等于全局最优。无约束高斯成分可能压到某个数据点并令方差趋零，使似然异常增大；正则、初始化和有效样本量检查都很重要。
RECAP_EN: EM alternates posterior responsibilities and weighted parameter estimation. Responsibilities sum to one per observation; mixture densities themselves are not class probabilities.
WORKED_Q: 两个观测 x=(0,2)，初始均值 (0,2)、混合权重各 1/2，两个方差固定为 1。本例只学习均值与混合权重。高斯密度在自身均值处约 0.398942，距离 2 处约 0.053991。完成一次 E/M 更新。 || For observations x=(0,2), initial means (0,2), equal mixture weights, and both variances fixed at 1, perform one E/M update of means and weights. Gaussian densities are about 0.398942 at distance zero and 0.053991 at distance two.
WORKED_A: E 步：x=0 的加权密度为 (0.199471,0.0269955)，归一化约 (0.8808,0.1192)；x=2 顺序相反。M 步：N₁=N₂=1，权重仍各 1/2。均值 μ₁=(0.8808×0+0.1192×2)/1≈0.2384；μ₂≈1.7616。这里方差按题设保持 1；新参数留给下一轮重新算责任度。 || E-step: for x=0, weighted densities (0.199471,0.0269955) normalize to approximately (0.8808,0.1192); x=2 reverses them. M-step: effective counts are both 1, hence weights remain 1/2. New means are 0.2384 and 1.7616. Variances remain 1 by design; recompute responsibilities using these new parameters in the next iteration.
PRACTICE_Q: 把数据和初始均值都改成 (0,4)，固定方差改为 4、混合权重各 1/2。标准化距离仍为 0 和 2，因此责任度仍为 (0.8808,0.1192) 与反序。补出有效样本数、权重和新均值。 || Change data and initial means to (0,4), fixed variances to 4, and keep equal weights. Standardized distances remain 0 and 2, so responsibilities remain (0.8808,0.1192) and the reverse. Update counts, weights, and means.
HINT: 每列责任度相加；均值用“责任度×观测”之和除该列总和。 || Sum responsibilities down each component column; divide its weighted observation sum by that count.
PRACTICE_A: N₁=N₂=1，权重仍各 1/2；μ₁=0×0.8808+4×0.1192≈0.4768，μ₂≈3.5232。所有长度放大两倍，均值更新也放大两倍。 || Both effective counts are 1 and weights 1/2. Means become approximately 0.4768 and 3.5232. Doubling all lengths doubles the updated means.
TRANSFER_Q: 两个观测仍为 (0,2)，初始均值 (0,2)、固定方差 1，但先验混合权重改成 (3/4,1/4)。令 a=exp(−2)≈0.135335。两点对成分 1 的责任度分别为 3/(3+a) 与 3a/(3a+1)。独立算出两点责任度、有效样本数、新权重及两均值。 || Keep observations and initial means (0,2), fixed variance 1, but change initial weights to (3/4,1/4). With a=exp(−2)≈0.135335, component-1 responsibilities are 3/(3+a) and 3a/(3a+1). Compute responsibilities, effective counts, new weights and both means.
TRANSFER_A: 责任度约为 (0.9568,0.0432)、(0.2888,0.7112)。N₁≈1.2456、N₂≈0.7544；新权重约 (0.6228,0.3772)。μ₁≈2×0.2888/1.2456≈0.4637，μ₂≈2×0.7112/0.7544≈1.8856（按未舍入值约 1.8856）。每个点跨成分和为 1；跨点的列和是有效样本数，不必为 1。 || Responsibilities are approximately (0.9568,0.0432) and (0.2888,0.7112). Counts are 1.2456 and 0.7544, giving weights (0.6228,0.3772). Means are about 0.4637 and 1.8856. Each observation’s row sums to one; a component’s column sum is its effective count and need not equal one.
BRIDGE: 聚类找组，PCA 找能保留主要变化的坐标方向；两者都不直接等于分类目标。

@@ ml23 | PCA：用少数方向保留数据的变化 | PCA, projection, and SVD
CARDS: M227,M228,M229,M230,M231,M232,M233,M234,M235,M236,M237,M238,M239,M240
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
TRANSFER_Q: 二维训练数据的协方差为 diag(9,1)。若第二特征由米改成毫米且不标准化，协方差对角变成什么？保留一个主成分的方向如何改变？ || Training covariance is diag(9,1). If the second feature changes from meters to millimeters without standardization, what is the new diagonal and which principal direction is retained?
TRANSFER_A: 第二特征乘 1000，方差乘 1000²，得到 diag(9,1000000)。原先第一轴方差最大，换单位后第二轴最大。单位会改变未标准化 PCA 的优化问题；是否标准化要结合变量含义。 || The second variance multiplies by 1000², giving diag(9,1000000). The selected direction changes from the first axis to the second. Units change the unstandardized PCA objective; choose standardization according to feature meaning.
BRIDGE: PCA 通过线性投影提取特征；神经网络通过多层可学习变换得到更丰富的表示。

@@ ml24 | 反向传播：沿计算图分配责任 | Backpropagation through a computation graph
CARDS: M241,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254
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
TRANSFER_Q: 令预测 q=wx，损失 L=½(q−y)²，x=2、y=3、w=1。独立画出 w→q→L 的计算顺序，求 L、dL/dw，并以学习率 0.1 更新 w；所有梯度使用旧参数。 || Use prediction q=wx and loss L=½(q−y)² with x=2,y=3,w=1. Trace w→q→L, compute L and dL/dw, then update w with learning rate 0.1 using old-parameter gradients.
TRANSFER_A: 前向 q=2、残差 −1、L=0.5。反向 dL/dq=−1，dq/dw=2，故 dL/dw=−2。更新 w=1−0.1×(−2)=1.2；新 q=2.4，新损失 0.18。前向求值、反向求导、更新参数是三个动作。 || Forward: q=2, residual −1, loss 0.5. Backward: dL/dq=−1 and dq/dw=2, giving dL/dw=−2. Update w to 1.2; then q=2.4 and loss=0.18. Evaluation, differentiation, and parameter updates are separate operations.
BRIDGE: CNN 在局部空间位置共享同一组参数，把图像结构融入网络。

@@ ml25 | CNN：同一个小检测器在图上滑动 | Convolution, shape, and receptive field
CARDS: M255,M256,M257,M258,M259,M260,M261,M262,M263,M264
PREREQ: ml24
GOAL: 能从窗口位置数推输出尺寸、从共享滤波器数推参数量；滑动内积见补充单元。
EXPLAIN: 卷积层在一个小窗口内，将像素与滤波器权重逐项相乘再求和，然后把同一滤波器移动到别的位置。一个滤波器产生一个输出通道；多个输入通道的贡献在该输出通道内相加。空间位置共享权重，参数数目通常不随图像宽高增长。

沿一个轴，若输入长度 n、核宽 k、两侧填充 p、步长 s、膨胀为 1，则输出长度为 $\lfloor(n+2p-k)/s\rfloor+1$。这是数“窗口能从哪些起点完整放下”，而不是背一个尺寸口令。池化也做局部汇聚，但不一定有可学习权重。

数学卷积会翻转核，很多深度学习层实际做互相关；手算序列题时要遵守原定义。平移等变指输入移动导致输出相应移动，平移不变指输出不变；边界、步长与采样还会限制严格等变性。
RECAP_EN: A convolutional layer shares local filters across spatial positions. Count valid window placements for output size and distinguish mathematical convolution from the cross-correlation used by many neural layers.
WORKED_Q: 32×32 RGB 输入，6 个 5×5 核，步长 1、无填充，求输出形状及含偏置参数量。 || For 32×32 RGB input and six 5×5 filters with stride 1 and no padding, find output shape and parameter count including biases.
WORKED_A: 每轴 32-5+1=28，输出 28×28×6。每核 5×5×3=75 个权重加 1 偏置，总参数 6×76=456。 || Output shape is 28×28×6. Each filter has 75 weights and one bias, giving 456 parameters.
PRACTICE_Q: 16×16 单通道输入，4 个 3×3 滤波器，步长 1、无填充、无膨胀，每输出通道一个偏置。补出输出形状和参数量。 || For 16×16 single-channel input and four 3×3 filters, stride 1, no padding or dilation, and one bias per output channel, find shape and parameter count.
HINT: 每轴数 16−3+1 个起点；每核有 3×3×1 个权重。 || Count 16−3+1 positions per axis and 3×3×1 weights per filter.
PRACTICE_A: 输出为 14×14×4；每核 9 个权重加 1 偏置，总参数 4×10=40。 || Output is 14×14×4; each filter has nine weights and one bias, totaling 40 parameters.
TRANSFER_Q: 把上一规格完整重述为：16×16 单通道、4 个 3×3 核、每核一偏置；现在步长改为 2、两侧填充均为 1、膨胀仍为 1。独立算输出尺寸及参数数目，并说明哪些改变、哪些不变。 || For 16×16 single-channel input and four 3×3 filters with one bias each, now use stride 2, padding 1 on each side, dilation 1. Compute output shape and parameter count, explaining changes.
TRANSFER_A: 每轴 floor((16+2−3)/2)+1=floor(7.5)+1=8，输出 8×8×4。权重核规格没变，仍有 40 个参数。步长和填充改变窗口位置，不增加这层的共享权重。 || Each axis is floor((16+2−3)/2)+1=8, so output is 8×8×4. Filter specifications are unchanged, leaving 40 parameters. Stride and padding change window positions, not the shared weights.
BRIDGE: 网络结构定义能表示什么；优化与训练模式决定如何学到参数。

@@ ml26 | 训练网络：梯度、状态和正则化分别做什么 | Optimization and training state
CARDS: M265,M266,M267,M268,M269,M270,M271,M272,M273,M274,M275,M276
PREREQ: ml24,ml25
GOAL: 能计算 inverted dropout 的保留值与期望，并区分训练模式和评估模式。
EXPLAIN: mini-batch SGD 每步用一部分样本估计梯度；一个 epoch 表示看完一遍训练集，不等于一次更新。Momentum 累积方向，Adam 还维护梯度及平方梯度的移动平均，并做初期偏差修正。它们改变更新规则，不会自动消除数据泄漏或错误标签。

正则化控制学习偏好。Inverted dropout 以保留概率 q>0 留下激活，保留时除以 q，使这一激活的期望不变；经过后续非线性，整网输出的期望不一定不变。评估时不再随机丢弃。常见 BatchNorm 训练时按通道汇集批内统计，评估时用运行统计；LayerNorm 通常对每个样本/token 的指定特征维归一化，不依赖其他样本的批统计。

先用小子集检查是否能过拟合，再扩大实验。检查学习率、梯度、模式切换和增强是否保留标签含义。Early stopping 根据验证表现决定何时停，学习率计划决定怎样迈步，职责不同。AdamW 的衰减与在 Adam 损失中加入 L2 也不应机械等同。
RECAP_EN: Optimizers maintain update state; normalization layers and dropout maintain or use different training behavior. Debug a small subset and keep evaluation separate from parameter fitting and model selection.
WORKED_Q: 一个激活为 3，训练时 inverted dropout 以 q=0.75 保留；保留值除以 q，丢弃则为 0。列出两种输出及概率，计算期望。 || An activation of 3 uses inverted dropout with retention q=0.75: divide retained values by q, otherwise output zero. List outcomes and probabilities and compute expectation.
WORKED_A: 概率 0.75 输出 3/0.75=4；概率 0.25 输出 0。期望 0.75×4+0.25×0=3。评估时关闭 dropout，直接传递激活 3，不再乘 0.75。 || Output is 4 with probability 0.75 and 0 with probability 0.25. Expectation is 3. Evaluation disables dropout and passes 3 directly; do not multiply it by 0.75 again.
PRACTICE_Q: 激活改为 8，q=0.5，使用同一种 inverted dropout。求保留输出、期望和评估输出。 || For activation 8 and retention 0.5 under inverted dropout, find retained output, expectation, and evaluation output.
HINT: 分别写“保留”“丢弃”“评估”三种情况。 || Separate retained, dropped, and evaluation behavior.
PRACTICE_A: 保留时 8/0.5=16，丢弃时 0，期望 0.5×16=8；评估直接输出 8。 || Retained output is 16, dropped output zero, expectation 8, and evaluation output 8.
TRANSFER_Q: 固定网络权重，输入激活恒为 2，q=0.5；训练 dropout 后紧接平方函数。计算平方输出的期望，再与关闭 dropout 时比较。能否由单个激活期望不变推出整网期望不变？ || With fixed weights and activation 2, apply training dropout at q=0.5 then square its output. Compare expected squared output with evaluation mode. Does preserved activation expectation imply preserved whole-network expectation?
TRANSFER_A: 训练输出先为 4 或 0，各概率 1/2，平方后期望 (16+0)/2=8。评估输出为 2²=4。非线性使两者不同，所以不能推广；固定权重仍随机时也应先检查模式和随机增强。 || Training produces 4 or 0 equally, so expected squared output is 8. Evaluation gives 2²=4. Nonlinearity breaks the inference; repeated randomness with fixed weights also calls for checking mode and augmentation.
BRIDGE: 视觉任务的输出与评价标准不同，不能只按网络名称判断方法优劣。

@@ ml27 | 视觉任务：输出决定损失与评价 | Vision tasks and evaluation
CARDS: M277,M278,M279,M280,M281,M282,M283,M284
PREREQ: ml25,ml26
GOAL: 能根据问题选择图像类别、检测框、语义像素或实例像素输出，并解释输出中丢失的信息。
EXPLAIN: 分类给整图标签；检测还要给对象位置；语义分割给每个像素语义类别；实例分割还分开同类的不同对象。输出结构不同，所以头部、损失和评价标准不能直接混用。残差连接把变换结果与输入相加，需要形状兼容，目的是提供额外的信息和梯度路径。

图像恢复可写成 y=Ax+noise：y 是观测，x 是希望恢复的图，A 表示模糊、下采样等退化。多个不同 x 可能解释同一 y，因此恢复依赖先验。像素平方误差衡量数值接近，不能完整表达视觉感受或语义正确。

压缩还需同时考虑码率与失真。模型比较应先固定任务、数据、度量与测试协议；好看的样例不证明所有场景都可靠，反复针对同一测试集调参也会削弱它的独立性。
RECAP_EN: Output structure determines the task and evaluation. Pixelwise reconstruction error, perceptual quality, and semantic correctness measure different aspects of a result.
WORKED_Q: 画面中有两辆相邻汽车。要分别回答“有没有车”“两辆车各在哪里”“哪些像素是车”“每个车像素属于哪辆车”，各需要哪种输出？ || An image contains two adjacent cars. Which output answers whether cars exist, where each car is, which pixels are cars, and which car owns each car pixel?
WORKED_A: 图像分类给整体标签；目标检测给两个带类别的框；语义分割给每像素 car/非 car 标签；实例分割还给每辆车不同实例编号。后一任务比只知道 car 像素多保留对象身份。 || Classification gives an image label; detection gives two labeled boxes; semantic segmentation gives pixel classes; instance segmentation also separates the two object identities.
PRACTICE_Q: 机器人要绕开一张椅子，并知道它在图像中的轮廓；任务不要求区分多张同类椅子。只有图像级 chair 标签够吗？在上述输出中至少需要哪一种？ || A robot needs the image silhouette of a chair, without distinguishing multiple chairs of the same class. Is an image-level chair label enough, and which listed output supplies the silhouette?
HINT: 问题要像素边界，不只要“存在”或一个矩形。 || A silhouette needs pixel boundaries, not only presence or a rectangle.
PRACTICE_A: 图像级标签不够，语义分割可给椅子像素与轮廓。检测框只近似定位，包含背景，不能等同精确轮廓。 || No. Semantic segmentation supplies chair pixels and their boundary. A detection box includes background and is not an exact silhouette.
TRANSFER_Q: 两个人的像素连成同一片 person 区域。需求改为“分别计算两个人各占多少像素”。只保留语义分割结果能唯一回答吗？还缺什么？ || Two people form one connected person-class region. The task asks how many pixels belong to each person. Can semantic segmentation alone uniquely answer this, and what is missing?
TRANSFER_A: 不能，类别标签没有逐实例归属。需要实例分割或其他可靠的对象分离信息；同一语义掩码可以对应不同实例划分。不能把连通区域个数直接当成人数。 || No. Class labels omit instance ownership. Instance segmentation or other reliable separation is needed; the same semantic mask can admit different object partitions. Connected-component count need not equal person count.
BRIDGE: 恢复试图解释观测，生成模型则尝试从随机变量采样新的数据。

@@ ml28 | 生成模型：采样不等于计算密度 | GANs and diffusion models
CARDS: M285,M286,M287,M288,M289,M290,M291,M292,M293,M294
PREREQ: ml06,ml24,ml26
GOAL: 能逐项计算标准高斯扩散的前向加噪，并区分训练中已知噪声与生成时预测噪声。
EXPLAIN: 生成器可以把简单随机 z 映射为图像 G(z)，因此能采样，却未必能高效给某张图计算精确概率密度。GAN 训练判别器区分真实与生成样本，再训练生成器改变这种判断；双方改变彼此面对的目标，所以不能把两个损失都当作固定函数的普通下降。

标准高斯扩散训练可直接采样 $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$，其中 $\epsilon\sim\mathcal N(0,I)$ 与 x0 独立，bar-alpha 是各步 alpha 的乘积。可以理解为逐渐让信号被噪声淹没；两个系数的平方相加为 1，这是加噪的尺度安排，不是将两幅图按普通百分比混合。网络常学习预测 epsilon；生成时从噪声出发反复使用预测，不是掌握了新图的真实噪声再直接相减。

在这个前向模型中，给定 x0、xt 的一步后验可为高斯；只给 xt 的真实反向分布一般不能据此断言精确高斯。文字等条件可影响去噪预测：无条件预测 epsilon_u 与条件预测 epsilon_c 的差表示条件带来的调整，引导强度控制采用多少调整。质量、多样性与条件符合度须分别评价。
RECAP_EN: Sampling and density evaluation are distinct. GANs learn through a changing adversarial objective; diffusion trains a denoising-related model under a specified forward noise process and uses a learned reverse process for sampling.
WORKED_Q: 标准前向式 xt=√a·x0+√(1−a)·ε，a=0.36、x0=2、ε=1。求两系数与 xt。 || For xt=√a·x0+√(1−a)·ε with a=0.36,x0=2,ε=1, compute both coefficients and xt.
WORKED_A: √a=0.6，√(1−a)=0.8，故 xt=0.6×2+0.8×1=2。系数平方和为 1；结果刚好等于 x0，不代表没加噪声。 || Coefficients are 0.6 and 0.8, giving xt=2. Their squares sum to one; accidental equality with x0 does not mean no noise was added.
PRACTICE_Q: 同一前向式中 a=0.64、x0=1、ε=−1。补出平方根系数，并求 xt。 || Use the same forward formula with a=0.64,x0=1,ε=−1. Find coefficients and xt.
HINT: 噪声系数是 √(1−0.64)，不是 1−√0.64。 || The noise coefficient is √(1−0.64), not 1−√0.64.
PRACTICE_A: 信号系数 0.8、噪声系数 0.6，xt=0.8−0.6=0.2。 || Signal and noise coefficients are 0.8 and 0.6, giving xt=0.2.
TRANSFER_Q: 训练时 a=0.25、x0=4、采样 ε=−2。算出 xt；生成时若只给这一个 xt 和 a，能唯一恢复真实 x0 与 ε 吗？解释网络预测的作用。 || During training use a=0.25,x0=4 and sampled ε=−2. Compute xt. During generation, do xt and a alone uniquely determine the true x0 and ε? Explain the learned prediction’s role.
TRANSFER_A: xt=0.5×4+√0.75×(−2)=2−√3≈0.2679。一个方程不能唯一确定两个未知量；生成时依靠从数据学到的去噪相关预测与采样过程，不是持有真实噪声后直接相减。 || xt=2−√3≈0.2679. One equation does not uniquely determine both unknowns. Generation uses a denoising-related prediction learned from data and a sampling procedure, not access to the true noise of an unseen clean image.
BRIDGE: Transformer 的注意力是一种信息组合运算，可用于判别或生成，并不由任务名称决定。

@@ ml29 | 注意力：每个位置向其他位置取信息 | Attention, dimensions, and robustness
CARDS: M295,M296,M297,M298,M299,M300,M301,M302
PREREQ: ml03,ml11,ml24
GOAL: 能区分 query/key/value，手算注意力加权，并核对矩阵维度。
EXPLAIN: 把 token 暂时看作一个词块或图像小块。像查资料一样，query 是查询条件，key 是可匹配的索引，value 是取回后要组合的内容；它们都是学出来的向量，不是人工填写的文字。标准注意力为 $\operatorname{softmax}(QK^T/\sqrt{d_k})V$：对每个 query 的行归一化，再加权组合 values。权重和为一，输出仍通常是特征，不是类别概率。

若 X 为 n×D，WQ、WK 为 D×dk，WV 为 D×dv，则 QK^T 为 n×n，输出为 n×dv。投影处理特征维，不是 token 数。在独立、单位方差分量的直观模型下，内积分数方差随 dk 增长；除以 √dk 可抑制分数过大导致 softmax 过于尖锐。位置机制再补充顺序；自回归生成还需因果遮罩，阻止读取未来位置。

多头让模型在不同投影下组合关系；前馈块处理各 token 的特征。稠密注意力仍有两两交互成本。鲁棒性问题则问输入小改动是否改变决策：随机噪声与为了诱发错误而优化的扰动不同，任何结论都需说明威胁模型。
RECAP_EN: Queries and keys produce matching weights; values supply the mixed information. Normalize over keys for each query and check feature dimensions separately from token count.
WORKED_Q: 一个 query 的缩放后分数 (ln 3,0)，values=(2,10)，输出多少？ || For scaled scores (ln 3,0) and scalar values (2,10), what is the attention output?
WORKED_A: softmax 权重 (3/4,1/4)，输出为 3/4×2+1/4×10=4。 || Weights are (3/4,1/4), giving output 4.
PRACTICE_Q: 两个分数相等、values=(2,10)，输出多少？ || With equal scores and values (2,10), what is the output?
HINT: 两个权重相同且和为一。 || The two weights are equal and sum to one.
PRACTICE_A: 权重各 1/2，输出 6。 || Each weight is 1/2, so the output is 6.
TRANSFER_Q: 一个 query 的缩放后分数为 (0,ln 3)，对应标量 values=(2,10)。独立算权重和输出；若只把 values 对调、分数不变，输出又是多少？ || One query has scaled scores (0,ln 3) and scalar values (2,10). Compute weights and output; then swap only values while leaving scores fixed.
TRANSFER_A: 指数权重 (1,3)，归一化 (1/4,3/4)。输出 0.25×2+0.75×10=8；只换 values 后为 0.25×10+0.75×2=4。query/key 决定取信息的比例，value 决定被混合的内容。 || Weights normalize to (1/4,3/4), giving output 8. Swapping only values gives 4. Queries and keys determine mixing proportions; values determine the mixed content.
BRIDGE: 进入往年综合题时，先识别需要哪条知识链，再开始推导。

@@ ml30 | 综合题诊所：拆条件、补中间式、找反例 | A clinic for historical derivations
CARDS: M303,M304,M305,M306,M307,M308,M309,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M322,M323,M324,M325,M326
PREREQ: ml04,ml06,ml19,ml24
RELATED: ml13,ml23,ml25
GOAL: 能把复合函数拆成计算图、逐步使用链式法则，并在改变输入后独立重算。
EXPLAIN: 往年题跨越概率、熵、高斯条件分布、优化、线性代数、SVM、PCA、卷积与 DTFT，不应一口气按编号背完。按题回到相应微课：概率题回贝叶斯与 MLE；约束题回 KKT；秩与正规方程回最小二乘；PCA 回投影；卷积题回核翻转和索引。图题先打开卡片原图，保留原始下标。

推导时先写变量与成立条件，再给中间量命名。例如对 ell=(u exp(v)-2v exp(-u))²，先令 q 为括号项，然后写 2q 乘 q 的各偏导。同时梯度更新必须都使用旧的 u,v；先更新一个再算另一个，已经是另一种算法。

对“总成立”的命题优先找边界与反例：方阵也可能秩不足；零乘子不保证约束不活跃；线性不代表时不变。对历史解答的分组计数 4+ 也不能默认为 4。这里提供解题入口和代表性练习，24 张原题仍应分主题闭卷重做。
RECAP_EN: For a long derivation, state assumptions, introduce intermediate variables, and verify dimensions and boundary cases. A numerical answer is meaningful only under its data interpretation and update convention.
WORKED_Q: 令 L=q²，q=u exp(v)−2v exp(−u)。先对 q 分别求 u、v 偏导，再写 L 的两个偏导。 || Let L=q² with q=u exp(v)−2v exp(−u). Derive both partial derivatives of q, then those of L.
WORKED_A: ∂q/∂u=exp(v)+2v exp(−u)；第二项的两个负号相消。∂q/∂v=u exp(v)−2 exp(−u)。外层 dL/dq=2q，所以各偏导再乘 2q。 || The derivatives are q_u=exp(v)+2v exp(−u) and q_v=u exp(v)−2 exp(−u). The two negative signs in q_u cancel. Multiply each by the outer derivative 2q to obtain L_u and L_v.
PRACTICE_Q: 沿用完整定义 L=[u exp(v)−2v exp(−u)]²，在 u=0、v=0 时依次算 q、q_u、q_v 和 L 的梯度。 || For L=[u exp(v)−2v exp(−u)]² at u=v=0, compute q,q_u,q_v and the gradient of L.
HINT: 先用 exp(0)=1 算内部值，最后乘外层 2q。 || Use exp(0)=1 for the inner values, then multiply by 2q.
PRACTICE_A: q=0，q_u=1，q_v=−2；因为 2q=0，L 的梯度为 (0,0)。内部导数不为零不代表外层梯度不为零。 || q=0,q_u=1,q_v=−2. Because 2q=0, the loss gradient is (0,0). Nonzero inner derivatives need not give a nonzero final gradient.
TRANSFER_Q: 同一 L 在 u=1、v=0 时，独立求 L、L_u、L_v。给精确形式并用 exp(−1)≈0.367879 检查。 || For the same L at u=1,v=0, independently compute L,L_u,L_v, giving exact forms and a check using exp(−1)≈0.367879.
TRANSFER_A: q=1，L=1；q_u=1，q_v=1−2/e；故 L_u=2，L_v=2−4/e≈0.52848。先求内部量再求外部量，可避免漏乘 2q。 || q=1 and L=1. q_u=1 and q_v=1−2/e, giving L_u=2 and L_v=2−4/e≈0.52848. Evaluate inner quantities before the outer derivative to avoid omitting 2q.
BRIDGE: 复习顺序是先讲通一条推导，再拆成几张检索卡，最后用未见变式检查能否迁移。
