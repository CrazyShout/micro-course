# CS5489 bilingual card source — editable master text

@@ M001 | 01-map | learn | I:23-28
Q_EN: What is supervised learning, and what are a feature, a label and a model?
Q_ZH: 什么是监督学习？特征、标签和模型分别是什么？
A_EN: A feature vector $x$ describes an example; a label $y$ is the target supplied during training. A model learns a rule $f$ from labeled pairs $(x_i,y_i)$ and predicts $f(x)$ for new inputs. For SMS classification, the message's word counts are features and normal/spam/smishing is the label. Training fits the rule; inference applies it.
A_ZH: 特征向量 $x$ 描述一个样本，标签 $y$ 是训练时提供的目标。模型从带标签的样本对 $(x_i,y_i)$ 学到规则 $f$，再对新输入预测 $f(x)$。例如短信分类中，词频可以作为特征，正常/垃圾/钓鱼短信是标签。训练是拟合规则，推理是应用规则。

@@ M002 | 01-map | learn | I:23-25
Q_EN: How do classification and regression differ?
Q_ZH: 分类和回归有什么区别？
A_EN: Classification predicts a discrete class, such as one of three SMS categories. Regression predicts a numerical quantity, such as tomorrow's temperature. The output type determines the model and evaluation metric: class accuracy is meaningful for classification, while a numerical prediction error is natural for regression. A class encoded as 0, 1 or 2 is still a category, not a continuous amount.
A_ZH: 分类预测离散类别，例如三种短信类型之一；回归预测数值，例如明天的温度。输出类型决定模型和评估指标：分类可看分类准确率，回归通常看数值误差。把类别编码为 0、1、2，并不意味着它们成为连续数值或有大小距离关系。

@@ M003 | 01-map | learn | I:23-25
Q_EN: What is the basic train–validate–test workflow?
Q_ZH: 训练—验证—测试的基本流程是什么？
A_EN: Fit parameters on training data. Use validation data, or cross-validation within training data, to choose settings such as smoothing strength. After choices are fixed, evaluate on held-out test data. A good training score alone does not show generalization: the model may have memorized training examples. Keep the same feature transformation at inference.
A_ZH: 用训练数据拟合参数；用验证数据，或训练集内部的交叉验证，选择平滑强度等设置；固定选择后再用留出的测试数据评估。训练分数高并不能证明泛化好，模型可能记住了训练样本。推理时应使用与训练一致的特征转换。

@@ M004 | 01-map | learn | I:24-26
Q_EN: What is the difference between a parameter and a hyperparameter?
Q_ZH: 参数和超参数有什么区别？
A_EN: A parameter is learned from data, such as a class mean or word probability. A hyperparameter controls the learning procedure or model family, such as the smoothing value $\alpha$ or vocabulary cutoff. Fit parameters on the training split; compare hyperparameters using validation. Choosing a hyperparameter after looking at test scores makes the test less independent.
A_ZH: 参数由数据估计，例如每类的均值或单词概率；超参数控制学习过程或模型形式，例如平滑系数 $\alpha$ 和词表筛选阈值。参数在训练集上拟合，超参数通过验证比较。看到测试分数后再改超参数，会破坏测试评估的独立性。

@@ M007 | 02-python | learn | P1:1-14
Q_EN: How does a Jupyter notebook execute, and why can execution order cause bugs?
Q_ZH: Jupyter Notebook 如何执行？为什么运行顺序可能导致错误？
A_EN: Markdown cells explain; code cells execute in a shared kernel that keeps variables in memory. Running a later cell first may use an old value or an undefined variable. Before trusting a result, restart the kernel and run all cells from top to bottom. Save outputs together with the code so another reader can follow the computation.
A_ZH: Markdown 单元解释内容；代码单元在共享的内核中执行，变量会留在内存里。先运行后面的单元可能使用旧值，或遇到未定义变量。确认结果前应重启内核并从上到下运行所有单元。把输出和代码一起保存，方便别人追踪计算过程。

@@ M008 | 02-python | learn | P1:15-28
Q_EN: What do assignment, equality and Python's basic numeric operators mean?
Q_ZH: Python 的赋值、相等比较和基本数值运算分别是什么意思？
A_EN: `x = 3` assigns a value; `x == 3` returns a Boolean comparison. With positive integers, `7 / 2` is 3.5, `7 // 2` is 3, `7 % 2` is 1, and `2 ** 3` is 8. Integer, float, Boolean and string values have different types. `%` tests divisibility: `n % d == 0` means $d$ divides $n$.
A_ZH: `x = 3` 给变量赋值；`x == 3` 返回布尔比较结果。对这里的正整数，`7 / 2` 为 3.5，`7 // 2` 为 3，`7 % 2` 为 1，`2 ** 3` 为 8。整数、浮点数、布尔值、字符串是不同类型。`%` 可测试整除：`n % d == 0` 表示 $d$ 是 $n$ 的因数。

@@ M009 | 02-python | learn | P1:29-57
Q_EN: How do list indexing and slicing work?
Q_ZH: 列表的索引与切片如何使用？
A_EN: Python starts at index 0. For `a = [10,20,30,40]`, `a[0]` is 10, `a[-1]` is 40, and `a[1:3]` is `[20,30]`. A slice includes its start and excludes its stop. `a[::2]` takes every second element. Out-of-range single indexing raises an error; slicing can stop at the available end.
A_ZH: Python 索引从 0 开始。若 `a = [10,20,30,40]`，则 `a[0]` 为 10，`a[-1]` 为 40，`a[1:3]` 为 `[20,30]`。切片包含起点，不包含终点；`a[::2]` 每隔一个取一个。单个索引越界会报错，切片则可在实际末尾结束。

@@ M010 | 02-python | learn | P1:29-64
Q_EN: When should I use a list, tuple or string?
Q_ZH: 什么时候用列表、元组或字符串？
A_EN: A list is an ordered mutable collection; a tuple is an ordered immutable collection; a string is an immutable text sequence. Use a list to accumulate predictions, a tuple for a fixed pair such as `(mean, variance)`, and strings for SMS text. Reassigning a variable is different from changing the object it refers to.
A_ZH: 列表是有序、可修改的集合；元组是有序、不可修改的集合；字符串是不可修改的文本序列。收集预测结果可用列表，固定的 `(均值, 方差)` 可用元组，短信文本用字符串。给变量重新赋值，和修改变量指向的对象，是两件不同的事。

@@ M011 | 02-python | learn | P1:64-95
Q_EN: How do dictionaries and sets support text processing?
Q_ZH: 字典和集合如何帮助处理文本？
A_EN: A dictionary maps unique keys to values, for example `{'free': 3}` stores a word count. A set stores distinct elements and supports membership, union and intersection. `set(['a','a','b'])` contains only `a` and `b`. A set loses repetition counts, so it cannot replace a count vector when frequency matters.
A_ZH: 字典把唯一的键映射到值，例如 `{'free': 3}` 保存词频。集合保存互不重复的元素，支持成员判断、并集和交集。`set(['a','a','b'])` 只包含 `a` 和 `b`。集合丢失重复次数，因此需要词频时不能用它替代计数向量。

@@ M012 | 02-python | learn | P1:96-124
Q_EN: How do conditions, loops and comprehensions express a computation?
Q_ZH: 条件、循环和列表推导式怎样表达计算？
A_EN: `if` chooses a branch using a Boolean condition. `for` iterates over a sequence; `while` repeats while a condition holds. Indentation defines each block. `[n*n for n in range(1,4)]` produces `[1,4,9]`; `range` excludes its stop. A comprehension is useful for a short transformation, while a loop is clearer for several steps.
A_ZH: `if` 根据布尔条件选择分支；`for` 遍历序列；`while` 在条件成立时重复。缩进决定代码块。`[n*n for n in range(1,4)]` 得到 `[1,4,9]`，因为 `range` 不包含终点。简短转换适合推导式，多步骤过程通常用循环更清楚。

@@ M013 | 02-python | learn | P1:125-136
Q_EN: What is the difference between returning and printing a function result?
Q_ZH: 函数中的 return 和 print 有什么区别？
A_EN: `return` sends a value to the caller so later code can use it. `print` only displays text. A function without an explicit return returns `None`. For example, a factor-counting function should return an integer; a Gram–Schmidt function should return an array. Printing the right number does not make that number the function's output value.
A_ZH: `return` 把值交给调用者，后续代码可以继续使用；`print` 只是显示文本。没有显式 `return` 的函数返回 `None`。例如数因数的函数应返回整数，Gram–Schmidt 函数应返回数组。屏幕上打印出正确数字，不等于函数真的返回了这个数字。

@@ M014 | 02-python | learn | P1:125-136
Q_EN: What are arguments, local variables and default arguments?
Q_ZH: 什么是函数参数、局部变量和默认参数？
A_EN: Arguments supply a function's inputs; variables created inside a function are normally local. A default argument supplies a value when the caller omits it, for example `def scale(x, factor=2): return x*factor`. Calling `scale(3)` gives 6, while `scale(3,4)` gives 12. Explicit inputs and return values make experiments easier to reproduce than hidden global state.
A_ZH: 调用参数为函数提供输入，函数内创建的变量通常是局部变量。默认参数在调用者省略时提供默认值，例如 `def scale(x, factor=2): return x*factor`。`scale(3)` 得到 6，`scale(3,4)` 得到 12。明确的输入和返回值比依赖隐藏全局状态更利于复现实验。

@@ M015 | 02-python | learn | P1:137-154
Q_EN: What are a class, an instance, an attribute and a method?
Q_ZH: 类、实例、属性和方法分别是什么？
A_EN: A class defines an object's structure and behavior. An instance is one object created from it. Attributes store state; methods are functions attached to the object. In a classifier, learned means can be attributes, while `fit` and `predict` are methods. `self` refers to the current instance, and `__init__` initializes its state.
A_ZH: 类定义对象的结构与行为，实例是依据类创建的具体对象。属性保存状态，方法是附属于对象的函数。在分类器中，学到的均值可作为属性，`fit` 和 `predict` 是方法。`self` 指当前实例，`__init__` 初始化实例状态。

@@ M016 | 02-python | learn | P1:146-154
Q_EN: What does inheritance add to a Python class?
Q_ZH: Python 类的继承有什么作用？
A_EN: A child class can reuse behavior from a parent and override selected methods. For example, a base classifier can define an interface while a Gaussian classifier implements its own probability calculation. An instance method operates on one object's state; a class method receives the class through `cls`. Inheritance is an organization tool, not an improvement in statistical accuracy.
A_ZH: 子类可以复用父类行为，并重写某些方法。例如基类定义分类器接口，高斯分类器实现自己的概率计算。实例方法操作某个对象的状态，类方法通过 `cls` 接收类本身。继承是组织程序的方法，不会自动提升统计预测精度。

@@ M017 | 02-python | learn | P1:155-168
Q_EN: How do text files, CSV and pickle differ?
Q_ZH: 文本文件、CSV 和 pickle 有什么区别？
A_EN: Plain text stores characters; CSV organizes text into rows and columns with quoting rules; pickle stores Python objects in a Python-specific binary representation. Use `with open(...)` to close files reliably. Use a CSV parser rather than splitting every comma, because messages may contain quoted commas. Load pickle only from a trusted source, since unpickling can execute code.
A_ZH: 纯文本保存字符；CSV 按带引号规则的行列组织文本；pickle 用 Python 专用二进制表示保存对象。用 `with open(...)` 保证文件关闭。短信可能含被引号包住的逗号，因此应使用 CSV 解析器，不能简单按所有逗号切分。只读取可信来源的 pickle，因为反序列化可能执行代码。

@@ M018 | 02-python | learn | P1:169-179
Q_EN: How do exceptions and pandas help debug a data pipeline?
Q_ZH: 异常处理和 pandas 如何帮助检查数据流程？
A_EN: An exception reports that an operation failed; catch a specific expected error with `try/except` and explain or fix it. Do not silently replace failed data loading with fake results. A pandas DataFrame is a labeled table: inspect columns, shape, missing values and sample rows after loading. Confirm IDs and labels before converting the table to NumPy arrays.
A_ZH: 异常说明某个操作失败；用 `try/except` 捕获明确预期的错误，并解释或修复。不要在读取失败后悄悄生成假结果。pandas DataFrame 是带标签的表格，读取后应检查列、形状、缺失值与样例行。转成 NumPy 数组前，先确认 ID 和标签对应关系。

@@ M019 | 02-python | check | P1:29-43;P2:110-121
Q_EN: Why can `b = a` make changes appear in both variables?
Q_ZH: 为什么 `b = a` 后修改一个变量，另一个也可能发生变化？
A_EN: Assignment can make two names refer to the same mutable object. With `a = [1,2]` and `b = a`, changing `b[0]` changes `a[0]`. For a flat list, `a.copy()` creates a separate list; nested objects still need care. NumPy slices often share data too, so use `.copy()` when an independent data buffer is required.
A_ZH: 赋值可能让两个名字指向同一个可变对象。若 `a = [1,2]`、`b = a`，修改 `b[0]` 也会改变 `a[0]`。对平坦列表，`a.copy()` 会创建独立列表；嵌套对象还需注意浅拷贝。NumPy 切片也经常共享数据，需要独立数据缓冲区时应使用 `.copy()`。

@@ M020 | 02-python | worked | P1:105-136;T1:14-18
Q_EN: Write the logic for counting proper factors of a positive integer $n$.
Q_ZH: 如何编写正整数 $n$ 的真因数计数逻辑？
A_EN: Here the tutorial excludes both 1 and $n$. Inspect integers $d=2,\ldots,n-1$ and count those with zero remainder. A compact function body is `return sum(n % d == 0 for d in range(2, n))`. For $n=12$, the factors counted are 2, 3, 4 and 6, giving 4. For a prime such as 7, the count is 0.
A_ZH: 本教程规定不计 1 和 $n$ 本身。检查 $d=2,\ldots,n-1$，统计余数为 0 的项。简洁的函数体是 `return sum(n % d == 0 for d in range(2, n))`。例如 $n=12$ 时计入 2、3、4、6，共 4 个；质数 7 的计数为 0。

@@ M021 | 03-numpy | learn | P2:3-19
Q_EN: What is a NumPy array, and what do shape, ndim and dtype describe?
Q_ZH: 什么是 NumPy 数组？shape、ndim 和 dtype 分别描述什么？
A_EN: An array stores a regular collection of values with a common data type. `shape` gives axis lengths, `ndim` gives the number of axes, and `dtype` gives the element type. For $N$ examples with $d$ features, use $X\in\mathbb{R}^{N\times d}$: rows are examples and columns are features. Writing this convention down prevents many indexing errors.
A_ZH: 数组保存规则排列、具有共同数据类型的数值。`shape` 给出各轴长度，`ndim` 给出轴数，`dtype` 给出元素类型。若有 $N$ 个样本、每个有 $d$ 个特征，可写成 $X\in\mathbb{R}^{N\times d}$：行对应样本，列对应特征。明确这个约定能避免很多索引错误。

@@ M022 | 03-numpy | learn | P2:10-33
Q_EN: How do arange, linspace, zeros and ones differ?
Q_ZH: arange、linspace、zeros 和 ones 有什么区别？
A_EN: `np.arange(start, stop, step)` specifies a step and normally excludes `stop`. `np.linspace(start, stop, num)` specifies a number of evenly spaced samples and includes the endpoint by default. `np.zeros((2,3))` and `np.ones((2,3))` create arrays with two rows and three columns. Prefer an explicit shape and dtype when allocating numerical work arrays.
A_ZH: `np.arange(start, stop, step)` 指定步长，通常不包含 `stop`；`np.linspace(start, stop, num)` 指定等间隔采样的个数，默认包含终点。`np.zeros((2,3))` 和 `np.ones((2,3))` 创建两行三列的数组。分配数值计算数组时，最好明确形状和数据类型。

@@ M023 | 03-numpy | worked | P2:20-49
Q_EN: For a data matrix $X$ of shape $(100,4)$, what do `X[:,1]` and `X[:,1:2]` return?
Q_ZH: 数据矩阵 $X$ 的形状为 $(100,4)$，`X[:,1]` 与 `X[:,1:2]` 返回什么？
A_EN: Both select the second feature of every sample. `X[:,1]` has shape `(100,)`, a one-dimensional array. `X[:,1:2]` has shape `(100,1)`, a two-dimensional column. This distinction matters for broadcasting and APIs that expect a two-dimensional feature matrix. The colon before the comma means all rows.
A_ZH: 两者都取所有样本的第二个特征。`X[:,1]` 形状是 `(100,)`，是一维数组；`X[:,1:2]` 形状是 `(100,1)`，保留二维列。广播和要求二维特征矩阵的接口会区分它们。逗号前的冒号表示选择所有行。

@@ M024 | 03-numpy | learn | P2:20-43
Q_EN: How does Boolean indexing select a class from a dataset?
Q_ZH: 如何用布尔索引选出某一类别的数据？
A_EN: If `y` contains one label per row of `X`, then `mask = (y == c)` marks samples of class $c$, and `X[mask]` selects those rows. To count them, use `mask.sum()`. Parenthesize elementwise conditions, for example `(y == 0) | (y == 1)`. Python's scalar `and/or` do not replace NumPy's elementwise `&/|` operations.
A_ZH: 若 `y` 的每个标签对应 `X` 的一行，`mask = (y == c)` 标记类别 $c$ 的样本，`X[mask]` 取出这些行。`mask.sum()` 可统计数量。逐元素条件应加括号，例如 `(y == 0) | (y == 1)`。Python 标量逻辑 `and/or` 不能代替 NumPy 逐元素的 `&/|`。

@@ M025 | 03-numpy | learn | P2:44-56
Q_EN: What do reshape, transpose, concatenate and stack do?
Q_ZH: reshape、转置、concatenate 和 stack 分别做什么？
A_EN: `reshape` changes the arrangement while preserving the element count. Transpose swaps axes; for a matrix it exchanges rows and columns. `concatenate` joins along an existing axis; `stack` introduces a new axis. Concatenating two $(3,2)$ arrays along axis 0 gives $(6,2)$; stacking them along axis 0 gives $(2,3,2)$.
A_ZH: `reshape` 改变排列方式，但元素总数不变；转置交换轴，矩阵转置就是交换行列。`concatenate` 沿已有轴拼接，`stack` 新增一个轴。两个 $(3,2)$ 数组沿轴 0 拼接得到 $(6,2)$，沿轴 0 堆叠得到 $(2,3,2)$。

@@ M026 | 03-numpy | learn | P2:57-83
Q_EN: What does axis mean in a reduction such as mean or sum?
Q_ZH: mean 或 sum 等归约运算中的 axis 表示什么？
A_EN: The specified axis is the direction collapsed by the operation. For $X$ shaped $(N,d)$, `X.mean(axis=0)` averages over samples and returns $d$ feature means; `X.mean(axis=1)` averages over features and returns $N$ row means. `keepdims=True` preserves a length-one axis, which can make subsequent broadcasting easier to reason about.
A_ZH: 指定的轴是运算要压缩掉的方向。对形状为 $(N,d)$ 的 $X$，`X.mean(axis=0)` 跨样本求平均，得到 $d$ 个特征均值；`X.mean(axis=1)` 跨特征求平均，得到 $N$ 个行均值。`keepdims=True` 保留长度为 1 的轴，有助于理解后续广播。

