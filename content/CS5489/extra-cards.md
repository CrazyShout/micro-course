# Extra Resources · historical preview

@@ M183 | x01-neighbors | learn | XKNN:8-14
Q_EN: How does k-nearest-neighbor classification produce a prediction?
Q_ZH: k 近邻分类怎样得到预测结果？
A_EN: Store labeled training examples. For a query, measure distances, select the k nearest examples, and return their majority class. Training mainly stores data; prediction performs the comparison. Specify the distance, k and tie rule. Nearby points are assumed to have useful label information, so a poor distance can make the vote meaningless.
A_ZH: 保存带标签的训练样本。对新样本计算距离，选最近的 k 个，再用多数类别作预测。训练主要是保存数据，预测时才进行比较。必须说明距离、k 和平票处理规则。该方法依赖“距离近的样本，其标签有参考价值”；距离不合理时，投票也可能失效。

@@ M184 | x01-neighbors | worked | XKNN:8-16
Q_EN: The three nearest labels are A, B, B. What does ordinary 3-NN predict, and can distance weighting change it?
Q_ZH: 最近三个样本的标签是 A、B、B，普通 3-NN 预测什么？距离加权会改变结果吗？
A_EN: Ordinary 3-NN predicts B by two votes to one. With weights 10, 1, 1 respectively, A receives weight 10 and B receives 2, so weighted voting predicts A. This added example shows that the weighting convention is part of the model. Choose it using validation data rather than selecting whichever rule fixes one test mistake.
A_ZH: 普通 3-NN 以两票对一票预测 B。若三个权重依次为 10、1、1，则 A 总权重为 10，B 为 2，加权投票会预测 A。这个补充例子说明权重规则也是模型的一部分，应通过验证集选择，不能为了修正某个测试错误临时换规则。

@@ M185 | x01-neighbors | check | XKNN:12-17
Q_EN: Why do scaling and the choice of k matter for k-NN?
Q_ZH: 为什么特征缩放和 k 的选择会影响 k-NN？
A_EN: Euclidean distance squares coordinate differences, so a feature measured on a large numerical scale can dominate. Fit any scaling on training data. Small k gives flexible, noise-sensitive neighborhoods; larger k smooths the vote and can erase local distinctions. Neither extreme is always better. Select k within training/validation splits.
A_ZH: 欧氏距离会平方各坐标差，因此数值尺度大的特征可能主导距离。缩放参数只能在训练集上拟合。较小的 k 更灵活，也更容易受噪声影响；较大的 k 更平滑，但可能抹掉局部类别差异。两端都不一定最好，应通过训练集内部验证选择。

@@ M186 | x01-neighbors | check | XKNN:17; XKREF:1-NN Convergence Proof
Q_EN: Does keeping k=1 guarantee Bayes-optimal prediction as the dataset grows?
Q_ZH: 数据越来越多时，固定 k=1 能保证达到贝叶斯最优吗？
A_EN: No. Suppose features carry no label information and independent labels are A with probability 0.7 and B with 0.3. The Bayes rule always predicts A, with error 0.3. A single neighbor supplies another independent label, giving error 2(0.7)(0.3)=0.42, even with more data. This added counterexample qualifies the historical slide's broad convergence statement.
A_ZH: 不能。假设特征不含标签信息，各样本标签独立，以 0.7 概率为 A、0.3 概率为 B。贝叶斯规则总预测 A，错误率为 0.3。单个近邻提供另一个独立标签，错误率为 2(0.7)(0.3)=0.42，增加数据也不改变这一点。这个补充反例限定了旧课件较宽泛的收敛表述。

@@ M187 | x02-regression | learn | XR1:10-14
Q_EN: What does ordinary least squares optimize, and what is a residual?
Q_ZH: 普通最小二乘优化什么？什么是残差？
A_EN: For prediction $\hat y_i=w^Tx_i+b$, the residual is $r_i=y_i-\hat y_i$. OLS chooses parameters to minimize $\sum_i r_i^2$, or its mean. Squaring makes large errors count more and removes their sign. The model output is numerical; rounding it into a class changes the task and evaluation.
A_ZH: 对预测 $\hat y_i=w^Tx_i+b$，残差是 $r_i=y_i-\hat y_i$。OLS 选择参数使 $\sum_i r_i^2$ 或其平均值最小。平方使大误差受到更重惩罚，也消除了正负号。模型输出是数值；把它四舍五入成类别，会改变任务与评价方式。

@@ M188 | x02-regression | worked | XR1:10
Q_EN: Predictions are (2,4,5) and targets are (1,4,7). Compute MSE and RMSE.
Q_ZH: 预测值为 (2,4,5)，真实值为 (1,4,7)，计算 MSE 和 RMSE。
A_EN: Residuals are (-1,0,2), and squared errors sum to 5. Thus MSE is $5/3$ and RMSE is $\sqrt{5/3}\approx1.291$. MSE has squared target units; RMSE has the original target unit. These are added teaching numbers, not a reproduced experiment.
A_ZH: 残差为 (-1,0,2)，平方误差之和为 5。因此 MSE 为 $5/3$，RMSE 为 $\sqrt{5/3}\approx1.291$。MSE 的单位是目标单位的平方，RMSE 与目标量使用相同单位。这是补充计算例子，不是复现实验成绩。

@@ M189 | x02-regression | learn | XR1:13,18
Q_EN: How does a design matrix include the intercept?
Q_ZH: 设计矩阵怎样包含截距项？
A_EN: Put one example per row and prepend a column of ones. With n examples and d measured features, $X$ is $n\times(d+1)$ and $w=(b,w_1,\ldots,w_d)^T$. Then all predictions are $Xw$. The ones column is a convention, not an extra measured feature. Keep row/column conventions explicit.
A_ZH: 每行放一个样本，并在前面加一列 1。若有 n 个样本和 d 个测量特征，则 $X$ 为 $n\times(d+1)$，参数为 $w=(b,w_1,\ldots,w_d)^T$，全部预测写成 $Xw$。常数列是一种表示约定，不是额外测得的特征，必须明确行列含义。

@@ M190 | x02-regression | learn | XR1:18-19
Q_EN: Derive the normal equations for linear least squares.
Q_ZH: 怎样推导线性最小二乘的正规方程？
A_EN: For $J(w)=\frac12\|Xw-y\|^2$, the gradient is $X^T(Xw-y)$. Setting it to zero gives $X^TXw=X^Ty$. The Hessian $X^TX$ is positive semidefinite, so any solution is a global minimizer. The inverse expression $w=(X^TX)^{-1}X^Ty$ additionally requires full column rank.
A_ZH: 对 $J(w)=\frac12\|Xw-y\|^2$，梯度为 $X^T(Xw-y)$。令其为零，得到 $X^TXw=X^Ty$。Hessian $X^TX$ 半正定，因此方程的解是全局极小点。进一步写成逆矩阵形式 $w=(X^TX)^{-1}X^Ty$，还需要列满秩。

@@ M191 | x02-regression | check | XR1:19; XR2:17
Q_EN: Is having at least as many samples as coefficients sufficient for a unique OLS fit?
Q_ZH: 样本数不少于系数个数，就足以保证 OLS 解唯一吗？
A_EN: No. Full column rank of X is required. Even with many rows, duplicate or linearly dependent columns make $X^TX$ singular. OLS still has least-squares solutions, but coefficients may not be unique. QR, SVD or a pseudoinverse can compute a solution without pretending that a singular inverse exists.
A_ZH: 不足够，还要求 X 列满秩。即使有很多样本，重复或线性相关的特征列仍会使 $X^TX$ 奇异。最小二乘解仍存在，但系数可能不唯一。可用 QR、SVD 或伪逆求解，不能把不存在的逆矩阵当作有效公式。

@@ M192 | x02-regression | worked | XR1:15-17
Q_EN: Fit a line through (0,1), (1,3), (2,5). What do slope and intercept mean?
Q_ZH: 对 (0,1)、(1,3)、(2,5) 拟合直线，斜率和截距是什么？
A_EN: The line $\hat y=2x+1$ fits every point, so the slope is 2, intercept is 1 and training MSE is zero. A one-unit increase in x changes this model's prediction by 2. A perfect fit to these three points does not establish accuracy outside the observed range or a causal relationship.
A_ZH: 直线 $\hat y=2x+1$ 通过全部点，所以斜率为 2、截距为 1、训练 MSE 为零。x 增加一个单位，模型预测增加 2。对这三个点拟合完美，并不能证明范围外预测准确，也不能证明因果关系。

@@ M193 | x02-regression | learn | XR1:22-24
Q_EN: Under what noise model does OLS coincide with maximum likelihood?
Q_ZH: 在什么噪声模型下，OLS 等价于最大似然估计？
A_EN: Assume independent errors $\epsilon_i\sim N(0,\sigma^2)$ with common variance and $y_i=x_i^Tw+\epsilon_i$. The negative log likelihood is a constant plus $\sum_i(y_i-x_i^Tw)^2/(2\sigma^2)$. For fixed positive variance, maximizing likelihood therefore minimizes squared error. Gaussian noise is needed for this probabilistic interpretation, not for defining OLS.
A_ZH: 假设误差独立，$\epsilon_i\sim N(0,\sigma^2)$ 且方差相同，并有 $y_i=x_i^Tw+\epsilon_i$。负对数似然等于常数加 $\sum_i(y_i-x_i^Tw)^2/(2\sigma^2)$。固定正方差时，最大化似然就等价于最小化平方误差。高斯假设用于概率解释，并非定义 OLS 的必要条件。

@@ M194 | x02-regression | learn | XR2:3-6
Q_EN: State the ridge objective and derive its solution under the stated scaling.
Q_ZH: 写出岭回归目标，并在明确系数约定下求解。
A_EN: Use $J=\frac12\|Xw-y\|^2+\frac{\lambda}{2}\|w\|^2$. Stationarity gives $(X^TX+\lambda I)w=X^Ty$. For $\lambda>0$, the matrix is positive definite and the solution is unique. This formula penalizes every coordinate in w. If the intercept is exempt, replace I with a diagonal penalty mask.
A_ZH: 采用 $J=\frac12\|Xw-y\|^2+\frac{\lambda}{2}\|w\|^2$。驻点条件为 $(X^TX+\lambda I)w=X^Ty$。当 $\lambda>0$ 时，该矩阵正定，解唯一。此式惩罚 w 的全部坐标；若截距不受惩罚，应把 I 换成相应的对角惩罚矩阵。

@@ M195 | x02-regression | check | XR2:4-7,17
Q_EN: Why can ridge help with nearly collinear features, and what does it cost?
Q_ZH: 岭回归为何能改善近共线特征的问题？代价是什么？
A_EN: Along an eigenvector of $X^TX$ with eigenvalue s, ridge replaces division by s with division by $s+\lambda$. Small-eigenvalue directions are therefore less amplified. This improves conditioning and reduces variance, at the cost of bias. It does not prove that the model is correctly specified or that a chosen lambda generalizes best.
A_ZH: 沿 $X^TX$ 特征值为 s 的方向，岭回归把除以 s 改为除以 $s+\lambda$，减少了小特征值方向上的放大，从而改善条件数并降低方差，代价是引入偏差。它不能证明模型形式正确，也不能保证任意选定的 lambda 泛化最好。

@@ M196 | x02-regression | learn | XR2:10-16
Q_EN: What distinguishes lasso regularization from ridge regularization?
Q_ZH: Lasso 与岭回归的正则化有什么区别？
A_EN: Lasso uses $\lambda\|w\|_1=\lambda\sum_j|w_j|$ instead of a squared L2 penalty. The kink at zero can produce exactly zero coefficients, giving a form of feature selection. Ridge usually shrinks coefficients continuously without making them exactly zero. Lasso does not guarantee that selected features are causal or that its solution is always unique.
A_ZH: Lasso 使用 $\lambda\|w\|_1=\lambda\sum_j|w_j|$，而不是平方 L2 惩罚。零点处的折角可使系数精确为零，从而进行一种特征选择。岭回归通常连续缩小系数，而不把它们精确变成零。Lasso 不保证选中特征具有因果意义，也不总保证解唯一。

@@ M197 | x02-regression | worked | XR2:15-16
Q_EN: With $X^TX=I$, OLS weights (3,-0.4) and $\lambda=1$, compare ridge and lasso weights. Use data loss $\frac12\|Xw-y\|^2$ and penalties $\frac\lambda2\|w\|^2$ and $\lambda\|w\|_1$, respectively.
Q_ZH: 设 $X^TX=I$、OLS 权重为 (3,-0.4)、$\lambda=1$，比较 Ridge 与 LASSO 权重。数据损失为 $\frac12\|Xw-y\|^2$，两者惩罚分别为 $\frac\lambda2\|w\|^2$ 与 $\lambda\|w\|_1$。
A_EN: Under these objective scalings, ridge gives $w_{\rm OLS}/(1+\lambda)=(1.5,-0.2)$. Lasso soft-thresholds each coordinate: $\operatorname{sign}(w_j)\max(|w_j|-\lambda,0)$, giving (2,0). These coordinatewise formulas rely on orthonormal design columns; they do not hold for arbitrary correlated columns.
A_ZH: 在题设目标函数系数下，Ridge 得到 $w_{\rm OLS}/(1+\lambda)=(1.5,-0.2)$。LASSO 对各坐标软阈值化：$\operatorname{sign}(w_j)\max(|w_j|-\lambda,0)$，得到 (2,0)。这些逐坐标公式依赖设计矩阵列正交归一，不能直接用于任意相关列。

@@ M198 | x02-regression | learn | XR2:4
Q_EN: How can ridge be interpreted as maximum a posteriori estimation?
Q_ZH: 怎样把岭回归解释为最大后验估计？
A_EN: Combine Gaussian observation noise of variance $\sigma^2$ with an independent zero-mean Gaussian prior $w_j\sim N(0,\tau^2)$. Negative log posterior, multiplied by $\sigma^2$, gives $\frac12\|Xw-y\|^2+\frac{\sigma^2}{2\tau^2}\|w\|^2$. Hence $\lambda=\sigma^2/\tau^2$ under this convention. A tighter prior means stronger shrinkage.
A_ZH: 将方差为 $\sigma^2$ 的高斯观测噪声，与独立零均值高斯先验 $w_j\sim N(0,\tau^2)$ 结合。负对数后验乘以 $\sigma^2$ 后，得到 $\frac12\|Xw-y\|^2+\frac{\sigma^2}{2\tau^2}\|w\|^2$。因此在此约定下 $\lambda=\sigma^2/\tau^2$，先验越集中，收缩越强。

@@ M199 | x02-regression | check | XR2:7-8,17; XROB:34
Q_EN: Why should feature scales and intercept treatment be specified before comparing regression coefficients?
Q_ZH: 比较回归系数前，为什么必须说明特征尺度和截距处理？
A_EN: Rescaling a feature changes the coefficient needed for the same prediction. An L1/L2 penalty on that coefficient then changes its effective cost. Standardization makes comparisons more interpretable, but fit it only on training data. Also state whether b is penalized. Coefficient magnitude alone is not a scale-free measure of importance or evidence of causation.
A_ZH: 改变特征单位后，同一预测所需的系数也会变化，施加在系数上的 L1/L2 惩罚成本随之改变。标准化可改善可比性，但只能在训练数据上拟合；还要说明是否惩罚截距 b。单看系数大小既不是与尺度无关的重要性指标，也不是因果证据。

@@ M200 | x02-regression | check | XR2:7,12,17
Q_EN: How should I choose regularization strength for a regression model?
Q_ZH: 回归模型的正则化强度应怎样选择？
A_EN: Fix a metric and compare candidate strengths on a validation split or cross-validation, fitting preprocessing separately inside each training fold. After choosing, refit using the intended training data and evaluate once on held-out test data. Training error alone favors weaker regularization and cannot settle the generalization tradeoff.
A_ZH: 固定评价指标，在验证集或交叉验证中比较候选强度，每折的预处理都仅使用该折训练数据。选定后在计划使用的训练数据上重新拟合，最后在独立测试集评价一次。训练误差通常偏好较弱正则化，无法单独决定泛化上的取舍。

