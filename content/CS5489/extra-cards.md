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
A_EN: For prediction $\hat y_i=w^Tx_i+b$, this course uses residual $r_i=\hat y_i-y_i$ (prediction minus target). OLS minimizes $\sum_i r_i^2$, or its mean. The alternative residual $y_i-\hat y_i$ has the opposite sign but the same squared loss. Squaring prevents positive and negative errors from cancelling and penalizes large errors more strongly.
A_ZH: 对预测 $\hat y_i=w^Tx_i+b$，本课程统一用残差 $r_i=\hat y_i-y_i$（预测减真实）。OLS最小化 $\sum_i r_i^2$ 或其平均值。若课件用 $y_i-\hat y_i$，只是残差符号相反，平方损失相同。平方避免正负误差抵消，并加重较大误差的惩罚。

@@ M188 | x02-regression | worked | XR1:10
Q_EN: Predictions are (2,4,5) and targets are (1,4,7). Compute MSE and RMSE.
Q_ZH: 预测值为 (2,4,5)，真实值为 (1,4,7)，计算 MSE 和 RMSE。
A_EN: Using prediction minus target, residuals are (1,0,-2), so the squared-error sum is $1+0+4=5$. MSE is $5/3$ and RMSE is $\sqrt{5/3}\approx1.291$. MSE uses squared target units; RMSE uses the target unit. Reversing every residual sign would leave both measures unchanged.
A_ZH: 按预测减真实，残差为 (1,0,-2)，平方误差和为 $1+0+4=5$。MSE为 $5/3$，RMSE为 $\sqrt{5/3}\approx1.291$。MSE用目标单位的平方，RMSE用原目标单位；全部残差反号不会改变这两个结果。

@@ M189 | x02-regression | learn | XR1:13,18
Q_EN: How does a design matrix include the intercept?
Q_ZH: 设计矩阵怎样包含截距项？
A_EN: Put one example per row and prepend a column of ones. With n examples and d measured features, $X$ is $n\times(d+1)$ and $w=(b,w_1,\ldots,w_d)^T$. Then all predictions are $Xw$. The ones column is a convention, not an extra measured feature. Keep row/column conventions explicit.
A_ZH: 每行放一个样本，并在前面加一列 1。若有 n 个样本和 d 个测量特征，则 $X$ 为 $n\times(d+1)$，参数为 $w=(b,w_1,\ldots,w_d)^T$，全部预测写成 $Xw$。常数列是一种表示约定，不是额外测得的特征，必须明确行列含义。

@@ M190 | x02-regression | learn | XR1:18-19
Q_EN: Derive the normal equations for linear least squares.
Q_ZH: 怎样推导线性最小二乘的正规方程？
A_EN: Write $J=\frac12\sum_i(\sum_jX_{ij}w_j-y_i)^2$. For coordinate k, the chain rule gives $\partial J/\partial w_k=\sum_iX_{ik}(X_iw-y_i)$. Collecting these derivatives yields $X^T(Xw-y)$. Setting them to zero gives $X^TXw=X^Ty$. Its Hessian $X^TX$ is positive semidefinite, so solutions minimize J globally; an inverse formula additionally needs full column rank.
A_ZH: 先写 $J=\frac12\sum_i(\sum_jX_{ij}w_j-y_i)^2$。对第k个系数用链式法则：$\partial J/\partial w_k=\sum_iX_{ik}(X_iw-y_i)$。把各坐标导数排成向量即 $X^T(Xw-y)$，令零得 $X^TXw=X^Ty$。Hessian $X^TX$ 半正定，所以方程解为全局极小点；要写逆矩阵解还需列满秩。

@@ M191 | x02-regression | check | XR1:19; XR2:17
Q_EN: Is having at least as many samples as coefficients sufficient for a unique OLS fit?
Q_ZH: 样本数不少于系数个数，就足以保证 OLS 解唯一吗？
A_EN: No. Full column rank of X is required. Even with many rows, duplicate or linearly dependent columns make $X^TX$ singular. OLS still has least-squares solutions, but coefficients may not be unique. QR, SVD or a pseudoinverse can compute a solution without pretending that a singular inverse exists.
A_ZH: 不足够，还要求 X 列满秩。即使有很多样本，重复或线性相关的特征列仍会使 $X^TX$ 奇异。最小二乘解仍存在，但系数可能不唯一。可用 QR、SVD 或伪逆求解，不能把不存在的逆矩阵当作有效公式。

@@ M192 | x02-regression | worked | XR1:15-17
Q_EN: Fit a line through (0,1), (1,3), (2,5). What do slope and intercept mean?
Q_ZH: 对 (0,1)、(1,3)、(2,5) 拟合直线，斜率和截距各是多少、各表示什么？
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
A_EN: For $J=\frac12\|Xw-y\|^2+\frac\lambda2\|w\|^2$, differentiate: $\nabla J=X^T(Xw-y)+\lambda w$. Setting this to zero gives $(X^TX+\lambda I)w=X^Ty$. With $\lambda>0$, all eigenvalues of this matrix are positive, so w is unique. Every coordinate is penalized here; exempting an intercept replaces I with the appropriate diagonal penalty mask.
A_ZH: 对 $J=\frac12\|Xw-y\|^2+\frac\lambda2\|w\|^2$ 求导：$\nabla J=X^T(Xw-y)+\lambda w$。令零得到 $(X^TX+\lambda I)w=X^Ty$。当 $\lambda>0$ 时该矩阵特征值均正，解唯一。这里惩罚全部坐标；若截距豁免，应将I换成相应对角惩罚矩阵。

@@ M195 | x02-regression | check | XR2:4-7,17
Q_EN: Why can ridge help with nearly collinear features, and what does it cost?
Q_ZH: 岭回归为何能改善近共线特征的问题？代价是什么？
A_EN: Along an eigenvector of $X^TX$ with positive eigenvalue s, OLS divides by s, whereas ridge divides by $s+\lambda$. Small-s directions amplify noise less. This improves conditioning; in the usual fixed-design, equal-variance noise model it reduces coefficient-estimation variance while introducing bias. The selected lambda still needs validation.
A_ZH: 沿 $X^TX$ 特征值为正数s的方向，OLS除以s，岭回归改为除以 $s+\lambda$，因此小s方向不再强烈放大噪声。这改善条件数；在常见的固定设计、同方差噪声模型中，系数估计方差降低，但引入偏差。lambda仍需通过验证选择。

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
A_EN: Assume independent Gaussian observation errors with known $\sigma^2>0$ and independent priors $w_j\sim N(0,\tau^2)$ with $\tau^2>0$. Multiplying the negative log posterior by $\sigma^2$ and dropping constants gives $\frac12\|Xw-y\|^2+\frac{\sigma^2}{2\tau^2}\|w\|^2$. Thus $\lambda=\sigma^2/\tau^2$ in this objective convention: a tighter prior produces stronger shrinkage.
A_ZH: 假设观测误差独立高斯，已知 $\sigma^2>0$，并取独立先验 $w_j\sim N(0,\tau^2)$、$\tau^2>0$。将负对数后验乘 $\sigma^2$、去掉无关常数，得到 $\frac12\|Xw-y\|^2+\frac{\sigma^2}{2\tau^2}\|w\|^2$。因此此目标约定下 $\lambda=\sigma^2/\tau^2$；先验越集中，收缩越强。

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
A_EN: Let w be the inlier probability per draw, s the sample size, and p the target success probability. Under the ideal model, s independent draws are all inliers with probability $w^s$, and a clean sample is nondegenerate. T independent trials succeed with probability $1-(1-w^s)^T$. For $0<w<1$ and $0<p<1$, use $T=\lceil\log(1-p)/\log(1-w^s)\rceil$. If w=1 one trial suffices; w=0 cannot succeed. Without-replacement sampling or degeneracy changes this model.
A_ZH: 令w为单次抽样取到内点的概率，s为每组样本大小，p为目标成功概率。理想模型下，独立抽s个点全部为内点的概率为 $w^s$，并假设全内点样本不退化。T次独立尝试的成功率为 $1-(1-w^s)^T$。当 $0<w<1$、$0<p<1$，取 $T=\lceil\log(1-p)/\log(1-w^s)\rceil$。w=1一次足够，w=0不可能成功；无放回抽样或退化会改变模型。

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
A_EN: Inertia is the sum of squared distances to assigned centers. Restarts help because different initial centers can reach different local optima. The globally smallest inertia cannot increase as k grows: extra centers can reproduce the old fit. Separate local runs need not be monotone. Thus training inertia alone favors too many clusters; consider stability, task meaning or a justified validation criterion, none of which universally recovers a true k.
A_ZH: 惯性是样本到所属中心的平方距离之和。不同初始中心可能进入不同局部最优，因此需要重启。k增大时，全局最小惯性不会增加，因为额外中心能复现原拟合；各次局部运行却未必单调。只看训练惯性容易偏向过多簇，应结合稳定性、任务意义或合理验证标准，没有方法普遍保证找出真实k。