@@ M027 | 03-numpy | learn | P2:72-83
Q_EN: What is the NumPy broadcasting rule?
Q_ZH: NumPy 广播的规则是什么？
A_EN: Compare shapes from the trailing axes. Each pair must be equal, or one length must be 1; missing leading axes act as length 1. Thus $(N,d)-(d,)$ centers each feature, and $(N,1)+(1,d)$ produces $(N,d)$. Broadcasting conceptually repeats values without requiring an explicitly tiled copy. Check the resulting shape before trusting the arithmetic.
A_ZH: 从最后一个轴开始比较形状，每对长度必须相等，或其中一个是 1；缺失的前导轴视为长度 1。因此 $(N,d)-(d,)$ 可逐特征中心化，$(N,1)+(1,d)$ 得到 $(N,d)$。广播在概念上重复数值，不必先手动复制数组。计算后要检查结果形状。

@@ M028 | 03-numpy | check | P2:72-83
Q_EN: Why can subtracting arrays of shapes $(N,1)$ and $(N,)$ silently give the wrong result?
Q_ZH: 为什么形状为 $(N,1)$ 和 $(N,)$ 的数组相减，可能不报错却算错？
A_EN: Broadcasting treats the second array as $(1,N)$, so the result is $(N,N)$: every element is paired with every other element. If you intended one error per example, make both arrays shape $(N,)$ or both $(N,1)$. In model evaluation, always assert that predictions and targets have compatible intended shapes before subtraction.
A_ZH: 广播会把第二个数组视为 $(1,N)$，因此结果变成 $(N,N)$，每个元素与所有另一个数组元素配对。若本意是每个样本一个误差，应让两者都为 $(N,)$，或都为 $(N,1)$。评估模型时，相减前应检查预测与目标的预期形状一致。

@@ M029 | 03-numpy | learn | P2:84-97
Q_EN: What are a vector's inner product and Euclidean norm?
Q_ZH: 什么是向量的内积和欧几里得范数？
A_EN: For real vectors, $u^Tv=\sum_i u_i v_i$. The norm is $\|v\|_2=\sqrt{v^Tv}$, a measure of length. With $u=(1,2)$ and $v=(3,4)$, the inner product is 11 and $\|v\|_2=5$. Orthogonal nonzero vectors have inner product zero; a unit vector has norm one.
A_ZH: 实向量内积为 $u^Tv=\sum_i u_i v_i$；范数 $\|v\|_2=\sqrt{v^Tv}$ 表示长度。若 $u=(1,2)$、$v=(3,4)$，内积为 11，$\|v\|_2=5$。非零正交向量的内积为 0，单位向量的范数为 1。

@@ M030 | 03-numpy | learn | P2:98-109
Q_EN: How do elementwise multiplication and matrix multiplication differ?
Q_ZH: 逐元素乘法与矩阵乘法有什么区别？
A_EN: For NumPy arrays, `A * B` multiplies corresponding entries under broadcasting. `A @ B` forms dot products of rows and columns. If $A$ is $(m,n)$ and $B$ is $(n,p)$, then $AB$ is $(m,p)$. For $X$ shaped $(N,d)$ and weights $w$ shaped $(d,)$, `X @ w` gives one score per sample, shape $(N,)$.
A_ZH: 对 NumPy 数组，`A * B` 按广播规则逐元素相乘；`A @ B` 用行与列的内积计算矩阵乘法。若 $A$ 为 $(m,n)$、$B$ 为 $(n,p)$，则 $AB$ 为 $(m,p)$。当 $X$ 为 $(N,d)$、权重 $w$ 为 $(d,)$ 时，`X @ w` 得到每个样本一个分数，形状是 $(N,)$。

@@ M031 | 03-numpy | learn | P2:84-109;T1:35-45
Q_EN: What does the identity matrix do, and why is $E^TE$ useful?
Q_ZH: 单位矩阵有什么作用？为什么 $E^TE$ 很有用？
A_EN: The identity matrix $I$ has ones on its diagonal and zeros elsewhere; $Iv=v$. If the columns of $E$ are vectors, entry $(i,j)$ of $E^TE$ is their inner product $e_i^Te_j$. Therefore $E^TE=I$ says each column has unit length and different columns are orthogonal. For a tall matrix, this does not imply $EE^T=I$.
A_ZH: 单位矩阵 $I$ 对角线为 1，其余为 0，并满足 $Iv=v$。若 $E$ 的列是向量，$E^TE$ 的第 $(i,j)$ 项就是 $e_i^Te_j$。所以 $E^TE=I$ 表示各列长度为 1，不同列互相正交。对高矩阵而言，这并不意味着 $EE^T=I$。

@@ M032 | 03-numpy | learn | P2:110-121
Q_EN: What is a NumPy view, and when should I copy an array?
Q_ZH: 什么是 NumPy 视图？什么时候需要复制数组？
A_EN: A view shares the original data buffer; changing it may change the original array. Basic slicing often returns a view. `B = A.copy()` creates independent storage. If preprocessing must preserve raw input, copy before in-place modification. Reshaping may return a view or a copy depending on layout, so do not infer independence merely from a different shape.
A_ZH: 视图与原数组共享数据缓冲区，修改它可能同时修改原数组。基本切片经常返回视图；`B = A.copy()` 创建独立存储。若预处理需要保留原始输入，应先复制再原地修改。重塑形状可能返回视图或副本，取决于布局，因此不能仅凭形状不同判断数据独立。

@@ M033 | 03-numpy | learn | P2:122-127;B1:19-21
Q_EN: When should I use a line plot, scatter plot or histogram?
Q_ZH: 折线图、散点图和直方图分别适用于什么情况？
A_EN: A line plot shows change along an ordered axis; a scatter plot shows paired measurements; a histogram groups a variable into bins to reveal its distribution. Label axes and units, and identify classes with a legend. A histogram depends on bin width, so a jagged small-sample histogram is not proof of a complex true distribution.
A_ZH: 折线图展示沿有序轴的变化；散点图展示成对测量；直方图把变量分箱以观察分布。应标明坐标轴、单位，并用图例区分类别。直方图受箱宽影响，因此小样本直方图不平滑，并不能证明真实分布很复杂。

@@ M034 | 03-numpy | worked | P2:26-33;A1:7
Q_EN: Why set a random seed, and what does it not guarantee?
Q_ZH: 为什么要设置随机种子？它不能保证什么？
A_EN: A seed makes a pseudorandom sequence repeat under the same algorithm and environment, helping reproduce a split or toy sample. It does not prove a model is good, eliminate sampling uncertainty, or guarantee identical results across every library and device. Record the seed, split and software versions; compare models using the same split.
A_ZH: 在相同算法和环境下，种子使伪随机序列可重复，便于复现数据划分或模拟样本。它不能证明模型好、消除抽样不确定性，也不能保证所有库和设备上结果完全相同。应记录种子、划分与软件版本，并用同一划分比较模型。

@@ M035 | 04-tutorial | classroom | T1:14-24
Q_EN: In Tutorial 1, what exactly should the factor-counting plot contain?
Q_ZH: Tutorial 1 的因数计数图具体应该画什么？
A_EN: For every integer $n$ from 2 through 100 inclusive, compute the number of divisors excluding 1 and $n$. Use `range(2,101)` for the horizontal values and evaluate the counting function for each. The x-axis is the integer; the y-axis is its proper-factor count. Check $n=2\to0$, $n=4\to1$, and $n=12\to4$ before plotting.
A_ZH: 对 2 到 100（包含两端）的每个整数 $n$，统计除 1 和 $n$ 外的因数个数。横轴用 `range(2,101)`，逐个调用计数函数。横轴是整数，纵轴是对应真因数个数。画图前先检查 $n=2\to0$、$n=4\to1$、$n=12\to4$。

@@ M036 | 04-tutorial | classroom | T1:26-33
Q_EN: How should I approach the data1.pickle plotting exercise?
Q_ZH: 应该怎样完成 data1.pickle 的绘图练习？
A_EN: Load the provided trusted tutorial file and inspect the object's type and array shape before indexing. The supplied exercise contains 120 two-dimensional samples. Plot the first coordinate against the second with a scatter plot, preserving any grouping requested in the notebook. Do not assume a transposed orientation or a label column without inspecting the loaded object.
A_ZH: 读取课程提供的可信文件后，先检查对象类型与数组形状，再索引。该练习提供 120 个二维样本。用散点图将第一坐标与第二坐标对应绘出，并保留 Notebook 要求的分组。不能在未检查对象前，就假定数据需要转置或额外一列是标签。

@@ M037 | 04-tutorial | learn | T1:35-36
Q_EN: What is the projection of $v$ onto a nonzero vector $u$?
Q_ZH: 向量 $v$ 在非零向量 $u$ 上的投影是什么？
A_EN: The projection is $P_u(v)=\frac{v^Tu}{u^Tu}u$. It extracts the part of $v$ pointing along $u$. The residual $r=v-P_u(v)$ satisfies $u^Tr=0$. If $u$ is already unit length, the denominator is 1. For $u=(1,0)$ and $v=(3,4)$, the projection is $(3,0)$ and the residual is $(0,4)$.
A_ZH: 投影为 $P_u(v)=\frac{v^Tu}{u^Tu}u$，提取 $v$ 沿 $u$ 方向的部分。残差 $r=v-P_u(v)$ 满足 $u^Tr=0$。若 $u$ 已是单位向量，分母为 1。例如 $u=(1,0)$、$v=(3,4)$ 时，投影为 $(3,0)$，残差为 $(0,4)$。

@@ M038 | 04-tutorial | classroom | T1:35-39
Q_EN: What are the steps of Gram–Schmidt orthonormalization?
Q_ZH: Gram–Schmidt 正交归一化的步骤是什么？
A_EN: Process input columns in order. For the next vector $v_k$, subtract its projections onto all previously obtained orthonormal columns: $r=v_k-\sum_{j<k}(e_j^Tv_k)e_j$. Then set $e_k=r/\|r\|_2$. Subtraction makes the vector orthogonal to earlier columns; normalization makes its length one. This requires a nonzero residual, hence linearly independent input columns.
A_ZH: 按顺序处理输入矩阵的列。对当前 $v_k$，减去它在此前所有正交单位列上的投影：$r=v_k-\sum_{j<k}(e_j^Tv_k)e_j$，再令 $e_k=r/\|r\|_2$。减投影保证与已有列正交，归一化使长度为 1。这要求残差非零，因此输入列须线性无关。

@@ M039 | 04-tutorial | worked | T1:35-39
Q_EN: Orthonormalize $v_1=(1,1)$ and $v_2=(1,0)$ by hand.
Q_ZH: 手算将 $v_1=(1,1)$、$v_2=(1,0)$ 正交归一化。
A_EN: First, $e_1=(1,1)/\sqrt2$. Then $e_1^Tv_2=1/\sqrt2$, so $r_2=(1,0)-(1/2,1/2)=(1/2,-1/2)$. Its norm is $1/\sqrt2$, giving $e_2=(1,-1)/\sqrt2$. Check $e_1^Te_2=0$ and both norms equal 1. The two output vectors span the same plane as the inputs.
A_ZH: 先得 $e_1=(1,1)/\sqrt2$。因为 $e_1^Tv_2=1/\sqrt2$，所以 $r_2=(1,0)-(1/2,1/2)=(1/2,-1/2)$。其范数为 $1/\sqrt2$，故 $e_2=(1,-1)/\sqrt2$。检查 $e_1^Te_2=0$，范数均为 1；输出向量与输入张成相同平面。

@@ M040 | 04-tutorial | classroom | T1:37-45
Q_EN: What should `myGS(V)` return for the tutorial's test matrix, and how do I check it?
Q_ZH: 对教程的测试矩阵，`myGS(V)` 应返回什么，怎样检查？
A_EN: The notebook transposes a $3\times4$ literal, giving $V$ shape $(4,3)$: three vectors in four-dimensional space. Return $E$ with shape $(4,3)$. Check `np.allclose(E.T @ E, np.eye(3))`, and check that projecting $V$ onto the output span reconstructs it: `E @ (E.T @ V)` should match $V$. Orthonormality alone does not prove preservation of the intended span.
A_ZH: Notebook 将一个 $3\times4$ 字面矩阵转置，得到形状 $(4,3)$ 的 $V$，即四维空间中的三个向量。返回的 $E$ 应为 $(4,3)$。用 `np.allclose(E.T @ E, np.eye(3))` 检查正交归一，还应验证 `E @ (E.T @ V)` 能重构 $V$。仅有正交归一不能证明保留了原来的子空间。

@@ M041 | 04-tutorial | check | T1:35-45
Q_EN: What if a Gram–Schmidt residual is zero or very small?
Q_ZH: Gram–Schmidt 的残差为零或很小时怎么办？
A_EN: A zero residual means the new column lies in the span of earlier columns, so it supplies no new direction. Do not divide by zero. For a function requiring full column rank, raise a clear error; a basis-extraction function may instead skip dependent columns. A very small residual indicates possible numerical instability. Modified Gram–Schmidt or QR methods are useful extensions.
A_ZH: 残差为零说明新列已经位于前面各列张成的空间内，没有提供新方向，不能继续除以零。若函数要求列满秩，应明确报错；若目标是提取基，可跳过相关列。残差很小还可能导致数值不稳定。改进 Gram–Schmidt 或 QR 方法是可继续学习的扩展。

@@ M042 | 05-probability | learn | P2:128-133
Q_EN: How do a discrete probability mass function and a continuous density differ?
Q_ZH: 离散概率质量函数与连续概率密度有什么区别？
A_EN: A mass function assigns probabilities to individual discrete outcomes and sums to 1. A density integrates to 1, and probabilities are areas: $P(a\le X\le b)=\int_a^b f(x)\,dx$. For a continuous variable, $P(X=x)=0$ even when $f(x)>0$. A density value can exceed 1; it is not itself the probability of one exact value.
A_ZH: 概率质量函数给离散结果分配概率，总和为 1；概率密度的积分为 1，区间概率对应面积：$P(a\le X\le b)=\int_a^b f(x)\,dx$。连续变量即使 $f(x)>0$，仍有 $P(X=x)=0$。密度值可以大于 1，因为它不是某个精确取值的概率。

@@ M043 | 05-probability | learn | P2:134-136
Q_EN: What are joint, marginal and conditional probabilities?
Q_ZH: 联合概率、边缘概率与条件概率是什么？
A_EN: $P(A,B)$ describes both events occurring. A marginal removes another variable by summing or integrating, for example $P(A)=\sum_b P(A,b)$. A conditional restricts attention to cases where $B$ occurred: $P(A\mid B)=P(A,B)/P(B)$ for $P(B)>0$. The comma means “and”; the vertical bar means “given.”
A_ZH: $P(A,B)$ 描述两个事件同时发生。边缘概率通过对其他变量求和或积分得到，例如 $P(A)=\sum_b P(A,b)$。条件概率只考虑已发生 $B$ 的情形：当 $P(B)>0$，$P(A\mid B)=P(A,B)/P(B)$。逗号表示“同时”，竖线表示“在给定条件下”。

@@ M044 | 05-probability | worked | P2:134-136
Q_EN: In 100 messages, 20 are spam and 10 are spam containing “free.” What is $P(\text{free}\mid\text{spam})$?
Q_ZH: 100 条短信中有 20 条垃圾短信，其中 10 条包含 free，$P(\text{free}\mid\text{spam})$ 是多少？
A_EN: Restrict the denominator to the 20 spam messages: $P(\text{free}\mid\text{spam})=10/20=0.5$. The joint probability is $P(\text{free},\text{spam})=10/100=0.1$. These numbers do not determine $P(\text{spam}\mid\text{free})$ unless we also know how many non-spam messages contain “free.” Reversing the conditioning changes the question.
A_ZH: 分母只包括 20 条垃圾短信，因此条件概率为 $10/20=0.5$。联合概率为 $P(\text{free},\text{spam})=10/100=0.1$。这些信息还不能确定 $P(\text{spam}\mid\text{free})$，因为不知道正常短信中有多少条包含 free。交换条件位置就是换了一个问题。

@@ M045 | 05-probability | learn | P2:137-140;B1:34-41
Q_EN: State Bayes' rule and explain prior, likelihood, evidence and posterior.
Q_ZH: 写出贝叶斯公式，并解释先验、似然、证据与后验。
A_EN: $P(y=c\mid x)=\frac{p(x\mid y=c)P(y=c)}{p(x)}$. The prior $P(y=c)$ is the class probability before observing $x$. The likelihood $p(x\mid y=c)$ describes how compatible $x$ is with that class. The evidence $p(x)$ normalizes across classes. The posterior combines prior knowledge and the observed features into a class probability.
A_ZH: $P(y=c\mid x)=\frac{p(x\mid y=c)P(y=c)}{p(x)}$。先验 $P(y=c)$ 是看到 $x$ 前的类别概率；似然 $p(x\mid y=c)$ 描述该类别对 $x$ 的解释程度；证据 $p(x)$ 负责跨类别归一化；后验综合先验与观测特征，给出新的类别概率。

@@ M046 | 05-probability | worked | P2:137-140;B1:34-41
Q_EN: Spam has prior 0.2; “free” appears in 0.6 of spam and 0.1 of normal messages. What is the spam posterior after seeing “free”?
Q_ZH: 垃圾短信先验为 0.2，free 在垃圾短信和正常短信中出现的概率分别为 0.6、0.1。看到 free 后垃圾短信的后验是多少？
A_EN: The spam joint score is $0.6\times0.2=0.12$; the normal score is $0.1\times0.8=0.08$. Evidence is $0.12+0.08=0.20$, so the posterior is $0.12/0.20=0.60$. The word increases the spam probability from 20% to 60%, but it does not make spam certain. The posterior still reflects the base rate.
A_ZH: 垃圾短信联合分数为 $0.6\times0.2=0.12$，正常短信分数为 $0.1\times0.8=0.08$。证据为 $0.12+0.08=0.20$，故后验为 $0.12/0.20=0.60$。这个词使垃圾短信概率从 20% 升到 60%，但并不代表一定是垃圾短信；后验仍受基础发生率影响。

@@ M047 | 05-probability | learn | P2:134-136;B2:3
Q_EN: How do independence and conditional independence differ?
Q_ZH: 独立与条件独立有什么区别？
A_EN: Independence means $p(x_1,x_2)=p(x_1)p(x_2)$. Conditional independence given $y$ means $p(x_1,x_2\mid y)=p(x_1\mid y)p(x_2\mid y)$. Features can be related overall because class membership affects both, yet approximately independent within each class. Naive Bayes assumes independence given the class, not independence of all features in the combined dataset.
A_ZH: 独立意味着 $p(x_1,x_2)=p(x_1)p(x_2)$；给定 $y$ 的条件独立意味着 $p(x_1,x_2\mid y)=p(x_1\mid y)p(x_2\mid y)$。类别同时影响两个特征时，它们整体可能相关，但在每类内部近似独立。朴素贝叶斯假设的是给定类别后的独立，并非整个混合数据集中的所有特征无关。

@@ M048 | 05-probability | learn | P2:129-133;B1:13,23-26
Q_EN: What do expectation, variance and standard deviation measure?
Q_ZH: 期望、方差与标准差分别衡量什么？
A_EN: Expectation is a probability-weighted mean. Variance is the expected squared deviation, $\operatorname{Var}(X)=E[(X-\mu)^2]$. Standard deviation is its square root. If a feature is measured in centimeters, its mean and standard deviation use centimeters, while variance uses square centimeters. Large variance means greater spread, not necessarily a different mean.
A_ZH: 期望是按概率加权的平均值；方差是平方偏差的期望，$\operatorname{Var}(X)=E[(X-\mu)^2]$；标准差是方差的平方根。若特征单位为厘米，均值与标准差仍以厘米计，方差则是平方厘米。方差大表示更分散，不代表均值一定不同。