@@ M201 | x02-regression | check | XR1:19; XR2:6
Q_EN: Why should code usually solve a linear system instead of explicitly forming an inverse?
Q_ZH: 为什么代码通常应解线性方程组，而不显式计算逆矩阵？
A_EN: To obtain w from $Aw=b$, a solver performs a factorization and solves for the requested right-hand side. Forming $A^{-1}$ computes more than needed and can add numerical error and cost. For least squares, QR/SVD also avoids explicitly squaring the condition number through $X^TX$. The inverse formula explains the mathematics; it need not dictate the implementation.
A_ZH: 从 $Aw=b$ 求 w 时，求解器通过矩阵分解处理所需的右端向量。显式计算 $A^{-1}$ 往往做了额外工作，并可能增加误差与成本。最小二乘中的 QR/SVD 还可避免显式形成 $X^TX$ 所带来的条件数平方效应。逆矩阵公式用于解释数学，不必照搬为实现步骤。

@@ M202 | x02-regression | check | XR1:21-24; XR2:8
Q_EN: What can a fitted regression coefficient tell me, and what can it not establish?
Q_ZH: 拟合得到的回归系数能说明什么，又不能证明什么？
A_EN: Within the fitted model, $w_j$ is the prediction change for a one-unit increase in feature j while other features are held fixed. It describes a conditional association under that model and representation. Confounding, correlated features, extrapolation and misspecification can break a causal reading. A small training error does not remove those issues.
A_ZH: 在拟合模型内部，保持其他特征不变时，第 j 个特征增加一个单位，预测值改变 $w_j$。它描述特定模型和表示下的条件关联。混杂、特征相关、外推和模型设定错误都会妨碍因果解释；较小训练误差不会自动消除这些问题。

@@ M203 | x03-robust | learn | XROB:5-7
Q_EN: Why are squared-error models sensitive to outliers?
Q_ZH: 平方误差模型为什么容易受离群点影响？
A_EN: A residual of 10 contributes 100 to squared loss, while a residual of 1 contributes only 1. A few extreme points can therefore move the fitted line substantially. Weight regularization controls coefficients, but does not replace a robust treatment of contaminated observations. First ask whether an unusual point is an error or a genuine part of the target population.
A_ZH: 残差 10 对平方损失贡献 100，而残差 1 只贡献 1，少量极端点就可能显著拉动拟合直线。参数正则化约束的是系数，不能代替对受污染观测的鲁棒处理。首先要判断异常点是错误数据，还是目标总体中真实存在的情况。

@@ M204 | x03-robust | learn | XROB:6-8
Q_EN: What are the main steps of RANSAC?
Q_ZH: RANSAC 的主要步骤是什么？
A_EN: Repeatedly sample a small subset, fit a candidate model, and count points whose residual is below a chosen inlier threshold. Keep a strong consensus model, then refit using its inliers. The method assumes that a sufficiently large coherent inlier set exists. The minimal sample size depends on the base model and on nondegenerate geometry.
A_ZH: 反复抽取小样本集，拟合候选模型，再统计残差低于阈值的内点。保留共识较强的模型，并用其内点重新拟合。它假设数据中存在足够大的、一致的内点集合。最小采样数取决于基础模型，还要求样本几何关系不退化。

@@ M205 | x03-robust | learn | XROB:8-9
Q_EN: How is the ideal RANSAC trial count related to inlier probability?
Q_ZH: 理想情况下，RANSAC 迭代次数如何由内点概率决定？
A_EN: For s>=1 independently sampled points, each an inlier with probability w, a clean sample has probability $w^s$. T independent trials succeed at least once with probability $1-(1-w^s)^T$. For $0<w<1$ and $0 < p < 1$, round $\log(1-p)/\log(1-w^s)$ upward. If w=1 one trial suffices; if w=0 no finite number succeeds. Sampling without replacement or degenerate clean samples requires a modified model.
A_ZH: 独立抽取 s>=1 个点，每个为内点的概率为 w，则全内点样本概率为 $w^s$。T 次独立试验至少成功一次的概率为 $1-(1-w^s)^T$。当 $0<w<1$、$0 < p < 1$，将 $\log(1-p)/\log(1-w^s)$ 向上取整即可。w=1 时一次足够；w=0 时有限次都不可能成功。无放回采样或全内点仍退化的情形，需要修改模型。

@@ M206 | x03-robust | worked | XROB:8-9
Q_EN: With inlier fraction 0.5, sample size 2 and target success 0.99, how many ideal RANSAC trials are needed?
Q_ZH: 内点比例 0.5、每次采样 2 点、目标成功率 0.99，理想 RANSAC 至少需要几次？
A_EN: A clean sample has probability $0.5^2=0.25$. Thus $T\ge\log(0.01)/\log(0.75)\approx16.01$, so use 17 trials. Sixteen trials give about 0.98998, slightly below 0.99. This assumes independent trials, the stated inlier rate and no geometric degeneracy.
A_ZH: 全内点样本概率为 $0.5^2=0.25$。因此 $T\ge\log(0.01)/\log(0.75)\approx16.01$，需要 17 次。16 次的成功率约为 0.98998，略低于 0.99。这里假设各轮独立、内点比例正确且不存在几何退化。

@@ M207 | x03-robust | learn | XROB:12-17
Q_EN: How can a model be nonlinear in its input yet linear in its parameters?
Q_ZH: 模型怎样做到对输入非线性，却对参数线性？
A_EN: Use fixed features $\phi(x)=(1,x,x^2)$ and predict $w^T\phi(x)$. The curve can be quadratic in x, but coefficients still enter linearly, so least squares can fit them. Higher degree expands the hypothesis class; training error need not rise, but validation error can. Choose degree together with regularization using validation.
A_ZH: 使用固定特征 $\phi(x)=(1,x,x^2)$，再预测 $w^T\phi(x)$。曲线对 x 可以是二次的，但各系数仍线性进入模型，因此可以用最小二乘拟合。提高次数扩展了模型集合，训练误差不必增加，验证误差却可能变差，应联合验证次数与正则化。

@@ M208 | x03-robust | learn | XROB:19-22
Q_EN: What is kernel ridge regression, and what is its main computational tradeoff?
Q_ZH: 什么是核岭回归？它的主要计算取舍是什么？
A_EN: For a positive-semidefinite kernel Gram matrix $K_{ij}=k(x_i,x_j)$ and $\lambda>0$, solve $(K+\lambda I)\alpha=y$ uniquely and predict $\hat y(x)=\sum_i\alpha_i k(x_i,x)$. This formula has no separately fitted intercept; centering or an intercept needs consistent extra treatment. The kernel avoids an explicit feature map, but storing a dense exact K takes n² entries.
A_ZH: 对半正定核的 Gram 矩阵 $K_{ij}=k(x_i,x_j)$ 及 $\lambda>0$，方程 $(K+\lambda I)\alpha=y$ 有唯一解，用 $\hat y(x)=\sum_i\alpha_i k(x_i,x)$ 预测。此式没有单独拟合截距；如需中心化或截距，应另作一致处理。核方法避免显式特征映射，但存储稠密精确 K 仍需 n² 个元素。

@@ M209 | x03-robust | learn | XROB:23-26
Q_EN: What does the epsilon-insensitive loss in support vector regression mean?
Q_ZH: 支持向量回归中的 epsilon 不敏感损失是什么意思？
A_EN: For residual r, the loss is $\max(0,|r|-\epsilon)$. Errors inside a tube of half-width epsilon cost zero; larger errors pay only the excess. SVR trades this loss against weight norm. Epsilon sets the tolerated error band, while C controls the penalty relative to regularization. They are different hyperparameters.
A_ZH: 对残差 r，损失为 $\max(0,|r|-\epsilon)$。半宽为 epsilon 的管道内部不计损失，超出后只惩罚超出部分。SVR 在该损失与权重范数之间取舍。Epsilon 决定容忍误差带，C 决定损失相对正则化的权重，两者作用不同。

@@ M210 | x03-robust | worked | XROB:24
Q_EN: For $\epsilon=0.2$, find epsilon-insensitive losses for residuals 0.1, -0.5 and 1.0.
Q_ZH: 当 $\epsilon=0.2$ 时，残差 0.1、-0.5、1.0 的不敏感损失分别是多少？
A_EN: Apply $\max(0,|r|-0.2)$ to get 0, 0.3 and 0.8. The sign does not matter, but the absolute magnitude does. These are data-loss terms, not the full SVR objective: the weight penalty and C still have to be included.
A_ZH: 逐项代入 $\max(0,|r|-0.2)$，得到 0、0.3 和 0.8。符号不影响结果，绝对值大小才影响。这些只是数据损失项，不是完整 SVR 目标，还必须包含权重惩罚和系数 C。

@@ M211 | x04-clustering | learn | XCL:3-9
Q_EN: How does clustering differ from classification?
Q_ZH: 聚类与分类有什么区别？
A_EN: Classification learns to predict supplied labels. Clustering groups examples using a similarity criterion without those target labels. Cluster numbers are arbitrary identifiers: exchanging labels 1 and 2 changes no partition. A geometric cluster need not equal a human semantic class, so state what structure you want the algorithm to capture.
A_ZH: 分类学习预测给定的标签，聚类则在没有这些目标标签时，根据相似性标准分组。簇编号只是标识，把 1 和 2 对调不会改变划分。几何上的簇不一定对应人类语义类别，因此应先说明希望发现哪种结构。

@@ M212 | x04-clustering | learn | XCL:13-18
Q_EN: What objective does k-means minimize?
Q_ZH: k-means 最小化什么目标？
A_EN: It minimizes within-cluster squared Euclidean distances, $\sum_i\|x_i-\mu_{z_i}\|^2$, over assignments $z_i$ and centers $\mu_k$. Each example is assigned to exactly one cluster. The objective rewards compact groups under the chosen feature scale; it is not a likelihood of arbitrary cluster shapes.
A_ZH: 它对类别分配 $z_i$ 和中心 $\mu_k$ 优化，使簇内平方欧氏距离 $\sum_i\|x_i-\mu_{z_i}\|^2$ 最小。每个样本只属于一个簇。该目标偏好当前特征尺度下紧凑的分组，并非任意形状簇的概率模型。

@@ M213 | x04-clustering | learn | XCL:15-18
Q_EN: Why does Lloyd's k-means algorithm alternate assignment and mean updates?
Q_ZH: 为什么 Lloyd k-means 算法交替进行分配和均值更新？
A_EN: With centers fixed, choose the nearest center for each point. With assignments fixed, each cluster's arithmetic mean minimizes its squared errors. Each exact step therefore cannot increase the objective. Handle empty clusters explicitly. The coupled problem is nonconvex, so this descent property does not guarantee the best global partition.
A_ZH: 固定中心时，将每点分给最近中心；固定分配时，簇内算术平均值使平方误差最小。因此每个精确步骤都不会增加目标值。空簇需要单独处理。联合问题是非凸的，所以这种下降性质不能保证得到全局最优划分。

@@ M214 | x04-clustering | worked | XCL:16-18
Q_EN: Run one k-means iteration on points (0,2,8,10), starting at centers 0 and 10.
Q_ZH: 数据点为 (0,2,8,10)，初始中心为 0 和 10，执行一次 k-means 迭代。
A_EN: Assign (0,2) to the first center and (8,10) to the second. Updated centers are 1 and 9. The squared-error objective falls from $0+4+4+0=8$ to $1+1+1+1=4$. The updated assignments remain unchanged in this example, so the next update keeps the same centers.
A_ZH: (0,2) 分入第一簇，(8,10) 分入第二簇，新中心分别为 1 和 9。平方误差从 $0+4+4+0=8$ 降到 $1+1+1+1=4$。该例更新后分配不变，下一轮中心也保持不变。

@@ M215 | x04-clustering | check | XCL:19-23
Q_EN: Why use multiple initializations, and why is lower training inertia insufficient for choosing k?
Q_ZH: 为什么要使用多个初始化？为什么不能仅凭较小训练惯性选择 k？
A_EN: Different initial centers can lead to different local optima, so use restarts. The globally minimal training inertia cannot increase when k increases: extra centers can reproduce or improve the old fit. Separate local algorithm runs need not show this monotonicity. Training inertia alone favors too many clusters; combine it with stability, an elbow, domain meaning or a justified validation criterion. None universally identifies a true k.
A_ZH: 不同初始中心可能进入不同局部最优，因此要多次重启。k 增大时，全局最小训练惯性不会增加，因为额外中心能复现或改善原拟合；但各自独立运行的局部算法结果未必单调。只看训练惯性容易偏向过多簇，应结合稳定性、肘部、领域意义或合理验证标准，没有一种方法普遍保证找出真实 k。

@@ M216 | x04-clustering | check | XCL:23,35
Q_EN: Does ordinary k-means require every cluster to contain the same number of points?
Q_ZH: 普通 k-means 是否强制每个簇包含相同数量的样本？
A_EN: No. Its objective has no equal-size constraint. Euclidean nearest-center assignments favor certain compact geometries, but cluster populations may differ greatly. Equal mixture weights and shared spherical covariance help explain a connection with Gaussian mixtures; they must not be confused with an enforced equal count. This corrects the historical slide's loose wording.
A_ZH: 不强制，目标函数中没有等大小约束。欧氏最近中心分配偏好某些紧凑形状，但各簇样本数仍可相差很大。相等混合权重和共享球形协方差可用于解释它与高斯混合的联系，却不等于强制各簇人数相同。这纠正了旧课件中不够严格的表述。

@@ M217 | x04-clustering | learn | XCL:25-28
Q_EN: What is a Gaussian mixture model?
Q_ZH: 什么是高斯混合模型？
A_EN: A GMM has density $p(x)=\sum_{k=1}^K\pi_k N(x;\mu_k,\Sigma_k)$, where $\pi_k\ge0$ and $\sum_k\pi_k=1$. A latent component selects a Gaussian, which then generates x. Means set locations and covariances set spread and orientation. The density sums components; choosing only the largest component is a different operation.
A_ZH: GMM 的密度为 $p(x)=\sum_{k=1}^K\pi_k N(x;\mu_k,\Sigma_k)$，其中 $\pi_k\ge0$ 且 $\sum_k\pi_k=1$。潜在成分先选一个高斯，再生成 x。均值决定位置，协方差决定形状和方向。密度需要把各成分相加，只取最大成分是另一种操作。

@@ M218 | x04-clustering | learn | XCL:28-30
Q_EN: What is a GMM responsibility?
Q_ZH: GMM 中的责任度是什么？
A_EN: It is the posterior component probability $r_{ik}=\pi_k N(x_i;\mu_k,\Sigma_k)/\sum_j\pi_jN(x_i;\mu_j,\Sigma_j)$. For one point, responsibilities sum to one. They are soft assignments, not Gaussian density values themselves. Compute component log scores and normalize stably when densities are very small.
A_ZH: 它是成分的后验概率 $r_{ik}=\pi_k N(x_i;\mu_k,\Sigma_k)/\sum_j\pi_jN(x_i;\mu_j,\Sigma_j)$。同一样本对各成分的责任度之和为一。它是软分配，不是高斯密度值本身。密度很小时应先计算对数分数，再稳定地归一化。

@@ M219 | x04-clustering | worked | XCL:29
Q_EN: Two GMM components have weighted densities 0.12 and 0.08 at a point. Find its responsibilities.
Q_ZH: 某点对两个 GMM 成分的加权密度为 0.12 和 0.08，责任度是多少？
A_EN: Normalize by their sum 0.20, giving (0.6,0.4). A hard assignment would choose the first component, but EM retains both weights when updating parameters. The point contributes 0.6 of an effective observation to the first component and 0.4 to the second.
A_ZH: 用总和 0.20 归一化，得到 (0.6,0.4)。硬分配会选择第一成分，但 EM 更新参数时保留两个权重。该点对第一成分贡献 0.6 个有效观测，对第二成分贡献 0.4 个。