@@ M216 | x04-clustering | check | XCL:23,35
Q_EN: Does ordinary k-means require every cluster to contain the same number of points?
Q_ZH: 普通 k-means 是否强制每个簇包含相同数量的样本？
A_EN: No. Its objective has no equal-size constraint. Euclidean nearest-center assignments favor certain compact geometries, but cluster populations may differ greatly. Equal mixture weights and shared spherical covariance help explain a connection with Gaussian mixtures; they must not be confused with an enforced equal count. This corrects the historical slide's loose wording.
A_ZH: 不强制，目标函数中没有等大小约束。欧氏最近中心分配偏好某些紧凑形状，但各簇样本数仍可相差很大。相等混合权重和共享球形协方差可用于解释它与高斯混合的联系，却不等于强制各簇人数相同。这纠正了旧课件中不够严格的表述。

@@ M217 | x04-clustering | learn | XCL:25-28
Q_EN: What is a Gaussian mixture model?
Q_ZH: 什么是高斯混合模型？
A_EN: A GMM has density $p(x)=\sum_{k=1}^K\pi_kN(x;\mu_k,\Sigma_k)$, with nonnegative weights summing to one and positive-definite covariances for ordinary nonsingular densities. First draw an unobserved component k with probability $\pi_k$, then draw x from its Gaussian. Means set locations; covariances set spread and orientation. Add component contributions rather than taking only the largest.
A_ZH: GMM密度为 $p(x)=\sum_{k=1}^K\pi_kN(x;\mu_k,\Sigma_k)$，权重非负且和为一；普通非奇异高斯密度还要求协方差正定。先按 $\pi_k$ 抽取不可观测的成分k，再由其高斯产生x，像先选一台机器再生产零件。均值决定位置，协方差决定散布与方向；各成分贡献要相加，不能只取最大者。

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
A_EN: For n observations, hold responsibilities $r_{ik}=P(z_i=k\mid x_i)$ fixed. Set $N_k=\sum_i r_{ik}$, $\pi_k=N_k/n$, and, when $N_k>0$, $\mu_k=\sum_i r_{ik}x_i/N_k$. These are effective counts, proportions and weighted means. A zero-count component needs a defined recovery strategy instead of division by zero.
A_ZH: 共有n个观测，固定责任度 $r_{ik}=P(z_i=k\mid x_i)$。令 $N_k=\sum_i r_{ik}$、$\pi_k=N_k/n$，并在 $N_k>0$ 时更新 $\mu_k=\sum_i r_{ik}x_i/N_k$。它们是有效计数、占比和加权均值。零有效计数的成分需要明确恢复策略，不能除以零。

@@ M221 | x04-clustering | learn | XCL:30,33
Q_EN: How is a GMM covariance updated, and why can unrestricted fitting become unstable?
Q_ZH: GMM 如何更新协方差？为什么无限制拟合可能不稳定？
A_EN: With fixed responsibilities r and $N_k=\sum_i r_{ik}>0$, use the newly updated mean in $\Sigma_k=\sum_i r_{ik}(x_i-\mu_k)(x_i-\mu_k)^T/N_k$. It averages weighted deviation outer products. An unrestricted mixture component can collapse onto a point as its covariance tends to zero, making likelihood unbounded. Covariance floors or constraints help prevent this; diagonal covariance only reduces parameter count.
A_ZH: 固定责任度r，且 $N_k=\sum_i r_{ik}>0$，用新均值计算 $\Sigma_k=\sum_i r_{ik}(x_i-\mu_k)(x_i-\mu_k)^T/N_k$，即对偏差外积作加权平均。无约束混合成分可塌缩到某点、协方差趋零，使似然无界增长。协方差下限或约束可防止这种退化；仅改为对角形式主要是减少参数。

@@ M222 | x04-clustering | learn | XEM:12-15
Q_EN: What do the E-step and M-step optimize in general EM?
Q_ZH: 一般 EM 算法中，E 步和 M 步分别做什么？
A_EN: The E-step computes the latent-variable posterior using current parameters. The M-step maximizes the expected complete-data log likelihood under that fixed posterior. The expectation is over hidden variables, not over new observed data. Keeping the posterior fixed during the M-step is essential to the coordinate-ascent argument.
A_ZH: E 步用当前参数计算潜变量的后验分布；M 步在固定该后验的条件下，最大化完整数据对数似然的期望。这里的期望是对隐藏变量求取，并不是增加新的观测数据。M 步中固定后验，是坐标上升论证的重要条件。

@@ M223 | x04-clustering | learn | XEM:12-19
Q_EN: Why does exact EM not decrease observed-data log likelihood?
Q_ZH: 为什么精确 EM 不会降低观测数据的对数似然？
A_EN: Let ell be observed log likelihood and F(q,theta) its EM lower bound. The E-step sets q to the current latent posterior, making $F(q,\theta_{old})=\ell(\theta_{old})$. Holding q fixed, the M-step raises F. Hence $\ell(\theta_{new})\ge F(q,\theta_{new})\ge F(q,\theta_{old})=\ell(\theta_{old})$. This proves nondecrease, not strict improvement or a global optimum; inaccurate updates may violate it.
A_ZH: 令ell为观测对数似然，F(q,theta)为EM下界。E步令q等于当前潜变量后验，使 $F(q,\theta_{old})=\ell(\theta_{old})$；M步固定q提高F。因此 $\ell(\theta_{new})\ge F(q,\theta_{new})\ge F(q,\theta_{old})=\ell(\theta_{old})$。这只保证不下降，不保证严格提高或全局最优；不准确的更新可能破坏保证。

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
A_EN: Check feature scaling, distance/covariance assumptions, k, initialization and stability under reasonable data changes. Cluster numbers can permute across runs without changing the partition. A two-dimensional plot discards other coordinates and may distort distances, so visual appearance alone does not validate the full-space grouping. Relate the groups to the actual task rather than treating every partition as discovered truth.
A_ZH: 检查特征缩放、距离或协方差假设、k、初始化及合理数据变化下的稳定性。不同运行可交换簇编号而不改变划分。二维图舍弃其他坐标，可能扭曲距离，因此不能只凭图形外观确认完整空间分组有意义。还须联系实际任务，不能把任意划分都当作发现了客观类别。

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
A_EN: Keep the k largest singular values: $X_k=U_k\Sigma_kV_k^T$. This minimizes $\|X-Y\|_F^2=\sum_{i,j}(X_{ij}-Y_{ij})^2$ among matrices of rank at most k. The minimum is $\sum_{j>k}\sigma_j^2$. Thus “best” means smallest sum of squared entrywise errors, not necessarily best label prediction or semantic preservation.
A_ZH: 保留最大的k个奇异值：$X_k=U_k\Sigma_kV_k^T$。它在秩不超过k的矩阵中最小化 $\|X-Y\|_F^2=\sum_{i,j}(X_{ij}-Y_{ij})^2$，最小值为 $\sum_{j>k}\sigma_j^2$。“最佳”指所有元素的平方误差和最小，不必然指标签预测或语义保留最好。