@@ M049 | 05-probability | learn | P2:129-133;B1:13,23
Q_EN: What are Bernoulli, Poisson and Gaussian distributions used to represent?
Q_ZH: 伯努利、泊松和高斯分布分别表示什么？
A_EN: Bernoulli models one binary outcome, such as whether a word appears, with success probability $p$. Poisson models a nonnegative event count in a fixed interval, with rate parameter $\lambda$. Gaussian models a continuous quantity around a mean $\mu$ with variance $\sigma^2$. Choose a distribution to match the observation type and assumptions, not simply because its formula is familiar.
A_ZH: 伯努利分布描述单次二元结果，例如一个词是否出现，参数是成功概率 $p$；泊松分布描述固定区间内的非负事件次数，参数为 $\lambda$；高斯分布描述围绕均值 $\mu$ 波动的连续量，方差为 $\sigma^2$。选择分布应匹配观测类型与假设，而不是只选熟悉的公式。

@@ M050 | 06-bayes | learn | B1:8-11
Q_EN: What does a generative classifier learn?
Q_ZH: 生成式分类器学习什么？
A_EN: It learns the class prior $\pi_c=P(y=c)$ and the class-conditional distribution $p(x\mid y=c)$. Their product gives the joint model $p(x,y=c)$. Bayes' rule converts this into a posterior for prediction. “Generative” refers to modeling how class and features could be generated; classification still outputs a label for an observed example.
A_ZH: 它学习类别先验 $\pi_c=P(y=c)$，以及类条件分布 $p(x\mid y=c)$，两者相乘得到联合模型 $p(x,y=c)$。再用贝叶斯公式计算预测所需的后验。“生成式”指对类别与特征如何产生进行建模；用于分类时，仍是给观测样本输出标签。

@@ M051 | 06-bayes | learn | B1:11-13
Q_EN: What is maximum likelihood estimation (MLE)?
Q_ZH: 什么是最大似然估计（MLE）？
A_EN: Choose parameters $\theta$ that make the observed training data most likely: $\hat\theta=\arg\max_\theta\prod_{i=1}^N p(x_i\mid\theta)$ for independent samples. Equivalently maximize $\sum_i\log p(x_i\mid\theta)$. The data are fixed while the parameter varies. A likelihood is a function of the parameter; it is not automatically a normalized probability distribution over parameters.
A_ZH: 选择使已观测训练数据最可能出现的参数：独立样本下，$\hat\theta=\arg\max_\theta\prod_{i=1}^N p(x_i\mid\theta)$，等价于最大化 $\sum_i\log p(x_i\mid\theta)$。这里数据固定、参数变化。似然是关于参数的函数，并不自动成为参数上的归一化概率分布。

@@ M052 | 06-bayes | learn | B1:11-13
Q_EN: Derive the MLE of a Bernoulli probability.
Q_ZH: 如何推导伯努利概率的最大似然估计？
A_EN: Let $s$ of $N$ observations equal 1. The log likelihood is $\ell(p)=s\log p+(N-s)\log(1-p)$. For an interior optimum, $\ell'(p)=s/p-(N-s)/(1-p)=0$, giving $\hat p=s/N$. If $s=0$ or $s=N$, the maximum is at a boundary, 0 or 1. The estimate is the observed success fraction.
A_ZH: 设 $N$ 次观测中有 $s$ 次为 1，对数似然为 $\ell(p)=s\log p+(N-s)\log(1-p)$。内部最优点满足 $\ell'(p)=s/p-(N-s)/(1-p)=0$，得到 $\hat p=s/N$。若 $s=0$ 或 $s=N$，最大值在边界 0 或 1。估计结果就是观测到的成功比例。

@@ M053 | 06-bayes | worked | B1:11-13
Q_EN: How do I estimate class priors from training labels?
Q_ZH: 怎样根据训练标签估计类别先验？
A_EN: Count each class: $\hat\pi_c=N_c/N$, where $N_c$ is its sample count and $N$ is the total. With 60 normal, 30 spam and 10 smishing examples, priors are 0.6, 0.3 and 0.1, summing to 1. Estimate from training labels only. These are training-population estimates; a changed deployment population may have different class frequencies.
A_ZH: 统计每类数量：$\hat\pi_c=N_c/N$，其中 $N_c$ 是该类样本数，$N$ 是总数。若正常、垃圾、钓鱼分别为 60、30、10 条，则先验为 0.6、0.3、0.1，和为 1。只用训练标签估计。这描述训练总体，部署环境中的类别比例可能不同。

@@ M054 | 06-bayes | learn | B1:18-26
Q_EN: State the univariate Gaussian density and interpret its parameters.
Q_ZH: 写出一维高斯密度，并解释参数。
A_EN: $p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp[-\frac{(x-\mu)^2}{2\sigma^2}]$, with $\sigma^2>0$. The mean $\mu$ locates the center; variance $\sigma^2$ controls spread. The leading factor normalizes the area to 1. A narrow Gaussian has a taller peak, so comparing only distances to means can ignore an important variance effect.
A_ZH: $p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp[-\frac{(x-\mu)^2}{2\sigma^2}]$，要求 $\sigma^2>0$。均值 $\mu$ 决定中心，方差 $\sigma^2$ 控制离散程度，前面的系数保证积分为 1。窄高斯的峰更高，因此只比较到均值的距离，会忽略重要的方差影响。
MEDIA: Lecture2a-cell-25.png

@@ M055 | 06-bayes | learn | B1:23-26
Q_EN: Derive the Gaussian MLE for the mean.
Q_ZH: 如何推导高斯均值的最大似然估计？
A_EN: The log likelihood contains $-\frac{1}{2\sigma^2}\sum_i(x_i-\mu)^2$. Differentiating with respect to $\mu$ gives $\frac{1}{\sigma^2}\sum_i(x_i-\mu)=0$. Hence $\hat\mu=\frac1N\sum_i x_i$. The best center under the squared-deviation Gaussian model is the sample mean. For a class-conditional model, use only samples in that class.
A_ZH: 对数似然含有 $-\frac{1}{2\sigma^2}\sum_i(x_i-\mu)^2$。对 $\mu$ 求导并令其为 0，得 $\frac{1}{\sigma^2}\sum_i(x_i-\mu)=0$，所以 $\hat\mu=\frac1N\sum_i x_i$。平方偏差形式的高斯模型中，最佳中心就是样本均值。类条件模型须只使用该类样本。

@@ M056 | 06-bayes | learn | B1:26;B2:44
Q_EN: What is the Gaussian variance MLE, and why do I sometimes see $N-1$ instead?
Q_ZH: 高斯方差的 MLE 是什么？为什么有时分母是 $N-1$？
A_EN: The MLE is $\hat\sigma^2_{ML}=\frac1N\sum_i(x_i-\bar x)^2$. The usual unbiased sample estimator uses $1/(N-1)$ instead, correcting the bias from estimating the mean. They answer different estimation goals. NumPy `var` defaults to denominator $N$, while the lecture's `np.cov` call uses $N-1$ by default. Do not call both the exact same MLE.
A_ZH: MLE 为 $\hat\sigma^2_{ML}=\frac1N\sum_i(x_i-\bar x)^2$。常用无偏样本估计改用 $1/(N-1)$，修正估计均值带来的偏差。它们对应不同估计目标。NumPy 的 `var` 默认分母为 $N$，而课上 `np.cov` 的默认分母为 $N-1$，不能把两者都称作完全相同的 MLE。

@@ M057 | 06-bayes | worked | B1:26
Q_EN: Find the Gaussian mean and variance MLEs for $x=(1,2,3)$.
Q_ZH: 对 $x=(1,2,3)$，求高斯均值和方差的 MLE。
A_EN: $\hat\mu=(1+2+3)/3=2$. Squared deviations are 1, 0 and 1, so $\hat\sigma^2_{ML}=2/3$. The unbiased sample variance is $2/(3-1)=1$. State which estimator you use; “variance equals 1” and “variance equals $2/3$” are not contradictory when their definitions differ.
A_ZH: 均值 $\hat\mu=(1+2+3)/3=2$。平方偏差依次为 1、0、1，因此 MLE 方差为 $2/3$；无偏样本方差为 $2/(3-1)=1$。应说明采用哪种估计量：在定义不同的情况下，“方差为 1”和“方差为 $2/3$”并不矛盾。

@@ M058 | 06-bayes | learn | B1:32-41
Q_EN: How does maximum a posteriori class prediction work, and why can evidence be dropped?
Q_ZH: 最大后验类别预测如何进行？为什么可以忽略证据项？
A_EN: Under equal misclassification costs, predict $\hat y=\arg\max_c P(y=c\mid x)=\arg\max_c p(x\mid y=c)\pi_c$. For a fixed $x$, $p(x)$ is the same positive denominator for every candidate class, so it does not change the maximizer. Keep the denominator if you need normalized probabilities. Dropping evidence does not permit dropping unequal priors.
A_ZH: 错分代价相同时，预测 $\hat y=\arg\max_c P(y=c\mid x)=\arg\max_c p(x\mid y=c)\pi_c$。固定 $x$ 后，各候选类别的正分母 $p(x)$ 相同，不影响最大者。如果需要归一化概率，就必须保留分母。忽略证据不等于可以忽略不相等的先验。

@@ M059 | 06-bayes | worked | B1:34-48
Q_EN: Class A has likelihood 0.4 and prior 0.2; B has likelihood 0.2 and prior 0.8. Which class wins?
Q_ZH: A 类似然 0.4、先验 0.2；B 类似然 0.2、先验 0.8。应该选择哪类？
A_EN: Joint scores are $0.4\times0.2=0.08$ and $0.2\times0.8=0.16$. Predict B, despite its smaller likelihood. Normalized posteriors are $1/3$ and $2/3$. Equal priors guarantee the same ranking by likelihood and posterior; unequal priors can change the ranking, as here, though the winning class may sometimes still coincide.
A_ZH: 联合分数分别为 $0.4\times0.2=0.08$ 和 $0.2\times0.8=0.16$，因此选择 B，虽然其似然更小。归一化后验为 $1/3$ 和 $2/3$。先验相等保证似然与后验排序相同；先验不等时可能像本例这样改变排序，但在某些样本上获胜类别仍可碰巧相同。

@@ M060 | 06-bayes | learn | B1:41-48;B2:44
Q_EN: Why compute log scores rather than products of many probabilities?
Q_ZH: 为什么要计算对数分数，而不是直接连乘大量概率？
A_EN: Products of small values can underflow to zero. Logarithms turn products into sums: $s_c=\log\pi_c+\log p(x\mid c)$. Because log is increasing, maximizing a positive score or its log gives the same class. To obtain posteriors, normalize in log space, then exponentiate. A log probability can be negative without indicating an invalid probability.
A_ZH: 很多小数连乘容易下溢成 0。取对数可把乘积转成和：$s_c=\log\pi_c+\log p(x\mid c)$。对数单调递增，因此最大化正分数或其对数得到同一类别。求后验时先在对数域归一化，再取指数。对数概率为负并不意味着原概率无效。

@@ M061 | 07-gaussian | learn | B2:3,14-19
Q_EN: What is the Gaussian naive Bayes class-conditional model?
Q_ZH: 高斯朴素贝叶斯的类条件模型是什么？
A_EN: For $d$ features, $p(x\mid y=c)=\prod_{j=1}^{d}\mathcal N(x_j\mid\mu_{cj},\sigma^2_{cj})$. Each class has a separate mean and variance for each feature. “Gaussian” specifies each feature's conditional distribution; “naive” assumes conditional independence of features given the class. Fit these quantities within each class, then combine with class priors for prediction.
A_ZH: 对 $d$ 个特征，$p(x\mid y=c)=\prod_{j=1}^{d}\mathcal N(x_j\mid\mu_{cj},\sigma^2_{cj})$。每个类别的每个特征都有各自均值和方差。“高斯”规定特征的条件分布形式，“朴素”规定给定类别后各特征条件独立。在各类内部估计这些量，再结合先验预测。
MEDIA: Lecture2b-cell-19.png

@@ M062 | 07-gaussian | worked | B2:14-19
Q_EN: In a two-feature Gaussian NB model, what does a training row contribute?
Q_ZH: 在双特征 Gaussian NB 模型中，一条训练样本如何参与估计？
A_EN: A row $x=(x_1,x_2)$ labeled $c$ contributes $x_1$ to class $c$'s first-feature mean and variance, and $x_2$ to its second-feature estimates. The model does not fit a within-class cross-covariance term. If class samples are $(1,2)$ and $(3,4)$, means are $(2,3)$ and MLE variances are $(1,1)$, before any numerical smoothing.
A_ZH: 标签为 $c$ 的一行 $x=(x_1,x_2)$，将 $x_1$ 用于该类第一个特征的均值与方差估计，将 $x_2$ 用于第二个特征。模型不拟合类内交叉协方差项。例如该类样本为 $(1,2)$、$(3,4)$，则均值为 $(2,3)$，MLE 方差为 $(1,1)$，这里尚未加入数值平滑。

@@ M063 | 07-gaussian | learn | B2:14-27
Q_EN: Write the Gaussian NB log decision score.
Q_ZH: 写出 Gaussian NB 的对数决策分数。
A_EN: $s_c(x)=\log\pi_c-\frac12\sum_j\left[\log(2\pi\sigma^2_{cj})+\frac{(x_j-\mu_{cj})^2}{\sigma^2_{cj}}\right]$. Predict the class with largest score. The squared-distance term penalizes being far from a class mean relative to its spread; the log-variance term accounts for density normalization. Unequal feature variances can produce curved decision boundaries.
A_ZH: $s_c(x)=\log\pi_c-\frac12\sum_j\left[\log(2\pi\sigma^2_{cj})+\frac{(x_j-\mu_{cj})^2}{\sigma^2_{cj}}\right]$，选择分数最大的类别。平方距离项惩罚相对于该类离散程度而言偏离均值的情况；对数方差项对应密度归一化。特征方差不同时，决策边界可能弯曲。

@@ M064 | 07-gaussian | learn | B2:19-32
Q_EN: How do I read a class-density plot and a posterior decision-region plot?
Q_ZH: 如何阅读类条件密度图和后验决策区域图？
A_EN: A class-density plot shows where features are likely under a specified class, $p(x\mid c)$. A posterior plot compares classes after including priors and normalization. A decision boundary is where competing posterior scores tie, not necessarily halfway between visible clusters. Test points falling in another class's region indicate classification errors relative to their labels.
A_ZH: 类条件密度图展示给定某类别时特征在哪些位置更可能出现，即 $p(x\mid c)$；后验图则加入先验并归一化后比较各类。决策边界是竞争类别后验分数相等的位置，不一定在两个簇的几何中点。测试点落入另一类别的区域，表示相对于其标签发生错分。
MEDIA: Lecture2b-cell-27.png

@@ M065 | 07-gaussian | learn | B2:11,28-32
Q_EN: What is stratified splitting, and why use it for classification?
Q_ZH: 什么是分层划分？为什么分类任务中有用？
A_EN: A stratified split approximately preserves each class's proportion in each subset. This reduces the chance that a small validation set omits a minority class. The lecture illustrates a 50/50 train–test split and mentions stratified alternatives. Stratification helps class representation, but does not fix temporal leakage, duplicate messages across splits, or too few independent examples.
A_ZH: 分层划分使各子集中类别比例近似保持一致，减少小验证集遗漏少数类的风险。课堂示例采用 50/50 训练—测试划分，并介绍了分层替代方法。分层改善类别代表性，但不能解决时间泄漏、重复短信跨集合出现，或独立样本太少的问题。

@@ M066 | 07-gaussian | learn | B2:33-38
Q_EN: What does a covariance matrix describe?
Q_ZH: 协方差矩阵描述什么？
A_EN: $\Sigma_{ij}=E[(X_i-\mu_i)(X_j-\mu_j)]$. Diagonal entries are feature variances; off-diagonal entries describe joint variation. Positive covariance means two centered features tend to move in the same direction; negative covariance means opposite directions. A covariance matrix is symmetric and positive semidefinite. Covariance depends on measurement units.
A_ZH: $\Sigma_{ij}=E[(X_i-\mu_i)(X_j-\mu_j)]$。对角线是各特征方差，非对角线描述共同变化。正协方差表示中心化后的特征倾向同向变化，负协方差表示反向变化。协方差矩阵对称且半正定，其数值受测量单位影响。
MEDIA: Lecture2b-cell-38.png

@@ M067 | 07-gaussian | learn | B2:34-38
Q_EN: State the multivariate Gaussian density and explain its two main matrix terms.
Q_ZH: 写出多元高斯密度，并解释两个主要矩阵项。
A_EN: $p(x)=\frac{\exp[-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)]}{(2\pi)^{d/2}|\Sigma|^{1/2}}$ for positive-definite $\Sigma$. The quadratic form measures squared distance adjusted for spread and correlation. The determinant term normalizes for the distribution's volume. With diagonal covariance, this density factors into independent univariate Gaussian densities.
A_ZH: 正定 $\Sigma$ 下，$p(x)=\frac{\exp[-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)]}{(2\pi)^{d/2}|\Sigma|^{1/2}}$。二次型衡量考虑离散程度与相关性后的平方距离，行列式项按分布体积进行归一化。协方差为对角矩阵时，密度可分解成独立的一维高斯密度乘积。

@@ M068 | 07-gaussian | worked | B2:36-38
Q_EN: Interpret $\Sigma=\begin{bmatrix}1&0.9\\0.9&1\end{bmatrix}$ and compare it with $I$.
Q_ZH: 如何理解 $\Sigma=\begin{bmatrix}1&0.9\\0.9&1\end{bmatrix}$？它与 $I$ 有何不同？
A_EN: Both features have variance 1, but the positive off-diagonal entries create strong positive correlation. In two dimensions the density contours are elongated along approximately $x_1=x_2$. Identity covariance gives circular contours with no preferred direction. A diagonal naive Bayes model cannot represent this tilted class-conditional shape.
A_ZH: 两个特征的方差都是 1，但正的非对角项表示较强正相关。二维密度等高线大致沿 $x_1=x_2$ 方向拉长；单位协方差对应无偏好方向的圆形等高线。对角协方差的朴素贝叶斯不能表达这种倾斜的类条件形状。

@@ M069 | 07-gaussian | learn | B2:33-44
Q_EN: How many covariance parameters does a full Gaussian model need compared with diagonal Gaussian NB?
Q_ZH: 完整高斯协方差与 Gaussian NB 对角协方差各需多少参数？
A_EN: Per class, a symmetric full covariance matrix has $d(d+1)/2$ distinct entries; diagonal covariance has $d$. Both also need $d$ means. At $d=100$, this is 5,050 versus 100 covariance parameters. Full covariance can capture correlations, but needs more data and more careful regularization. More flexibility does not guarantee better held-out prediction.
A_ZH: 每类对称完整协方差有 $d(d+1)/2$ 个独立项，对角协方差只有 $d$ 个；两者都另需 $d$ 个均值。$d=100$ 时协方差参数分别为 5,050 与 100。完整协方差能描述相关性，但需要更多数据和更谨慎的正则化；更灵活不保证留出集预测更好。

@@ M070 | 07-gaussian | learn | B2:39-44
Q_EN: Why add $\alpha I$ to an estimated covariance matrix?
Q_ZH: 为什么给估计的协方差矩阵加上 $\alpha I$？
A_EN: Use $\Sigma_{reg}=\hat\Sigma+\alpha I$ with $\alpha>0$. It increases every eigenvalue by $\alpha$, helping a singular or ill-conditioned positive-semidefinite estimate become invertible and numerically stable. It also imposes extra spread in every direction. Choose $\alpha$ using validation; too much regularization can wash out useful structure.
A_ZH: 令 $\Sigma_{reg}=\hat\Sigma+\alpha I$，其中 $\alpha>0$。每个特征值都会增加 $\alpha$，有助于让奇异或病态的半正定估计变得可逆、数值更稳定，同时在各方向增加离散程度。应通过验证选择 $\alpha$，过大可能抹去有用结构。
MEDIA: Lecture2b-cell-42.png