@@ M220 | x04-clustering | learn | XCL:30
Q_EN: How does the GMM M-step update weights and means?
Q_ZH: GMM 的 M 步怎样更新混合权重和均值？
A_EN: With responsibilities fixed, set $N_k=\sum_i r_{ik}$, $\pi_k=N_k/n$, and $\mu_k=\sum_i r_{ik}x_i/N_k$. These are soft counts and weighted means. A component with zero effective count needs a defined recovery strategy rather than division by zero.
A_ZH: 固定责任度后，令 $N_k=\sum_i r_{ik}$、$\pi_k=N_k/n$，并更新 $\mu_k=\sum_i r_{ik}x_i/N_k$。它们分别是软计数和加权均值。若某个成分的有效计数为零，需要明确的恢复策略，不能直接除以零。

@@ M221 | x04-clustering | learn | XCL:30,33
Q_EN: How is a GMM covariance updated, and why can unrestricted fitting become unstable?
Q_ZH: GMM 如何更新协方差？为什么无限制拟合可能不稳定？
A_EN: Use $\Sigma_k=\sum_i r_{ik}(x_i-\mu_k)(x_i-\mu_k)^T/N_k$, with the updated mean. An unrestricted component may collapse around a point with nearly zero covariance, making Gaussian likelihood grow without bound. A covariance floor, suitable constraints and adequate data help; diagonal covariance also reduces the number of parameters.
A_ZH: 使用新均值，按 $\Sigma_k=\sum_i r_{ik}(x_i-\mu_k)(x_i-\mu_k)^T/N_k$ 更新。无约束成分可能塌缩到某个点附近、协方差接近零，使高斯似然无界增长。协方差下限、适当约束和充足数据有助于稳定，对角协方差还能减少参数量。

@@ M222 | x04-clustering | learn | XEM:12-15
Q_EN: What do the E-step and M-step optimize in general EM?
Q_ZH: 一般 EM 算法中，E 步和 M 步分别做什么？
A_EN: The E-step computes the latent-variable posterior using current parameters. The M-step maximizes the expected complete-data log likelihood under that fixed posterior. The expectation is over hidden variables, not over new observed data. Keeping the posterior fixed during the M-step is essential to the coordinate-ascent argument.
A_ZH: E 步用当前参数计算潜变量的后验分布；M 步在固定该后验的条件下，最大化完整数据对数似然的期望。这里的期望是对隐藏变量求取，并不是增加新的观测数据。M 步中固定后验，是坐标上升论证的重要条件。

@@ M223 | x04-clustering | learn | XEM:12-19
Q_EN: Why does exact EM not decrease observed-data log likelihood?
Q_ZH: 为什么精确 EM 不会降低观测数据的对数似然？
A_EN: The E-step chooses a posterior that makes a lower bound tight at the current parameters. The M-step increases that bound, and the new likelihood is at least as large as the bound. Chaining these inequalities gives nondecrease. This is not a guarantee of a global optimum, strict improvement every step, or stability under inaccurate numerical updates.
A_ZH: E 步选择后验，使似然下界在当前参数处取等号；M 步提高这个下界，而新参数的似然至少不低于下界。串联这些不等式即可证明不下降。但它不保证全局最优、每步严格提高，也不保证不准确的数值更新仍有该性质。

@@ M224 | x04-clustering | learn | XCL:31,35; XEM:21-23
Q_EN: In what sense are k-means and GMM/EM related?
Q_ZH: k-means 与 GMM/EM 在什么意义上相关？
A_EN: Both alternate assignments and representative updates. K-means uses hard nearest-center assignments; GMM EM uses posterior weights and fits a density. For equal-weight spherical Gaussians, as shared variance tends to zero a point with a unique nearest center gets hard assignment in the limit. Exactly tied nearest centers can retain split responsibility. Unit covariance alone still gives soft assignments, not ordinary k-means.
A_ZH: 两者都交替分配样本和更新代表参数。k-means 用硬最近中心分配；GMM 的 EM 用后验权重并拟合密度。对等权球形高斯，共享方差趋零时，具有唯一最近中心的点在极限下变成硬分配；最近距离恰好并列时，责任度仍可分摊。仅设单位协方差，仍是软分配，并不等于普通 k-means。

@@ M225 | x04-clustering | worked | XCL:30
Q_EN: Points are 0 and 10, with responsibilities 0.8 and 0.2 for one component. Find its updated mean and mixture weight.
Q_ZH: 两个点为 0 和 10，对某成分的责任度分别为 0.8、0.2，更新后的均值与混合权重是多少？
A_EN: The effective count is $N_k=0.8+0.2=1$. The mean is $(0.8\cdot0+0.2\cdot10)/1=2$. With two observations, the mixture weight is $N_k/2=0.5$. The mean uses responsibility-normalized values; the mixture weight divides by the total number of observations.
A_ZH: 有效计数为 $N_k=0.8+0.2=1$。均值为 $(0.8\cdot0+0.2\cdot10)/1=2$。共有两个观测，所以混合权重为 $N_k/2=0.5$。均值按责任度总和归一化，而混合权重按总观测数归一化，两个分母不能混淆。

@@ M226 | x04-clustering | check | XCL:21-23,33; XEM:21-23
Q_EN: What should I check before interpreting a clustering result as meaningful?
Q_ZH: 把聚类结果解释为有意义的结构前，应检查什么？
A_EN: Check scaling, distance/covariance assumptions, choice of k, sensitivity to initialization and whether the result is stable across reasonable data changes. Cluster identifiers can permute between runs. A visually separated projection can also hide overlap in the original space. Connect clusters to the actual learning question instead of treating every partition as a discovered truth.
A_ZH: 检查缩放、距离或协方差假设、k 的选择、初始化敏感性，以及结果在合理数据变化下是否稳定。不同运行中的簇编号可以互换；低维投影中看似分离，也可能掩盖原空间的重叠。应把簇与具体学习问题联系起来，而不是把每次划分都当作客观真相。

@@ M227 | x05-pca | learn | XSVD:3-7
Q_EN: How do feature selection and feature extraction differ?
Q_ZH: 特征选择与特征提取有什么区别？
A_EN: Feature selection keeps a subset of original coordinates. Feature extraction constructs new coordinates, for example linear combinations in PCA. Both can reduce dimension, but fewer coordinates do not automatically mean lossless compression or better prediction. PCA is unsupervised; dimensionality reduction in general can also use supervision.
A_ZH: 特征选择保留原始坐标的子集，特征提取则构造新坐标，例如 PCA 中的线性组合。两者都能降维，但坐标更少并不自动意味着无损压缩或预测更好。PCA 属于无监督方法，而广义降维也可以使用监督信息。

@@ M228 | x05-pca | learn | XSVD:18-22; NPSVD:Parameters,Returns
Q_EN: What does the singular value decomposition represent?
Q_ZH: 奇异值分解表示什么？
A_EN: For real n-by-d X, $X=U\Sigma V^T$ uses orthogonal directions and nonnegative singular values. A compact rank-r SVD keeps only positive singular values: U is n-by-r, V d-by-r, and Sigma r-by-r. NumPy `full_matrices=False` instead keeps min(n,d) directions, including zero singular values if rank-deficient. Each retained positive term $\sigma_j u_jv_j^T$ has rank one; rectangular and singular matrices also have an SVD.
A_ZH: 实数 n 行 d 列矩阵的 $X=U\Sigma V^T$ 使用正交方向和非负奇异值。秩为 r 的紧致 SVD 只保留正奇异值：U 为 n 行 r 列、V 为 d 行 r 列、Sigma 为 r 阶。NumPy 的 `full_matrices=False` 则保留 min(n,d) 个方向，秩不足时仍包含零奇异值。每个正奇异值项 $\sigma_j u_jv_j^T$ 秩为一；矩形与奇异矩阵也有 SVD。

@@ M229 | x05-pca | learn | XSVD:21-22
Q_EN: How does truncated SVD give a best low-rank approximation?
Q_ZH: 截断 SVD 怎样给出最佳低秩近似？
A_EN: Keep the k largest singular values: $X_k=U_k\Sigma_kV_k^T$. It minimizes Frobenius reconstruction error among matrices of rank at most k, with squared error $\sum_{j>k}\sigma_j^2$. This is an optimality statement for the chosen matrix norm, not automatically for classification accuracy or semantic preservation.
A_ZH: 保留最大的 k 个奇异值，得到 $X_k=U_k\Sigma_kV_k^T$。它在秩不超过 k 的矩阵中最小化 Frobenius 重构误差，平方误差为 $\sum_{j>k}\sigma_j^2$。这是针对该矩阵范数的最优性结论，不自动保证分类准确率或语义信息最好。

@@ M230 | x05-pca | check | XSVD:22; XPCA:7,16
Q_EN: Is a best rank-k approximation always unique?
Q_ZH: 最佳秩 k 近似总是唯一的吗？
A_EN: No. A tie at the truncation boundary can make multiple subspaces equally good. For $X=I_2$ and k=1, projecting onto any unit direction gives the same squared Frobenius error 1. Signs of singular/eigenvectors can also flip without changing the represented subspace. This qualifies the lecture's unqualified uniqueness claim.
A_ZH: 不是。截断位置处奇异值相同时，多个子空间可以同样好。例如 $X=I_2$、k=1 时，投影到任意单位方向的平方 Frobenius 误差均为 1。奇异向量或特征向量还可整体变号而不改变所表示的子空间。因此课件中不加条件的唯一性说法需要限定。

@@ M231 | x05-pca | learn | XPCA:9-12,17-18
Q_EN: Why is mean-centering essential for standard PCA?
Q_ZH: 标准 PCA 为什么需要先减去均值？
A_EN: PCA seeks variation around the mean. Form $X_c=X-\mathbf1\mu^T$ using the training mean. Its covariance is proportional to $X_c^TX_c$. Without centering, a large offset can dominate the second-moment matrix even if variation is small. Apply the same training mean to validation, test and later queries.
A_ZH: PCA 寻找围绕均值的变化。用训练均值构造 $X_c=X-\mathbf1\mu^T$，协方差与 $X_c^TX_c$ 成比例。不中心化时，即使波动很小，较大的整体偏移也可能主导二阶矩阵。验证、测试和后续样本都应减去同一个训练均值。

@@ M232 | x05-pca | learn | XPCA:10-16
Q_EN: Why is the first principal component an eigenvector of the covariance matrix?
Q_ZH: 为什么第一主成分是协方差矩阵的特征向量？
A_EN: A unit direction v has projected variance $v^T\Sigma v$. Maximize it subject to $v^Tv=1$. Stationarity of $v^T\Sigma v-\lambda(v^Tv-1)$ gives $\Sigma v=\lambda v$. The objective at a unit eigenvector is its eigenvalue, so select a largest-eigenvalue direction. Orthogonality constraints give later components.
A_ZH: 单位方向 v 上的投影方差为 $v^T\Sigma v$。在 $v^Tv=1$ 下最大化它，对 $v^T\Sigma v-\lambda(v^Tv-1)$ 求驻点得到 $\Sigma v=\lambda v$。单位特征向量处的目标值就是其特征值，因此选择最大特征值方向；后续分量再加正交约束。

@@ M233 | x05-pca | learn | XPCA:17-18,28-30
Q_EN: What are PCA scores and the reconstructed data matrix?
Q_ZH: 什么是 PCA 得分矩阵？怎样重构数据？
A_EN: With orthonormal component columns $V_k$, scores are $Z=X_cV_k$. Reconstruction is $\hat X=ZV_k^T+\mathbf1\mu^T$. For n samples, d features and k components, Z is n-by-k while the reconstruction is n-by-d. Projection coefficients and component vectors are different objects.
A_ZH: 若 $V_k$ 的列是正交单位主成分，得分为 $Z=X_cV_k$，重构为 $\hat X=ZV_k^T+\mathbf1\mu^T$。n 个样本、d 个特征、k 个分量时，Z 为 n 行 k 列，重构仍为 n 行 d 列。投影系数与主成分向量是不同对象。

@@ M234 | x05-pca | worked | XPCA:21,25
Q_EN: Covariance eigenvalues are (9,3,2,1). How many PCs retain at least 90% variance?
Q_ZH: 协方差特征值为 (9,3,2,1)，至少保留 90% 方差需要几个主成分？
A_EN: Total variance is 15. The first two retain $12/15=80\%$, below the target. The first three retain $14/15\approx93.33\%$, so choose three. Explained variance measures this unsupervised reconstruction criterion; a low-variance direction can still matter for predicting a label.
A_ZH: 总方差为 15。前两个保留 $12/15=80\%$，未达到目标；前三个保留 $14/15\approx93.33\%$，因此需要三个。解释方差衡量的是这一无监督重构标准，低方差方向仍可能对标签预测重要。

@@ M235 | x05-pca | learn | XPCA:28-31
Q_EN: How are PCA covariance eigenvalues related to singular values of centered data?
Q_ZH: PCA 协方差特征值与中心化数据的奇异值有什么关系？
A_EN: If $X_c=U\Sigma V^T$, then $X_c^TX_c=V\Sigma^2V^T$. Thus covariance eigenvalues are $\sigma_j^2/n$ under the lecture's 1/n convention, or $\sigma_j^2/(n-1)$ for unbiased sample covariance. Component directions and explained-variance ratios agree under either common scaling.
A_ZH: 若 $X_c=U\Sigma V^T$，则 $X_c^TX_c=V\Sigma^2V^T$。按课件的 1/n 约定，协方差特征值为 $\sigma_j^2/n$；按无偏样本协方差约定，则为 $\sigma_j^2/(n-1)$。这两种整体缩放下，主成分方向和解释方差比例相同。

@@ M236 | x05-pca | check | XPCA:9,23,26,32
Q_EN: Does decorrelation by PCA establish statistical independence or optimal prediction?
Q_ZH: PCA 去相关是否意味着统计独立或预测最优？
A_EN: No. PCA diagonalizes second-order covariance in its component coordinates. Higher-order dependence can remain, and directions with large variance need not be the most label-informative. For jointly Gaussian variables, uncorrelated coordinates are independent, but that special condition is not universal. Evaluate a PCA-based pipeline on the actual downstream task.
A_ZH: 不意味着。PCA 使主成分坐标中的二阶协方差对角化，但高阶依赖仍可能存在，高方差方向也不一定最有标签信息。联合高斯变量中，不相关意味着独立，但这一特殊条件并非普遍成立。应在实际下游任务上评价 PCA 流程。

@@ M237 | x05-pca | check | XPCA:11,23; XROB:34
Q_EN: When does changing feature units change PCA?
Q_ZH: 改变特征单位，什么时候会改变 PCA？
A_EN: Covariance-based PCA is sensitive to relative feature scales. Measuring one coordinate in millimeters rather than meters multiplies its variance by a million. Standardizing each feature is an optional modeling choice, not identical to mean-centering. Decide whether absolute variation or scale-normalized variation is meaningful, and fit both transformations on training data only.
A_ZH: 基于协方差的 PCA 对特征间相对尺度敏感。把某坐标从米改为毫米，其方差会扩大一百万倍。逐特征标准化是一种建模选择，并不等于仅减均值。应判断绝对波动还是标准化波动更有意义，并只在训练数据上拟合这些变换。

@@ M238 | x05-pca | learn | XKPCA:6-13
Q_EN: What does kernel PCA change relative to ordinary PCA?
Q_ZH: 核 PCA 相比普通 PCA 改变了什么？
A_EN: It performs PCA in an implicit feature space $\phi(x)$ using inner products $k(x_i,x_j)$. The resulting coordinates can depend nonlinearly on the original input. The kernel defines the geometry; selecting a kernel is therefore a modeling choice. The training Gram matrix is n-by-n, so exact kernel PCA can be costly for many samples.
A_ZH: 它利用内积 $k(x_i,x_j)$，在隐式特征空间 $\phi(x)$ 中执行 PCA，因此所得坐标可对原始输入呈非线性。核决定该空间的几何关系，选择核也是建模选择。训练 Gram 矩阵为 n 阶方阵，样本多时精确核 PCA 成本较高。

