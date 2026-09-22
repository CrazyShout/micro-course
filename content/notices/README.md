# 课程信息与学习指南 / Course information and study guidance

整理日期：2026-09-22。材料快照日期见各条目；不是教师新发布的公告。

## CS5489

### 9月22日内容更新与Markji位置 / September 22 content and Markji locations

新内容已整理进网页：41张原卡按新Canvas复用，原卡仍可在Markji按卡号查找。原卡文字已同步，Markji内的章节位置尚待更新。CS5489新增M338–M341目前可在网页预览，尚未入Markji；不必反复搜索不存在的卡。

New Canvas content reuses 41 existing cards, whose updated text is available in Markji under the same IDs. Their Markji chapter locations are still pending. New CS5489 cards M338–M341 can be previewed on the website but are not yet in Markji.

材料快照 / Material snapshot: 2026-09-22 · ID: CS5489-UPDATE-20260922

来源 / Source: micro-course · update 2026-09-22

### 课程范围、学习顺序与考核 / Scope, study sequence, and assessment

先学 Python/NumPy 和概率，再学贝叶斯分类与文本朴素贝叶斯，并用于 Assignment 1。当前介绍列出平时成绩 70%、期末 30%；期末考试与项目各自至少达到 30% 才能通过。幻灯片对项目所在周的描述不一致，截止时间以当前 Canvas 为准。正式章节卡覆盖 Lecture 1–4 和 Tutorial 1–3；Extra Resources 提前介绍后续历史主题，两者均不等于已确认的 QE 范围。

Learn Python/NumPy and probability, then Bayes classification and text naive Bayes, then apply them to Assignment 1. The current introduction lists 70% coursework and 30% final examination; the final and project each require at least 30% individually to pass. The slides disagree on the project week, so use current Canvas deadlines. The Canvas-aligned cards cover Lectures 1–4 and Tutorials 1–3; Extra Resources previews later historical topics. Neither defines a confirmed QE syllabus.

材料快照 / Material snapshot: 2026-09-22 · ID: CS5489-M005

来源 / Source: Lecture1 Intro.pdf · page 4-5,29

### Assignment 1：任务与标签约定 / Assignment 1: task and label mapping

预测三类短信标签：0 为正常，1 为垃圾，2 为短信钓鱼。Smishing 指通过短信实施的钓鱼，在本作业中单独作为一类。训练文件提供文本与标签，评估时使用给定的验证/测试 Usage 划分。预处理、建模、评估和导出的类别含义必须始终一致。

Predict one of three SMS labels: 0 = normal, 1 = spam, 2 = smishing. Smishing is phishing conducted through SMS; it is a separate target label here. The supplied training file contains message text and labels. Use the documented validation/test usage split for evaluation. Class meaning must remain consistent in preprocessing, modeling, evaluation and exported predictions.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M090

来源 / Source: Assignment1-Doc.ipynb · cell 2-5,10-12

### Assignment 1：提交文件清单 / Assignment 1: submission checklist

要求将带说明的 `Assignment1-Doc.ipynb`、导出的 PDF、最终预测 CSV，以及能重新生成 CSV 的 `Assignment1-Final.ipynb` 打包为一个 zip。须说明预处理、模型选择、超参数搜索与结果，并记录 ID/顺序、种子及依赖。Notebook 中的随机预测仅用于示范文件格式，不是训练好的答案。

The brief requests the documented `Assignment1-Doc.ipynb`, its exported PDF, the final prediction CSV, and `Assignment1-Final.ipynb` that regenerates the CSV, compressed into one zip. Explain preprocessing, model choices, hyperparameter search and results. Record IDs/order, seeds and dependencies. The notebook's random-prediction example demonstrates file format only; it is not a trained solution.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M097

来源 / Source: Assignment1-Doc.ipynb · cell 3,5-14
来源 / Source: Assignment1-Final.ipynb · cell 1-11

### Assignment 1：评分比例与准备 / Assignment 1: rubric and preparation

当前说明中，分类器与特征比较占 45%，课堂例子以外的特征或分类器占 30%，报告占 20%，最终排名占 5%；排名得分要求代码可复现。应保留带真实结果及解释的比较记录。作业是个人作业，此处为要求摘要，用于规划准备。

The current brief allocates 45% to classifier/feature comparisons, 30% to features or classifiers beyond the lecture examples, 20% to the report, and 5% to final ranking. Reproducible code is required for ranking credit. Keep a comparison log with honest results and explanations. The assignment is individual; this summary supports preparation and planning.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M100

来源 / Source: Assignment1-Doc.ipynb · cell 3

### Assignment 1：文件名与导入提醒 / Assignment 1: filenames and imports