@@ M071 | 07-gaussian | learn | B2:44-52
Q_EN: Does the lecture's custom `GaussianBayes` use a shared covariance across classes?
Q_ZH: 课堂自定义的 `GaussianBayes` 是否在所有类别间共享协方差？
A_EN: No. Its `fit` method computes a separate `cov(Xc, rowvar=False)` for each class, then adds `alpha*I`. The resulting model is a class-specific full-covariance Gaussian classifier, with generally quadratic boundaries. A shared-covariance model can produce linear discriminants. Historical notes about a shared-covariance model should not be silently substituted for this implementation.
A_ZH: 不共享。其 `fit` 对每个类别分别计算 `cov(Xc, rowvar=False)`，然后加 `alpha*I`。得到的是各类具有独立完整协方差的高斯分类器，通常有二次决策边界。共享协方差模型可产生线性判别。因此不能把往年笔记中的共享协方差模型直接当成本次代码实现。
MEDIA: Lecture2b-cell-52.png

@@ M072 | 07-gaussian | learn | B2:44
Q_EN: How does log-sum-exp normalize class log scores stably?
Q_ZH: log-sum-exp 如何稳定地归一化类别对数分数？
A_EN: Given log joint scores $s_c$, compute $\log p(c\mid x)=s_c-\operatorname{LSE}(s)$, where $\operatorname{LSE}(s)=m+\log\sum_c e^{s_c-m}$ and $m=\max_c s_c$. Subtracting $m$ prevents large exponentials. For scores $(-1000,-1001)$, the posterior is approximately $(0.7311,0.2689)$ even though directly exponentiating both raw scores may underflow.
A_ZH: 已有对数联合分数 $s_c$ 时，计算 $\log p(c\mid x)=s_c-\operatorname{LSE}(s)$，其中 $\operatorname{LSE}(s)=m+\log\sum_c e^{s_c-m}$、$m=\max_c s_c$。先减最大值可避免指数过大。分数为 $(-1000,-1001)$ 时，后验约为 $(0.7311,0.2689)$，直接对原分数取指数却可能下溢。

@@ M073 | 07-gaussian | check | B2:44
Q_EN: What assumptions in the custom classifier's code should I inspect before reusing it?
Q_ZH: 复用课堂自定义分类器前，应检查哪些代码假设？
A_EN: It sets `K = max(y)+1` and loops through `range(K)`, assuming consecutive integer labels starting at zero. Each class must contain enough observations for covariance estimation, and covariance must be numerically usable. The assignment labels 0, 1, 2 fit the label convention; arbitrary strings or labels 1, 3 do not. Map labels explicitly when generalizing the code.
A_ZH: 它用 `K = max(y)+1` 并遍历 `range(K)`，假设标签为从 0 开始的连续整数。每类还须有足够观测估计协方差，协方差必须数值可用。作业标签 0、1、2 满足约定，任意字符串或 1、3 这样的标签则不满足。推广代码时应显式映射标签。

@@ M074 | 07-gaussian | check | B2:3,33-52
Q_EN: When might Gaussian NB outperform a full-covariance Gaussian classifier?
Q_ZH: 什么时候 Gaussian NB 可能比完整协方差高斯分类器更好？
A_EN: When data are limited relative to dimension, estimating fewer parameters can reduce estimation noise. Even if independence is imperfect, a simpler model may generalize better than an unstable full covariance estimate. Compare held-out scores under the same split and inspect class-wise errors. The choice is a tradeoff between modeling correlations and reliably estimating them.
A_ZH: 当样本量相对于维度较少时，少估计一些参数可以降低估计噪声。即使独立假设不完全成立，简单模型也可能比不稳定的完整协方差估计泛化更好。应在同一划分上比较留出集分数，并检查各类错误。关键权衡是既能描述相关性，又能可靠估计它。

@@ M075 | 08-text | learn | B2:55-58
Q_EN: How does bag-of-words turn text into a vector?
Q_ZH: 词袋模型如何把文本变成向量？
A_EN: Fix an ordered vocabulary of $V$ words. Feature $x_j$ records the count of vocabulary word $j$. With vocabulary `[this, test, spam, foo]`, “This is a test document” becomes $(1,1,0,0)$ after lowercasing and ignoring out-of-vocabulary words. Bag-of-words preserves occurrence information but loses word order and most syntax.
A_ZH: 固定一个包含 $V$ 个词的有序词表，特征 $x_j$ 记录第 $j$ 个词的次数。词表为 `[this, test, spam, foo]` 时，“This is a test document” 转小写并忽略词表外词后得到 $(1,1,0,0)$。词袋保留出现信息，但丢失词序和大部分句法结构。

@@ M076 | 08-text | learn | B2:58-62
Q_EN: Why lowercase text, remove stopwords or limit vocabulary size?
Q_ZH: 为什么转小写、去停用词或限制词表大小？
A_EN: Lowercasing merges variants such as “Free” and “free.” Stopword removal can discard frequent low-information words. Limiting vocabulary size reduces dimension and memory. Each step can also remove useful signals: capitalization or a word such as “not” may matter. Treat preprocessing choices as hypotheses to compare on validation data, not universally beneficial rules.
A_ZH: 转小写合并 “Free” 与 “free” 等变体；去停用词可去掉常见但信息少的词；限制词表大小减少维度与内存。每一步也可能丢掉有用信号，例如大写形式或 not 可能很重要。应将预处理选择作为验证集上要比较的假设，而非一定有益的规则。

@@ M077 | 08-text | learn | B2:61-71
Q_EN: What is the correct use of a vectorizer's fit, transform and fit_transform methods?
Q_ZH: 词向量器的 fit、transform 和 fit_transform 应怎样使用？
A_EN: `fit(traintext)` learns the vocabulary from training text. `transform(text)` converts text using that fixed vocabulary. `fit_transform(traintext)` combines the two on training data. Use only `transform` on validation and test text. Refitting on test text changes feature meanings and lets information from evaluation data influence preprocessing.
A_ZH: `fit(traintext)` 从训练文本学习词表；`transform(text)` 使用固定词表转换文本；`fit_transform(traintext)` 把训练集上的两步合并。对验证与测试文本只使用 `transform`。在测试文本上重新拟合会改变特征含义，也让评估数据的信息进入预处理。

@@ M078 | 08-text | learn | B2:65-68
Q_EN: Why are document matrices stored sparsely?
Q_ZH: 为什么文档矩阵通常采用稀疏存储？
A_EN: A document contains only a small subset of a large vocabulary, so most feature entries are zero. Sparse storage records nonzero values and their locations instead of every zero. Converting the whole matrix with `.toarray()` can consume much more memory. Inspect a small row densely if useful, while keeping large training matrices sparse when the model supports them.
A_ZH: 一篇文档只包含大词表中的少量词，因此大多数特征为零。稀疏存储记录非零值及位置，不逐个保存所有零。对整个矩阵调用 `.toarray()` 可能大幅增加内存。需要时可查看少量行的稠密表示；模型支持时，大训练矩阵应保持稀疏。

@@ M079 | 08-text | learn | B2:72-74
Q_EN: What does Bernoulli naive Bayes model for each word?
Q_ZH: 伯努利朴素贝叶斯对每个词建模的是什么？
A_EN: Let $x_j\in\{0,1\}$ indicate whether word $j$ occurs. For class $c$, $\theta_{cj}=P(x_j=1\mid c)$ and $p(x_j\mid c)=\theta_{cj}^{x_j}(1-\theta_{cj})^{1-x_j}$. Repeating a word five times still gives $x_j=1$. The class-conditional likelihood multiplies these terms across the fixed vocabulary, including absent words.
A_ZH: 令 $x_j\in\{0,1\}$ 表示第 $j$ 个词是否出现。对类别 $c$，$\theta_{cj}=P(x_j=1\mid c)$，且 $p(x_j\mid c)=\theta_{cj}^{x_j}(1-\theta_{cj})^{1-x_j}$。词重复五次仍只有 $x_j=1$。类条件似然对固定词表中所有项相乘，未出现的词也包括在内。

@@ M080 | 08-text | worked | B2:72-73
Q_EN: Under Bernoulli NB, how does an absent word contribute to a document score?
Q_ZH: 在 Bernoulli NB 中，未出现的词如何影响文档分数？
A_EN: If the two vocabulary words have class probabilities $(0.8,0.3)$ and the document vector is $(1,0)$, its class-conditional likelihood is $0.8(1-0.3)=0.56$. The absent second word contributes 0.7, not 1. In log space the contribution is $\log0.8+\log0.7$. Ignoring all absent words would implement a different scoring rule.
A_ZH: 若两个词在某类的出现概率为 $(0.8,0.3)$，文档向量为 $(1,0)$，则类条件似然为 $0.8(1-0.3)=0.56$。缺席的第二个词贡献 0.7，而不是 1。对数域中是 $\log0.8+\log0.7$。忽略所有缺席词会变成另一种评分规则。

@@ M081 | 08-text | learn | B2:72,80-81
Q_EN: Why smooth Bernoulli word probabilities, and what is the formula?
Q_ZH: 为什么要对伯努利词概率做平滑？公式是什么？
A_EN: An unseen word in a class gives an unsmoothed estimate of zero, making any document containing it impossible under that class. Use $\hat\theta_{cj}=\frac{N_{cj}+\alpha}{N_c+2\alpha}$, where $N_{cj}$ counts class-$c$ documents containing word $j$, and $N_c$ is the total number of class-$c$ documents. The denominator has $2\alpha$ because the outcome is binary. $\alpha=1$ is Laplace smoothing; other positive values give additive smoothing.
A_ZH: 某词在一个类别中未出现时，不平滑估计为 0，会让任何包含该词的文档在该类下都变得“不可能”。可用 $\hat\theta_{cj}=\frac{N_{cj}+\alpha}{N_c+2\alpha}$，其中 $N_{cj}$ 是类别 $c$ 中包含词 $j$ 的文档数，$N_c$ 是类别 $c$ 的总文档数。分母加 $2\alpha$ 因为有出现/不出现两种结果。$\alpha=1$ 称拉普拉斯平滑，其他正值是加性平滑。

@@ M082 | 08-text | worked | B2:80-81
Q_EN: A word appears in none of 10 class documents. What is its Bernoulli estimate with $\alpha=1$?
Q_ZH: 某词在某类 10 篇文档中一次也没出现，$\alpha=1$ 时伯努利平滑估计是多少？
A_EN: $\hat\theta=(0+1)/(10+2)=1/12\approx0.0833$. Its absence probability is $11/12$. The estimate expresses uncertainty from limited observations rather than asserting impossibility. As $N_c$ grows while $\alpha$ is fixed, the effect of these virtual counts becomes smaller relative to the observed data.
A_ZH: $\hat\theta=(0+1)/(10+2)=1/12\approx0.0833$，缺席概率为 $11/12$。这个估计承认有限观测下的不确定性，不直接断言该词绝不出现。当 $\alpha$ 固定而 $N_c$ 增大时，虚拟计数相对于真实数据的影响会减弱。

@@ M083 | 08-text | learn | B2:87-88
Q_EN: What makes a word informative for distinguishing two classes?
Q_ZH: 什么样的词有助于区分两个类别？
A_EN: A word is informative when its probabilities differ substantially between classes, not merely when it is common. A useful presence score is $\log P(w\text{ present}\mid c=1)-\log P(w\text{ present}\mid c=0)$. A large positive value supports class 1 when the word occurs. This single-word comparison is not the full document posterior, which also includes priors and other features.
A_ZH: 有区分力的词在不同类别中的概率差异大，而不只是总频率高。可比较出现概率的对数差：$\log P(w\text{ 出现}\mid c=1)-\log P(w\text{ 出现}\mid c=0)$。较大正值表示该词出现时支持类别 1。这并非完整文档后验，后者还包括先验和其他特征。

@@ M084 | 08-text | learn | B2:89-92
Q_EN: What are term frequency and inverse document frequency?
Q_ZH: 词频 TF 和逆文档频率 IDF 分别是什么？
A_EN: In the lecture's simplified definition, $TF_j=w_j/|D|$, where $w_j$ is a word count and $|D|$ is document length. $IDF_j=\log(N/df_j)$ measures rarity across $N$ documents, with $df_j$ counting documents containing the word. TF-IDF multiplies the two. Libraries may add smoothing constants and apply an additional vector normalization.
A_ZH: 课件的简化定义中，$TF_j=w_j/|D|$，$w_j$ 为词频计数，$|D|$ 为文档长度。$IDF_j=\log(N/df_j)$ 衡量在 $N$ 篇文档中的稀有程度，$df_j$ 是含该词的文档数。TF-IDF 将二者相乘。实际库可能加入平滑常数，并进一步归一化向量。

@@ M085 | 08-text | worked | B2:90-91
Q_EN: Must every TF-IDF vector sum to 1?
Q_ZH: 每个 TF-IDF 向量的元素和都必须为 1 吗？
A_EN: No. The lecture explicitly uses `TfidfTransformer(norm='l1')`, so a nonzero nonnegative output vector sums to 1 because of that normalization choice. With L2 normalization, the sum of squared entries is 1 instead. An all-zero vector remains zero. TF-IDF itself is a weighting idea, not a universal sum-to-one rule.
A_ZH: 不是。课堂代码显式设置 `TfidfTransformer(norm='l1')`，所以非零、非负输出向量的元素和为 1，这是所选归一化方式的结果。L2 归一化则使平方和为 1；全零向量仍为零。TF-IDF 本身是加权思路，并不天然要求元素和为 1。

@@ M086 | 08-text | learn | B2:93-99
Q_EN: What does multinomial naive Bayes model, and how are word probabilities estimated?
Q_ZH: 多项式朴素贝叶斯建模什么？怎样估计词概率？
A_EN: In the count model, $x_j$ is the number of occurrences of word $j$. Let $T_{cj}$ be its total count in class $c$ and $V$ the vocabulary size. Additive smoothing gives $\hat\theta_{cj}=(T_{cj}+\alpha)/(\sum_k T_{ck}+\alpha V)$. These word probabilities sum to 1 within each class. The denominator counts tokens, unlike Bernoulli's document-count denominator.
A_ZH: 在计数模型中，$x_j$ 是第 $j$ 个词出现的次数。设 $T_{cj}$ 是该词在类别 $c$ 中的总次数，词表大小为 $V$，则加性平滑为 $\hat\theta_{cj}=(T_{cj}+\alpha)/(\sum_k T_{ck}+\alpha V)$。每类词概率之和为 1。分母统计词元总数，而伯努利模型的分母统计文档数。

@@ M087 | 08-text | learn | B2:93-99
Q_EN: What is the multinomial NB decision score, and why can a combinatorial term be omitted?
Q_ZH: 多项式 NB 的决策分数是什么？为什么可以省略组合系数？
A_EN: For count vector $x$, use $s_c=\log\pi_c+\sum_j x_j\log\theta_{cj}$. The multinomial coefficient $(\sum_jx_j)!/\prod_jx_j!$ depends on the observed document but not the candidate class, so it cancels in class comparison. Repeated words contribute repeatedly through $x_j$. The vocabulary word probabilities, not raw document counts, must sum to 1.
A_ZH: 对计数向量 $x$，用 $s_c=\log\pi_c+\sum_j x_j\log\theta_{cj}$。多项式系数 $(\sum_jx_j)!/\prod_jx_j!$ 取决于观测文档，不取决于候选类别，因此比较类别时可抵消。重复词通过 $x_j$ 多次贡献分数。必须和为 1 的是词概率，而非原始文档计数。

@@ M088 | 08-text | worked | B2:93-99
Q_EN: A class has token counts $(3,1,0)$ in a three-word vocabulary. Find smoothed probabilities for $\alpha=1$.
Q_ZH: 某类在三词词表中的词元计数为 $(3,1,0)$，$\alpha=1$ 时平滑概率是多少？
A_EN: Total observed tokens are 4, and the denominator is $4+3=7$. The probabilities are $(4/7,2/7,1/7)$, which sum to 1. For a new document with counts $(2,0,1)$, its class-dependent likelihood factor is $(4/7)^2(1/7)$. Multiply by the class prior, or add its log, before comparing classes.
A_ZH: 观测词元总数为 4，分母为 $4+3=7$，因此概率为 $(4/7,2/7,1/7)$，和为 1。若新文档计数为 $(2,0,1)$，与类别有关的似然因子为 $(4/7)^2(1/7)$。比较类别前还需乘类别先验，或在对数域加上先验对数。

@@ M089 | 08-text | check | B2:72-99
Q_EN: How should I choose among Gaussian, Bernoulli and multinomial NB?
Q_ZH: 如何在 Gaussian、Bernoulli 和 Multinomial NB 之间选择？
A_EN: Gaussian NB suits continuous features modeled as class-conditional Gaussians. Bernoulli NB suits binary occurrence indicators and scores both presence and absence. Multinomial NB suits nonnegative token counts; nonnegative TF-IDF is also commonly used in practice. Do not feed arbitrary negative standardized features into a multinomial count model. Match representation, assumptions and validation evidence.
A_ZH: Gaussian NB 适合可用类条件高斯描述的连续特征；Bernoulli NB 适合二元出现指示，同时对出现与缺席计分；Multinomial NB 适合非负词频，实践中也常用于非负 TF-IDF。不能把任意含负值的标准化特征直接当成多项式计数输入。应同时匹配表示方式、假设与验证证据。

@@ M091 | 09-assignment | learn | A1:3
Q_EN: What is balanced accuracy, and why is it used here?
Q_ZH: 什么是平衡准确率？为什么本作业使用它？
A_EN: For $C$ classes, balanced accuracy is mean class recall: $BA=\frac1C\sum_c TP_c/(TP_c+FN_c)$. Each class contributes equally, even when sample counts differ. Ordinary accuracy weights frequent classes more heavily through their sample counts. Here the normal class is much more common, so balanced accuracy helps expose failure on spam or smishing.
A_ZH: 对 $C$ 个类别，平衡准确率是各类召回率的平均：$BA=\frac1C\sum_c TP_c/(TP_c+FN_c)$。即使各类样本数不同，每类也有相同权重。普通准确率因样本数量而更偏向常见类。这里正常短信占多数，平衡准确率能更好地暴露模型对垃圾或钓鱼短信的失效。

@@ M092 | 09-assignment | worked | A1:3
Q_EN: A three-class classifier has recalls 0.95, 0.60 and 0.40. What is balanced accuracy?
Q_ZH: 三类召回率分别为 0.95、0.60、0.40，平衡准确率是多少？
A_EN: $BA=(0.95+0.60+0.40)/3=0.65$, or 65%. A classifier that always predicts the majority class has recalls $(1,0,0)$ and $BA=1/3$, provided all three classes are present. Its ordinary accuracy could still look high if the majority class dominates. These are illustrative calculations, not measured assignment results.
A_ZH: $BA=(0.95+0.60+0.40)/3=0.65$，即 65%。若三类均存在，永远预测多数类的模型召回率为 $(1,0,0)$，平衡准确率为 $1/3$。当多数类占比很高时，它的普通准确率仍可能很好看。这里是计算示例，不是已测得的作业实验结果。

@@ M093 | 09-assignment | learn | A1:3
Q_EN: How do I read a confusion matrix and distinguish precision from recall?
Q_ZH: 如何阅读混淆矩阵？精确率与召回率怎样区分？
A_EN: First state the axes; a common convention uses true classes as rows and predicted classes as columns. For class $c$, recall is $TP_c/(TP_c+FN_c)$: how much of the true class was found? Precision is $TP_c/(TP_c+FP_c)$: how much of what was predicted as that class is correct? Balanced accuracy averages recall, not precision.
A_ZH: 先说明坐标约定，常见方式是行表示真实类，列表示预测类。对类别 $c$，召回率 $TP_c/(TP_c+FN_c)$ 回答“真实该类找回多少”；精确率 $TP_c/(TP_c+FP_c)$ 回答“预测为该类的有多少正确”。平衡准确率平均的是召回率，不是精确率。