@@ M239 | x05-pca | learn | XKPCA:10-13
Q_EN: How is the training Gram matrix centered for kernel PCA?
Q_ZH: 核 PCA 如何中心化训练 Gram 矩阵？
A_EN: Let $H=I-\mathbf1\mathbf1^T/n$. Use $K_c=HKH$, which subtracts row/column means and adds the grand mean. This corresponds to subtracting the training mean in feature space. Subtracting the raw-input mean alone does not generally center nonlinear features. A new point must use the training centering statistics as well.
A_ZH: 令 $H=I-\mathbf1\mathbf1^T/n$，使用 $K_c=HKH$，即减去行、列均值，再加回总体均值。它对应在特征空间中减去训练均值。仅减原始输入均值通常不能使非线性特征中心化，新样本也必须使用训练时的中心化统计量。

@@ M240 | x05-pca | check | XKPCA:10-13,20
Q_EN: Why must kernel-PCA eigenvectors be normalized using their eigenvalues?
Q_ZH: 为什么核 PCA 的系数要结合特征值进行归一化？
A_EN: If $K_c a=\lambda_K a$ and $a^Ta=1$, the unit feature-space direction uses coefficients $a/\sqrt{\lambda_K}$ for positive $\lambda_K$. Its training scores are $\sqrt{\lambda_K}a$. A zero eigenvalue cannot be divided by. This distinguishes Gram-matrix eigenvectors from unit principal directions and makes the projection scale explicit.
A_ZH: 若 $K_c a=\lambda_K a$ 且 $a^Ta=1$，对于正的 $\lambda_K$，单位特征空间方向的系数为 $a/\sqrt{\lambda_K}$，训练得分为 $\sqrt{\lambda_K}a$。零特征值不能用于相除。这样才能区分 Gram 矩阵特征向量与单位主方向，并明确投影尺度。

@@ M241 | x06-networks | learn | XNN:12-21
Q_EN: How does the perceptron update a misclassified example?
Q_ZH: 感知机怎样利用误分类样本更新参数？
A_EN: For labels $y\in\{-1,+1\}$ and an augmented feature vector containing the bias coordinate, update $w\leftarrow w+\eta yx$ when the signed score is nonpositive. The update moves the score toward the correct side. Under separability and suitable bounded-data assumptions it terminates, but nonseparable data need not yield convergence.
A_ZH: 对标签 $y\in\{-1,+1\}$，把偏置也并入扩展特征；有符号分数非正时，更新 $w\leftarrow w+\eta yx$。更新使分数朝正确一侧移动。在可分、数据有界等条件下可终止，但不可分数据不保证收敛。

@@ M242 | x06-networks | worked | XNN:14-20
Q_EN: Start with w=(0,0), take x=(2,1), y=-1 and learning rate 0.5. What is one perceptron update without a bias?
Q_ZH: 无偏置时，w=(0,0)、x=(2,1)、y=-1、学习率 0.5，一次感知机更新得到什么？
A_EN: The initial signed score is zero, so apply $w_{\rm new}=w+0.5(-1)x=(-1,-0.5)$. The new raw score is -2.5 and signed score is 2.5, correctly placing this example on the negative side. Correcting this one example can still change predictions for other examples.
A_ZH: 初始有符号分数为零，因此更新为 $w_{\rm new}=w+0.5(-1)x=(-1,-0.5)$。新原始分数为 -2.5，有符号分数为 2.5，故该样本位于正确的负类一侧。但修正这个样本仍可能改变其他样本的预测。

@@ M243 | x06-networks | learn | XNN:23-25
Q_EN: Why does an MLP need nonlinear activation functions?
Q_ZH: 多层感知机为什么需要非线性激活函数？
A_EN: Composing affine layers without nonlinearities produces another affine map: $W_2(W_1x+b_1)+b_2=(W_2W_1)x+W_2b_1+b_2$. Depth alone then does not create nonlinear boundaries. An activation changes this composition, allowing hidden features to represent patterns that one affine map cannot express.
A_ZH: 没有非线性时，仿射层的复合仍是仿射映射：$W_2(W_1x+b_1)+b_2=(W_2W_1)x+W_2b_1+b_2$。仅增加深度不会产生非线性边界。激活函数改变了这一结构，使隐藏特征可以表达单个仿射映射无法表示的模式。

@@ M244 | x06-networks | learn | XNN:24,33
Q_EN: How should I check the dimensions of a fully connected layer?
Q_ZH: 怎样检查全连接层的维度？
A_EN: With row-wise batches, input X is B-by-d, weights W are d-by-h and bias b has h entries. Then $Z=XW+b$ and activated output both have shape B-by-h. Some lectures use column vectors and transpose W instead; either convention works when all products and gradients are consistent.
A_ZH: 若每行一个样本，输入 X 为 B 行 d 列，权重 W 为 d 行 h 列，偏置 b 有 h 个元素，则 $Z=XW+b$ 及激活后的输出均为 B 行 h 列。有些课件用列向量并转置 W；两种约定都可用，但乘法与梯度必须保持一致。

@@ M245 | x06-networks | worked | XNN:23-24
Q_EN: How many trainable parameters are in a dense layer from 4 inputs to 3 outputs with one bias per output?
Q_ZH: 4 个输入、3 个输出且每个输出有一个偏置的全连接层，有多少参数？
A_EN: There are $4\times3=12$ weights and 3 biases, totaling 15. Batch size does not multiply the parameter count because all examples share the same layer. A second layer has its own parameters and must be counted separately.
A_ZH: 权重数为 $4\times3=12$，再加 3 个偏置，共 15 个。批量大小不会使参数量倍增，因为不同样本共享同一层。若还有第二层，需要另外统计它自己的参数。

@@ M246 | x06-networks | learn | XNN:26-29
Q_EN: How do sigmoid and ReLU affect gradient flow?
Q_ZH: Sigmoid 和 ReLU 如何影响梯度传播？
A_EN: Sigmoid has derivative $\sigma(z)(1-\sigma(z))$, at most 1/4 and very small in saturated regions. ReLU has derivative 1 for positive inputs and 0 for negative inputs, with a convention at zero. Repeated small derivatives can weaken early-layer gradients. ReLU helps in positive regions but does not guarantee healthy gradients everywhere.
A_ZH: Sigmoid 导数为 $\sigma(z)(1-\sigma(z))$，最大为 1/4，在饱和区域很小。ReLU 对正输入的导数为 1，对负输入为 0，零点需采用约定。连续相乘的小导数会削弱前层梯度。ReLU 改善了正半轴的传播，但不保证所有位置都有良好梯度。

@@ M247 | x06-networks | check | XNN:28-30
Q_EN: What is a dying ReLU, and why might a leaky slope help?
Q_ZH: 什么是失活的 ReLU？小的负半轴斜率为什么可能有帮助？
A_EN: If a unit receives negative preactivations for all relevant training examples, its ReLU output and local gradient stay zero. Upstream parameter updates through that unit can stop. Leaky ReLU uses a small nonzero negative-side slope, allowing a gradient there. Initialization, input scaling and learning rate can also influence this problem.
A_ZH: 如果某单元对所有相关训练样本的激活前数值都为负，ReLU 的输出和局部梯度就一直为零，通过该单元更新前方参数可能停滞。Leaky ReLU 在负半轴保留小的非零斜率，使梯度仍可通过。初始化、输入尺度和学习率也会影响这一问题。

@@ M248 | x06-networks | learn | XNN:33-34; XCNN:3-5
Q_EN: What is the difference between forward propagation, backpropagation and an optimizer step?
Q_ZH: 前向传播、反向传播和优化器更新有什么区别？
A_EN: A forward pass computes intermediate activations, predictions and loss. Backpropagation applies the chain rule backward to obtain derivatives of that loss. An optimizer uses these gradients to update parameters. Backpropagation itself is a differentiation procedure, not a synonym for gradient descent or a guarantee that the next update improves generalization.
A_ZH: 前向传播计算中间激活、预测和损失；反向传播向后应用链式法则，求出损失的导数；优化器再利用梯度更新参数。反向传播本身是求导过程，不等于梯度下降，也不保证下一次更新改善泛化表现。

@@ M249 | x06-networks | worked | XCNN:4-5
Q_EN: For $f=(x+y)z$ at x=-2, y=5, z=-4, compute f and all three partial derivatives.
Q_ZH: 对 $f=(x+y)z$，取 x=-2、y=5、z=-4，求 f 和三个偏导数。
A_EN: Let q=x+y=3, giving f=-12. Since $\partial f/\partial q=z=-4$ and q has derivative 1 with respect to x and y, both $\partial f/\partial x$ and $\partial f/\partial y$ are -4. Also $\partial f/\partial z=q=3$. Multiply local derivatives along each path.
A_ZH: 先令 q=x+y=3，所以 f=-12。由于 $\partial f/\partial q=z=-4$，而 q 对 x、y 的导数均为 1，因此 f 对 x、y 的偏导数均为 -4。另有 $\partial f/\partial z=q=3$。沿每条路径相乘局部导数即可。

@@ M250 | x06-networks | learn | XCNN:15
Q_EN: Why do gradient contributions add when a value is reused in a computation graph?
Q_ZH: 计算图中同一数值被多次使用时，为什么梯度贡献要相加？
A_EN: The total derivative includes every path from that value to the loss. For $f=x^2+3x$, the two branches contribute 2x and 3, so the result is $2x+3$. Replacing a gradient with the newest branch contribution loses information. This same accumulation principle applies when a parameter is shared across convolution positions or repeated uses.
A_ZH: 总导数必须包含从该数值到损失的全部路径。例如 $f=x^2+3x$ 的两条支路分别贡献 2x 和 3，总梯度是 $2x+3$。只保留最新一条支路会丢失信息。同样的累加原则也适用于卷积位置之间或多次使用之间共享的参数。

@@ M251 | x06-networks | learn | XCNN:3-15
Q_EN: For $Z=XW+b$ with upstream gradient G, what are the dense-layer gradients under the row-batch convention?
Q_ZH: 对 $Z=XW+b$，若上游梯度为 G，在逐行存样本的约定下各梯度是什么？
A_EN: The gradients are $\nabla_W L=X^TG$, $\nabla_X L=GW^T$, and $\nabla_b L=\sum_i G_{i,:}$. Check their shapes against W, X and b. If an activation follows Z, G must already include that activation's local derivative. A mean-loss reduction must be reflected consistently in G.
A_ZH: 梯度为 $\nabla_W L=X^TG$、$\nabla_X L=GW^T$，偏置梯度为 $\nabla_b L=\sum_i G_{i,:}$。形状应分别与 W、X、b 对应。若 Z 后还有激活函数，G 必须已包含其局部导数；损失取平均时，相应缩放也应体现在 G 中。

@@ M252 | x06-networks | learn | XNN:33,35; XOPT:4-5
Q_EN: How should the output layer and loss match a neural-network task?
Q_ZH: 神经网络的输出层与损失应如何匹配任务？
A_EN: A single-label multiclass task commonly uses class logits with softmax cross-entropy. A real-valued regression task can use a linear output with squared error. Binary and multi-label tasks need their own target and probability conventions. Do not add an activation merely because it appeared in another example; specify the target domain and the loss's expected input.
A_ZH: 单标签多分类常用类别 logits 与 softmax 交叉熵；实数回归可用线性输出和平方误差。二分类与多标签任务还需各自的目标编码与概率约定。不能因为别的例子用了某激活就照搬，应明确目标取值范围，以及损失函数希望接收什么输入。

@@ M253 | x06-networks | check | XNN:40
Q_EN: What does the universal approximation theorem guarantee, and what does it leave open?
Q_ZH: 通用逼近定理保证什么，又没有保证什么？
A_EN: Under suitable activation assumptions, a sufficiently wide single hidden layer can approximate a continuous function on a compact domain to arbitrary prescribed accuracy. It is an existence statement. It does not require an actually infinite network for a fixed tolerance, and does not promise an efficient size, successful training, or generalization from limited data.
A_ZH: 在适当激活函数条件下，足够宽的单隐藏层网络可以在紧致区域内，将连续函数逼近到任意给定精度。这是存在性结论：对固定误差容限，并不要求实际使用无限网络，也不保证网络规模高效、训练一定成功，或少量数据下能够泛化。

@@ M254 | x06-networks | check | XNN:38-39; XREG:39-48
Q_EN: Why is fitting a tiny training subset useful for debugging a neural network?
Q_ZH: 为什么让神经网络拟合一个很小的训练子集，有助于调试？
A_EN: With a capable model and weak regularization, failure to fit a tiny clean subset can expose label, shape, loss or gradient bugs. Success checks basic optimization, not generalization. Afterwards restore the actual split and regularization. A small train–validation gap alone does not prove underfitting; both scores and the task's attainable error matter.
A_ZH: 对有足够容量、正则化较弱的模型，若连很小的干净子集都拟合不了，可能暴露标签、形状、损失或梯度错误。拟合成功只检查基础优化，不证明泛化；之后应恢复正式划分与正则化。训练和验证差距小也不能单独证明欠拟合，还要看两者水平和任务可达到的误差。

@@ M255 | x07-cnn | learn | XCNN:17-25
Q_EN: What does a convolutional filter compute at one image location?
Q_ZH: 卷积滤波器在图像的一个位置计算什么？
A_EN: For ordinary dense convolution, one filter spans a local spatial window and all input channels. It takes a weighted sum of that patch plus a bias, producing one output value. Sliding the same filter produces one feature map; multiple filters produce multiple output channels. This combines local connectivity with parameter sharing.
A_ZH: 普通非分组卷积的一个滤波器覆盖局部空间窗口和全部输入通道，对该图像块加权求和并加偏置，产生一个输出数值。同一滤波器滑动形成一张特征图，多个滤波器形成多个输出通道，兼具局部连接和参数共享。

@@ M256 | x07-cnn | learn | XCNN:23-29
Q_EN: What is the output size of a 2D convolution along one spatial axis?
Q_ZH: 二维卷积沿某一空间轴的输出尺寸如何计算？
A_EN: With input length L, kernel size k, padding p on each side, stride s and dilation d, output length is $\lfloor(L+2p-d(k-1)-1)/s\rfloor+1$. The lecture's basic examples use d=1. Compute height and width separately. Padding called “same” preserves size at stride 1 under the appropriate padding convention, not at every stride.
A_ZH: 输入长度为 L，核大小 k，两侧各填充 p，步长 s，膨胀率 d 时，输出长度为 $\lfloor(L+2p-d(k-1)-1)/s\rfloor+1$。课件基础例子取 d=1。高度、宽度应分别计算；“same” 在步长 1 且采用相应填充约定时保持尺寸，并非任意步长都保持不变。

@@ M257 | x07-cnn | worked | XCNN:20-25
Q_EN: A 32×32 RGB input passes through six 5×5 filters, stride 1, no padding. What are the output shape and parameter count?
Q_ZH: 32×32 RGB 输入经过 6 个 5×5 滤波器，步长 1、无填充，输出形状和参数量是多少？
A_EN: Each spatial output size is $32-5+1=28$, giving 28×28×6 under height-width-channel notation. Each filter has $5\cdot5\cdot3=75$ weights and one bias, so there are $6(75+1)=456$ trainable parameters. The 28×28 positions reuse these weights rather than each having a separate filter.
A_ZH: 每个空间维度为 $32-5+1=28$，按高、宽、通道记法，输出是 28×28×6。每个滤波器有 $5\cdot5\cdot3=75$ 个权重和一个偏置，总计 $6(75+1)=456$ 个参数。28×28 个位置共享这些权重，不是每个位置另设滤波器。