@@ M230 | x05-pca | check | XSVD:22; XPCA:7,16
Q_EN: Is a best rank-k approximation always unique?
Q_ZH: 最佳秩 k 近似总是唯一的吗？
A_EN: No. Equal singular values at the truncation boundary can produce different optimal approximating matrices. For $X=I_2$, k=1, every $uu^T$ with $u^Tu=1$ has squared Frobenius error 1. By contrast, simultaneously flipping both singular-vector signs in a rank-one term leaves that term unchanged; this is only nonuniqueness of its representation.
A_ZH: 不总唯一。截断边界出现相同奇异值时，可能得到不同但同样好的近似矩阵。例如 $X=I_2$、k=1，任意 $u^Tu=1$ 的 $uu^T$ 都有平方Frobenius误差1。另一方面，一项中的左右奇异向量同时反号，该项本身不变；这只是表示不唯一，不是另一个近似矩阵。

@@ M231 | x05-pca | learn | XPCA:9-12,17-18
Q_EN: Why is mean-centering essential for standard PCA?
Q_ZH: 标准 PCA 为什么需要先减去均值？
A_EN: PCA seeks variation around the mean. Form $X_c=X-\mathbf1\mu^T$ using the training mean. Its covariance is proportional to $X_c^TX_c$. Without centering, a large offset can dominate the second-moment matrix even if variation is small. Apply the same training mean to validation, test and later queries.
A_ZH: PCA 寻找围绕均值的变化。用训练均值构造 $X_c=X-\mathbf1\mu^T$，协方差与 $X_c^TX_c$ 成比例。不中心化时，即使波动很小，较大的整体偏移也可能主导二阶矩阵。验证、测试和后续样本都应减去同一个训练均值。

@@ M232 | x05-pca | learn | XPCA:10-16
Q_EN: Why is the first principal component an eigenvector of the covariance matrix?
Q_ZH: 为什么第一主成分是协方差矩阵的特征向量？
A_EN: A unit direction has variance $v^T\Sigma v$. For $L=v^T\Sigma v-\lambda(v^Tv-1)$, differentiation gives $2\Sigma v-2\lambda v=0$, hence $\Sigma v=\lambda v$. In an orthonormal eigenbasis the variance is a weighted average of eigenvalues, with nonnegative weights summing to one. Its maximum is therefore the largest eigenvalue, achieved by a corresponding unit eigenvector.
A_ZH: 单位方向的方差为 $v^T\Sigma v$。对 $L=v^T\Sigma v-\lambda(v^Tv-1)$ 求导得 $2\Sigma v-2\lambda v=0$，所以 $\Sigma v=\lambda v$。在正交特征基中，该方差是特征值的加权平均，权重非负且和为一，因此最大值就是最大特征值，由相应单位特征向量取得。

@@ M233 | x05-pca | learn | XPCA:17-18,28-30
Q_EN: What are PCA scores and the reconstructed data matrix?
Q_ZH: 什么是 PCA 得分矩阵？怎样重构数据？
A_EN: For n rows and d features, let $X_c=X-\mathbf1\mu^T$ use the training mean mu. With d-by-k orthonormal component columns $V_k$, scores are $Z=X_cV_k$ (n-by-k). Reconstruction is $\hat X=ZV_k^T+\mathbf1\mu^T$ (n-by-d). Scores are new coordinates; component vectors are the directions; adding mu restores the data location.
A_ZH: n行样本、d个特征时，用训练均值mu构造 $X_c=X-\mathbf1\mu^T$。d行k列的 $V_k$ 存正交单位主方向，得分 $Z=X_cV_k$ 为n行k列；重构 $\hat X=ZV_k^T+\mathbf1\mu^T$ 恢复为n行d列。得分是新坐标，主成分向量是方向，加回mu恢复数据的位置。

@@ M234 | x05-pca | worked | XPCA:21,25
Q_EN: Covariance eigenvalues are (9,3,2,1). How many PCs retain at least 90% variance?
Q_ZH: 协方差特征值为 (9,3,2,1)，至少保留 90% 方差需要几个主成分？
A_EN: Total variance is 15. The first two retain $12/15=80\%$, below the target. The first three retain $14/15\approx93.33\%$, so choose three. Explained variance measures this unsupervised reconstruction criterion; a low-variance direction can still matter for predicting a label.
A_ZH: 总方差为 15。前两个保留 $12/15=80\%$，未达到目标；前三个保留 $14/15\approx93.33\%$，因此需要三个。解释方差衡量的是这一无监督重构标准，低方差方向仍可能对标签预测重要。

@@ M235 | x05-pca | learn | XPCA:28-31
Q_EN: How are PCA covariance eigenvalues related to singular values of centered data?
Q_ZH: PCA 协方差特征值与中心化数据的奇异值有什么关系？
A_EN: Use compact SVD $X_c=UDV^T$, with $D=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$ and orthonormal columns of U,V. Then $X_c^TX_c=VD^2V^T$. Covariance eigenvalues are $\sigma_j^2/n$, or $\sigma_j^2/(n-1)$ when n>1; remaining eigenvalues are zero if r<d. For nonzero total variance, these common scalings give the same explained-variance ratios and principal subspaces.
A_ZH: 采用紧致SVD $X_c=UDV^T$，其中 $D=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$ 为方形对角矩阵，U、V的列正交归一。于是 $X_c^TX_c=VD^2V^T$。协方差特征值为 $\sigma_j^2/n$，或n>1时的 $\sigma_j^2/(n-1)$；r<d时其余特征值为零。总方差非零时，两种统一缩放得到相同解释方差比例与主子空间。

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
A_EN: For n training points, let $\mathbf1$ be the n-entry ones vector and $H=I-\mathbf1\mathbf1^T/n$. Use $K_c=HKH$: subtract row and column means, then add the grand mean. It centers the feature vectors represented by the kernel. Centering raw inputs need not center nonlinear features. New queries must use the training feature-space centering statistics.
A_ZH: 共有n个训练点，$\mathbf1$ 是n维全1列向量，令 $H=I-\mathbf1\mathbf1^T/n$。使用 $K_c=HKH$，即减行均值、减列均值、加总体均值。这是在核所代表的特征空间中中心化；原输入减均值不保证非线性特征也中心化，新查询仍须采用训练统计。