@@ M094 | 09-assignment | learn | A1:3;B2:61-71
Q_EN: What is a defensible first baseline for Assignment 1?
Q_ZH: Assignment 1 怎样建立合理的第一个基线？
A_EN: Start with a majority-class baseline to reveal the effect of imbalance, then a training-only word vectorizer plus a smoothed NB classifier. Compare count/Bernoulli and count or TF-IDF/multinomial variants on the same validation split. Record feature settings, smoothing, class recalls and balanced accuracy. This is an experiment plan; actual performance must come from your runs.
A_ZH: 先用多数类基线观察类别不平衡的影响，再用仅在训练集拟合的词向量器配合平滑 NB。使用同一验证划分，比较计数/伯努利，以及计数或 TF-IDF/多项式方案。记录特征设置、平滑参数、各类召回率和平衡准确率。这是实验方案，实际效果须来自你的运行结果。

@@ M095 | 09-assignment | learn | A1:3;LEAK:11.2
Q_EN: Where can data leakage occur even if I never train the classifier on test labels?
Q_ZH: 即使不用测试标签训练分类器，哪里仍可能发生数据泄漏？
A_EN: A vocabulary, IDF weights, normalization statistics or feature selection can leak evaluation information if fitted before splitting. In cross-validation, fit each learned preprocessing step within that fold's training subset. A pipeline helps enforce this sequence. Fixed transformations such as a predetermined lowercase rule differ from statistics learned from the full dataset.
A_ZH: 如果先用全体数据学习词表、IDF、归一化统计量或特征选择，再划分数据，仍会泄漏评估信息。交叉验证中，每个需学习的预处理步骤都应只在该折训练子集拟合。Pipeline 有助于保证顺序。预先固定的转小写规则，与从全体数据学到的统计量不同。

@@ M096 | 09-assignment | learn | A1:3
Q_EN: How can I add meaningful features beyond the basic lecture baseline?
Q_ZH: 除课堂基础方案外，可以怎样增加有意义的特征？
A_EN: Candidate extensions include character n-grams, URL indicators, digit ratios or message length. Give each a hypothesis, such as character fragments handling spelling variants, then compare with the same baseline and validation protocol. Check representation compatibility: additional continuous features do not automatically fit a multinomial likelihood. Describe these as proposed experiments until tested.
A_ZH: 候选扩展包括字符 n-gram、URL 指示、数字比例和短信长度。每项都应有假设，例如字符片段可能应对拼写变体，再用同样基线和验证流程比较。还要检查表示兼容性：额外连续特征不会自动适配多项式似然。未经测试时，应称为候选实验而非有效提升。

@@ M099 | 09-assignment | learn | A1:3
Q_EN: What should an informative classification error analysis contain?
Q_ZH: 有价值的分类错误分析应包含什么？
A_EN: Show confusion patterns and a few authorized evaluation examples, then propose reasons tied to features or assumptions: unseen vocabulary, ambiguous language, or overlapping spam/smishing signals. Distinguish an observation from a causal explanation. Use validation errors for model development; do not repeatedly tune on held-out test mistakes. A good report explains both improvements and unresolved failures.
A_ZH: 展示混淆模式和少量符合评估流程的例子，再提出与特征或假设相关的可能原因，例如未见词、语义歧义、垃圾与钓鱼信号重叠。应区分观察事实与因果解释。模型开发使用验证错误，不应反复根据留出测试错误调参。好的报告同时解释改进与仍未解决的问题。

@@ M101 | 10-extension | extension | B2:93-99;NB:1.9.2
Q_EN: Is a TF-IDF vector literally a multinomial count observation?
Q_ZH: TF-IDF 向量在严格意义上是多项式计数观测吗？
A_EN: No. The ordinary multinomial distribution is defined for nonnegative integer counts with a fixed total. TF-IDF supplies nonnegative real weights. Multinomial NB software commonly uses these weights in its scoring and estimation procedure, often usefully, but that is not the same literal count-generating interpretation. Keep the practical model and the probability definition distinct.
A_ZH: 不是。普通多项式分布定义在总次数固定的非负整数计数上，TF-IDF 则提供非负实数权重。多项式 NB 软件常将这些权重用于评分与估计，实践中可能有效，但不能直接视为同一个严格计数生成过程。应区分实用模型与概率分布定义。

@@ M102 | 10-extension | extension | B1:32-41
Q_EN: How does a decision change when false positives and false negatives have unequal costs?
Q_ZH: 假阳性与假阴性的代价不相等时，决策如何变化？
A_EN: Let $p=P(y=1\mid x)$, with zero cost for correct predictions. Predicting 1 costs $C_{FP}(1-p)$ in expectation; predicting 0 costs $C_{FN}p$. Choose 1 when $p>C_{FP}/(C_{FP}+C_{FN})$. A threshold of 0.5 follows only when the two costs are equal. This is an extension of the lecture's equal-cost Bayes decision.
A_ZH: 设 $p=P(y=1\mid x)$，正确分类代价为 0。预测为 1 的期望代价是 $C_{FP}(1-p)$，预测为 0 的期望代价是 $C_{FN}p$。当 $p>C_{FP}/(C_{FP}+C_{FN})$ 时选择 1。只有两种错误代价相同时，阈值才是 0.5。这是对课堂等代价贝叶斯决策的扩展。

@@ M103 | 10-extension | extension | B2:3,25-28;NB:1.9
Q_EN: Does an NB posterior of 0.99 guarantee about 99% correctness on such predictions?
Q_ZH: NB 输出后验 0.99，是否保证这类预测约有 99% 正确？
A_EN: No. That interpretation requires calibration on the relevant data population. Misspecified distributions or correlated features can make NB probabilities overconfident even when the winning class is useful. Check probability quality separately from classification accuracy. This extension explains why a model-generated confidence number should not be treated as an independently verified success rate.
A_ZH: 不保证。这种解释要求概率在相关数据总体上经过校准。分布假设错误或特征相关，可能使 NB 概率过于自信，即使最大分数类别仍有预测价值。概率质量应与分类准确率分开检查。本扩展说明：模型输出的置信数字不能当作独立验证的成功率。

@@ M104 | 10-extension | extension | T1:35-45;B2:34-44
Q_EN: Does zero covariance always imply independence?
Q_ZH: 零协方差一定意味着独立吗？
A_EN: No. Let $X$ be uniform on $\{-1,0,1\}$ and $Y=X^2$. Symmetry gives $\operatorname{Cov}(X,Y)=0$, but $Y$ is determined by $X$, so they are dependent. For jointly Gaussian variables, zero cross-covariance does imply independence. The Gaussian qualification is essential when connecting diagonal covariance to naive Bayes.
A_ZH: 不一定。令 $X$ 在 $\{-1,0,1\}$ 上均匀分布，$Y=X^2$。对称性使 $\operatorname{Cov}(X,Y)=0$，但 $Y$ 被 $X$ 完全确定，两者仍相关依赖。对联合高斯变量，零交叉协方差才意味着独立。由对角协方差联系到朴素贝叶斯时，这个高斯前提很关键。

@@ M105 | 10-extension | extension | B1:8-48;B2:3-99
Q_EN: Give a one-minute English explanation of naive Bayes, including a limitation.
Q_ZH: 用一分钟英语解释朴素贝叶斯，并说明一项局限。
A_EN: “Naive Bayes is a generative classifier. It estimates class priors and class-conditional feature distributions, assuming features are conditionally independent given the class. Bayes' rule combines these terms into posterior class scores. We usually add log probabilities for numerical stability and use smoothing to avoid zero estimates. The independence assumption reduces the number of parameters, but correlated features can distort probabilities.” Practice adapting this explanation to Gaussian or text features.
A_ZH: “朴素贝叶斯是生成式分类器。它估计类别先验和类条件特征分布，假设给定类别后特征条件独立。贝叶斯公式将这些量组合为类别后验分数。通常使用对数概率求和以稳定计算，并通过平滑避免零估计。独立假设减少参数量，但特征相关可能使概率失真。”练习将这段解释改成高斯特征或文本特征的具体版本。

@@ M106 | 10-extension | extension | A1:3;B2:61-99
Q_EN: Design a small experiment that separates the effect of representation from the effect of classifier.
Q_ZH: 怎样设计小实验，区分特征表示和分类器各自的影响？
A_EN: Fix the split and metric. First compare count versus TF-IDF features with the same multinomial NB settings; then compare compatible classifiers under a fixed representation. Tune each method fairly within training/validation and report class recalls as well as balanced accuracy. Change one factor at a time for interpretation, while acknowledging possible interactions. This is an AI-added research habit, not a confirmed QE question.
A_ZH: 固定划分与指标。先在相同多项式 NB 设置下比较计数与 TF-IDF，再在固定表示下比较兼容的分类器。训练/验证内部公平调参，同时报告各类召回率和平衡准确率。为便于解释，每次改变一个因素，但也承认因素之间可能有交互。这是 AI 补充的研究训练，不是已确认的 QE 考题。

@@ M108 | 11-tutorial2 | classroom | T2:10-18
Q_EN: How should the Bernoulli and multinomial text-classification pipelines differ?
Q_ZH: 伯努利与多项式文本分类流程应怎样区分？
A_EN: Learn one vocabulary from training documents. Bernoulli NB uses whether each vocabulary word occurs, so counts must be binarized. The requested multinomial experiment uses nonnegative TF-IDF weights instead. Fit vocabulary and IDF on training data, and only transform held-out documents. Compare both pipelines under the same evaluation split and record `max_features` and smoothing.
A_ZH: 从训练文档学习词表。Bernoulli NB 使用各词是否出现，因此计数要二值化；题目要求的多项式实验则使用非负 TF-IDF 权重。词表和 IDF 都只在训练数据拟合，留出文档仅做转换。应使用同一评估划分比较两条流程，并记录词表上限与平滑参数。

@@ M109 | 11-tutorial2 | classroom | T2:15-20
Q_EN: Do the ten words with the largest `feature_log_prob_` values necessarily best distinguish one news class?
Q_ZH: `feature_log_prob_` 最大的十个词，一定最能区分某个新闻类别吗？
A_EN: No. They have high estimated probability within that class, but may also be common in other classes. To assess discrimination, compare log probabilities across classes. Also distinguish a stored log probability from its exponential: a value of -2 is a log probability, while the corresponding probability is about 0.1353. Describe the notebook output as frequent/high-probability words unless you perform a class contrast.
A_ZH: 不一定。它们在该类内估计概率高，但也可能在其他类中常见。判断区分力还需跨类别比较对数概率。另要区分对数值与取指数后的概率：-2 是对数概率，对应概率约为 0.1353。未做类别对比时，应将输出描述为高频或高概率词。

@@ M110 | 11-tutorial2 | classroom | T2:21-28
Q_EN: How should I interpret smoothing and vocabulary-size experiments without overstating test performance?
Q_ZH: 如何解释平滑和词表大小实验，同时避免夸大测试效果？
A_EN: For each setting, refit the model and plot accuracy against that setting while keeping other choices fixed. The tutorial asks you to try settings against its named test set. Once used for selection, that set functions as validation and its best score is no longer an independent final estimate. A stronger protocol selects settings by cross-validation inside the 2,000 training documents, then evaluates the 1,000 held-out documents once.
A_ZH: 每个设置都重新训练，保持其他选择固定，再画准确率随该设置变化的图。教程要求对名为 test 的集合反复尝试参数；一旦用它选参，它实际上承担验证集角色，最高分不再是独立最终评估。更严格的做法是在 2,000 篇训练文档内部交叉验证选参，最后只评估一次 1,000 篇留出文档。

@@ M111 | 11-tutorial2 | learn | T2:29-31
Q_EN: What is the Poisson distribution, and how is its rate estimated from counts?
Q_ZH: 什么是泊松分布？如何根据计数估计其参数？
A_EN: $P(X=x)=e^{-\mu}\mu^x/x!$ for nonnegative integer $x$ and rate $\mu\ge0$. Its mean and variance both equal $\mu$. For independent observations, the MLE is their average: $\hat\mu=N^{-1}\sum_n x^{(n)}$. Word counts $(0,1,3,0)$ therefore give $\hat\mu=1$. Raw nonnegative counts match this observation model; fractional TF-IDF values do not literally represent Poisson counts.
A_ZH: 对非负整数 $x$ 和参数 $\mu\ge0$，$P(X=x)=e^{-\mu}\mu^x/x!$，其均值与方差都为 $\mu$。独立观测的 MLE 是平均值：$\hat\mu=N^{-1}\sum_n x^{(n)}$。词计数 $(0,1,3,0)$ 给出 $\hat\mu=1$。原始非负计数匹配此观测模型，分数形式的 TF-IDF 则不是真正的泊松计数。

@@ M112 | 11-tutorial2 | classroom | T2:31-32
Q_EN: What parameters must a Poisson naive Bayes classifier learn?
Q_ZH: Poisson Naive Bayes 分类器需要学习哪些参数？
A_EN: Learn a class prior $\pi_c=N_c/N$ and a mean count $\mu_{cj}=N_c^{-1}\sum_{n:y_n=c}x_{nj}$ for every class $c$ and vocabulary word $j$. Given the class, assume word counts are independent, so $p(x\mid c)=\prod_j\mathrm{Poisson}(x_j;\mu_{cj})$. A class with longer documents can have larger total expected counts. Do not force these means to sum to 1.
A_ZH: 学习类别先验 $\pi_c=N_c/N$，以及每类每个词的平均计数 $\mu_{cj}=N_c^{-1}\sum_{n:y_n=c}x_{nj}$。给定类别后假设计数独立，于是 $p(x\mid c)=\prod_j\mathrm{Poisson}(x_j;\mu_{cj})$。文档更长的类别可以有更大的总期望计数，这些均值不要求和为 1。

@@ M113 | 11-tutorial2 | classroom | T2:29-32
Q_EN: Derive a numerically stable Poisson NB class score.
Q_ZH: 如何推导数值稳定的 Poisson NB 类别分数？
A_EN: For positive rates, taking logs gives $s_c=\log\pi_c+\sum_j[x_j\log\mu_{cj}-\mu_{cj}-\log(x_j!)]$. For class selection, omit the shared factorial sum, leaving $\log\pi_c+x^T\log\mu_c-\sum_j\mu_{cj}$. Keep the negative-rate term: absent words contribute through it. Use positive smoothed rates or handle zero-rate Poisson cases explicitly, avoiding numerical 0 times log 0. Normalize posteriors with log-sum-exp.
A_ZH: 对正的率参数，取对数得 $s_c=\log\pi_c+\sum_j[x_j\log\mu_{cj}-\mu_{cj}-\log(x_j!)]$。选类别时可省略共同的阶乘项，剩下 $\log\pi_c+x^T\log\mu_c-\sum_j\mu_{cj}$。负率项不能省略，未出现的词也通过它作贡献。应使用正的平滑率，或显式处理零率 Poisson 边界，避免数值计算 0 乘 log 0。后验用 log-sum-exp 归一化。

@@ M114 | 11-tutorial2 | worked | T2:31-32
Q_EN: Two classes have equal priors and Poisson means $(2,1)$ and $(1,2)$. Which class does document $x=(2,0)$ favor?
Q_ZH: 两类先验相等，泊松均值分别为 $(2,1)$、$(1,2)$，文档 $x=(2,0)$ 更支持哪类？
A_EN: Both rate sums equal 3. After dropping shared prior and factorial terms, scores are $2\log2-3$ and $2\log1-3=-3$. The first exceeds the second by $2\log2=\log4$, giving likelihood ratio 4 and posterior probability $4/(4+1)=0.8$ for the first class. This is a toy calculation, not an AGNews experiment result.
A_ZH: 两类参数和都是 3。省略共同先验和阶乘项后，分数为 $2\log2-3$ 与 $2\log1-3=-3$。第一类高出 $2\log2=\log4$，因此似然比为 4，第一类后验为 $4/(4+1)=0.8$。这是手算例子，不是 AGNews 实验成绩。

@@ M115 | 11-tutorial2 | classroom | T2:31-32
Q_EN: Why smooth Poisson count rates, and how do pseudo-counts differ from pseudo-exposure?
Q_ZH: 为什么要平滑泊松计数率？伪计数与额外暴露量有什么区别？
A_EN: An estimated rate of zero assigns zero probability to every positive count. One explicit smoothing rule is $\tilde\mu_{cj}=(T_{cj}+a)/(N_c+b)$, where $T_{cj}$ is the total feature count in class c, $N_c>0$ is the number of equal-exposure documents, $a>0$ is a pseudo-count, and $b\ge0$ is extra exposure measured in document units. The numerator adds events; the denominator adds exposure. This is not Bernoulli's two-outcome denominator. State the convention and select its strength using validation data.
A_ZH: 若估计率为零，任何正计数都会得到零概率。一种明确的平滑规则为 $\tilde\mu_{cj}=(T_{cj}+a)/(N_c+b)$：$T_{cj}$ 是 c 类中该特征的总计数，$N_c>0$ 是等暴露量文档数，$a>0$ 为伪计数，$b\ge0$ 为以文档数计的额外暴露量。分子补事件，分母补暴露量；它不等于伯努利两种结果的分母。必须说明约定，并用验证数据选择强度。

@@ M116 | 11-tutorial2 | check | T2:31-35
Q_EN: Why might Poisson NB be a poor model for some document collections?
Q_ZH: 为什么 Poisson NB 对某些文档集合可能不合适？
A_EN: It assumes independent counts within each class and equates each count's mean and variance. Real text can have correlated words, bursty repetition and widely varying document lengths. These violate the simple model and may cause overdispersion or excessive length effects. Compare held-out errors and scores against Bernoulli and multinomial models; an assumption violation alone does not establish which classifier will win.
A_ZH: 它假设类内计数独立，且各计数的均值等于方差。真实文本可能有词语相关、突发重复和很不一致的文档长度，从而出现过度离散或过强长度效应。应比较它与伯努利、多项式模型的留出错误与分数；仅指出假设不完美，还不能断言哪个分类器一定获胜。

@@ M117 | 11-tutorial2 | classroom | T2:31-34
Q_EN: What checks make a custom PoissonNB implementation credible?
Q_ZH: 哪些检查能验证自定义 PoissonNB 实现？
A_EN: Confirm nonnegative integer inputs, one rate per class/feature, and normalized priors. Compare matrix scores with a direct sum of Poisson log probabilities on a tiny dataset. Check that posterior rows sum to 1 and that predicted labels follow their largest entries. Map arbitrary class labels explicitly. If using sparse word counts, compute $X\log\mu_c$ without expanding a large document matrix to dense form.
A_ZH: 检查输入是非负整数、每类每特征有一个参数、先验已归一化。用小数据对比矩阵分数与逐项泊松对数概率之和。验证后验每行和为 1，预测标签对应最大后验，并显式映射任意类别标签。使用稀疏词频时，应直接计算 $X\log\mu_c$，避免把大文档矩阵全变成稠密数组。

@@ M118 | 11-tutorial2 | check | T2:21-28,35
Q_EN: What belongs in the tutorial's final comparison and misclassification explanation?
Q_ZH: 教程最后的模型比较与错分解释应包括什么？
A_EN: Record model, representation, vocabulary size, smoothing, selection protocol and measured accuracy. Inspect a few errors for overlapping topics, missing vocabulary or misleading common words. “Business versus Sci/Tech overlap may explain this case” is a hypothesis; point to the actual text before presenting it as an explanation. Keep observed scores separate from expected behavior and untested improvements.
A_ZH: 记录模型、表示、词表大小、平滑、选参流程与实测准确率。观察少量错误是否涉及主题交叉、词表缺词或常用词误导。“商业与科技交叉可能导致此例错分”是假设，必须结合实际文本说明。应区分观测分数、预期行为和未测试的改进。