@@ M258 | x07-cnn | learn | XCNN:20-30
Q_EN: What is the difference between translation equivariance and translation invariance?
Q_ZH: 平移等变与平移不变有什么区别？
A_EN: Equivariance means shifting the input shifts the output correspondingly. Invariance means the output stays unchanged. Shared convolution supports equivariance under appropriate boundary and sampling assumptions; pooling or aggregation can add limited invariance. Padding, striding and finite boundaries can break exact shift relationships, so a CNN is not automatically invariant to all translations.
A_ZH: 等变表示输入平移后，输出也相应平移；不变表示输出保持不变。共享卷积在适当边界和采样条件下支持等变，池化或聚合可以增加有限的不变性。填充、步长和有限边界会破坏精确对应，因此 CNN 不会自动对所有平移不变。

@@ M259 | x07-cnn | learn | XCNN:27-29
Q_EN: How do stride and padding affect a convolution?
Q_ZH: 步长与填充怎样影响卷积？
A_EN: Stride sets how far the window moves between outputs and can downsample the feature map. Padding supplies values outside the observed image, controlling output size and boundary behavior. Zero, reflection and replication padding encode different boundary assumptions. Padding does not create newly observed image content.
A_ZH: 步长决定窗口在相邻输出间移动多远，并可对特征图降采样。填充为观测图像之外提供数值，影响输出尺寸和边界行为。零填充、镜像填充和复制填充采用不同边界假设。填充值并不是新观测到的图像内容。

@@ M260 | x07-cnn | learn | XCNN:29
Q_EN: How does max pooling differ from a learned convolution?
Q_ZH: 最大池化与可学习卷积有什么区别？
A_EN: Max pooling takes the largest value in each window and usually has no learned weights. A convolution applies learned weighted sums. Pooling reduces spatial resolution and can discard exact position information. During backpropagation, a max operation routes gradient to a selected maximizing entry, with a convention for ties.
A_ZH: 最大池化取窗口内最大值，通常没有可学习权重；卷积则执行可学习的加权和。池化减少空间分辨率，也可能丢失精确位置信息。反向传播时，最大值操作把梯度传给选定的最大元素，出现并列最大值时需采用约定。

@@ M261 | x07-cnn | worked | XCNN:26
Q_EN: What is the receptive-field size of two consecutive 3×3 convolutions with stride 1 and no dilation?
Q_ZH: 连续两个 3×3 卷积，步长均为 1、无膨胀时，理论感受野多大？
A_EN: The first output sees a 3×3 input region. A 3×3 neighborhood of those outputs spans a 5×5 input region, so the second layer has a 5×5 theoretical receptive field. This is the set of possible dependencies; it does not mean every input pixel has equal influence on the final value.
A_ZH: 第一层输出看到一个 3×3 区域；第二层使用第一层的 3×3 邻域，合起来覆盖原输入的 5×5 区域，因此理论感受野为 5×5。它表示可能影响输出的范围，不意味着其中每个输入像素的实际影响都相等。

@@ M262 | x07-cnn | worked | XCNN:38-45
Q_EN: Compute full discrete convolution of sequences (3,1,2) and (3,2,1), both starting at index 0.
Q_ZH: 两个序列 (3,1,2) 与 (3,2,1) 均从下标 0 开始，求完整离散卷积。
A_EN: Using $y[n]=\sum_k x[k]h[n-k]$, the result is (9,9,11,5,2). For example, $y[2]=3\cdot1+1\cdot2+2\cdot3=11$. Full output length is $3+3-1=5$. Specifying the starting indices matters because shifting either sequence shifts the convolution's index locations.
A_ZH: 使用 $y[n]=\sum_k x[k]h[n-k]$，结果为 (9,9,11,5,2)。例如 $y[2]=3\cdot1+1\cdot2+2\cdot3=11$。完整输出长度为 $3+3-1=5$。必须说明起始下标，因为移动任何输入序列都会移动输出的下标位置。

@@ M263 | x07-cnn | check | XCNN:20-25,32-39
Q_EN: Why is a deep-learning operation often called convolution even when it does not flip the filter?
Q_ZH: 为什么深度学习中不翻转滤波器的运算也常被称为卷积？
A_EN: Mathematical convolution uses a reversed kernel in the summation; the usual neural-network implementation computes cross-correlation. Since filter coefficients are learned, reversing the parameterization still gives the same set of possible filters. For hand calculations with a specified filter, however, convolution and correlation can produce different numbers, so state the convention.
A_ZH: 数学卷积的求和含核的翻转，而神经网络常见实现执行的是互相关。由于滤波器系数由训练学习，翻转参数化后仍对应同一组可表达滤波器。但对指定核进行手算时，卷积与互相关可能得到不同数值，因此必须说明约定。

@@ M264 | x07-cnn | check | XCNN:47-50
Q_EN: Why must channel order and input shape be checked before feeding images to a CNN?
Q_ZH: 输入 CNN 前为什么必须检查通道顺序和数据形状？
A_EN: A batch may use (B,C,H,W) or (B,H,W,C). Confusing them can treat spatial positions as channels or trigger shape errors. Grayscale still has a channel dimension. Normalization must also match training. Flattening is appropriate only at a layer expecting vectors, not as an automatic preprocessing step for convolution.
A_ZH: 图像批次可能按 (B,C,H,W) 或 (B,H,W,C) 排列，混淆后会把空间位置当成通道，或引起形状错误。灰度图同样需要通道维度，归一化也必须与训练一致。只有期望向量输入的层才应展平，不能默认在卷积前先把图像展开。

@@ M265 | x08-training | learn | XOPT:4-8; XREG:33
Q_EN: How do batch gradient descent, mini-batch SGD, an iteration and an epoch differ?
Q_ZH: 批量梯度下降、小批量 SGD、迭代和 epoch 有何区别？
A_EN: Full-batch descent uses every training example for one gradient. Mini-batch SGD uses a subset, giving cheaper but noisier updates. An iteration usually means one parameter update; an epoch is one pass through the training set. If n=1,000 and batch size is 100, one full pass has ten updates when every sample is used once.
A_ZH: 全批量下降用全部训练样本计算一次梯度，小批量 SGD 用子集计算，单次更便宜但噪声更大。一次迭代通常指一次参数更新，一个 epoch 指遍历一遍训练集。若 n=1,000、批量大小为 100 且每个样本使用一次，则一遍包含十次更新。

@@ M266 | x08-training | learn | XOPT:9-17
Q_EN: What does momentum add to SGD?
Q_ZH: Momentum 为 SGD 增加了什么？
A_EN: Maintain velocity $v_{t+1}=\rho v_t-\eta g_t$ and update $\theta_{t+1}=\theta_t+v_{t+1}$. Past gradients influence the direction, which can reduce zigzagging and accelerate motion along persistent directions. The sign convention for v must be consistent. Momentum can still overshoot if the learning rate or velocity is too large.
A_ZH: 保存速度 $v_{t+1}=\rho v_t-\eta g_t$，再更新 $\theta_{t+1}=\theta_t+v_{t+1}$。过去梯度会影响方向，有助于减轻来回振荡，并沿持续方向加速。速度的符号约定必须一致；学习率或速度过大时，动量仍可能导致越过最优区域。

@@ M267 | x08-training | learn | XOPT:18-22
Q_EN: How do AdaGrad and RMSProp adapt coordinatewise step sizes?
Q_ZH: AdaGrad 和 RMSProp 怎样调整每个坐标的步长？
A_EN: AdaGrad accumulates past squared gradients, while RMSProp uses an exponential moving average of them. Each scales a coordinate's gradient by the inverse square root of its accumulator plus a stabilizer. AdaGrad's accumulator grows continually, potentially shrinking steps too far. RMSProp forgets old history gradually. Neither method removes the need to choose a global learning rate.
A_ZH: AdaGrad 累加历史梯度平方，RMSProp 则使用梯度平方的指数移动平均。两者都用相应累积量平方根的倒数，加数值稳定项后，对各坐标梯度缩放。AdaGrad 持续累加，步长可能过度缩小；RMSProp 逐渐遗忘旧历史。两者仍需选择全局学习率。

@@ M268 | x08-training | learn | XOPT:23-24
Q_EN: What are Adam's two moment estimates and bias corrections?
Q_ZH: Adam 的两个矩估计及偏差修正是什么？
A_EN: Adam tracks $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ and $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$, elementwise. Starting at zero biases early estimates, so use $\hat m_t=m_t/(1-\beta_1^t)$ and $\hat v_t=v_t/(1-\beta_2^t)$. Update by $-\eta\hat m_t/(\sqrt{\hat v_t}+\epsilon)$. These estimates do not guarantee a global optimum.
A_ZH: Adam 逐元素维护 $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ 和 $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$。从零初始化会使早期估计偏小，因此用 $\hat m_t=m_t/(1-\beta_1^t)$、$\hat v_t=v_t/(1-\beta_2^t)$ 修正，再按 $-\eta\hat m_t/(\sqrt{\hat v_t}+\epsilon)$ 更新。这些估计不保证全局最优。

@@ M269 | x08-training | check | XOPT:25-26
Q_EN: Why is AdamW's decoupled weight decay different from simply adding L2 loss to Adam?
Q_ZH: 为什么 AdamW 的解耦权重衰减不同于直接给 Adam 加 L2 损失？
A_EN: Adding L2 loss puts a term proportional to w into the gradient, where Adam's adaptive moments rescale it. Decoupled decay instead shrinks w separately, for example by a factor $1-\eta\lambda$, alongside the adaptive gradient update. The two operations generally differ for adaptive optimizers. Record which parameters receive decay.
A_ZH: 加 L2 损失会把与 w 成比例的项并入梯度，随后被 Adam 的自适应矩估计重新缩放。解耦衰减则在自适应梯度更新之外，单独按例如 $1-\eta\lambda$ 的比例缩小 w。对自适应优化器，两种操作通常不同，还应记录哪些参数接受衰减。

@@ M270 | x08-training | check | XREG:34
Q_EN: What does fan-in mean in He initialization for an ordinary convolution?
Q_ZH: 普通卷积采用 He 初始化时，fan-in 指什么？
A_EN: For a kH-by-kW filter with Cin input channels, fan-in is $k_Hk_WC_{\rm in}$, not just Cin. A common zero-mean Gaussian initialization for ReLU has variance $2/\text{fan-in}$. The goal is to manage activation/gradient scale. Identically initialized hidden units can remain symmetric; biases alone may still legitimately start at zero.
A_ZH: 对 kH×kW 的核、Cin 个输入通道，fan-in 是 $k_Hk_WC_{\rm in}$，不只是 Cin。用于 ReLU 的一种常见零均值高斯初始化，其方差为 $2/\text{fan-in}$，目的是控制激活与梯度尺度。隐藏单元完全相同地初始化可能保持对称，但偏置本身仍可以合理地初始化为零。

@@ M271 | x08-training | learn | XREG:15-19
Q_EN: In inverted dropout, should surviving activations be divided by the drop probability or keep probability?
Q_ZH: Inverted dropout 中，保留下来的激活应除以丢弃概率还是保留概率？
A_EN: Divide by the keep probability q. With mask $m\sim\mathrm{Bernoulli}(q)$, use $\tilde h=mh/q$, giving $E[\tilde h]=h$. At ordinary inference, disable masking and use h. If dropout rate is 0.2, q=0.8 and a surviving value is multiplied by 1.25. Mixing up drop and keep probabilities gives incorrect scaling.
A_ZH: 应除以保留概率 q。若掩码 $m\sim\mathrm{Bernoulli}(q)$，则使用 $\tilde h=mh/q$，从而 $E[\tilde h]=h$。通常推理时关闭掩码，直接使用 h。若丢弃率为 0.2，则 q=0.8，保留值乘 1.25。混淆丢弃概率与保留概率会导致缩放错误。

@@ M272 | x08-training | learn | XREG:21-24
Q_EN: How do batch normalization and layer normalization choose their statistics?
Q_ZH: Batch normalization 和 layer normalization 如何选择归一化统计量？
A_EN: BN normally computes per-feature or per-channel statistics using a batch, also aggregating spatial positions for CNN features. LN normalizes a specified feature set within each example or token. Both can learn scale and shift. The axes are part of the definition; saying only “normalize the tensor” is insufficient.
A_ZH: BN 通常跨批量计算逐特征或逐通道统计量，对 CNN 特征还会聚合空间位置。LN 则在每个样本或 token 内，对指定的特征集合归一化。两者都可学习缩放与平移参数。归一化轴属于定义的一部分，仅说“归一化张量”是不够的。

@@ M273 | x08-training | check | XREG:17-24
Q_EN: Why can train/evaluation mode change a neural network's predictions even with fixed weights?
Q_ZH: 即使权重固定，训练和评估模式为什么仍可能产生不同预测？
A_EN: Dropout samples masks in training, while ordinary evaluation disables them. BN typically uses current-batch statistics in training and accumulated running statistics in evaluation. With fixed statistics, BN is an affine transform. Disabling gradient recording and switching evaluation mode are separate actions; one does not automatically imply the other.
A_ZH: Dropout 在训练中随机采样掩码，通常评估时关闭；BN 训练时使用当前批量统计量，评估时一般使用累计运行统计量。固定统计量后，BN 是仿射变换。关闭梯度记录和切换评估模式是两个不同操作，不能认为做一个就自动完成另一个。

@@ M274 | x08-training | check | XREG:3-11
Q_EN: What makes a data augmentation valid for a learning task?
Q_ZH: 怎样判断一种数据增强是否适合当前任务？
A_EN: It should preserve the intended label, or transform the label consistently. A crop may remove the only target object; flipping an image may require updating boxes or keypoints. Mixing samples may require mixing targets. Augmentation expresses assumptions about valid variation and should be checked against the task, rather than copied blindly from another dataset.
A_ZH: 增强应保留目标标签，或相应地正确变换标签。裁剪可能移除唯一目标物体，翻转可能需要同步修改框或关键点；混合样本也可能需要混合目标。增强表达了对合理变化的假设，应结合任务检查，而不能机械照搬其他数据集的做法。

@@ M275 | x08-training | learn | XREG:12-14,35-36
Q_EN: How do early stopping and a learning-rate schedule differ?
Q_ZH: 提前停止与学习率计划有什么区别？
A_EN: A schedule changes update step sizes during training. Early stopping selects when to stop, often restoring the checkpoint with the best validation metric. Both affect the resulting fit but act through different mechanisms. Keep the test set outside these choices, and do not confuse the last checkpoint with the best validated one.
A_ZH: 学习率计划改变训练过程中的更新步长，提前停止则选择何时结束，通常恢复验证指标最好的检查点。两者都影响最终拟合，但机制不同。测试集不应参与这些选择，也不能把最后保存的检查点直接当作验证效果最好的一个。

@@ M276 | x08-training | learn | XREG:37-44
Q_EN: How does feature extraction with a pretrained network differ from fine-tuning?
Q_ZH: 用预训练网络做特征提取，与微调有什么区别？
A_EN: Feature extraction freezes the backbone and trains a new predictor on its outputs. Fine-tuning updates some or all pretrained weights using the new task. Data size, domain shift and compute influence the choice. Use a held-out validation protocol and record frozen layers, learning rates and preprocessing; pretraining does not establish accuracy on the new domain.
A_ZH: 特征提取冻结骨干，只在其输出上训练新预测器；微调则根据新任务更新部分或全部预训练权重。数据量、领域差异与计算资源会影响选择。应保留验证流程，并记录冻结层、学习率和预处理；预训练本身不证明模型在新领域中的准确性。

@@ M277 | x09-vision | learn | XVIS:3,21,29,34
Q_EN: How do image classification, detection, semantic segmentation and instance segmentation differ?
Q_ZH: 图像分类、目标检测、语义分割和实例分割有什么区别？
A_EN: Classification predicts image-level categories. Detection adds object locations, often boxes. Semantic segmentation assigns a class to each pixel. Instance segmentation also distinguishes separate objects of the same class. Two adjacent people may share one semantic label while requiring two instance masks. These tasks need different annotations and evaluation rules.
A_ZH: 分类预测图像级类别；检测增加目标位置，常用边界框表示；语义分割为每个像素赋类别；实例分割还区分同类的不同个体。两个相邻的人可具有相同语义标签，却需要两个实例掩码。这些任务所需标注和评价规则不同。