@@ M240 | x05-pca | check | XKPCA:10-13,20
Q_EN: Why must kernel-PCA eigenvectors be normalized using their eigenvalues?
Q_ZH: 为什么核 PCA 的系数要结合特征值进行归一化？
A_EN: Let $K_ca=\lambda_Ka$, $a^Ta=1$, and $\phi_c(x_i)$ be centered feature vectors. The squared norm of $v=\sum_i a_i\phi_c(x_i)$ is $a^TK_ca=\lambda_K$. Therefore divide v, equivalently its coefficients a, by $\sqrt{\lambda_K}$ to get a unit direction. Training scores are $K_ca/\sqrt{\lambda_K}=\sqrt{\lambda_K}a$. Only positive eigenvalues can be used in this normalization.
A_ZH: 设 $K_ca=\lambda_Ka$、$a^Ta=1$，$\phi_c(x_i)$ 为中心化特征向量。组合 $v=\sum_i a_i\phi_c(x_i)$ 的范数平方是 $a^TK_ca=\lambda_K$，所以将v（等价地将系数a）除以 $\sqrt{\lambda_K}$ 才得到单位方向。训练得分为 $K_ca/\sqrt{\lambda_K}=\sqrt{\lambda_K}a$；只可用正特征值归一化。

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
Q_EN: For a batch layer $Z=XW+b$, rows of X are samples and the row-vector bias b is added to every row. Given upstream gradient $G=\partial L/\partial Z$, find gradients with respect to X, W and b.
Q_ZH: 批量层为 $Z=XW+b$，X 逐行存样本，行向量偏置 b 加到每一行。已知上游梯度 $G=\partial L/\partial Z$，求对 X、W、b 的梯度。
A_EN: The gradients are $\nabla_W L=X^TG$, $\nabla_X L=GW^T$, and $\nabla_b L=\sum_i G_{i,:}$. Check their shapes against W, X and b. If an activation follows Z, G must already include that activation's local derivative. A mean-loss reduction must be reflected consistently in G.
A_ZH: 梯度为 $\nabla_W L=X^TG$、$\nabla_X L=GW^T$，偏置梯度为 $\nabla_b L=\sum_i G_{i,:}$。形状应分别与 W、X、b 对应。若 Z 后还有激活函数，G 必须已包含其局部导数；损失取平均时，相应缩放也应体现在 G 中。

@@ M252 | x06-networks | learn | XNN:33,35; XOPT:4-5
Q_EN: How should the output layer and loss match a neural-network task?
Q_ZH: 神经网络的输出层与损失应如何匹配任务？
A_EN: Single-label K-class: K logits, softmax probabilities, categorical cross-entropy. Binary: one logit, sigmoid probability, binary cross-entropy. Multi-label: one logit per separate yes/no target, per-label sigmoid and binary cross-entropy; probabilities need not sum to one. Unbounded real regression: linear output and, for example, squared error. A loss that expects logits already applies its probability transformation; do not apply it twice.
A_ZH: 单标签K分类：K个logit，经softmax成为类别概率，配多类交叉熵。二分类：一个logit、sigmoid概率、二元交叉熵。多标签：每个“是/否”目标一个logit，逐标签sigmoid与二元交叉熵，概率无需合计为一。无界实数回归：线性输出，可配平方误差。若损失接口要求logits，它已内含相应变换，不要重复处理。

@@ M253 | x06-networks | check | XNN:40
Q_EN: What does the universal approximation theorem guarantee, and what does it leave open?
Q_ZH: 通用逼近定理保证什么，又没有保证什么？
A_EN: For example, a network with biases, one sufficiently wide sigmoid hidden layer and a linear output can uniformly approximate any continuous real-valued function on a compact input set (closed and bounded in finite dimensions) to any chosen positive tolerance. This asserts existence of a finite network for that tolerance. It does not guarantee a small network, successful training or generalization from limited samples.
A_ZH: 例如，含偏置、单个足够宽的sigmoid隐藏层与线性输出层的网络，可在紧致输入集（有限维中闭且有界）上，把任意连续实值函数一致逼近到指定正误差内。它保证该容差下存在有限网络，不保证网络很小、训练成功，也不保证有限样本下的泛化。

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
Q_EN: A 32×32 RGB input uses ordinary dense convolution with six 5×5 filters, stride 1, dilation 1, no padding and one bias per output channel. Find output shape and parameter count.
Q_ZH: 32×32 RGB输入采用普通非分组卷积：6个5×5滤波器、步长1、膨胀率1、无填充、每输出通道一个偏置。求输出形状和参数量。
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
A_EN: Max pooling takes each window’s largest value and normally has no learned weights; convolution computes learned weighted sums. Pooling with a downsampling stride reduces resolution, whereas stride 1 with suitable padding can preserve size. Max pooling may discard within-window position information. Backpropagation routes gradient to a maximizing entry, with a stated rule for ties.
A_ZH: 最大池化取各窗口最大值，通常没有可学习权重；卷积计算可学习加权和。采用降采样步长时池化降低分辨率，步长1配适当填充则可保持尺寸。池化可能丢失窗口内位置信息；反向传播把梯度传给最大元素，并列最大时需规定处理规则。

@@ M261 | x07-cnn | worked | XCNN:26
Q_EN: Ignoring image-boundary effects, what is the theoretical receptive field of two consecutive 3×3 convolutions with stride 1 and dilation 1?
Q_ZH: 忽略图像边界影响，连续两个3×3卷积、步长1、膨胀率1时，理论感受野为多大？
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
A_EN: Full-batch descent uses all training examples for one gradient; mini-batch SGD uses a subset. An optimizer step changes parameters; an epoch processes the dataset once. “Iteration” often means one step, but check the program’s convention. For n=1000, batch size 100, one update per batch and no gradient accumulation, an epoch has ten updates. Accumulating several batches changes update count without changing the data-pass definition.
A_ZH: 全批量下降用全部训练样本求一次梯度，小批量SGD用子集。优化器步更新参数，epoch遍历一次数据；“iteration”常指一步，但应看代码约定。n=1000、batch=100、每批更新一次且无梯度累积时，一个epoch有十次更新。多批累积再更新会改变步数，不改变遍历次数定义。

@@ M266 | x08-training | learn | XOPT:9-17
Q_EN: What does momentum add to SGD?
Q_ZH: Momentum 为 SGD 增加了什么？
A_EN: Maintain velocity $v_{t+1}=\rho v_t-\eta g_t$ and update $\theta_{t+1}=\theta_t+v_{t+1}$. Past gradients influence the direction, which can reduce zigzagging and accelerate motion along persistent directions. The sign convention for v must be consistent. Momentum can still overshoot if the learning rate or velocity is too large.
A_ZH: 保存速度 $v_{t+1}=\rho v_t-\eta g_t$，再更新 $\theta_{t+1}=\theta_t+v_{t+1}$。过去梯度会影响方向，有助于减轻来回振荡，并沿持续方向加速。速度的符号约定必须一致；学习率或速度过大时，动量仍可能导致越过最优区域。

@@ M267 | x08-training | learn | XOPT:18-22
Q_EN: How do AdaGrad and RMSProp adapt coordinatewise step sizes?
Q_ZH: AdaGrad 和 RMSProp 怎样调整每个坐标的步长？
A_EN: For coordinate gradient g, AdaGrad uses $s_t=s_{t-1}+g_t^2$; RMSProp uses $s_t=\rho s_{t-1}+(1-\rho)g_t^2$, $0\le\rho<1$. Starting from zero, update each coordinate by $-\eta g_t/(\sqrt{s_t}+\epsilon)$ with $\epsilon>0$. AdaGrad remembers every squared gradient; RMSProp gradually forgets old ones. Both still require a global learning rate eta.
A_ZH: 对每坐标梯度g，AdaGrad累积 $s_t=s_{t-1}+g_t^2$；RMSProp用 $s_t=\rho s_{t-1}+(1-\rho)g_t^2$，$0\le\rho<1$。从零初始化，逐坐标更新 $-\eta g_t/(\sqrt{s_t}+\epsilon)$，其中 $\epsilon>0$。AdaGrad保留全部历史平方梯度，RMSProp逐渐遗忘旧值；两者仍需全局学习率eta。