@@ M119 | 12-logistic | learn | L3A:4-7
Q_EN: What does a discriminative classifier learn compared with a generative classifier?
Q_ZH: 判别式分类器与生成式分类器分别学习什么？
A_EN: A generative classifier models $p(x\mid y)$ and class priors, then obtains $p(y\mid x)$ by Bayes' rule. A discriminative method learns the posterior or a decision rule directly. Logistic regression models $p(y\mid x)$; an SVM directly learns a separating decision function. Both can classify without first modeling the complete feature distribution of each class.
A_ZH: 生成式分类器先建模 $p(x\mid y)$ 和类别先验，再通过贝叶斯公式得到 $p(y\mid x)$。判别式方法直接学习后验或决策规则。逻辑回归建模 $p(y\mid x)$，SVM 直接学习分隔决策函数，两者都不必先描述每类完整的特征分布。

@@ M120 | 12-logistic | learn | L3A:8-22
Q_EN: Why can a Gaussian generative classifier have a linear decision boundary?
Q_ZH: 为什么高斯生成式分类器也可能具有线性决策边界？
A_EN: In the lecture's binary example, all features and both classes share variance $\sigma^2$. Subtracting Gaussian log densities cancels the $x_j^2$ terms. With class means $\mu,\nu$, the log posterior ratio is $w^Tx+b$, where $w=(\mu-\nu)/\sigma^2$ and $b=(\|\nu\|^2-\|\mu\|^2)/(2\sigma^2)+\log(\pi_1/\pi_2)$. A linear boundary therefore does not identify the training method as discriminative.
A_ZH: 课堂二分类例子假设两个类别、所有特征共用方差 $\sigma^2$，相减高斯对数密度时，$x_j^2$ 项抵消。设两类均值为 $\mu,\nu$，对数后验比为 $w^Tx+b$，其中 $w=(\mu-\nu)/\sigma^2$，$b=(\|\nu\|^2-\|\mu\|^2)/(2\sigma^2)+\log(\pi_1/\pi_2)$。所以边界线性，不能证明训练方法一定是判别式。

@@ M121 | 12-logistic | learn | L3A:24-30
Q_EN: What do $w$ and $b$ control in the linear classifier $f(x)=w^Tx+b$?
Q_ZH: 在线性分类器 $f(x)=w^Tx+b$ 中，$w$ 和 $b$ 分别控制什么？
A_EN: Predict +1 for positive score and -1 for negative score, with an explicit tie rule at zero. The boundary is $w^Tx+b=0$; $w$ is perpendicular to it and $b$ shifts its position. In $d$ dimensions, a nonzero $w$ defines a $(d-1)$-dimensional hyperplane. The score is not automatically a probability or a physical distance.
A_ZH: 分数为正预测 +1，为负预测 -1，等于零时须约定规则。边界为 $w^Tx+b=0$，$w$ 与边界垂直，$b$ 改变边界位置。在 $d$ 维中，非零 $w$ 定义一个 $(d-1)$ 维超平面。原始分数并不自动等于概率或几何距离。
MEDIA: Lecture3a-cell-29-output-1.png

@@ M122 | 12-logistic | worked | L3A:24-30
Q_EN: For $w=(2,1)$ and $b=-3$, classify $(2,0)$ and $(0,1)$ and describe the boundary.
Q_ZH: 若 $w=(2,1)$、$b=-3$，如何分类 $(2,0)$ 与 $(0,1)$？边界是什么？
A_EN: Scores are $2(2)+0-3=1$ and $0+1-3=-2$, so predict +1 and -1. The boundary is $2x_1+x_2-3=0$, or $x_2=3-2x_1$. Its normal vector is $(2,1)$. Multiplying both $w$ and $b$ by the same positive number preserves these labels and the boundary, though it changes raw scores.
A_ZH: 两个分数为 $2(2)+0-3=1$ 与 $0+1-3=-2$，因此分别预测 +1、-1。边界为 $2x_1+x_2-3=0$，即 $x_2=3-2x_1$，法向量是 $(2,1)$。将 $w,b$ 同时乘同一个正数，会保持边界和标签，但改变原始分数。

@@ M123 | 12-logistic | learn | L3A:32-35
Q_EN: How does logistic regression turn a linear score into a class probability?
Q_ZH: 逻辑回归怎样把线性分数变成类别概率？
A_EN: Use the sigmoid $\sigma(z)=1/(1+e^{-z})$. Let $p(y=+1\mid x)=\sigma(w^Tx+b)$ and $p(y=-1\mid x)=1-p(y=+1\mid x)$. The mapping lies between 0 and 1, equals 0.5 at score zero, and increases with the score. Despite its name, logistic regression is used here for classification.
A_ZH: 使用 sigmoid 函数 $\sigma(z)=1/(1+e^{-z})$。令 $p(y=+1\mid x)=\sigma(w^Tx+b)$，另一类概率为补数 $p(y=-1\mid x)=1-p(y=+1\mid x)$。输出位于 0 与 1 之间，分数为零时为 0.5，并随分数增大而增大。虽然名字含 regression，本课用它做分类。
MEDIA: Lecture3a-cell-34.png

@@ M124 | 12-logistic | learn | L3A:32-44
Q_EN: What is the log-odds interpretation of a logistic-regression score?
Q_ZH: 逻辑回归分数的对数几率解释是什么？
A_EN: If $p=\sigma(w^Tx+b)$, then $\log[p/(1-p)]=w^Tx+b$. Holding other features fixed, increasing feature $j$ by one unit changes log odds by $w_j$ and multiplies odds by $e^{w_j}$. It does not add $w_j$ directly to the probability, and a learned association is not automatically a causal effect.
A_ZH: 若 $p=\sigma(w^Tx+b)$，则 $\log[p/(1-p)]=w^Tx+b$。其他特征固定时，第 $j$ 个特征增加一个单位，会使对数几率增加 $w_j$、几率乘 $e^{w_j}$。这不等于概率直接加 $w_j$，学到的关联也不能自动解释为因果效应。

@@ M125 | 12-logistic | learn | L3A:39-46
Q_EN: Why can the true-class probability be written as $\sigma(yf(x))$ when $y\in\{-1,+1\}$?
Q_ZH: 标签为 $y\in\{-1,+1\}$ 时，为什么真实类别概率可写成 $\sigma(yf(x))$？
A_EN: For $y=+1$, it is $\sigma(f(x))$. For $y=-1$, use $1-\sigma(f(x))=\sigma(-f(x))$. Combining both gives $\sigma(yf(x))$. The signed score $z=yf(x)$ is positive for a correct classification and negative for an error. This formula assumes the ±1 label convention; do not substitute 0/1 labels unchanged.
A_ZH: $y=+1$ 时概率为 $\sigma(f(x))$；$y=-1$ 时利用 $1-\sigma(f(x))=\sigma(-f(x))$。合并得到 $\sigma(yf(x))$。带标签的分数 $z=yf(x)$ 正值表示分类正确，负值表示错误。本式采用 ±1 标签，不能不改公式就代入 0/1 标签。

@@ M126 | 12-logistic | learn | L3A:44-48
Q_EN: How does maximum likelihood produce the logistic loss?
Q_ZH: 最大似然怎样导出逻辑损失？
A_EN: The negative log probability of the true label is $\ell(z)=-\log\sigma(z)=\log(1+e^{-z})$, with $z=yf(x)$. Minimize the sum of this loss over training examples. At $z=0$, the loss is $\log2\approx0.6931$; at $z=2$, it is about 0.1269; at $z=-2$, about 2.1269. Confident errors receive much larger penalties than confident correct predictions.
A_ZH: 真实标签概率的负对数为 $\ell(z)=-\log\sigma(z)=\log(1+e^{-z})$，其中 $z=yf(x)$，训练时最小化各样本损失之和。$z=0$ 时为 $\log2\approx0.6931$，$z=2$ 时约为 0.1269，$z=-2$ 时约为 2.1269。自信但错误的预测会受到更大惩罚。
MEDIA: Lecture3a-cell-48.png

@@ M127 | 12-logistic | learn | L3A:38-45
Q_EN: What is binary cross-entropy under the alternative 0/1 label convention?
Q_ZH: 改用 0/1 标签时，二元交叉熵是什么？
A_EN: For target $t\in\{0,1\}$ and predicted positive probability $p$, use $\ell=-t\log p-(1-t)\log(1-p)$. If $t=1$, only $-\log p$ remains; if $t=0$, only $-\log(1-p)$ remains. This matches the ±1 logistic loss after converting $y=2t-1$. Keep the label encoding explicit when copying equations into code.
A_ZH: 对目标 $t\in\{0,1\}$ 和正类概率 $p$，损失为 $\ell=-t\log p-(1-t)\log(1-p)$。$t=1$ 时只剩 $-\log p$，$t=0$ 时只剩 $-\log(1-p)$。通过 $y=2t-1$ 转换后，它与 ±1 写法的逻辑损失一致。把公式写成代码时必须明确标签编码。

@@ M128 | 12-logistic | learn | L3A:45,52
Q_EN: What gradient does one logistic-regression example contribute?
Q_ZH: 一个逻辑回归样本对梯度贡献什么？
A_EN: With a 0/1 target $t$, score $z=w^Tx+b$ and $p=\sigma(z)$, the chain rule gives $\partial\ell/\partial z=p-t$. Therefore $\nabla_w\ell=(p-t)x$ and $\partial\ell/\partial b=p-t$. The feature vector directs the update, while prediction error determines its sign and size. Sum or average consistently across samples, then add any regularizer's gradient.
A_ZH: 对 0/1 标签 $t$、分数 $z=w^Tx+b$ 与 $p=\sigma(z)$，链式法则给出 $\partial\ell/\partial z=p-t$，所以 $\nabla_w\ell=(p-t)x$、$\partial\ell/\partial b=p-t$。特征向量决定更新方向，预测误差决定符号和大小。跨样本求和或平均时须保持一致，再加入正则项梯度。

@@ M129 | 12-logistic | worked | L3A:52
Q_EN: Perform one gradient step for $x=2,t=1,w=0$, holding $b=0$, with learning rate 0.1 and no regularization.
Q_ZH: 对 $x=2,t=1,w=0$，固定 $b=0$，学习率 0.1、无正则，做一步梯度下降。
A_EN: Initially $p=\sigma(0)=0.5$. The weight gradient is $(0.5-1)\times2=-1$. Thus $w_{new}=0-0.1(-1)=0.1$. The new score is 0.2, so $p_{new}\approx0.5498$, moving toward the positive target. The bias is held fixed in this example; updating it would be a different calculation.
A_ZH: 初始概率为 $p=\sigma(0)=0.5$，权重梯度是 $(0.5-1)\times2=-1$，故 $w_{new}=0-0.1(-1)=0.1$。新分数为 0.2，概率约为 0.5498，向正类目标移动。本例固定偏置，若连偏置一起更新，计算结果会不同。

@@ M130 | 12-logistic | learn | L3A:49-51
Q_EN: Why does a Gaussian prior on weights give an L2 regularization term?
Q_ZH: 为什么给权重加高斯先验会产生 L2 正则项？
A_EN: For the lecture's prior $w\sim\mathcal N(0,(C/2)I)$, the negative log prior is $\|w\|^2/C$ plus a parameter-independent constant. Maximum a posteriori estimation therefore minimizes $\|w\|^2/C+\sum_i\log(1+e^{-y_if(x_i)})$. Small $C$ penalizes large weights more strongly. The coefficient depends on the chosen prior variance and on whether the data loss is summed or averaged.
A_ZH: 课堂先验为 $w\sim\mathcal N(0,(C/2)I)$，负对数先验等于 $\|w\|^2/C$ 加上与权重无关的常数。因此最大后验估计最小化 $\|w\|^2/C+\sum_i\log(1+e^{-y_if(x_i)})$。较小 $C$ 更强地惩罚大权重。具体系数取决于先验方差，也取决于数据损失是求和还是求平均。

@@ M131 | 12-logistic | check | L3A:51-52,65-69
Q_EN: How do regularization strength, learning rate and training duration differ?
Q_ZH: 正则化强度、学习率和训练时长有什么区别？
A_EN: Regularization changes the optimization objective and the solutions it prefers. Learning rate controls the size of each optimization step. Training duration controls how many steps the solver takes. A small learning rate does not replace regularization, and stopping because the iteration limit was reached does not prove convergence. In the lecture's convention, smaller $C$ means stronger weight regularization.
A_ZH: 正则化改变优化目标及其偏好的解；学习率控制每一步更新大小；训练时长控制迭代次数。小学习率不能代替正则化，达到迭代上限也不代表已经收敛。课堂采用的约定中，较小 $C$ 表示更强的权重正则。

@@ M132 | 12-logistic | learn | L3A:45,49-52
Q_EN: Why can unregularized logistic regression have no finite optimum on perfectly separable data?
Q_ZH: 为什么完全可分数据上的无正则逻辑回归可能没有有限最优参数？
A_EN: If one separating direction makes every $y_if(x_i)>0$, scaling its weights and bias upward keeps reducing $\log(1+e^{-y_if(x_i)})$ toward zero. The loss approaches an infimum while parameter norms can diverge. A weight penalty opposes that growth. Thus convexity does not by itself guarantee that a finite minimizing parameter vector exists.
A_ZH: 若某分隔方向让所有 $y_if(x_i)>0$，不断放大权重和偏置，就会使损失 $\log(1+e^{-y_if(x_i)})$ 趋向零。损失逼近下确界时，参数范数却可能发散。权重惩罚会抑制这种增长。因此目标凸，并不单独保证存在有限参数的最小点。

@@ M133 | 12-logistic | classroom | L3A:68-73
Q_EN: How does the lecture select $C$ by cross-validation?
Q_ZH: 课堂如何用交叉验证选择 $C$？
A_EN: Choose candidate values, split the training data into folds, fit each candidate using each fold's training portion, and evaluate on that fold's validation portion. Average validation scores and choose the best candidate. Refit it on the entire training set before evaluating the held-out test set. The held-out test samples are excluded from both selection and refitting.
A_ZH: 先选候选值，将训练数据分折；每个候选都在各折训练部分拟合，在对应验证部分评估。平均验证分数后选最佳候选，再用整个训练集重训，最后评估留出测试集。测试样本既不参与选参，也不参与这里的重训。
MEDIA: Lecture3-10_fold_cv.png

@@ M134 | 12-logistic | worked | L3A:68-73
Q_EN: $C=0.1$ scores $(0.82,0.86,0.84)$ across three folds; $C=10$ scores $(0.90,0.74,0.79)$. Which should this mean-score rule select?
Q_ZH: 三折中 $C=0.1$ 得分 $(0.82,0.86,0.84)$，$C=10$ 得分 $(0.90,0.74,0.79)$，按平均分应选哪个？
A_EN: The means are 0.84 and 0.81, so select $C=0.1$. Choosing $C=10$ because it achieved one 0.90 score ignores its other folds. These scores are a teaching example. In real small datasets, also consider variation and use consistent splits and metrics when comparing candidates.
A_ZH: 平均分分别为 0.84、0.81，因此选 $C=0.1$。仅因某一折达到 0.90 就选 $C=10$，忽视了其他折的表现。这是教学例子；真实小数据集还应关注波动，并在一致划分和指标下比较候选。

@@ M135 | 12-logistic | check | L3A:68-73;L3C:7-8
Q_EN: If scaling is learned once before cross-validation, what information can leak?
Q_ZH: 如果交叉验证前先统一拟合标准化，会泄漏什么信息？
A_EN: Validation-fold means, variances or extrema can influence the transformation used to train that fold's model. Fit the scaler within each fold's training portion, then apply it unchanged to validation. A pipeline containing both preprocessing and classifier supports this design. The same rule applies to vocabulary and IDF estimation for text models.
A_ZH: 验证折的均值、方差或极值可能影响该折训练模型所用的转换。应在每折训练部分拟合缩放器，再原样用于验证。将预处理与分类器一起放进 Pipeline 可支持这个流程。文本模型的词表和 IDF 估计也遵守同样原则。

@@ M136 | 12-logistic | learn | L3A:74-85
Q_EN: How does one-vs-rest extend binary classification to $K$ classes?
Q_ZH: One-vs-rest 如何把二分类扩展到 $K$ 类？
A_EN: Train $K$ binary classifiers: class $c$ versus all other classes for each $c$. At prediction, compare their class scores and select the largest. With three classes, the tasks are 1 versus {2,3}, 2 versus {1,3}, and 3 versus {1,2}. Independently trained binary probabilities need not sum to 1 before an explicit combining or normalization rule.
A_ZH: 训练 $K$ 个二分类器，每个区分类别 $c$ 与其他所有类别。预测时比较类别分数，取最大者。三类时分别训练 1 对 {2,3}、2 对 {1,3}、3 对 {1,2}。各二分类器独立输出的概率，在明确组合或归一化前不一定和为 1。

@@ M137 | 12-logistic | learn | L3A:86-91
Q_EN: How does softmax define a joint multiclass probability model?
Q_ZH: Softmax 如何定义联合的多类别概率模型？
A_EN: Assign each class a score $f_c(x)=w_c^Tx+b_c$ and set $p_c=e^{f_c(x)}/\sum_k e^{f_k(x)}$. All classes share one denominator, so probabilities sum to 1 and the largest score gives the largest probability. The parameters are trained jointly. A bias can be included explicitly or through a constant feature, even when a shorthand equation omits it.
A_ZH: 给每类一个分数 $f_c(x)=w_c^Tx+b_c$，令 $p_c=e^{f_c(x)}/\sum_k e^{f_k(x)}$。各类共享分母，因此概率和为 1，最大分数对应最大概率，参数也联合训练。偏置可以显式加入，也可以用常数特征表示，不能因简写公式省略它就误以为不允许偏置。

@@ M138 | 12-logistic | worked | L3A:86-89
Q_EN: Compute softmax for scores $(\log2,0,0)$. What if all scores increase by 1,000?
Q_ZH: 分数为 $(\log2,0,0)$ 时 Softmax 是多少？若全部增加 1,000 呢？
A_EN: Exponentials are $(2,1,1)$, giving probabilities $(0.5,0.25,0.25)$. Adding the same constant to every score multiplies numerator and denominator by the same factor, leaving the probabilities unchanged. For stability, subtract the maximum score before exponentiating. This prevents avoidable overflow while preserving the prediction.
A_ZH: 指数为 $(2,1,1)$，归一化得 $(0.5,0.25,0.25)$。所有分数加同一常数，会让分子分母乘相同因子，概率不变。数值计算时先减最大分数再取指数，可避免不必要的上溢，同时保持预测结果。

@@ M139 | 12-logistic | learn | L3A:90-91
Q_EN: Why does one-hot cross-entropy reduce to the negative log probability of the true class?
Q_ZH: 为什么 one-hot 交叉熵等于真实类别概率的负对数？
A_EN: With one-hot target $t$, only the true class $c$ has $t_c=1$. Thus $-\sum_j t_j\log p_j=-\log p_c$. If the true class probability is 0.25, loss is $-\log0.25=\log4\approx1.3863$. Improving another wrong class at the expense of the true class does not improve this loss.
A_ZH: One-hot 目标中，只有真实类别 $c$ 的 $t_c=1$，所以 $-\sum_j t_j\log p_j=-\log p_c$。真实类别概率为 0.25 时，损失为 $-\log0.25=\log4\approx1.3863$。若牺牲真实类别概率来提高另一个错误类别，并不能改善该损失。