@@ M278 | x09-vision | learn | XVIS:23-27
Q_EN: What changed from R-CNN to Fast R-CNN and Faster R-CNN?
Q_ZH: R-CNN、Fast R-CNN 到 Faster R-CNN 的主要变化是什么？
A_EN: R-CNN processes proposed regions separately. Fast R-CNN shares image feature computation and extracts region features from a shared map. Faster R-CNN adds a learned region-proposal network. This separates two questions: where candidate regions come from and how feature computation is shared. It is a historical architectural progression, not a current speed ranking.
A_ZH: R-CNN 分别处理候选区域；Fast R-CNN 共享整图特征计算，再从共享特征图中提取区域特征；Faster R-CNN 加入可学习的区域建议网络。应区分候选区域如何产生，以及特征计算如何共享。这是历史架构演进，不是当前模型速度排名。

@@ M279 | x09-vision | learn | XVIS:11-12
Q_EN: What is a residual connection, and why must its tensor dimensions match?
Q_ZH: 什么是残差连接？为什么相加的张量维度必须匹配？
A_EN: A residual block predicts a change F(x) and forms $y=x+F(x)$. The identity path provides a direct information/gradient route. If dimensions differ, use a specified projection or other compatible transformation. The connection aids optimization but does not guarantee that any deeper network will improve validation performance.
A_ZH: 残差块预测变化 F(x)，并形成 $y=x+F(x)$。恒等路径提供直接的信息和梯度通道。维度不同时，需要明确的投影或其他兼容变换。残差连接有助于优化，但不能保证任意更深网络都会提高验证性能。

@@ M280 | x09-vision | learn | XVIS:31-35
Q_EN: Why is a segmentation model's output structurally different from a classifier's output?
Q_ZH: 为什么分割模型的输出结构不同于分类模型？
A_EN: A classifier can reduce an image to one category vector. Segmentation must retain or recover spatial alignment so predictions correspond to individual pixels or regions. Upsampling, skip connections and region-alignment operations serve different spatial roles. Increasing output resolution alone does not recover detail that the model never learned.
A_ZH: 分类器可以把图像压缩为一个类别向量，分割则必须保留或恢复空间对应，使预测关联到具体像素或区域。上采样、跳跃连接和区域对齐分别承担不同空间作用。仅提高输出分辨率，并不能恢复模型从未学到的细节。

@@ M281 | x09-vision | learn | XLOW:4-8,10,14,17
Q_EN: How does $y=Ax+\epsilon$ unify several image restoration problems?
Q_ZH: $y=Ax+\epsilon$ 如何统一描述多种图像恢复问题？
A_EN: x is the unknown clean signal, y the observation, A the degradation operator and epsilon the noise. Denoising uses A=I; deblurring uses a blur operator; super-resolution may combine blur and downsampling. Recovering x can be underdetermined, so data fidelity must be combined with assumptions or learned priors about plausible images.
A_ZH: x 是未知干净信号，y 是观测，A 是退化算子，epsilon 为噪声。去噪取 A=I，去模糊使用模糊算子，超分辨率可结合模糊与降采样。恢复 x 可能欠定，因此需要把数据一致性与对合理图像的假设或学习到的先验结合。

@@ M282 | x09-vision | learn | XLOW:20-23
Q_EN: What tradeoff does learned image compression optimize?
Q_ZH: 学习式图像压缩优化什么取舍？
A_EN: A rate–distortion objective such as $R+\lambda D$ trades expected coding cost R against reconstruction distortion D. A learned latent representation must ultimately be quantized and coded. A small latent tensor does not automatically imply a short bitstream because entropy and precision also matter. State the distortion metric and rate unit.
A_ZH: 例如 $R+\lambda D$ 的率失真目标，在预期编码成本 R 与重构失真 D 之间取舍。学习得到的潜表示最终仍需量化和编码。潜张量尺寸小不自动意味着码流短，因为熵和精度也很重要，必须说明失真指标与码率单位。

@@ M283 | x09-vision | check | XLOW:31-44
Q_EN: Why can two reconstructions with similar MSE look perceptually different?
Q_ZH: 为什么两个重构的 MSE 接近，视觉感受却可能不同？
A_EN: MSE measures squared pixel-value differences, not perceived structure or texture directly. SSIM and learned feature losses emphasize other properties, so rankings can differ. Squared Euclidean distance is not itself a metric. For N compared scalar values, RMSE is Euclidean distance divided by sqrt(N); when averaging all RGB channel values, N counts channels as well as pixel locations.
A_ZH: MSE 衡量像素数值的平方差，并不直接衡量感知结构或纹理。SSIM 和学习到的特征损失强调其他属性，因此排序可能不同。平方欧氏距离本身不是度量。比较 N 个标量数值时，RMSE 为欧氏距离除以 sqrt(N)；若对全部 RGB 通道值取平均，N 需同时计入通道数和像素位置。

@@ M284 | x09-vision | check | XVIS:37-40
Q_EN: What can repeated reuse of a fixed test set hide when comparing vision models?
Q_ZH: 反复使用同一固定测试集比较视觉模型，可能掩盖什么？
A_EN: Model development can adapt indirectly to the benchmark, while rare failures and distribution shifts remain poorly sampled. The lecture's maximum-discrepancy idea seeks informative cases where models disagree, then evaluates those cases with appropriate reference judgments. A high average benchmark score and a useful failure analysis answer different questions.
A_ZH: 模型开发可能间接适应固定基准，而罕见失败和分布变化仍缺乏充分采样。课件中的最大差异思路寻找模型分歧明显、有信息量的样本，再结合适当参考判断评价。较高平均基准分数与有价值的失败分析，回答的是不同问题。

@@ M285 | x10-generative | learn | XGEN:3-9
Q_EN: How can a model generate samples without evaluating their exact density?
Q_ZH: 模型怎样在不计算精确密度的情况下生成样本？
A_EN: An implicit generator transforms a simple random input z into $x=G_\theta(z)$. This defines a distribution through sampling, even when $p_\theta(x)$ is hard to evaluate. A tractable likelihood and an efficient sampler are separate properties. Being able to draw realistic examples does not by itself prove coverage of the full data distribution.
A_ZH: 隐式生成器把简单随机输入 z 转成 $x=G_\theta(z)$，即使难以计算 $p_\theta(x)$，也能通过采样定义一个分布。易计算似然与高效采样是不同性质。能够生成逼真样本，本身不能证明覆盖了完整数据分布。

@@ M286 | x10-generative | learn | XGEN:11-15
Q_EN: What are the two roles in a GAN?
Q_ZH: GAN 中的两个模型分别承担什么角色？
A_EN: The generator maps noise to synthetic data. The discriminator learns to distinguish real training examples from generated ones. Training alternates their updates, so each model changes the learning problem faced by the other. The discriminator's “real” score is a training signal, not a general certificate of factual truth or sample quality.
A_ZH: 生成器把噪声映射成合成数据，判别器学习区分真实训练样本与生成样本。训练交替更新两者，每个模型都会改变另一方面对的学习问题。判别器的“真实”分数是训练信号，不是对事实真实性或样本质量的通用保证。

@@ M287 | x10-generative | learn | XGEN:13-15
Q_EN: Write the original GAN minimax objective with its optimization directions.
Q_ZH: 写出原始 GAN 的极小极大目标，并说明优化方向。
A_EN: One convention is $\min_G\max_D E_{x\sim p_{\rm data}}\log D(x)+E_z\log(1-D(G(z)))$. D maximizes correct discrimination, while G minimizes the expression to make generated samples harder to reject. If the expression is negated and called discriminator loss, min/max directions reverse. Compare the algebraic sign before declaring two formulas inconsistent.
A_ZH: 一种约定为 $\min_G\max_D E_{x\sim p_{\rm data}}\log D(x)+E_z\log(1-D(G(z)))$。D 最大化正确区分能力，G 最小化该式，使生成样本更难被拒绝。若整体取负并称为判别器损失，极小与极大方向会反转，比较公式时应先核对符号。

@@ M288 | x10-generative | check | XGEN:13-15,19-20
Q_EN: Why can alternating GAN optimization be difficult even if each network uses ordinary gradient updates?
Q_ZH: 即使两个网络都使用普通梯度更新，GAN 交替优化为什么仍可能困难？
A_EN: The target changes whenever the other player updates, so this is not ordinary descent on one fixed objective for both networks. An overly strong discriminator can provide unhelpful gradients, and updates can oscillate. Loss values must be interpreted with generated samples and distributional coverage; a low loss for one player does not alone establish a well-trained generator.
A_ZH: 另一方一更新，当前目标就会变化，因此不能把两者都视为在同一个固定目标上做普通下降。过强判别器可能提供不利于学习的梯度，更新也可能振荡。解释损失时还要结合生成样本和分布覆盖，某一方损失低并不能单独证明生成器训练良好。

@@ M289 | x10-generative | learn | XGEN:19-26
Q_EN: What is mode collapse, and does conditioning automatically prevent it?
Q_ZH: 什么是模式坍塌？加入条件后能自动避免吗？
A_EN: Mode collapse means generated samples cover too few modes or varieties of the target distribution. A generator may produce plausible but repetitive outputs. Conditioning asks for samples associated with c, such as a class, but diversity can still collapse within that condition. Evaluate both quality and coverage instead of selecting a few attractive examples.
A_ZH: 模式坍塌表示生成样本只覆盖目标分布中过少的模式或变化，样本可能看起来合理却高度重复。条件生成要求产生与 c（例如类别）相关的样本，但同一条件内部仍可能坍塌。应同时评价质量与覆盖度，不能只挑几张好看的例子。

@@ M290 | x10-generative | learn | XGEN:33-36
Q_EN: What is the forward noising process in a DDPM?
Q_ZH: DDPM 的前向加噪过程是什么？
A_EN: Choose a variance schedule with $0<\beta_t<1$ and use $q(x_t|x_{t-1})=N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)$. Signal is attenuated while Gaussian noise is added. This forward process is specified by the schedule; the reverse denoising model is learned. Increasing beta linearly is one schedule choice, not the definition of diffusion.
A_ZH: 选取满足 $0<\beta_t<1$ 的方差计划，并令 $q(x_t|x_{t-1})=N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)$。信号逐步衰减，同时加入高斯噪声。前向过程由计划指定，反向去噪模型则需要学习。Beta 线性增长只是一种计划选择，不是扩散模型的定义。

@@ M291 | x10-generative | learn | XGEN:35-39
Q_EN: How can training sample a noisy state at timestep t without simulating every earlier step?
Q_ZH: 训练时怎样不逐步模拟前面所有时刻，直接得到第 t 步的带噪状态？
A_EN: Define $\alpha_t=1-\beta_t$ and $\bar\alpha_t=\prod_{s=1}^t\alpha_s$. Then sample $\epsilon\sim N(0,I)$ and set $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$. The product, not a sum, accumulates signal retention. When bar-alpha is near zero, x_t is approximately standard Gaussian under the model.
A_ZH: 定义 $\alpha_t=1-\beta_t$、$\bar\alpha_t=\prod_{s=1}^t\alpha_s$，采样 $\epsilon\sim N(0,I)$ 后，直接令 $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$。信号保留比例通过乘积而非求和累计。Bar-alpha 接近零时，模型中的 x_t 近似标准高斯。

@@ M292 | x10-generative | check | XGEN:37-39; XDDPM:2-3
Q_EN: Is the reverse conditional $q(x_{t-1}\mid x_t)$ exactly Gaussian merely because forward diffusion adds Gaussian noise?
Q_ZH: 正向扩散加入高斯噪声，是否就意味着反向条件分布 $q(x_{t-1}\mid x_t)$ 精确为高斯？
A_EN: No. The data distribution need not be Gaussian. In DDPM, the tractable posterior conditioned on both x_t and x_0 is Gaussian, while the reverse model conditioned only on x_t is a learned Gaussian approximation/parameterization. Noise prediction with time input trains its mean-related parameters. This corrects the historical slide's overly broad joint-Gaussian justification.
A_ZH: 不能，数据分布本身未必是高斯。DDPM 中同时给定 x_t 和 x_0 的可计算后验是高斯；仅给定 x_t 的反向模型，则采用学习到的高斯近似或参数化。带时间输入的噪声预测用于学习其均值相关参数。这纠正了旧课件中过于宽泛的“联合高斯”理由。

@@ M293 | x10-generative | learn | XGEN:38-42
Q_EN: What happens during DDPM sampling after the noise predictor has been trained?
Q_ZH: 噪声预测器训练好后，DDPM 采样过程做什么？
A_EN: Start from $x_T\sim N(0,I)$ and iterate backward using the learned noise prediction to compute a denoising mean, adding the sampler's prescribed random noise when required. In the lecture's sampler, the last step adds no fresh noise. Sampling follows a learned reverse process; it is not subtraction of the exact forward noise, which is unavailable for a newly generated sample.
A_ZH: 从 $x_T\sim N(0,I)$ 开始，逐步向后迭代，利用学习到的噪声预测计算去噪均值，并按采样器要求加入随机噪声。课件中的最后一步不再添加新噪声。采样遵循学习到的反向过程，并不是减去某个新生成样本未知的“真实前向噪声”。

@@ M294 | x10-generative | learn | XGEN:43,50-51
Q_EN: What does classifier-free guidance combine?
Q_ZH: 无分类器引导结合了什么？
A_EN: It combines conditional and unconditional model predictions, often written $\hat\epsilon=\epsilon_{\rm uncond}+s(\epsilon_{\rm cond}-\epsilon_{\rm uncond})$. In this convention s=1 gives the conditional prediction and s=0 the unconditional one. Larger guidance can strengthen conditioning while reducing diversity or causing artifacts. The two branches can share a network trained with dropped conditions.
A_ZH: 它结合有条件和无条件的模型预测，常写为 $\hat\epsilon=\epsilon_{\rm uncond}+s(\epsilon_{\rm cond}-\epsilon_{\rm uncond})$。按此约定，s=1 为有条件预测，s=0 为无条件预测。更强引导可能增强条件符合度，也可能降低多样性或产生伪影。两条分支可共享一个通过丢弃条件训练的网络。

@@ M295 | x11-transformers | worked | XATT:5-11
Q_EN: A 224×224 RGB image uses nonoverlapping 16×16 ViT patches. How many patch tokens and raw numbers per patch are there?
Q_ZH: 224×224 RGB 图像使用不重叠的 16×16 ViT 图像块，有多少 patch token？每块包含多少原始数值？
A_EN: There are $(224/16)^2=196$ patches. Each flattened patch has $16\cdot16\cdot3=768$ numbers before projection into the model's embedding dimension. Adding one class token gives sequence length 197. The embedding dimension is a design choice and need not equal the raw patch dimension.
A_ZH: 图像块数为 $(224/16)^2=196$。每块展平后有 $16\cdot16\cdot3=768$ 个数，再投影到模型嵌入维度。加入一个类别 token 后，序列长度为 197。嵌入维度由模型设计决定，不必等于原始图像块维度。

@@ M296 | x11-transformers | learn | XATT:8-12
Q_EN: Why does a ViT add positional information to patch embeddings?
Q_ZH: ViT 为什么要为 patch 嵌入加入位置信息？
A_EN: Content-based self-attention alone does not encode where a patch came from. Permuting tokens permutes the corresponding outputs when no positional mechanism breaks that symmetry. Positional embeddings or related mechanisms supply spatial/order information. Learned absolute embeddings may require adaptation when the patch grid changes.
A_ZH: 仅根据内容执行自注意力，并不能表示图像块来自哪里；没有位置机制打破对称时，置换 token 会相应置换输出。位置嵌入或其他位置机制补充空间与顺序信息。若 patch 网格改变，学习到的绝对位置嵌入可能需要适配。