@@ M268 | x08-training | learn | XOPT:23-24
Q_EN: What are Adam's two moment estimates and bias corrections?
Q_ZH: Adam 的两个矩估计及偏差修正是什么？
A_EN: Adam tracks a gradient mean $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ and raw second moment $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$ elementwise, starting at zero. This pulls early estimates toward zero. For t starting at 1, correct with $\hat m_t=m_t/(1-\beta_1^t)$ and $\hat v_t=v_t/(1-\beta_2^t)$. Apply $-\eta\hat m_t/(\sqrt{\hat v_t}+\epsilon)$. Here $0\le\beta_1,\beta_2<1$, $\epsilon>0$; v is not centered variance.
A_ZH: Adam逐元素维护梯度均值 $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ 与非中心二阶矩 $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$。零初始化使早期估计偏向零。t从1起，修正为 $\hat m_t=m_t/(1-\beta_1^t)$、$\hat v_t=v_t/(1-\beta_2^t)$，更新 $-\eta\hat m_t/(\sqrt{\hat v_t}+\epsilon)$。其中 $0\le\beta_1,\beta_2<1$、$\epsilon>0$；v不是中心化方差。

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
A_EN: Divide by keep probability $0<q\le1$. For a fixed activation h and mask $m\sim\mathrm{Bernoulli}(q)$, use $\tilde h=mh/q$, so its mask-average is $E_m[\tilde h]=h$. Ordinary inference disables masking and passes h. Drop rate 0.2 means q=0.8 and surviving values scale by 1.25. This single-activation expectation does not imply equality after every later nonlinearity.
A_ZH: 除以保留概率 $0<q\le1$。对固定激活h与掩码 $m\sim\mathrm{Bernoulli}(q)$，使用 $\tilde h=mh/q$，对掩码取期望有 $E_m[\tilde h]=h$。通常推理关闭掩码、直接传h。丢弃率0.2意味着q=0.8，保留值乘1.25；单个激活期望不变不代表后续任意非线性后仍相等。

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
A_EN: MSE averages squared scalar errors and forgets their spatial arrangement. Errors (1,1,1,1) and (2,0,0,0) both give MSE 1, although one is spread out and the other localized. Perceived structure and texture can therefore differ; SSIM or learned feature losses assess other properties. MSE itself does not satisfy the triangle inequality and is not a distance metric. A score ranking alone does not replace viewing the reconstruction.
A_ZH: MSE平均各标量的平方误差，会丢失误差的空间排列。误差(1,1,1,1)与(2,0,0,0)的MSE均为1，但前者分散、后者集中，所以结构和纹理感受可能不同；SSIM或学习特征损失强调其他属性。MSE本身不满足三角不等式，不是距离度量；指标排名不能替代查看重构图。

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
A_EN: Write $V=E_{x\sim p_{data}}\log D(x)+E_z\log(1-D(G(z)))$. Original GAN training is $\min_G\max_D V$: D raises the real/fake discrimination score, and G lowers V through generated examples. Equivalently D minimizes $-V$. A commonly used generator loss $-E_z\log D(G(z))$ is the non-saturating alternative, not simply the same original minimax loss with its sign flipped.
A_ZH: 令 $V=E_{x\sim p_{data}}\log D(x)+E_z\log(1-D(G(z)))$。原始GAN为 $\min_G\max_D V$：D提高真假区分得分，G通过生成样本降低V。等价地，D最小化 $-V$。常见生成器损失 $-E_z\log D(G(z))$ 是非饱和替代目标，不能当成原始极小极大损失简单反号。

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

@@ M291 | x10-generative | learn | XGEN:33-39
Q_EN: A DDPM starts from clean data x0 and uses the Gaussian forward process $x_s=\sqrt{1-\beta_s}x_{s-1}+\sqrt{\beta_s}\epsilon_s$, with independent $\epsilon_s\sim N(0,I)$ and noise variances $0<\beta_s<1$. How can training sample x_t directly without simulating steps 1 through t?
Q_ZH: DDPM 从干净数据 x0 出发，采用高斯前向过程 $x_s=\sqrt{1-\beta_s}x_{s-1}+\sqrt{\beta_s}\epsilon_s$，各 $\epsilon_s\sim N(0,I)$ 相互独立，噪声方差 $0<\beta_s<1$。训练时怎样直接采样 x_t，而不逐步模拟 1 至 t？
A_EN: Define $\bar\alpha_t=\prod_{s=1}^t(1-\beta_s)$. Draw fresh $\epsilon\sim N(0,I)$ and set $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$. The product accumulates signal retention. This has the correct conditional distribution given x0; it need not reproduce one particular previously sampled noise path.
A_ZH: 定义 $\bar\alpha_t=\prod_{s=1}^t(1-\beta_s)$，重新采样 $\epsilon\sim N(0,I)$，令 $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$。乘积累计信号保留比例。这给出给定 x0 后正确的条件分布，不要求复现先前某次逐步加噪的具体轨迹。

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
Q_EN: One attention query has scaled scores (ln 3,0), where ln is the natural logarithm, and scalar values (2,10). What is its output?
Q_ZH: 某个注意力query的缩放后分数为(ln 3,0)，ln表示自然对数；对应标量value为(2,10)。输出是多少？
A_EN: Softmax gives weights (3/4,1/4), so the weighted value is $(3/4)2+(1/4)10=4$. The scores select weights; the values supply the information being averaged. Attention weights sum to one per query, but the output does not have to be a probability.
A_ZH: Softmax 得到权重 (3/4,1/4)，所以加权输出为 $(3/4)2+(1/4)10=4$。分数决定权重，value 提供被加权的信息。每个 query 的注意力权重和为一，但输出本身不必是概率。

@@ M299 | x11-transformers | learn | XATT:14-18; XFLASH:1,3.1
Q_EN: What do multiple attention heads add, and why can global attention be expensive?
Q_ZH: 多个注意力头增加了什么能力？全局注意力为什么可能昂贵？
A_EN: Each head learns projections that combine different feature subspaces and token relationships; outputs are concatenated and projected. Dense attention compares all n-by-n token pairs, with quadratic pairwise arithmetic for fixed feature width. A naive implementation materializes n² scores per head; peak memory depends on implementation and need not store that entire matrix at once. More heads do not by themselves remove pairwise interactions.
A_ZH: 每个头学习投影，组合不同特征子空间与token关系，输出再拼接并投影。稠密注意力比较n×n个token对，固定特征宽度时两两计算量呈二次增长。朴素实现每头显式保存n²个分数；峰值内存还取决于实现，不一定同时存完整矩阵。增加头数本身不会消除两两交互。

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
A_EN: Add mutually exclusive even faces: $P(2)+P(4)+P(6)=0.1+0.2+0=0.3$. This is below a fair die's even probability 0.5. Counting three even faces out of six is valid only when all faces are equally likely.
A_ZH: 把互斥偶数面相加：$P(2)+P(4)+P(6)=0.1+0.2+0=0.3$，低于公平骰子的偶数概率0.5。只有各面等可能时，才可用三个偶数面除以六。