@@ M140 | 12-logistic | learn | L3A:86-97
Q_EN: How do one-vs-rest logistic regression and multinomial logistic regression differ?
Q_ZH: One-vs-rest 逻辑回归与多项式逻辑回归有什么区别？
A_EN: One-vs-rest trains separate binary tasks. Multinomial logistic regression trains a joint softmax model whose class scores compete through one normalization and one cross-entropy objective. Both can produce linear boundaries in the original features, but their training objectives differ. A multiclass dataset alone does not tell you which formulation an implementation uses.
A_ZH: One-vs-rest 分别训练多个二元任务；多项式逻辑回归联合训练 Softmax 模型，各类分数在共享归一化和交叉熵目标中竞争。两者都可能在原特征空间产生线性边界，但训练目标不同。仅看到多分类数据，不能判断程序用了哪种形式。

@@ M141 | 12-logistic | check | L3A:59,98-99
Q_EN: What can I infer from a positive learned coefficient, and what additional context is needed?
Q_ZH: 学到正系数能说明什么？还需要哪些上下文？
A_EN: Holding other inputs fixed, increasing that feature raises the positive-class logit under the model. Check the label mapping, feature scaling and whether other features are correlated. The coefficient's magnitude depends on units, so it is not automatically a comparable feature-importance score. The lecture's fitted Iris coefficients are one saved run, not universal constants.
A_ZH: 在其他输入固定时，增加该特征会提高模型的正类 logit。还应检查标签映射、特征缩放和特征间相关性。系数大小依赖单位，不能自动当作可直接比较的特征重要性。课件中的 Iris 拟合系数只是一次保存的运行结果，不是通用常数。

@@ M143 | 13-svm | learn | L3B:4-27;SVM:1
Q_EN: What margin does a hard-margin SVM try to maximize?
Q_ZH: 硬间隔 SVM 要最大化什么间隔？
A_EN: For correctly separated training data, the margin is the smallest perpendicular distance from any training point to the decision hyperplane. Maximizing it leaves more geometric room between the classes. It is a minimum over points, so the closest points matter most. The initial hard-margin formulation requires linearly separable data; overlapping data need a different formulation.
A_ZH: 对已正确分开的训练数据，间隔是所有训练点到决策超平面的最小垂直距离。最大化它，为两类之间留出更多几何余量。由于取最小值，最近的点最关键。最初的硬间隔形式要求数据线性可分，重叠数据需要另一个形式。
MEDIA: Lecture3b-cell-20-output-1.png

@@ M144 | 13-svm | worked | L3B:27-32;SVM:1
Q_EN: Find the distance from $(2,0)$ to $2x_1+x_2-3=0$. Why does rescaling the equation not change it?
Q_ZH: 求 $(2,0)$ 到 $2x_1+x_2-3=0$ 的距离。为什么缩放方程不改变距离？
A_EN: The distance is $|w^Tx+b|/\|w\|=|1|/\sqrt5\approx0.4472$. Multiplying both $w$ and $b$ by a nonzero number scales numerator and denominator equally in absolute value. The hyperplane is unchanged. A negative scale reverses the sign-based class convention, whereas a positive scale preserves it.
A_ZH: 距离为 $|w^Tx+b|/\|w\|=|1|/\sqrt5\approx0.4472$。将 $w,b$ 同乘非零数时，分子分母的绝对值同比缩放，超平面不变。负比例会颠倒按符号划分的类别方向，正比例则保持类别方向。

@@ M145 | 13-svm | learn | L3B:33-36;SVM:1
Q_EN: State the hard-margin SVM primal optimization problem and interpret its constraints.
Q_ZH: 写出硬间隔 SVM 的原始优化问题，并解释约束。
A_EN: Minimize $\frac12\|w\|^2$ over $w,b$, subject to $y_i(w^Tx_i+b)\ge1$ for every training point, with $y_i\in\{-1,+1\}$. The constraints enforce correct classification and a normalized functional margin. Minimizing the weight norm then maximizes the geometric margin. Using only $|w^Tx_i+b|\ge1$ would fail to enforce the correct side for each label.
A_ZH: 对 $w,b$ 最小化 $\frac12\|w\|^2$，并对所有训练点要求 $y_i(w^Tx_i+b)\ge1$，其中 $y_i\in\{-1,+1\}$。约束保证类别方向正确且具有归一化函数间隔；此时最小化权重范数就最大化几何间隔。仅要求 $|w^Tx_i+b|\ge1$，不能保证各标签位于正确一侧。

@@ M146 | 13-svm | check | L3B:33-36,46;SVM:1
Q_EN: Is the SVM margin $1/\|w\|$ or $2/\|w\|$?
Q_ZH: SVM 的间隔是 $1/\|w\|$ 还是 $2/\|w\|$？
A_EN: Under the normalization $f(x)=\pm1$ on the supporting planes, each supporting plane is $1/\|w\|$ from the decision plane $f(x)=0$. The full width between the two supporting planes is $2/\|w\|$. Both conventions appear in explanations. State whether you mean the one-sided distance or the full margin width before comparing formulas.
A_ZH: 将两侧支撑平面归一化为 $f(x)=\pm1$ 时，每侧到决策面 $f(x)=0$ 的距离为 $1/\|w\|$，两支撑平面之间的完整宽度为 $2/\|w\|$。解释中两种约定都可能出现，比较公式前应说明指单侧距离还是整个间隔宽度。

@@ M147 | 13-svm | learn | L3B:37-41;SVM:2-3
Q_EN: How do I choose the sign of a Lagrange multiplier term for an inequality?
Q_ZH: 不等式约束的拉格朗日乘子项应选什么符号？
A_EN: For minimization with $g(x)\ge0$, use $L(x,\lambda)=f(x)-\lambda g(x)$ and $\lambda\ge0$. If the same constraint is written as $h(x)=-g(x)\le0$, use $f(x)+\lambda h(x)$. The two expressions agree. In SVM, $g_i=y_i(w^Tx_i+b)-1$, so its term is $-\alpha_i g_i$.
A_ZH: 最小化问题若写作 $g(x)\ge0$，则用 $L(x,\lambda)=f(x)-\lambda g(x)$、$\lambda\ge0$。同一约束若写成 $h(x)=-g(x)\le0$，则用 $f(x)+\lambda h(x)$，二者一致。SVM 中 $g_i=y_i(w^Tx_i+b)-1$，所以对应项是 $-\alpha_i g_i$。

@@ M148 | 13-svm | learn | L3B:41-43;SVM:3
Q_EN: What do stationarity with respect to $w$ and $b$ give in the SVM derivation?
Q_ZH: SVM 推导中，对 $w$ 和 $b$ 的驻点条件给出什么？
A_EN: From $L=\frac12\|w\|^2-\sum_i\alpha_i[y_i(w^Tx_i+b)-1]$, setting $\nabla_wL=0$ gives $w=\sum_i\alpha_i y_i x_i$. Setting $\partial L/\partial b=0$ gives $\sum_i\alpha_i y_i=0$. The first expresses the classifier through training points; the second becomes a constraint in the dual problem.
A_ZH: 由 $L=\frac12\|w\|^2-\sum_i\alpha_i[y_i(w^Tx_i+b)-1]$，令 $\nabla_wL=0$ 得 $w=\sum_i\alpha_i y_i x_i$；令 $\partial L/\partial b=0$ 得 $\sum_i\alpha_i y_i=0$。前者用训练点表示分类器，后者成为对偶问题的约束。

@@ M149 | 13-svm | learn | L3B:42-43;SVM:3
Q_EN: State the hard-margin SVM dual and explain what its variables represent.
Q_ZH: 写出硬间隔 SVM 对偶问题，并解释变量含义。
A_EN: Maximize $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j$, subject to $\alpha_i\ge0$ and $\sum_i\alpha_i y_i=0$. There is one multiplier per training example. Training samples enter through inner products, which will enable kernels. This version is hard-margin; the soft-margin dual additionally requires $\alpha_i\le C$.
A_ZH: 最大化 $\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j$，约束为 $\alpha_i\ge0$、$\sum_i\alpha_i y_i=0$。每个训练样本对应一个乘子。样本通过内积进入目标，这为核方法提供了基础。本式是硬间隔形式，软间隔对偶还要求 $\alpha_i\le C$。

@@ M150 | 13-svm | learn | L3B:37-41;SVM:2-4
Q_EN: What are the KKT conditions for differentiable minimization with constraints $g_i(x)\ge0$?
Q_ZH: 对约束 $g_i(x)\ge0$ 的可微最小化问题，KKT 条件包括什么？
A_EN: They include primal feasibility $g_i(x)\ge0$, dual feasibility $\lambda_i\ge0$, stationarity $\nabla f(x)-\sum_i\lambda_i\nabla g_i(x)=0$, and complementary slackness $\lambda_i g_i(x)=0$. They are necessary under appropriate constraint qualifications; for a convex problem they also provide sufficiency. Do not replace complementary slackness by demanding every $g_i(x)=0$.
A_ZH: 包括原始可行性 $g_i(x)\ge0$、对偶可行性 $\lambda_i\ge0$、驻点条件 $\nabla f(x)-\sum_i\lambda_i\nabla g_i(x)=0$，以及互补松弛 $\lambda_i g_i(x)=0$。满足适当约束资格时它们是必要条件，凸问题中还可给出充分性。不能把互补松弛替换成要求所有 $g_i(x)=0$。

@@ M151 | 13-svm | check | L3B:38,41,44;SVM:2,4
Q_EN: Does a zero multiplier prove that a constraint is strictly inactive?
Q_ZH: 乘子等于零，能否证明约束严格不活跃？
A_EN: No. Under the lecture convention $g_i(x)\ge0$ with nonnegative multipliers, complementary slackness implies $g_i>0\Rightarrow\lambda_i=0$ and $\lambda_i>0\Rightarrow g_i=0$, but the converse implications need not hold. For $\min x^2$ subject to $x\ge0$, the optimum is $x=0$ with multiplier 0: the constraint is active despite a zero multiplier. This clarifies the lecture's simplified active/inactive descriptions.
A_ZH: 不能。按课件的 $g_i(x)\ge0$ 和非负乘子约定，互补松弛可推出 $g_i>0\Rightarrow\lambda_i=0$、$\lambda_i>0\Rightarrow g_i=0$，但反向不一定成立。最小化 $x^2$、约束 $x\ge0$ 时，最优为 $x=0$，乘子也为 0，但约束仍是活跃的。这补清了课件中活跃/不活跃描述的简写。

@@ M152 | 13-svm | check | L3B:39-40;SVM:2;CVX:5.2.3
Q_EN: What is the distinction between weak and strong duality?
Q_ZH: 弱对偶和强对偶有什么区别？
A_EN: For a minimization primal, the dual optimum is a lower bound: $d^*\le p^*$. Strong duality means equality. Convexity alone is not a universal sufficient condition; a constraint qualification such as Slater's condition is a standard sufficient addition. Separable hard-margin SVM and finite-data soft-margin SVM admit strictly feasible choices, supporting the usual primal–dual equivalence.
A_ZH: 对最小化原问题，对偶最优值提供下界：$d^*\le p^*$；强对偶表示二者相等。仅有凸性并非普遍充分条件，通常还用 Slater 等约束资格。线性可分的硬间隔 SVM 和有限数据的软间隔 SVM 可构造严格可行点，因而具有常用的原始—对偶等价性。

@@ M153 | 13-svm | learn | L3B:41-45;SVM:3-4
Q_EN: How do support vectors determine prediction and the bias term?
Q_ZH: 支持向量怎样决定预测和偏置？
A_EN: Since $w=\sum_i\alpha_i y_i x_i$, points with $\alpha_i=0$ contribute nothing to that representation. For a hard-margin support vector, $y_i(w^Tx_i+b)=1$, so $b=y_i-w^Tx_i$. For a soft-margin SVM, use a free support vector with $0<\alpha_i<C$ for that equality. Averaging consistent bias estimates can reduce numerical noise.
A_ZH: 因为 $w=\sum_i\alpha_i y_i x_i$，$\alpha_i=0$ 的点在此表示中没有贡献。硬间隔支持向量满足 $y_i(w^Tx_i+b)=1$，故 $b=y_i-w^Tx_i$。软间隔时，应选 $0<\alpha_i<C$ 的自由支持向量使用该等式。对一致的偏置估计取平均可减少数值噪声。

@@ M154 | 13-svm | learn | L3B:49-54;SVM:3
Q_EN: How does the soft-margin SVM handle data that cannot be perfectly separated?
Q_ZH: 软间隔 SVM 怎样处理不能完全分开的数据？
A_EN: Introduce slack variables $\xi_i\ge0$ and minimize $\frac12\|w\|^2+C\sum_i\xi_i$, subject to $y_i(w^Tx_i+b)\ge1-\xi_i$. The weight term favors a wider margin, while slack penalties discourage violations. $C>0$ controls their tradeoff. Soft margin permits some violations; it does not guarantee every training label can or should be classified correctly.
A_ZH: 引入 $\xi_i\ge0$，最小化 $\frac12\|w\|^2+C\sum_i\xi_i$，约束为 $y_i(w^Tx_i+b)\ge1-\xi_i$。权重项偏好更宽间隔，松弛惩罚抑制违反约束，$C>0$ 控制权衡。软间隔允许部分违反，不保证所有训练标签都能或都应该被正确分类。
MEDIA: Lecture3b-cell-52-output-1.png

@@ M155 | 13-svm | learn | L3B:50-54
Q_EN: How do I interpret slack values 0, between 0 and 1, and greater than 1?
Q_ZH: 如何理解松弛量为 0、介于 0 与 1、以及大于 1 的情况？
A_EN: At an optimum with $C>0$, minimal slack is $\xi_i=\max(0,1-y_if(x_i))$. Zero slack means on or beyond the correct margin. $0<\xi_i<1$ means inside the margin but correctly classified. $\xi_i=1$ places the point on the decision boundary; $\xi_i>1$ means misclassification. Thus a margin violation is not always a classification error.
A_ZH: $C>0$ 的最优解处，最小松弛量为 $\xi_i=\max(0,1-y_if(x_i))$。零表示位于正确间隔边缘或外侧；$0<\xi_i<1$ 表示在间隔内但类别仍正确；$\xi_i=1$ 表示在决策面上；$\xi_i>1$ 才表示错分。因此违反间隔不一定就是分类错误。

@@ M156 | 13-svm | learn | L3B:54,58;SVM:3
Q_EN: How is the slack-variable objective related to hinge loss, and where does the factor 1/2 go?
Q_ZH: 松弛变量目标怎样对应 hinge loss？其中的 1/2 因子去了哪里？
A_EN: Eliminating minimal slacks gives $\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))$. Dividing by $C$ gives $\|w\|^2/(2C)+\sum_i\mathrm{hinge}_i$. The notebook later writes $1/C$ instead of $1/(2C)$: that can describe the same family after redefining $C$, but is not algebraically identical at the same numerical $C$. State your objective convention.
A_ZH: 消去最小松弛量得到 $\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))$；除以 $C$ 后为 $\|w\|^2/(2C)+\sum_i\mathrm{hinge}_i$。Notebook 后面写成 $1/C$ 而非 $1/(2C)$，可通过重定义 $C$ 表示同一家族，但在相同数值 $C$ 下不严格等价。应说明所用目标约定。

@@ M157 | 13-svm | learn | L3B:54;SVM:3
Q_EN: Why does the soft-margin dual constrain $0\le\alpha_i\le C$?
Q_ZH: 为什么软间隔对偶要求 $0\le\alpha_i\le C$？
A_EN: Add a multiplier $\beta_i\ge0$ for $\xi_i\ge0$. Stationarity in $\xi_i$ gives $C-\alpha_i-\beta_i=0$. Since both multipliers are nonnegative, $\alpha_i\le C$. The dual has the same quadratic objective as hard-margin SVM, together with this box constraint and $\sum_i\alpha_i y_i=0$. Omitting the upper bound changes the soft-margin problem.
A_ZH: 为 $\xi_i\ge0$ 加乘子 $\beta_i\ge0$。对 $\xi_i$ 的驻点条件给出 $C-\alpha_i-\beta_i=0$。两个乘子均非负，因此 $\alpha_i\le C$。对偶目标与硬间隔的二次目标相同，但多了箱约束，并仍满足 $\sum_i\alpha_i y_i=0$。漏掉上界就改变了软间隔问题。

@@ M158 | 13-svm | check | SVM:3-4;L3B:44,54
Q_EN: What do $\alpha_i=0$, $0<\alpha_i<C$ and $\alpha_i=C$ imply at a soft-margin optimum?
Q_ZH: 在软间隔最优解处，$\alpha_i=0$、$0<\alpha_i<C$ 和 $\alpha_i=C$ 分别意味着什么？
A_EN: With $C>0$, $\alpha_i=0$ implies zero slack and $y_if(x_i)\ge1$. A free multiplier $0<\alpha_i<C$ implies zero slack and $y_if(x_i)=1$. At $\alpha_i=C$, the point satisfies $y_if(x_i)=1-\xi_i\le1$; it may be on the margin, inside it or misclassified. Do not turn these non-strict inequalities into strict ones without extra assumptions.
A_ZH: $C>0$ 时，$\alpha_i=0$ 意味着零松弛且 $y_if(x_i)\ge1$；$0<\alpha_i<C$ 意味着零松弛且 $y_if(x_i)=1$。$\alpha_i=C$ 时满足 $y_if(x_i)=1-\xi_i\le1$，可能在间隔边缘、间隔内或被错分。没有额外假设时，不能把这些非严格不等式改成严格不等式。

@@ M159 | 13-svm | learn | L3B:54-58;SVM:3
Q_EN: How does changing $C$ affect soft-margin SVM, and does it eliminate sensitivity to outliers?
Q_ZH: 改变 $C$ 怎样影响软间隔 SVM？能否消除异常点影响？
A_EN: A larger $C$ penalizes violations more relative to weight norm; a smaller $C$ permits more violations in exchange for a simpler/wider-margin fit. The dual upper bound caps each multiplier, but does not make arbitrary outliers harmless: feature magnitude and geometry still matter. Compare generalization across validated settings instead of assuming the largest $C$ gives the best classifier.
A_ZH: 大 $C$ 相对权重范数更重罚违反间隔；小 $C$ 更愿意允许违反，换取较简单、较宽间隔的拟合。对偶上界限制每个乘子，但不让任意异常点变得无害，特征大小和几何位置仍有影响。应验证泛化表现，而不是默认最大 $C$ 最好。
MEDIA: Lecture3b-cell-57-output-1.png

@@ M160 | 13-svm | worked | L3B:36,42-43
Q_EN: Solve the one-dimensional hard-margin problem for $(x,y)=(-1,-1)$ and $(1,+1)$.
Q_ZH: 对一维样本 $(x,y)=(-1,-1)$、$(1,+1)$，求硬间隔 SVM。
A_EN: The constraints are $w-b\ge1$ and $w+b\ge1$, implying $w\ge1+|b|$. Minimum norm occurs at $w=1,b=0$. The one-sided margin is 1 and objective is 0.5. In the dual, $\alpha_1=\alpha_2=0.5$ gives $w=\sum_i\alpha_i y_i x_i=1$ and dual objective 0.5, matching the primal.
A_ZH: 约束为 $w-b\ge1$、$w+b\ge1$，因此 $w\ge1+|b|$。最小范数解为 $w=1,b=0$，单侧间隔为 1，目标值为 0.5。对偶中取 $\alpha_1=\alpha_2=0.5$，得到 $w=\sum_i\alpha_i y_i x_i=1$，对偶值也为 0.5，与原问题相同。