@@ M297 | x11-transformers | learn | XATT:13-15; XATREF:3.2
Q_EN: State scaled dot-product attention and give consistent matrix dimensions.
Q_ZH: 写出缩放点积注意力，并给出一致的矩阵维度。
A_EN: For n tokens with feature width D, use $Q=XW_Q$, $K=XW_K$, $V=XW_V$, where $W_Q,W_K$ are D-by-d_k and $W_V$ is D-by-d_v. Then $A=\operatorname{softmax}(QK^T/\sqrt{d_k})$ is n-by-n and AV is n-by-d_v. Softmax acts across keys for each query. This fixes the historical slide's token-dimension projection matrices.
A_ZH: 对 n 个、特征宽度为 D 的 token，取 $Q=XW_Q$、$K=XW_K$、$V=XW_V$，其中 $W_Q,W_K$ 为 D 行 d_k 列，$W_V$ 为 D 行 d_v 列。于是 $A=\operatorname{softmax}(QK^T/\sqrt{d_k})$ 为 n 阶矩阵，AV 为 n 行 d_v 列。Softmax 对每个 query 的各 key 归一化，这修正了旧课件按 token 维度写投影矩阵的问题。

@@ M298 | x11-transformers | worked | XATT:13
Q_EN: One attention query has scaled scores (log 3,0) and scalar values (2,10). What is its output?
Q_ZH: 某个注意力 query 的缩放后分数为 (log 3,0)，对应标量 value 为 (2,10)，输出是多少？
A_EN: Softmax gives weights (3/4,1/4), so the weighted value is $(3/4)2+(1/4)10=4$. The scores select weights; the values supply the information being averaged. Attention weights sum to one per query, but the output does not have to be a probability.
A_ZH: Softmax 得到权重 (3/4,1/4)，所以加权输出为 $(3/4)2+(1/4)10=4$。分数决定权重，value 提供被加权的信息。每个 query 的注意力权重和为一，但输出本身不必是概率。

@@ M299 | x11-transformers | learn | XATT:14-18
Q_EN: What do multiple attention heads add, and why can global attention be expensive?
Q_ZH: 多个注意力头增加了什么能力？全局注意力为什么可能昂贵？
A_EN: Each head uses its own learned projections, allowing different combinations of features and token relationships. Head outputs are concatenated and projected. Standard dense attention forms pairwise token scores, giving n-by-n score storage and roughly quadratic dependence on token count. Multiple heads do not automatically remove this cost; windowed or sparse patterns change the interactions.
A_ZH: 每个头有自己的可学习投影，可组合不同特征和 token 关系，输出再拼接并投影。标准稠密注意力形成两两 token 分数，需要 n×n 分数存储，对 token 数量具有近似二次依赖。增加头数不会自动消除这一成本，窗口或稀疏模式改变了交互范围。

@@ M300 | x11-transformers | learn | XATT:12,15
Q_EN: What distinct roles do attention, the feed-forward block, residual paths and normalization play in a Transformer block?
Q_ZH: Transformer 块中的注意力、前馈块、残差路径和归一化分别做什么？
A_EN: Attention mixes information across tokens. The feed-forward block transforms each token's features with shared parameters. Residual paths preserve a direct route around a sublayer, and normalization controls feature statistics. Their ordering varies by architecture, so pre-norm and post-norm should not be treated as identical computations.
A_ZH: 注意力在 token 之间混合信息；前馈块用共享参数变换各 token 的特征；残差路径提供绕过子层的直接通道；归一化控制特征统计量。不同架构的排列不同，因此 pre-norm 和 post-norm 不能当作完全相同的计算。

@@ M301 | x11-transformers | learn | XATT:21-32
Q_EN: How does an adversarial perturbation differ from ordinary random input noise?
Q_ZH: 对抗扰动与普通随机输入噪声有什么区别？
A_EN: An adversarial perturbation is chosen to induce a model error under a stated constraint, such as a norm budget. Random noise is sampled without optimizing that failure objective. For an untargeted differentiable model, FGSM uses the sign of the input-loss gradient in one step; projected iterative methods repeat updates while enforcing the allowed region.
A_ZH: 对抗扰动是在范数预算等限制下，为诱发模型错误而选择的扰动；随机噪声则不专门优化这种失败目标。对可微模型的非定向攻击，FGSM 一步使用输入损失梯度的符号；投影迭代方法则反复更新，并维持扰动位于允许区域内。

@@ M302 | x11-transformers | check | XATT:29-37
Q_EN: What must a robustness result specify before it is interpretable?
Q_ZH: 一个鲁棒性结果必须说明哪些条件，才有可解释性？
A_EN: State the data, model access, perturbation norm/budget, attack strength and success metric. Adversarial training can improve resistance within a tested threat model, but does not prove immunity to all attacks, physical changes or distribution shifts. A weak attack can make a fragile model look robust. Evaluate the defense against an appropriate, independently checked procedure.
A_ZH: 应说明数据、可访问的模型信息、扰动范数与预算、攻击强度和成功指标。对抗训练可改善已测试威胁模型内的抵抗能力，但不证明能免疫所有攻击、物理变化或分布偏移。过弱攻击会使脆弱模型看起来鲁棒，因此应采用适当且独立检查过的评价过程。

@@ M303 | x12-problems | historical | XHA1:1; XHA1S:1-2
Q_EN: Historical Assignment 1 gives die probabilities (0.1,0.1,0.2,0.2,0.4,0) for faces 1–6. What is the chance of an even result?
Q_ZH: 往年 Assignment 1 中，骰子 1–6 面的概率依次为 (0.1,0.1,0.2,0.2,0.4,0)，掷出偶数的概率是多少？
A_EN: Add the probabilities of mutually exclusive even faces: $P(2)+P(4)+P(6)=0.1+0.2+0=0.3$. A fair die gives 0.5, so the stated winning rule is less favorable with this biased die. Do not count three even faces and divide by six unless the faces are equally likely.
A_ZH: 把互斥的偶数面概率相加：$P(2)+P(4)+P(6)=0.1+0.2+0=0.3$。公平骰子的概率为 0.5，因此这个偏置骰子对题中的获胜规则更不利。只有各面等可能时，才可以用三个偶数面除以六。

@@ M304 | x12-problems | historical | XHA1:1; XHA1S:1-2
Q_EN: If X takes 3, 8 and 9 with probabilities p3, p8 and p9, what is $E[I(X=8)]$?
Q_ZH: X 以 p3、p8、p9 的概率取 3、8、9，则 $E[I(X=8)]$ 是多少？
A_EN: The indicator is 0 at X=3 or 9 and 1 at X=8. Therefore its expectation is $0p_3+1p_8+0p_9=p_8$. More generally, the expected indicator of an event equals that event's probability. The expected indicator is not the indicator evaluated at the expected value of X.
A_ZH: X 为 3 或 9 时指示函数为 0，为 8 时为 1，因此期望为 $0p_3+1p_8+0p_9=p_8$。一般而言，事件指示函数的期望等于该事件的概率。它不是先求 X 的期望，再把该期望代入指示函数。

@@ M305 | x12-problems | historical | XHA1:2; XHA1S:2-3
Q_EN: Prove the discrete entropy chain rule $H(X,Y)=H(Y)+H(X|Y)$.
Q_ZH: 证明离散熵的链式法则 $H(X,Y)=H(Y)+H(X|Y)$。
A_EN: On positive-probability events, write $p(x,y)=p(y)p(x|y)$ and split its logarithm. In $-\sum_{x,y}p(x,y)\log p(x,y)$, the log p(y) part sums over x to H(Y), while the conditional part is H(X|Y). Use the convention $0\log0=0$ and consistent log bases; base 2 gives bits.
A_ZH: 在正概率事件上，写成 $p(x,y)=p(y)p(x|y)$，再把对数拆开。在 $-\sum_{x,y}p(x,y)\log p(x,y)$ 中，log p(y) 那一项对 x 求和后得到 H(Y)，条件概率那项得到 H(X|Y)。采用 $0\log0=0$ 的约定，并保持对数底一致，底数 2 对应 bit。

@@ M306 | x12-problems | historical | XHA1:2; XHA1S:2-3
Q_EN: Why does independence imply zero mutual information in the historical entropy exercise?
Q_ZH: 往年熵练习中，为什么独立意味着互信息为零？
A_EN: Mutual information averages $\log[p(x,y)/(p(x)p(y))]$ under the joint distribution. Independence makes the ratio 1 wherever joint probability is positive, and $\log1=0$. Zero-probability terms contribute zero. This is stronger than merely zero covariance, which only concerns a second-order moment.
A_ZH: 互信息是在联合分布下，对 $\log[p(x,y)/(p(x)p(y))]$ 求平均。独立时，在联合概率为正的地方，该比值等于 1，而 $\log1=0$；零概率项按零处理。这比仅有零协方差更强，后者只描述二阶矩。

@@ M307 | x12-problems | historical | XHA1:2; XHA1S:3-5
Q_EN: For a Laplace class-conditional feature density, how do I estimate location and scale by maximum likelihood?
Q_ZH: 对 Laplace 类条件特征密度，怎样用最大似然估计位置和尺度？
A_EN: Within each class, maximizing $\prod_i(2b)^{-1}e^{-|x_i-\mu|/b}$ makes mu a sample median, since it minimizes absolute deviations. Then $\hat b=\sum_i|x_i-\hat\mu|/n_c$ and the class prior is $n_c/n$. An even sample can admit several medians. Identical observations give a zero-scale boundary issue, requiring a positive floor or other modeling treatment.
A_ZH: 在每一类内部，最大化 $\prod_i(2b)^{-1}e^{-|x_i-\mu|/b}$ 时，mu 应取样本中位数，因为它最小化绝对偏差。随后 $\hat b=\sum_i|x_i-\hat\mu|/n_c$，类别先验为 $n_c/n$。偶数个样本可能有多个中位数；若观测完全相同，会出现尺度趋零的边界问题，需要正下限或其他建模处理。

@@ M308 | x12-problems | historical | XHA1:2; XHA1S:5-6
Q_EN: Why does binary LDA with shared covariance yield a sigmoid posterior?
Q_ZH: 共享协方差的二分类 LDA 为什么产生 sigmoid 后验？
A_EN: For positive priors and common positive-definite Sigma, quadratic terms cancel in the Gaussian log ratio. Thus log odds are $w^Tx+b$, where $w=\Sigma^{-1}(\mu_1-\mu_0)$ and $b=\log(\pi_1/\pi_0)-(\mu_1^T\Sigma^{-1}\mu_1-\mu_0^T\Sigma^{-1}\mu_0)/2$. Converting odds to probability gives $\sigma(w^Tx+b)$. Unequal class covariances generally leave a quadratic boundary.
A_ZH: 类别先验为正且共享正定 Sigma 时，高斯对数比中的二次项抵消。因此对数优势为 $w^Tx+b$，其中 $w=\Sigma^{-1}(\mu_1-\mu_0)$，$b=\log(\pi_1/\pi_0)-(\mu_1^T\Sigma^{-1}\mu_1-\mu_0^T\Sigma^{-1}\mu_0)/2$。把优势换成概率得到 $\sigma(w^Tx+b)$。不同类别协方差通常会留下二次边界。

@@ M309 | x12-problems | historical | XHA1:3-4; XHA1S:6-8
Q_EN: For a nonsingular joint Gaussian partitioned into xa and xb, what is the distribution of xb given xa?
Q_ZH: 非退化联合高斯分为 xa 和 xb 时，给定 xa 后 xb 的分布是什么？
A_EN: It is Gaussian with mean $\mu_b+\Sigma_{ba}\Sigma_{aa}^{-1}(x_a-\mu_a)$ and covariance $\Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab}$. One derivation holds xa fixed and completes the square in xb in the joint exponent. The conditional covariance does not depend on the realized xa, while the conditional mean does.
A_ZH: 它仍是高斯，均值为 $\mu_b+\Sigma_{ba}\Sigma_{aa}^{-1}(x_a-\mu_a)$，协方差为 $\Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab}$。可在联合密度指数中固定 xa，对 xb 配方得到。条件协方差不依赖 xa 的具体观测值，而条件均值依赖它。

@@ M310 | x12-problems | historical | XHA2:1; XHA2S:1-2
Q_EN: Historical Assignment 2 reports frequencies (100,81,34,9,6) for counts (0,1,2,3,4+). When is the provided estimate 0.8696 valid?
Q_ZH: 往年 Assignment 2 中，计数 (0,1,2,3,4+) 的频数为 (100,81,34,9,6)，所给估计 0.8696 在什么条件下成立？
A_EN: The provided solution explicitly assumes every 4+ observation equals 4, giving $(81+68+27+24)/230=0.8696$. Without that assumption, the exact empirical mean is unknown and at least this large. If treating 4+ as censored Poisson data, maximize the grouped likelihood with a $P_\lambda(X\ge4)^6$ term instead of silently replacing all tail counts by 4.
A_ZH: 配套解答明确假设所有 4+ 观测都等于 4，得到 $(81+68+27+24)/230=0.8696$。不作这一假设，就不知道精确样本均值，只能知道其至少这么大。若将 4+ 当作删失的 Poisson 数据，应在分组似然中使用 $P_\lambda(X\ge4)^6$，不能默默把全部尾部计数替换成 4。

@@ M311 | x12-problems | historical | XHA2:1-2; XHA2S:2-4
Q_EN: Derive the gradient of $\ell(u,v)=(ue^v-2ve^{-u})^2$ for the historical gradient-descent exercise.
Q_ZH: 推导往年梯度下降题中 $\ell(u,v)=(ue^v-2ve^{-u})^2$ 的梯度。
A_EN: Let $q=ue^v-2ve^{-u}$. The chain rule gives $\partial_u\ell=2q(e^v+2ve^{-u})$ and $\partial_v\ell=2q(ue^v-2e^{-u})$. For simultaneous gradient descent, compute both derivatives at the old (u,v), then update both coordinates. Updating u first and using that new value in the v derivative implements a different procedure.
A_ZH: 令 $q=ue^v-2ve^{-u}$。链式法则给出 $\partial_u\ell=2q(e^v+2ve^{-u})$ 和 $\partial_v\ell=2q(ue^v-2e^{-u})$。同时梯度下降应先在旧 (u,v) 处计算两个导数，再更新两个坐标。先更新 u，再用新 u 算 v 的导数，会变成不同算法。

@@ M312 | x12-problems | historical | XHA2:1-2; XHA2S:2-4
Q_EN: For $\ell(u,v)=(ue^v-2ve^{-u})^2$, start at (1,1) and use simultaneous gradient descent with learning rate 0.1. After how many updates does loss first fall below $10^{-14}$?
Q_ZH: 对 $\ell(u,v)=(ue^v-2ve^{-u})^2$，从 (1,1) 出发，以学习率 0.1 同时更新两个坐标。损失首次低于 $10^{-14}$ 需要几次更新？
A_EN: It takes 10 double-precision updates; the resulting parameters round to (0.045,0.024). Compute both gradient components at the old parameter pair before changing either coordinate. Count updates from the initial point and check loss after each step. The gradient derivation is in companion card CS5489-M311; rounding intermediate values or using sequential coordinate updates can change the result.
A_ZH: 双精度下需 10 次更新，所得参数按三位小数舍入为 (0.045,0.024)。每次先在旧参数对处计算两个梯度分量，再更新两个坐标。从初始点开始计更新次数，每步后检查损失。梯度推导见配套卡 CS5489-M311；中途舍入或改成逐坐标顺序更新，可能改变结果。