说明文字提到 `smishing_test.txt`，实际加载代码及下载文件使用 `smishing_val_test.txt`。Final Notebook 使用 `pd.read_csv`，应确保运行副本里有 `import pandas as pd`。重启并运行全部单元可发现隐藏依赖。保留原始模板，在工作副本中修正。

The explanatory text mentions `smishing_test.txt`, while the actual loading code and downloaded file use `smishing_val_test.txt`. The final notebook uses `pd.read_csv`, so make sure `import pandas as pd` is present in the runnable copy. Restart and run all cells to detect hidden imports. Preserve the original starter files and make changes in a working copy.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M098

来源 / Source: Assignment1-Doc.ipynb · cell 3,5,10
来源 / Source: Assignment1-Final.ipynb · cell 1-11

### Tutorial 2：数据规模与标签映射 / Tutorial 2: dataset size and label mapping

提供的 `dataAG.json` 实际包含 2,000 篇训练文档和 1,000 篇测试文档，标签 0/1/2/3 分别为国际、体育、商业、科技。Notebook 文字中的 2,034 和 1,353 与本次文件不符，应先检查真实数据及标签映射，再构造特征矩阵。本教程使用普通分类准确率。

The supplied `dataAG.json` contains 2,000 training and 1,000 test documents, with labels 0 = World, 1 = Sports, 2 = Business, 3 = Sci/Tech. The notebook's prose says 2,034 and 1,353, but those counts do not match this downloaded file. Inspect the actual data and label mapping before constructing feature matrices. This tutorial uses ordinary classification accuracy.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M107

来源 / Source: Tutorial2v2.ipynb · cell 2-11

### 逻辑回归 Notebook：multi_class 参数兼容提醒 / Logistic regression notebook: multi_class compatibility

课程 Notebook 使用 `multi_class='multinomial'`。截至 2026-09-15 核对的 LogisticRegression 文档中，这个参数已不再列出；运行时应以所安装版本的文档为准。三类及以上时选择支持多项式损失的求解器；若目标是 OvR，则显式使用 OneVsRestClassifier。记录依赖版本，在工作副本中适配，保留原始 Notebook。

The course notebook uses `multi_class='multinomial'`. The LogisticRegression documentation checked on 2026-09-15 no longer listed this parameter; follow the documentation for the installed version. For three or more classes, choose a solver supporting multinomial loss; use an explicit OneVsRestClassifier when OvR is intended. Record dependencies and adapt a working copy while preserving the original notebook.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M142

来源 / Source: Lecture3a.ipynb · cell 92
来源 / Source: sklearn.linear_model.LogisticRegression.html · section parameters

### Tutorial 2：模板中的 alpha 未给出数学定义 / Tutorial 2: alpha has no specified formula

当前 PoissonNB 模板包含 alpha 参数，但没有规定它对应的平滑公式。实现时应明确写出采用的参数化和取值，不把自己的补充方案当作教师已给定的公式。平滑的数学含义见 M115 及对应微课。

The supplied PoissonNB template includes alpha without defining its smoothing formula. Document the chosen parameterization and values instead of presenting an added convention as an instructor-specified formula. Card M115 and its lesson explain the mathematical concept.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-TUTORIAL2-ALPHA

来源 / Source: Tutorial2v2.ipynb · cell 31-32

### 微课与记忆卡的使用方法 / Using lessons and flashcards

第一次按模块顺序阅读并展开答案；第二次遮住答案，用英语口述，理解卡住时再看中文。计算与编程卡先在纸上解或亲手写代码，再翻答案。最后改一个数值或假设重新做。这是为学习增加的方法建议，不是官方考核规定。

First read a module in order with answers visible. Then hide the answer and explain it aloud in English, using Chinese only to repair understanding. For calculation and coding cards, work on paper or type the code before revealing the answer. Finally change a number or assumption and solve again. This is a study strategy added for these cards, not an official assessment rule.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5489-M006

来源 / Source: Lecture1 Intro.pdf · page 23-28

## CS5222

### 9月22日内容更新与Markji位置 / September 22 content and Markji locations

Chapter2后续、Tutorial3与Assignment1已整理进网页。N135–N148、N231–N233、N260–N263已复用原卡并同步出处；Markji内目前仍在Extra Resources，可按原卡号找到，章节位置尚待更新。网络本轮没有增加新卡。

Later Chapter 2, Tutorial 3 and Assignment 1 are available here. Cards N135–N148, N231–N233 and N260–N263 reuse their original IDs and updated sources. They remain under Extra Resources in Markji while chapter moves are pending. No networking cards were added.

材料快照 / Material snapshot: 2026-09-22 · ID: CS5222-UPDATE-20260922