@@ M304 | x12-problems | historical | XHA1:1; XHA1S:1-2
Q_EN: If X takes 3, 8 and 9 with probabilities p3, p8 and p9, what is $E[I(X=8)]$?
Q_ZH: X 以 p3、p8、p9 的概率取 3、8、9，则 $E[I(X=8)]$ 是多少？
A_EN: The indicator is 0 at X=3 or 9 and 1 at X=8. Therefore its expectation is $0p_3+1p_8+0p_9=p_8$. More generally, the expected indicator of an event equals that event's probability. The expected indicator is not the indicator evaluated at the expected value of X.
A_ZH: X 为 3 或 9 时指示函数为 0，为 8 时为 1，因此期望为 $0p_3+1p_8+0p_9=p_8$。一般而言，事件指示函数的期望等于该事件的概率。它不是先求 X 的期望，再把该期望代入指示函数。

@@ M305 | x12-problems | historical | XHA1:2; XHA1S:2-3
Q_EN: For finite-valued X,Y, prove $H(X,Y)=H(Y)+H(X\mid Y)$ using base-2 logarithms and $0\log0=0$.
Q_ZH: X、Y取有限个值，以2为对数底、约定 $0\log0=0$，证明 $H(X,Y)=H(Y)+H(X\mid Y)$。
A_EN: Use $p(x,y)=p(y)p(x\mid y)$ wherever p(x,y)>0. Splitting the joint-entropy sum gives $-\sum_y[\sum_xp(x,y)]\log_2p(y)-\sum_{x,y}p(x,y)\log_2p(x\mid y)$. Since $\sum_xp(x,y)=p(y)$, the first term is H(Y). The second is the definition of H(X|Y), the average remaining uncertainty about X after observing Y. Zero-probability terms contribute zero.
A_ZH: 在p(x,y)>0处使用 $p(x,y)=p(y)p(x\mid y)$。拆开联合熵求和，得 $-\sum_y[\sum_xp(x,y)]\log_2p(y)-\sum_{x,y}p(x,y)\log_2p(x\mid y)$。因 $\sum_xp(x,y)=p(y)$，第一项为H(Y)；第二项按定义为H(X|Y)，即观察Y后X剩余不确定性的平均值。零概率项贡献零。

@@ M306 | x12-problems | historical | XHA1:2; XHA1S:2-3
Q_EN: Why does independence imply zero mutual information in the historical entropy exercise?
Q_ZH: 往年熵练习中，为什么独立意味着互信息为零？
A_EN: Mutual information averages $\log[p(x,y)/(p(x)p(y))]$ under the joint distribution. Independence makes the ratio 1 wherever joint probability is positive, and $\log1=0$. Zero-probability terms contribute zero. This is stronger than merely zero covariance, which only concerns a second-order moment.
A_ZH: 互信息是在联合分布下，对 $\log[p(x,y)/(p(x)p(y))]$ 求平均。独立时，在联合概率为正的地方，该比值等于 1，而 $\log1=0$；零概率项按零处理。这比仅有零协方差更强，后者只描述二阶矩。

@@ M307 | x12-problems | historical | XHA1:2; XHA1S:3-5
Q_EN: Within one class, IID observations have Laplace density $p(x\mid\mu,b)=(2b)^{-1}e^{-|x-\mu|/b}$, with location mu and scale b>0. Find their maximum-likelihood estimates.
Q_ZH: 某类的观测独立同分布，Laplace密度为 $p(x\mid\mu,b)=(2b)^{-1}e^{-|x-\mu|/b}$，mu为位置、b>0为尺度。求两参数的最大似然估计。
A_EN: Let n>0 and $S(\mu)=\sum_i|x_i-\mu|$. The log likelihood is $-n\log(2b)-S(\mu)/b$. A sample median minimizes S, so choose it as mu. Differentiating in b gives $-n/b+S/b^2=0$, hence $\hat b=S(\hat\mu)/n$ when S>0. Even samples may admit a median interval. If all values coincide, S=0 and likelihood diverges as b approaches zero; no positive-scale unconstrained MLE exists.
A_ZH: 令样本数n>0，$S(\mu)=\sum_i|x_i-\mu|$，对数似然为 $-n\log(2b)-S(\mu)/b$。中位数使S最小，所以mu取样本中位数；对b求导得 $-n/b+S/b^2=0$，S>0时 $\hat b=S(\hat\mu)/n$。偶数样本可有中位数区间。若观测全相同，S=0，b趋零时似然无界，不存在正尺度的无约束MLE。

@@ M308 | x12-problems | historical | XHA1:2; XHA1S:5-6
Q_EN: Why does binary LDA with shared covariance yield a sigmoid posterior?
Q_ZH: 共享协方差的二分类 LDA 为什么产生 sigmoid 后验？
A_EN: For positive priors and common positive-definite Sigma, quadratic terms cancel in the Gaussian log ratio. Thus log odds are $w^Tx+b$, where $w=\Sigma^{-1}(\mu_1-\mu_0)$ and $b=\log(\pi_1/\pi_0)-(\mu_1^T\Sigma^{-1}\mu_1-\mu_0^T\Sigma^{-1}\mu_0)/2$. Converting odds to probability gives $\sigma(w^Tx+b)$. Unequal class covariances generally leave a quadratic boundary.
A_ZH: 类别先验为正且共享正定 Sigma 时，高斯对数比中的二次项抵消。因此对数优势为 $w^Tx+b$，其中 $w=\Sigma^{-1}(\mu_1-\mu_0)$，$b=\log(\pi_1/\pi_0)-(\mu_1^T\Sigma^{-1}\mu_1-\mu_0^T\Sigma^{-1}\mu_0)/2$。把优势换成概率得到 $\sigma(w^Tx+b)$。不同类别协方差通常会留下二次边界。

@@ M309 | x12-problems | historical | XHA1:3-4; XHA1S:6-8
Q_EN: A joint Gaussian vector is split into x_a and x_b. Define mean blocks $\mu_a,\mu_b$ and covariance blocks $\Sigma_{ij}=\operatorname{Cov}(x_i,x_j)$ for i,j in {a,b}. Its joint covariance is positive definite. What are the mean and covariance of x_b given x_a?
Q_ZH: 联合高斯向量分为 x_a、x_b。均值分块为 $\mu_a,\mu_b$，协方差分块定义为 $\Sigma_{ij}=\operatorname{Cov}(x_i,x_j)$，其中 i,j 属于 {a,b}。联合协方差正定。给定 x_a 后，x_b 的均值和协方差是什么？
A_EN: The conditional distribution is Gaussian, with mean $\mu_b+\Sigma_{ba}\Sigma_{aa}^{-1}(x_a-\mu_a)$ and covariance $\Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab}$. The observed deviation of x_a shifts the predicted mean of x_b; the conditional covariance does not depend on that observed value. Positive definiteness ensures the required inverse exists.
A_ZH: 条件分布仍为高斯，均值为 $\mu_b+\Sigma_{ba}\Sigma_{aa}^{-1}(x_a-\mu_a)$，协方差为 $\Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab}$。x_a 的观测偏差会调整 x_b 的预测均值；条件协方差不依赖此次观测的具体值。正定条件保证所需逆矩阵存在。

@@ M310 | x12-problems | historical | XHA2:1; XHA2S:1-2
Q_EN: Historical Assignment 2 reports frequencies (100,81,34,9,6) for counts (0,1,2,3,4+). Under what assumption does the empirical mean, used to estimate a Poisson rate, equal the provided 0.8696?
Q_ZH: 往年 Assignment 2 中，计数 (0,1,2,3,4+) 的频数为 (100,81,34,9,6)。用经验均值估计泊松率时，所给 0.8696 依赖什么假设？
A_EN: The provided solution explicitly assumes every 4+ observation equals 4, giving $(81+68+27+24)/230=0.8696$. Without that assumption, the exact empirical mean is unknown and at least this large. If treating 4+ as censored Poisson data, maximize the grouped likelihood with a $P_\lambda(X\ge4)^6$ term instead of silently replacing all tail counts by 4.
A_ZH: 配套解答明确假设所有 4+ 观测都等于 4，得到 $(81+68+27+24)/230=0.8696$。不作这一假设，就不知道精确样本均值，只能知道其至少这么大。若将 4+ 当作删失的 Poisson 数据，应在分组似然中使用 $P_\lambda(X\ge4)^6$，不能默默把全部尾部计数替换成 4。