@@ M161 | 13-svm | check | L3B:58-60;L3C:44-46
Q_EN: How do logistic loss and hinge loss treat a correctly classified point with signed score $z=2$?
Q_ZH: 带标签分数 $z=2$ 的正确分类点，在逻辑损失与 hinge loss 下分别怎样计分？
A_EN: Hinge loss is $\max(0,1-2)=0$, because the point is beyond the unit margin. Logistic loss is $\log(1+e^{-2})\approx0.1269$, still positive and decreasing as confidence grows. Thus logistic loss keeps rewarding larger positive scores, while hinge loss becomes flat once the margin is satisfied. Both still interact with the regularizer.
A_ZH: Hinge loss 为 $\max(0,1-2)=0$，因为该点已超过单位间隔；逻辑损失为 $\log(1+e^{-2})\approx0.1269$，仍为正且会随置信增大继续下降。因此逻辑损失还奖励更大正分数，hinge 在满足间隔后变平。两者仍都受正则项影响。
MEDIA: Lecture3c-cell-46.png

@@ M162 | 13-svm | learn | L3B:76-77
Q_EN: How many binary models do one-vs-one and one-vs-rest need for $K$ classes?
Q_ZH: $K$ 类任务中，one-vs-one 和 one-vs-rest 各需要多少二分类器？
A_EN: One-vs-one uses one model for every class pair, so it needs $K(K-1)/2$ models. One-vs-rest uses $K$. For six classes, these are 15 and 6. Training cost also depends on how many samples each model sees, so model count alone is not a complete runtime comparison. The lecture's SVC example uses pairwise training.
A_ZH: One-vs-one 对每对类别训练一个模型，共 $K(K-1)/2$ 个；one-vs-rest 需要 $K$ 个。六类时分别为 15 与 6。训练成本还取决于各模型处理的样本量，不能只凭模型数量判断总耗时。课堂 SVC 示例使用两两分类训练。

@@ M163 | 13-svm | classroom | L3B:68-77
Q_EN: What does `estimator__C` mean in GridSearchCV around OneVsRestClassifier?
Q_ZH: 对 OneVsRestClassifier 使用 GridSearchCV 时，`estimator__C` 是什么意思？
A_EN: The wrapper's `estimator` is the underlying binary classifier, and `C` is that classifier's parameter. Double underscores traverse nested estimators. For a pipeline step called `svc`, the analogous name is `svc__C`. Parameter names must match the actual nesting; searching a nonexistent top-level `C` will not tune the intended inner classifier.
A_ZH: 包装器的 `estimator` 是内部二分类器，`C` 是该分类器参数，双下划线表示进入嵌套对象。如果 Pipeline 的步骤名为 `svc`，相应参数名是 `svc__C`。名称必须匹配实际嵌套关系，在不存在的顶层 `C` 上搜索不能调整目标内部模型。
MEDIA: Lecture3-nestedclassifier.png

@@ M164 | 13-svm | check | L3B:45,124;L3C:43
Q_EN: Is an SVM decision score of 2 a probability of class +1?
Q_ZH: SVM 决策分数为 2，是否就是正类概率？
A_EN: No. The decision function is used for ranking and sign-based classification and can take values outside [0,1]. In a linear model, division by $\|w\|$ converts its signed score to signed geometric distance. Probability estimates require an additional probability-modeling or calibration procedure. A wider margin does not by itself establish calibrated confidence.
A_ZH: 不是。决策函数用于排序和按符号分类，可以超出 [0,1]。在线性模型中，分数除以 $\|w\|$ 才得到带符号的几何距离。概率估计需要额外的概率建模或校准过程，更宽间隔本身不能证明置信概率已经校准。

@@ M165 | 14-kernels | learn | L3B:83-93
Q_EN: How can a linear classifier in a transformed space produce a nonlinear boundary in the original space?
Q_ZH: 变换空间中的线性分类器，怎样产生原空间中的非线性边界？
A_EN: Transform $x$ into features $\phi(x)$ and learn $f(x)=w^T\phi(x)+b$. The function is linear in the transformed features but can be nonlinear in the original coordinates. For example, using $\phi(x_1,x_2)=(x_1^2,x_2^2)$ allows a circular boundary. Increasing dimension does not universally guarantee separability, especially when identical inputs have conflicting labels.
A_ZH: 将 $x$ 变成 $\phi(x)$，再学习 $f(x)=w^T\phi(x)+b$。它对变换后特征线性，对原坐标却可非线性。例如采用 $\phi(x_1,x_2)=(x_1^2,x_2^2)$，就能得到圆形边界。增加维度并不普遍保证可分，特别是相同输入带有冲突标签时。
MEDIA: Lecture3b-cell-88.png

@@ M166 | 14-kernels | learn | L3B:89-94
Q_EN: What is the kernel trick?
Q_ZH: 什么是核技巧？
A_EN: A kernel computes $k(x,z)=\phi(x)^T\phi(z)$ without explicitly constructing the transformed vectors. Since the SVM dual uses inner products, replace $x_i^Tx_j$ by $k(x_i,x_j)$. Prediction becomes $\operatorname{sign}(\sum_i\alpha_i y_i k(x_i,x)+b)$. The trick changes the feature geometry while retaining the dual optimization structure and its constraints.
A_ZH: 核函数直接计算 $k(x,z)=\phi(x)^T\phi(z)$，不必显式构造变换向量。SVM 对偶只使用内积，因此把 $x_i^Tx_j$ 替换为 $k(x_i,x_j)$。预测为 $\operatorname{sign}(\sum_i\alpha_i y_i k(x_i,x)+b)$。核技巧改变特征几何，同时保留对偶优化结构及约束。

@@ M167 | 14-kernels | worked | L3B:90-92
Q_EN: Give an explicit feature map for the two-dimensional quadratic kernel $k(x,z)=(x^Tz)^2$.
Q_ZH: 对二维二次核 $k(x,z)=(x^Tz)^2$，给出显式特征映射。
A_EN: Use $\phi(x)=(x_1^2,\sqrt2 x_1x_2,x_2^2)$. Its inner product with $\phi(z)$ is $x_1^2z_1^2+2x_1x_2z_1z_2+x_2^2z_2^2=(x^Tz)^2$. The $\sqrt2$ factor accounts for the two cross terms. The notebook alternatively keeps both ordered cross products, which is a redundant but valid feature representation.
A_ZH: 可用 $\phi(x)=(x_1^2,\sqrt2 x_1x_2,x_2^2)$。与 $\phi(z)$ 的内积为 $x_1^2z_1^2+2x_1x_2z_1z_2+x_2^2z_2^2=(x^Tz)^2$。$\sqrt2$ 对应两个交叉项。Notebook 保留两个有序交叉乘积，是冗余但有效的另一种表示。

@@ M168 | 14-kernels | learn | L3B:101-112
Q_EN: How does $\gamma$ affect the RBF kernel $e^{-\gamma\|x-z\|^2}$?
Q_ZH: $\gamma$ 怎样影响 RBF 核 $e^{-\gamma\|x-z\|^2}$？
A_EN: Small $\gamma$ makes similarity decay slowly with distance, yielding broad influence. Large $\gamma$ makes influence very local and can create more irregular boundaries. In the Gaussian-width convention, $\gamma=1/(2\sigma^2)$. Thus larger $\gamma$ corresponds to a narrower kernel. Feature scaling changes distances and therefore changes the effective meaning of a fixed $\gamma$.
A_ZH: 小 $\gamma$ 让相似度随距离缓慢下降，影响范围宽；大 $\gamma$ 让影响很局部，可能形成更曲折的边界。按高斯宽度约定，$\gamma=1/(2\sigma^2)$，因此大 $\gamma$ 对应窄核。特征缩放改变距离，也会改变固定 $\gamma$ 的实际含义。
MEDIA: Lecture3b-cell-103.png

@@ M169 | 14-kernels | worked | L3B:101-104
Q_EN: Two points have squared distance 4. Compare RBF similarity for $\gamma=0.25$ and $\gamma=1$.
Q_ZH: 两点平方距离为 4，比较 $\gamma=0.25$ 与 $\gamma=1$ 时的 RBF 相似度。
A_EN: Similarities are $e^{-1}\approx0.3679$ and $e^{-4}\approx0.0183$. With larger $\gamma$, the same separation looks much less similar. Both values are pairwise kernel similarities, not class probabilities. If the feature units change, recompute distances or scale features before interpreting these numbers.
A_ZH: 相似度分别为 $e^{-1}\approx0.3679$ 和 $e^{-4}\approx0.0183$。较大 $\gamma$ 下，同样的距离显得不相似得多。这些是两点之间的核相似度，不是类别概率。特征单位改变后，应重新计算距离或先缩放特征，再解释数值。

@@ M170 | 14-kernels | classroom | L3B:113-118
Q_EN: Why should RBF-SVM tune both $C$ and $\gamma$?
Q_ZH: 为什么 RBF-SVM 要同时选择 $C$ 和 $\gamma$？
A_EN: $C$ controls how strongly training violations are penalized, while $\gamma$ controls the locality of the feature-space similarity. Their effects interact: one fixed value may make the other appear ineffective. Search a justified range for both using training-set cross-validation, with preprocessing fitted inside folds. Keep the final test set outside the search and report the selection protocol.
A_ZH: $C$ 控制训练违反间隔的惩罚，$\gamma$ 控制特征相似度的局部性。两者会交互，一个设置不合适可能掩盖另一个的作用。应在训练集内部交叉验证搜索两者的合理范围，预处理也在折内拟合。最终测试集不参与搜索，并记录选参过程。

@@ M171 | 14-kernels | learn | L3B:118-119
Q_EN: What condition must a real symmetric function satisfy to be a valid kernel for standard kernel SVM?
Q_ZH: 实对称函数满足什么条件，才能作为标准核 SVM 的有效核？
A_EN: For every finite set of inputs, its Gram matrix $K_{ij}=k(x_i,x_j)$ must be positive semidefinite: $v^TKv\ge0$ for all real $v$. Strict positive definiteness is not required. Checking one dataset numerically can catch a counterexample but cannot prove validity for every possible dataset. A verified inner-product feature construction is one way to establish validity.
A_ZH: 对任意有限输入集合，Gram 矩阵 $K_{ij}=k(x_i,x_j)$ 都须半正定，即对所有实向量 $v$ 有 $v^TKv\ge0$，不要求严格正定。只在一个数据集上数值检查能找反例，却不能证明对所有数据集都成立。明确构造内积特征映射，是证明有效的一种方法。

@@ M172 | 14-kernels | check | L3B:89-94,118-124
Q_EN: Does the kernel trick make training cheap for arbitrarily many samples?
Q_ZH: 核技巧是否能让任意大样本量的训练都很便宜？
A_EN: No. It can avoid a very large explicit feature map, but a dense Gram matrix for $N$ samples has $N^2$ entries. Prediction also depends on kernel evaluations with support vectors. An efficient pairwise kernel does not remove every time or memory bottleneck. Distinguish input dimension, transformed dimension, sample count and support-vector count when discussing cost.
A_ZH: 不能。它可以避免巨大显式特征映射，但 $N$ 个样本的稠密 Gram 矩阵有 $N^2$ 个元素；预测还需要与支持向量计算核。单次核计算高效，不意味着所有时间和内存瓶颈都消失。讨论成本时应区分输入维度、变换维度、样本数和支持向量数。

@@ M173 | 15-features | learn | L3C:7-11
Q_EN: How does standardization work, and which data determine its statistics?
Q_ZH: 标准化怎样进行？统计量应由哪些数据确定？
A_EN: For each feature, compute training mean $m$ and standard deviation $s$, then transform as $(x-m)/s$. Apply the same training statistics to validation and test data. The training feature is centered and rescaled; the test feature need not have exactly zero mean or unit variance. Constant features need explicit handling rather than division by zero.
A_ZH: 对每个特征计算训练均值 $m$ 和标准差 $s$，再做 $(x-m)/s$，验证和测试使用同一组训练统计量。训练特征因此中心化并缩放，但测试特征不一定恰好均值零、方差一。常量特征应明确处理，不能除以零。
MEDIA: Lecture3c-cell-11.png

@@ M174 | 15-features | worked | L3C:12-15
Q_EN: Map $x=4$ to [-1,1] using training minimum 2 and maximum 6. What happens to a new value 8?
Q_ZH: 用训练最小值 2、最大值 6 将 $x=4$ 映射到 [-1,1]，新值 8 会怎样？
A_EN: Use $\tilde x=2(x-2)/(6-2)-1$. The value 4 maps to 0, while 8 maps to 2. Without an explicit clipping rule, new values outside the training range can map outside [-1,1]. Do not refit the extrema on the test set merely to force its values into the displayed range.
A_ZH: 使用 $\tilde x=2(x-2)/(6-2)-1$，4 映射为 0，8 映射为 2。没有明确裁剪规则时，超出训练范围的新值可映射到 [-1,1] 之外。不能为了把测试值塞进该区间，就在测试集重新拟合极值。

@@ M175 | 15-features | learn | L3C:16-19
Q_EN: Why can integer codes be misleading for unordered categories, and what does one-hot encoding fix?
Q_ZH: 为什么无序类别直接编码成整数可能误导模型？One-hot 改善什么？
A_EN: Encoding cat/dog/horse as 0/1/2 creates numerical order and distances without a justified meaning. One-hot encoding gives each category its own indicator, avoiding that invented ordering. The encoding still needs a fixed category-to-column mapping and a policy for unseen categories. It does not automatically capture semantic similarity between categories.
A_ZH: 把猫/狗/马编码为 0/1/2，会引入未经论证的数值顺序和距离。One-hot 为每个类别设置独立指示列，避免虚构顺序。但仍须固定类别到列的映射，并规定如何处理未见类别。它也不会自动表达类别间的语义相似性。

@@ M176 | 15-features | learn | L3C:20-21
Q_EN: What does binning a continuous feature do, and what information can it lose?
Q_ZH: 对连续特征分箱会做什么？可能损失哪些信息？
A_EN: Choose interval boundaries, assign each value to a bin, and optionally one-hot encode the bin index. This can represent different behavior in different ranges. It discards within-bin differences and creates abrupt boundaries: two nearby values across a boundary may get different indicators. Specify which endpoint belongs to each bin and choose boundaries without using held-out outcomes.
A_ZH: 先定义区间边界，把值归入箱，再可对箱编号做 one-hot。这能表示不同数值区间的不同作用，但会丢失箱内差异并产生突变边界，相邻却跨界的两个值可能获得不同指示。须明确端点归属，选边界时不能利用留出目标信息。

@@ M177 | 15-features | worked | L3C:22-23
Q_EN: What second-degree polynomial features are produced from $(x_1,x_2)=(2,3)$ when including bias and lower degrees?
Q_ZH: 对 $(x_1,x_2)=(2,3)$，包含常数与低次项的二阶多项式特征是什么？
A_EN: In the order $(1,x_1,x_2,x_1^2,x_1x_2,x_2^2)$, the vector is $(1,2,3,4,6,9)$. The cross term captures an interaction between features. A model linear in these six features can be nonlinear in the original two coordinates. More features increase flexibility and can increase overfitting or numerical-scale problems.
A_ZH: 按 $(1,x_1,x_2,x_1^2,x_1x_2,x_2^2)$ 排列，得到 $(1,2,3,4,6,9)$。交叉项表示特征交互。模型对六个新特征线性，却可对原始两坐标非线性。特征增多提高灵活性，也可能增加过拟合与数值尺度问题。

@@ M178 | 15-features | learn | L3C:24
Q_EN: When can a log transform help, and what domain checks are necessary?
Q_ZH: 对数变换何时有用？需要检查什么定义域条件？
A_EN: A log transform compresses large positive ranges and turns multiplicative ratios into additive differences. Ordinary $\log x$ requires $x>0$. A justified `log1p(x)` transform can handle nonnegative values including zero, but it defines a different mapping. Do not apply a log blindly to negative, missing or arbitrarily shifted measurements.
A_ZH: 对数变换压缩很大的正值范围，并把乘法比例转成加法差异。普通 $\log x$ 要求 $x>0$；合理采用 `log1p(x)` 可处理包含零的非负值，但这是另一种映射。不能不检查就对负值、缺失值或随意平移的测量取对数。

@@ M179 | 15-features | learn | L3C:25-34
Q_EN: How does balanced class weighting change a classifier's training objective?
Q_ZH: 平衡类别权重怎样改变分类器的训练目标？
A_EN: Give class $c$ a weight inversely related to its training frequency, commonly $a_c=N/(K N_c)$. Each example's loss is multiplied by its class weight, increasing minority examples' relative contribution. This changes training incentives without duplicating every minority sample. It does not guarantee better balanced accuracy or preserve the interpretation of unweighted population probabilities.
A_ZH: 按类别训练频率的倒数分配权重，常用 $a_c=N/(K N_c)$。每个样本损失乘所属类权重，提高少数类的相对贡献。它通过改变训练目标起作用，不必复制每个少数类样本。但不保证平衡准确率一定提高，也不自动保持未加权总体概率的解释。
MEDIA: Lecture3c-cell-34.png

@@ M180 | 15-features | worked | L3C:31-34
Q_EN: For 200 class-0 and 20 class-1 examples, what are balanced weights $N/(K N_c)$?
Q_ZH: 类 0 有 200 个、类 1 有 20 个样本，平衡权重 $N/(K N_c)$ 是多少？
A_EN: Total $N=220$ and $K=2$, so weights are $220/(2\times200)=0.55$ and $220/(2\times20)=5.5$. Each minority example receives ten times the weight of a majority example. Total class weights are equal: $200(0.55)=20(5.5)=110$. The calculation uses training frequencies, not held-out label counts.
A_ZH: $N=220$、$K=2$，所以权重为 $220/(2\times200)=0.55$ 与 $220/(2\times20)=5.5$。每个少数类样本的权重是多数类的十倍，两类总权重相等：$200(0.55)=20(5.5)=110$。应使用训练频率，而非留出标签数量。

@@ M181 | 15-features | check | L3C:35-42
Q_EN: How does class imbalance differ from unequal error costs?
Q_ZH: 类别数量不平衡与错误代价不相等有什么区别？
A_EN: Imbalance concerns how many examples each class has. Unequal costs concern how harmful different errors are. A dataset can be balanced while false positives are far more costly, or imbalanced while costs are equal. The lecture's weights 0.2 and 5 assign a 25-fold relative loss weight; this does not mean one class occurs 25 times less often. Choose weights to match the intended goal.
A_ZH: 数量不平衡关注各类样本有多少，代价不等关注不同错误有多严重。数据可数量平衡但假阳性更昂贵，也可数量不平衡但错误代价相同。课堂的 0.2 与 5 表示损失权重相差 25 倍，不表示某类出现频率低 25 倍。权重应匹配实际目标。

@@ M182 | 15-features | learn | L3C:43-53
Q_EN: What common framework links logistic regression, SVM and regularized model selection?
Q_ZH: 什么共同框架联系逻辑回归、SVM 和正则化模型选择？
A_EN: Minimize a data-fit term plus a complexity penalty: $\sum_i L(y_i,f(x_i))+\lambda\Omega(f)$. Logistic and hinge losses reward different score behavior, while $\Omega$ limits complexity within a chosen model family. Choose the family, representation and hyperparameters using relevant validation evidence. “No free lunch” does not mean all methods perform equally on your actual task or that domain knowledge is useless.
A_ZH: 共同形式是最小化数据拟合项与复杂度惩罚：$\sum_i L(y_i,f(x_i))+\lambda\Omega(f)$。逻辑损失和 hinge loss 对分数行为的偏好不同，$\Omega$ 则限制所选模型家族的复杂度。应根据相关验证证据选择家族、表示与超参数。“没有免费午餐”不意味着所有方法在你的实际任务上同样好，也不意味着领域知识无用。