来源 / Source: micro-course · update 2026-09-22

### Chapter 2：已下载课件的覆盖范围 / Chapter 2: downloaded material coverage

现已下载 Chapter 2 全文107张和 Part 3 的42张，补齐 DNS 报文、P2P/BitTorrent、视频/CDN 及 UDP/TCP socket。Part 1、2、3 独立编号，引用必须注明具体文件。旧 Python 2 代码需按 Python 3 的输入、bytes 编解码及 TCP 消息边界处理；原件保留。

The 107-slide full Chapter 2 and 42-slide part 3 are now available, covering DNS messages, P2P/BitTorrent, video/CDNs and UDP/TCP sockets. Parts have separate numbering, so name the file with each citation. Qualify old Python 2 code for Python 3 input, bytes and TCP message framing; originals are preserved.

材料快照 / Material snapshot: 2026-09-22 · ID: CS5222-N070

来源 / Source: cs5222_cha2_2026_student_part1.pptx · slide 19-22
来源 / Source: cs5222_cha2_2026_student_part2.pptx · slide 1-43
来源 / Source: cs5222_cha2_2026_student.pptx · slide 1-107
来源 / Source: cs5222_cha2_2026_student_part3.pptx · slide 1-42

### 考核结构与资料范围 / Assessment structure and material scope

课程概览规定平时成绩 30%、期末 70%，通过要求包括期末考试至少达到满分的 30%。平时任务含习题/论文作业、Wireshark 和研究报告。正式章节卡对应 Chapter 1、Chapter 2 全文、Tutorial 1–3 与 Assignment 1；Extra Resources 单独预习后续历史主题和题目。此卡库不等于完整本学期课程，也不定义已确认的 QE 范围。

The overview assigns 30% to coursework and 70% to the final exam; passing requires at least 30% of the examination's maximum mark. Coursework includes problem/paper assignments, Wireshark and a research report. Canvas-aligned cards cover Chapter 1, the complete Chapter 2, Tutorials 1–3 and Assignment 1. Extra Resources separately previews historical later topics and exercises. This collection does not define a complete current course or a confirmed QE syllabus.

材料快照 / Material snapshot: 2026-09-22 · ID: CS5222-N089

来源 / Source: cs5222_overview_semA2026.pdf · page 5,11-13

### 研究报告：主题与提交格式 / Research report: topic and submission format

选择在生活中接触、且与教材第 1–7 章有关的新网络技术；要求排除第 8 章安全主题。提交最多 4 页、12 号字体、单栏的报告，参考文献不计入该页数；另附最多 1 页反思日志，两者均为 PDF。可选附录可记录提示词、截图或研究笔记。

Choose a new networking technology encountered in daily life and related to textbook Chapters 1–7; the brief excludes Chapter 8 security topics. Submit a report of at most four pages, 12-point, single column, with references excluded from that page count, plus a reflection log of at most one page, both as PDFs. An appendix with prompts, screenshots or research notes is optional.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5222-N090

来源 / Source: CS5222 Research Report 2026.pdf · page 1

### 研究报告：内容与评分标准 / Research report: content and rubric

说明如何接触该技术、它要解决什么问题、怎样工作、与课程概念如何联系，以及局限或未来挑战。用自己的解释和准确图示。评分中新颖性 10%、技术深度与清晰度 35%、呈现 30%、反思 25%。把一个具体机制讲透，比堆砌未解释的高级术语更有价值。

Explain how you encountered the technology, what problem motivated it, how it works, its connection to course concepts, and its limitations or future challenges. Use your own explanations and accurate illustrations. The rubric weights novelty 10%, technical depth and clarity 35%, presentation 30%, and reflection 25%. A narrow mechanism explained well is more useful than unexplained advanced terminology.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5222-N091

来源 / Source: CS5222 Research Report 2026.pdf · page 1-3

### 反思日志与 GenAI 使用说明 / Reflection log and GenAI disclosure

回答学到了什么、最难部分是什么、GenAI 如何帮助或妨碍理解、怎样验证输出、下次会如何改进。要求注明 GenAI 使用，并核实事实、参考文献和生成图示。研究过程中保留一手来源和具体验证记录，让反思描述真实学习，而非事后编造过程。

Address what you learned, the hardest part, how GenAI helped or hindered understanding, how you verified its output, and what you would change next time. The brief requires acknowledgment of GenAI use and verification of facts, references and generated figures. Keep primary sources and concrete verification notes while working so the reflection records actual learning rather than a reconstructed story.

材料快照 / Material snapshot: 2026-09-15 · ID: CS5222-N092

来源 / Source: CS5222 Research Report 2026.pdf · page 2-3