@@ M311 | x12-problems | historical | XHA2:1-2; XHA2S:2-4
Q_EN: Derive the gradient of $\ell(u,v)=(ue^v-2ve^{-u})^2$ for the historical gradient-descent exercise.
Q_ZH: 推导往年梯度下降题中 $\ell(u,v)=(ue^v-2ve^{-u})^2$ 的梯度。
A_EN: Let $q=ue^v-2ve^{-u}$. The chain rule gives $\partial_u\ell=2q(e^v+2ve^{-u})$ and $\partial_v\ell=2q(ue^v-2e^{-u})$. For simultaneous gradient descent, compute both derivatives at the old (u,v), then update both coordinates. Updating u first and using that new value in the v derivative implements a different procedure.
A_ZH: 令 $q=ue^v-2ve^{-u}$。链式法则给出 $\partial_u\ell=2q(e^v+2ve^{-u})$ 和 $\partial_v\ell=2q(ue^v-2e^{-u})$。同时梯度下降应先在旧 (u,v) 处计算两个导数，再更新两个坐标。先更新 u，再用新 u 算 v 的导数，会变成不同算法。

@@ M312 | x12-problems | historical | XHA2:1-2; XHA2S:2-4
Q_EN: For $\ell=(ue^v-2ve^{-u})^2$, start at (1,1), step size 0.1, double precision. How should simultaneous gradient descent find the first update with $\ell<10^{-14}$? Give the stopping count.
Q_ZH: 对 $\ell=(ue^v-2ve^{-u})^2$，从(1,1)开始、步长0.1、双精度，怎样用同时梯度下降找首次满足 $\ell<10^{-14}$ 的更新？给出停止计数。
A_EN: At the old pair compute $q=ue^v-2ve^{-u}$, $g_u=2q(e^v+2ve^{-u})$ and $g_v=2q(ue^v-2e^{-u})$. Then replace both coordinates by $(u-0.1g_u,v-0.1g_v)$, increment the count, and evaluate the new loss. Do not round intermediate values. The first passing update is 10; parameters round to (0.045,0.024). Updating one coordinate before computing the other gradient changes the algorithm.
A_ZH: 先在旧参数对计算 $q=ue^v-2ve^{-u}$、$g_u=2q(e^v+2ve^{-u})$、$g_v=2q(ue^v-2e^{-u})$，再同时换为 $(u-0.1g_u,v-0.1g_v)$，计数加一并检查新损失，中途不舍入。首次达标为第10次，参数舍入为(0.045,0.024)。先更新一个坐标再求另一梯度是不同算法。

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
A_EN: For constraints $y_i(w^Tx_i+b)\ge1$, set $L=\frac12\|w\|^2+\sum_i\alpha_i[1-y_i(w^Tx_i+b)]$, $\alpha_i\ge0$. Minimizing in w,b yields $w=\sum_i\alpha_i y_ix_i$ and $\sum_i\alpha_i y_i=0$. Substitution gives $\max_\alpha\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j$, subject to those alpha constraints. Hard margin has no upper bound; adding linear slack penalty $C\sum_i\xi_i$ adds $\alpha_i\le C$.
A_ZH: 约束为 $y_i(w^Tx_i+b)\ge1$，取 $L=\frac12\|w\|^2+\sum_i\alpha_i[1-y_i(w^Tx_i+b)]$、$\alpha_i\ge0$。对w、b最小化得 $w=\sum_i\alpha_i y_ix_i$、$\sum_i\alpha_i y_i=0$。代回得到 $\max_\alpha\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j$，满足上述乘子约束。硬间隔无上界；线性松弛罚 $C\sum_i\xi_i$ 才加入 $\alpha_i\le C$。

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
Q_EN: For least squares, use residual $r=Xw-y$ and let x_k be column k of X. With other weights fixed, derive the coordinate increment and residual update when $x_k^Tx_k>0$.
Q_ZH: 最小二乘采用残差 $r=Xw-y$，x_k为X第k列。固定其他权重且 $x_k^Tx_k>0$，推导坐标增量与残差更新。
A_EN: An increment delta gives objective $\frac12\|r+\delta x_k\|^2$. Its derivative is $x_k^Tr+\delta x_k^Tx_k$, so $\Delta w_k=-x_k^Tr/(x_k^Tx_k)$. Set $w_k\leftarrow w_k+\Delta w_k$ and $r\leftarrow r+\Delta w_kx_k$. A zero column cannot use this division. The historical solution uses the opposite residual $y-Xw$, so its signs reverse consistently.
A_ZH: 增量delta后的目标为 $\frac12\|r+\delta x_k\|^2$，导数为 $x_k^Tr+\delta x_k^Tx_k$。令零得 $\Delta w_k=-x_k^Tr/(x_k^Tx_k)$，再更新 $w_k\leftarrow w_k+\Delta w_k$、$r\leftarrow r+\Delta w_kx_k$。零列不能用于相除；往年解答使用反号残差 $y-Xw$，对应更新符号也一起反转。

@@ M320 | x12-problems | historical | XHA3:2-3; XHA3S:6-8
Q_EN: Why can the nonnegative-slack constraints be omitted in squared-slack SVM?
Q_ZH: 平方松弛惩罚 SVM 中，为什么可以省略松弛变量非负约束？
A_EN: Suppose a feasible point has $\xi_i<0$ under $y_if(x_i)\ge1-\xi_i$. Replacing xi by zero makes the margin constraint weaker and reduces $C\xi_i^2$ for C>0. Therefore no optimum needs negative slack. This argument is specific to the stated objective and constraint; do not remove constraints from other formulations without checking.
A_ZH: 若某可行点在 $y_if(x_i)\ge1-\xi_i$ 下满足 $\xi_i<0$，把 xi 换成零会放宽间隔约束，并在 C>0 时降低 $C\xi_i^2$。因此最优解无需负松弛量。该论证依赖此目标与约束，不能不加检查地删除其他模型的约束。

@@ M321 | x12-problems | historical | XHA3:3; XHA3S:6-8
Q_EN: Use squared-slack SVM objective $\frac12\|w\|^2+C\sum_i\xi_i^2$, C>0, with $y_i(w^Tx_i+b)\ge1-\xi_i$ and labels $y_i\in\{-1,1\}$. How does its dual differ from linear-slack SVM?
Q_ZH: 平方松弛SVM目标为 $\frac12\|w\|^2+C\sum_i\xi_i^2$，C>0；约束 $y_i(w^Tx_i+b)\ge1-\xi_i$，标签 $y_i\in\{-1,1\}$。对偶与线性松弛SVM有何不同？
A_EN: For $\frac12\|w\|^2+C\sum_i\xi_i^2$, stationarity gives $\xi_i=\alpha_i/(2C)$. The dual maximizes $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j-\sum_i\alpha_i^2/(4C)$, subject to $\alpha_i\ge0$ and $\sum_i\alpha_i y_i=0$. There is no ordinary upper bound C; an added quadratic penalty plays that role differently.
A_ZH: 对 $\frac12\|w\|^2+C\sum_i\xi_i^2$，驻点条件给出 $\xi_i=\alpha_i/(2C)$。对偶最大化 $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j-\sum_i\alpha_i^2/(4C)$，约束为 $\alpha_i\ge0$、$\sum_i\alpha_i y_i=0$。这里没有普通的上界 C，而是增加了不同作用的二次惩罚。