@@ M313 | x12-problems | historical | XHA2:2; XHA2S:4-5
Q_EN: Minimize $x_1^2+x_2^2$ subject to both unit disks centered at (1,1) and (1,-1). What is the feasible set?
Q_ZH: 在以 (1,1) 和 (1,-1) 为圆心、半径均为 1 的两个闭圆盘内，最小化 $x_1^2+x_2^2$，可行集是什么？
A_EN: The centers are distance 2 apart, exactly the sum of the radii, so the disks touch only at (1,0). Equivalently, adding their two inequalities gives $(x_1-1)^2+x_2^2\le0$. Thus the unique feasible point and primal optimizer is (1,0), with value 1. There is no strictly feasible point.
A_ZH: 两圆心相距 2，恰为半径之和，因此只在 (1,0) 相切。也可把两个不等式相加，得到 $(x_1-1)^2+x_2^2\le0$。所以唯一可行点、也就是原始最优点为 (1,0)，目标值为 1，且不存在严格可行点。

@@ M314 | x12-problems | historical | XHA2:2; XHA2S:5-7
Q_EN: Minimize $x_1^2+x_2^2$ subject to $(x_1-1)^2+(x_2-1)^2\le1$ and $(x_1-1)^2+(x_2+1)^2\le1$. Do finite KKT multipliers exist, and is the duality gap positive?
Q_ZH: 最小化 $x_1^2+x_2^2$，约束为 $(x_1-1)^2+(x_2-1)^2\le1$ 与 $(x_1-1)^2+(x_2+1)^2\le1$。存在有限 KKT 乘子吗？对偶间隙是否为正？
A_EN: No finite multipliers satisfy stationarity: at (1,0), the objective's x1 derivative is 2, while both constraint x1 derivatives are zero. But the dual is $g=(s-d^2)/(1+s)$ for $s=\lambda_1+\lambda_2$, $d=\lambda_1-\lambda_2$, with nonnegative multipliers. Taking equal multipliers to infinity gives supremum 1. The gap is zero, although the dual supremum is not attained.
A_ZH: 没有有限乘子满足驻点条件：在 (1,0)，目标对 x1 的导数为 2，而两个约束对 x1 的导数都为零。但对非负乘子，对偶函数为 $g=(s-d^2)/(1+s)$，其中 $s=\lambda_1+\lambda_2$、$d=\lambda_1-\lambda_2$。让两乘子相等并趋于无穷，上确界为 1，因此对偶间隙为零，却没有有限乘子取得对偶最优值。

@@ M315 | x12-problems | historical | XHA2:2-3; XHA2S:7-8
Q_EN: Derive the closest point on the hyperplane $w^Tx+b=0$ to a given point x0, assuming $w\ne0$.
Q_ZH: 给定点 x0 且 $w\ne0$，推导超平面 $w^Tx+b=0$ 上距它最近的点。
A_EN: Form the Lagrangian $L=\frac12\|x-x_0\|^2+\lambda(w^Tx+b)$. Stationarity in x gives $x=x_0-\lambda w$. Enforce the equality to get $\lambda=(w^Tx_0+b)/\|w\|^2$. The closest point is $x_0-(w^Tx_0+b)w/\|w\|^2$, at distance $|w^Tx_0+b|/\|w\|$. Lambda is an unrestricted equality multiplier, not another variable jointly minimized with x.
A_ZH: 构造拉格朗日函数 $L=\frac12\|x-x_0\|^2+\lambda(w^Tx+b)$。对 x 的驻点条件给出 $x=x_0-\lambda w$；再满足等式约束，得 $\lambda=(w^Tx_0+b)/\|w\|^2$。最近点为 $x_0-(w^Tx_0+b)w/\|w\|^2$，距离为 $|w^Tx_0+b|/\|w\|$。Lambda 是无符号限制的等式乘子，不能把它和 x 一起当作普通变量联合最小化。

@@ M316 | x12-problems | historical | XHA2:3; XHA2S:8-10
Q_EN: What steps derive the hard-margin SVM dual, and where does it differ from the ordinary soft-margin dual?
Q_ZH: 硬间隔 SVM 对偶的推导步骤是什么？它与普通软间隔对偶在哪里不同？
A_EN: Add nonnegative multipliers to the margin constraints, then minimize the Lagrangian over w and b. Stationarity yields $w=\sum_i\alpha_i y_i x_i$ and $\sum_i\alpha_i y_i=0$. Substitution gives the usual quadratic dual. Hard margin has $\alpha_i\ge0$ with no upper bound; the linear-slack soft-margin penalty adds $\alpha_i\le C$.
A_ZH: 对间隔约束引入非负乘子，再对 w、b 最小化拉格朗日函数。驻点条件给出 $w=\sum_i\alpha_i y_i x_i$ 和 $\sum_i\alpha_i y_i=0$，代回得到标准二次对偶。硬间隔只有 $\alpha_i\ge0$，没有上界；对松弛量作线性惩罚的软间隔才增加 $\alpha_i\le C$。

@@ M317 | x12-problems | historical | XHA3:1; XHA3S:1-2
Q_EN: For compatible real matrices P, R and B, prove $(P^{-1}+B^TR^{-1}B)^{-1}B^TR^{-1}=PB^T(BPB^T+R)^{-1}$. Which inverses must exist?
Q_ZH: 对维度相容的实矩阵 P、R、B，证明 $(P^{-1}+B^TR^{-1}B)^{-1}B^TR^{-1}=PB^T(BPB^T+R)^{-1}$。需要哪些逆矩阵存在？
A_EN: Put $A=P^{-1}+B^TR^{-1}B$ and $S=BPB^T+R$. Direct multiplication gives $APB^T=B^TR^{-1}S$. If P, R, A and S are invertible, multiply by $A^{-1}$ and $S^{-1}$ to obtain $A^{-1}B^TR^{-1}=PB^TS^{-1}$. Positive-definite P and R suffice. Invertibility of P and R alone does not guarantee the other inverses exist.
A_ZH: 令 $A=P^{-1}+B^TR^{-1}B$、$S=BPB^T+R$，直接相乘可得 $APB^T=B^TR^{-1}S$。若 P、R、A、S 均可逆，左乘 $A^{-1}$、右乘 $S^{-1}$，得到 $A^{-1}B^TR^{-1}=PB^TS^{-1}$。P、R 正定是充分条件，仅有 P、R 可逆不保证另外两个逆矩阵存在。

@@ M318 | x12-problems | historical | XHA3:1; XHA3S:2-4
Q_EN: For a real M-by-N matrix A, consider Ax=y. Which claims hold? Square means at most one solution; N>M means always solvable; N>M means nonzero nullity; N<M means some y is inconsistent; N<M means zero nullity.
Q_ZH: 对 M 行 N 列实矩阵 A，考虑方程 Ax=y。判断：方阵至多有一解；N>M 时总可解；N>M 时零空间非零；N<M 时存在无解的 y；N<M 时零空间维数为零。
A_EN: In order: false, false, true, true, false. Rank-nullity gives nullity $N-\operatorname{rank}(A)$. A zero matrix supplies counterexamples to uniqueness and universal solvability. When N<M, column-space dimension is at most N<M, so some y lies outside it. But deficient column rank can still give a nonzero nullspace even in a tall matrix.
A_ZH: 依次为：假、假、真、真、假。秩与零空间维数定理给出零空间维数 $N-\operatorname{rank}(A)$。零矩阵可反驳唯一性或总可解。N<M 时列空间维数至多 N，小于 M，因此存在列空间之外的 y；但高矩阵若列秩不足，仍可有非零零空间。

@@ M319 | x12-problems | historical | XHA3:2; XHA3S:4-6
Q_EN: What is the least-squares coordinate-descent update using the current residual?
Q_ZH: 利用当前残差，最小二乘的坐标下降更新式是什么？
A_EN: Let r=y-Xw and let xk be column k. If $x_k^Tx_k>0$, set $\Delta w_k=x_k^Tr/(x_k^Tx_k)$, update $w_k\leftarrow w_k+\Delta w_k$, then $r\leftarrow r-\Delta w_kx_k$. This exactly minimizes along that coordinate with others fixed. A zero column requires separate handling because it gives no information about its coefficient.
A_ZH: 令 r=y-Xw，xk 为第 k 列。若 $x_k^Tx_k>0$，则取 $\Delta w_k=x_k^Tr/(x_k^Tx_k)$，更新 $w_k\leftarrow w_k+\Delta w_k$，再令 $r\leftarrow r-\Delta w_kx_k$。它在固定其他坐标时精确最小化该坐标方向。零列不提供其系数的信息，需要单独处理。

@@ M320 | x12-problems | historical | XHA3:2-3; XHA3S:6-8
Q_EN: Why can the nonnegative-slack constraints be omitted in squared-slack SVM?
Q_ZH: 平方松弛惩罚 SVM 中，为什么可以省略松弛变量非负约束？
A_EN: Suppose a feasible point has $\xi_i<0$ under $y_if(x_i)\ge1-\xi_i$. Replacing xi by zero makes the margin constraint weaker and reduces $C\xi_i^2$ for C>0. Therefore no optimum needs negative slack. This argument is specific to the stated objective and constraint; do not remove constraints from other formulations without checking.
A_ZH: 若某可行点在 $y_if(x_i)\ge1-\xi_i$ 下满足 $\xi_i<0$，把 xi 换成零会放宽间隔约束，并在 C>0 时降低 $C\xi_i^2$。因此最优解无需负松弛量。该论证依赖此目标与约束，不能不加检查地删除其他模型的约束。

@@ M321 | x12-problems | historical | XHA3:3; XHA3S:6-8
Q_EN: How does a squared-slack penalty change the SVM dual?
Q_ZH: 对松弛量作平方惩罚，会怎样改变 SVM 对偶？
A_EN: For $\frac12\|w\|^2+C\sum_i\xi_i^2$, stationarity gives $\xi_i=\alpha_i/(2C)$. The dual maximizes $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j-\sum_i\alpha_i^2/(4C)$, subject to $\alpha_i\ge0$ and $\sum_i\alpha_i y_i=0$. There is no ordinary upper bound C; an added quadratic penalty plays that role differently.
A_ZH: 对 $\frac12\|w\|^2+C\sum_i\xi_i^2$，驻点条件给出 $\xi_i=\alpha_i/(2C)$。对偶最大化 $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j-\sum_i\alpha_i^2/(4C)$，约束为 $\alpha_i\ge0$、$\sum_i\alpha_i y_i=0$。这里没有普通的上界 C，而是增加了不同作用的二次惩罚。

@@ M322 | x12-problems | historical | XHA4:1; XHA4S:1-2
Q_EN: Why are eigenvalues of a real symmetric matrix real, and distinct-eigenvalue eigenvectors orthogonal?
Q_ZH: 为什么实对称矩阵的特征值为实数，不同特征值对应的特征向量正交？
A_EN: For a possibly complex eigenvector v, $\lambda=v^*Av/(v^*v)$ is real because A is Hermitian. For real eigenvectors u,v with eigenvalues lambda,mu, symmetry gives $\lambda u^Tv=(Au)^Tv=u^TAv=\mu u^Tv$. If lambda differs from mu, the inner product is zero. Repeated eigenvalues permit an orthonormal basis but do not force arbitrary chosen vectors to be orthogonal.
A_ZH: 对可能为复数的特征向量 v，因 A 为 Hermitian，$\lambda=v^*Av/(v^*v)$ 是实数。对特征值为 lambda、mu 的实向量 u、v，对称性给出 $\lambda u^Tv=(Au)^Tv=u^TAv=\mu u^Tv$。特征值不同则内积为零。重特征值的空间可选择正交归一基，但任意选出的向量并非天然正交。

@@ M323 | x12-problems | historical | XHA4:1; XHA4S:2-4; XPCA:14-16
Q_EN: Prove that the k-th PCA direction can be chosen as an eigenvector for the k-th largest covariance eigenvalue.
Q_ZH: 证明 PCA 的第 k 个方向可选为协方差矩阵第 k 大特征值对应的特征向量。
A_EN: Choose an orthonormal eigenbasis with $\lambda_1\ge\cdots\ge\lambda_d$. A unit vector orthogonal to the first k-1 basis vectors has $v=\sum_{j\ge k}c_ju_j$ with $\sum c_j^2=1$. Its variance is $\sum_{j\ge k}\lambda_jc_j^2\le\lambda_k$, achieved by $v=u_k$. Ties can make the maximizing direction nonunique.
A_ZH: 选取正交归一特征基，使 $\lambda_1\ge\cdots\ge\lambda_d$。与前 k-1 个基向量正交的单位向量可写成 $v=\sum_{j\ge k}c_ju_j$，且 $\sum c_j^2=1$。其方差为 $\sum_{j\ge k}\lambda_jc_j^2\le\lambda_k$，取 $v=u_k$ 即达到上界。出现相同特征值时，最大化方向可能不唯一。

@@ M324 | x12-problems | historical | XHA4:1,3; XHA4S:4,7
Q_EN: For the historical linear system shown, express x4 using x1,x2,x3, find y4, and test time invariance.
Q_ZH: 对图示往年线性系统，用 x1、x2、x3 表示 x4，求 y4，并判断是否时不变。
MEDIA_FRONT: extra-ha4-page3-image1.png;extra-ha4-page3-image2.png
A_EN: The inputs give $x_4=2x_1-2x_2+x_3$, so linearity gives $y_4=2y_1-2y_2+y_3$. Its nonzero values at n=(-1,0,1,2) are (2,1,2,-2). The system is not time invariant: $x_2=x_1[n]+x_1[n-1]$, but the supplied y2 is not $y_1[n]+y_1[n-1]$. Linearity alone does not imply shift invariance.
A_ZH: 由输入可得 $x_4=2x_1-2x_2+x_3$，线性性给出 $y_4=2y_1-2y_2+y_3$。在 n=(-1,0,1,2) 处的非零值为 (2,1,2,-2)。系统并非时不变：虽然 $x_2=x_1[n]+x_1[n-1]$，题给 y2 却不等于 $y_1[n]+y_1[n-1]$。线性并不蕴含平移不变。

@@ M325 | x12-problems | historical | XHA4:1-2,4; XHA4S:5,8
Q_EN: Compute the two historical convolution examples in the figures, preserving their starting indices.
Q_ZH: 计算图中的两个往年卷积例题，并保留正确起始下标。
MEDIA_FRONT: extra-ha4-page4-image1.png;extra-ha4-page4-image2.png
A_EN: First, x is four ones and h is four twos, both supported at n=0..3. Their convolution at n=0..6 is (2,4,6,8,6,4,2). Second, $x[n]=0.5\delta[n-2]$, so $y[n]=0.5h[n-2]$. With h=(1,2,3,2,1) at n=0..4, y=(0.5,1,1.5,1,0.5) at n=2..6, and zero elsewhere.
A_ZH: 第一例中，x 为四个 1，h 为四个 2，支撑均为 n=0..3，卷积在 n=0..6 处为 (2,4,6,8,6,4,2)。第二例 $x[n]=0.5\delta[n-2]$，故 $y[n]=0.5h[n-2]$。h 在 n=0..4 为 (1,2,3,2,1)，所以 y 在 n=2..6 为 (0.5,1,1.5,1,0.5)，其余位置为零。

@@ M326 | x12-problems | historical | XHA4:2; XHA4S:5-6
Q_EN: What is the key change of variables in proving the DTFT convolution theorem?
Q_ZH: 证明 DTFT 卷积定理时，关键的变量替换是什么？
A_EN: Start with $\sum_n\sum_m x[m]y[n-m]e^{-j\omega n}$ and set t=n-m. Under conditions allowing the sums to be exchanged, such as absolute summability, it factors into $(\sum_m x[m]e^{-j\omega m})(\sum_t y[t]e^{-j\omega t})=X(\omega)Y(\omega)$. The exponential also splits because n=t+m.
A_ZH: 从 $\sum_n\sum_m x[m]y[n-m]e^{-j\omega n}$ 出发，令 t=n-m。在绝对可和等允许交换求和的条件下，可分解成 $(\sum_m x[m]e^{-j\omega m})(\sum_t y[t]e^{-j\omega t})=X(\omega)Y(\omega)$。指数项能够拆开，是因为 n=t+m。