@@ M322 | x12-problems | historical | XHA4:1; XHA4S:1-2
Q_EN: Why are eigenvalues of a real symmetric matrix real, and distinct-eigenvalue eigenvectors orthogonal?
Q_ZH: 为什么实对称矩阵的特征值为实数，不同特征值对应的特征向量正交？
A_EN: Here * means conjugate transpose. A real symmetric A obeys $A^*=A$. For a nonzero possibly complex eigenvector v, $\overline{v^*Av}=v^*A^*v=v^*Av$, so $\lambda=(v^*Av)/(v^*v)$ is real because $v^*v>0$. For real eigenvectors u,v, $\lambda u^Tv=(Au)^Tv=u^TAv=\mu u^Tv$. Distinct eigenvalues force $u^Tv=0$; repeated ones allow an orthonormal basis but do not force every chosen pair to be orthogonal.
A_ZH: *表示共轭转置，实对称A满足 $A^*=A$。对非零、可为复数的特征向量v，$\overline{v^*Av}=v^*A^*v=v^*Av$，即分子为实数；又 $v^*v>0$，所以 $\lambda=(v^*Av)/(v^*v)$ 为实数。实特征向量u、v满足 $\lambda u^Tv=(Au)^Tv=u^TAv=\mu u^Tv$；特征值不同则内积为零，重值空间虽可选正交基，但任意选的向量未必正交。

@@ M323 | x12-problems | historical | XHA4:1; XHA4S:2-4; XPCA:14-16
Q_EN: Prove that the k-th PCA direction can be chosen as an eigenvector for the k-th largest covariance eigenvalue.
Q_ZH: 证明 PCA 的第 k 个方向可选为协方差矩阵第 k 大特征值对应的特征向量。
A_EN: Choose an orthonormal eigenbasis with $\lambda_1\ge\cdots\ge\lambda_d$. A unit vector orthogonal to the first k-1 basis vectors has $v=\sum_{j\ge k}c_ju_j$ with $\sum c_j^2=1$. Its variance is $\sum_{j\ge k}\lambda_jc_j^2\le\lambda_k$, achieved by $v=u_k$. Ties can make the maximizing direction nonunique.
A_ZH: 选取正交归一特征基，使 $\lambda_1\ge\cdots\ge\lambda_d$。与前 k-1 个基向量正交的单位向量可写成 $v=\sum_{j\ge k}c_ju_j$，且 $\sum c_j^2=1$。其方差为 $\sum_{j\ge k}\lambda_jc_j^2\le\lambda_k$，取 $v=u_k$ 即达到上界。出现相同特征值时，最大化方向可能不唯一。

@@ M324 | x12-problems | historical | XHA4:1,3; XHA4S:4,7
Q_EN: The two figures provide three input/output pairs and a fourth input x4 for a linear discrete-time system; unmarked samples are zero. Express x4 as a combination of x1,x2,x3, derive y4, and test whether the given responses are time invariant.
Q_ZH: 两张图给出一个线性离散时间系统的三组输入/输出及第四个输入 x4，未标出的采样值均为零。用 x1、x2、x3 组合出 x4，求 y4，并判断所给响应是否满足时不变性。
MEDIA_FRONT: extra-ha4-page3-image1.png;extra-ha4-page3-image2.png
A_EN: The inputs give $x_4=2x_1-2x_2+x_3$, so linearity gives $y_4=2y_1-2y_2+y_3$. Its nonzero values at n=(-1,0,1,2) are (2,1,2,-2). The system is not time invariant: $x_2=x_1[n]+x_1[n-1]$, but the supplied y2 is not $y_1[n]+y_1[n-1]$. Linearity alone does not imply shift invariance.
A_ZH: 由输入可得 $x_4=2x_1-2x_2+x_3$，线性性给出 $y_4=2y_1-2y_2+y_3$。在 n=(-1,0,1,2) 处的非零值为 (2,1,2,-2)。系统并非时不变：虽然 $x_2=x_1[n]+x_1[n-1]$，题给 y2 却不等于 $y_1[n]+y_1[n-1]$。线性并不蕴含平移不变。

@@ M325 | x12-problems | historical | XHA4:1-2,4; XHA4S:5,8
Q_EN: Compute full discrete convolution: (1) x=(1,1,1,1), h=(2,2,2,2), both starting at n=0; (2) $x[n]=0.5\delta[n-2]$, h=(1,2,3,2,1) starting at 0. Here delta[n] is 1 at n=0 and 0 elsewhere; unspecified samples are zero. Give values and indices.
Q_ZH: 求完整离散卷积：(1)x=(1,1,1,1)、h=(2,2,2,2)，均从n=0开始；(2)$x[n]=0.5\delta[n-2]$，h=(1,2,3,2,1)从0开始。delta[n]在n=0为1、其余为0，未指定样本均为零。给出值与下标。
MEDIA_FRONT: extra-ha4-page4-image1.png;extra-ha4-page4-image2.png
A_EN: First, x is four ones and h is four twos, both supported at n=0..3. Their convolution at n=0..6 is (2,4,6,8,6,4,2). Second, $x[n]=0.5\delta[n-2]$, so $y[n]=0.5h[n-2]$. With h=(1,2,3,2,1) at n=0..4, y=(0.5,1,1.5,1,0.5) at n=2..6, and zero elsewhere.
A_ZH: 第一例中，x 为四个 1，h 为四个 2，支撑均为 n=0..3，卷积在 n=0..6 处为 (2,4,6,8,6,4,2)。第二例 $x[n]=0.5\delta[n-2]$，故 $y[n]=0.5h[n-2]$。h 在 n=0..4 为 (1,2,3,2,1)，所以 y 在 n=2..6 为 (0.5,1,1.5,1,0.5)，其余位置为零。

@@ M326 | x12-problems | historical | XHA4:2; XHA4S:5-6
Q_EN: For absolutely summable sequences, define DTFT $X(\omega)=\sum_nx[n]e^{-j\omega n}$, where $j^2=-1$ and omega is angular frequency. With $z[n]=\sum_mx[m]y[n-m]$, what substitution proves $Z(\omega)=X(\omega)Y(\omega)$?
Q_ZH: 对绝对可和序列，定义离散时间傅里叶变换DTFT：$X(\omega)=\sum_nx[n]e^{-j\omega n}$，$j^2=-1$、omega为角频率。给定 $z[n]=\sum_mx[m]y[n-m]$，用什么变量替换证明 $Z(\omega)=X(\omega)Y(\omega)$？
A_EN: Start with $\sum_n\sum_m x[m]y[n-m]e^{-j\omega n}$ and set t=n-m. Under conditions allowing the sums to be exchanged, such as absolute summability, it factors into $(\sum_m x[m]e^{-j\omega m})(\sum_t y[t]e^{-j\omega t})=X(\omega)Y(\omega)$. The exponential also splits because n=t+m.
A_ZH: 从 $\sum_n\sum_m x[m]y[n-m]e^{-j\omega n}$ 出发，令 t=n-m。在绝对可和等允许交换求和的条件下，可分解成 $(\sum_m x[m]e^{-j\omega m})(\sum_t y[t]e^{-j\omega t})=X(\omega)Y(\omega)$。指数项能够拆开，是因为 n=t+m。
