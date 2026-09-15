# 卡片双语完整性核查 / Bilingual card review

核查范围为 CS5489 的 326 张与 CS5222 的 279 张，共 605 张、2,420 个中英题答字段。两门课的题目、答案正文均已逐项对照；60 张数字、公式或长度差异候选另行查看完整原文。未发现整道题、整段答案缺少一种语言。相同公式在正文对照时用标记压缩展示；公式差异候选保留原式检查。

The review covered 326 CS5489 and 279 CS5222 cards: 605 cards and 2,420 question/answer language fields. Both language versions of all prompts and answers were compared. Sixty candidates flagged by differences in numbers, formulas or length received additional inspection. No whole prompt or answer was missing a language version. Identical formulas were abbreviated during prose comparison; flagged formula differences were inspected in full.

## 补充与修正 / Clarifications

| 卡片 / Card | 调整 / Change |
| --- | --- |
| CS5489-M039 | 中文明确写出正交内积等于零的公式。 / Made the orthogonality equation explicit in Chinese. |
| CS5489-M046 | 中文补出证据项的加法中间式。 / Included the evidence-sum equation in Chinese. |
| CS5489-M081 | 两种语言都补充总文档数 Nc 的定义，并写清类别与词下标。 / Defined Nc and clarified class/word indices. |
| CS5489-M123 | 中文补出负类概率等于正类概率补数的公式。 / Wrote the negative-class complement explicitly. |
| CS5489-M126 | 中文补出零分数损失 log 2 的表达。 / Included log 2 for the zero-score loss. |
| CS5489-M151 | 两种语言明确课件采用的非负约束函数约定。 / Specified the lecture's nonnegative constraint convention. |
| CS5489-M160 | 中文明确样本对按 (x,y) 排列。 / Labeled the Chinese sample pairs as (x,y). |
| CS5489-M317 | 中文明确左乘和右乘的逆矩阵。 / Named the left and right inverse multiplications. |
| CS5222-N079 | 英文明确从开始组包时计时，与中文条件一致。 / Made the packetization start-time reference explicit in English. |
| CS5222-N241 | 中文将定时器界限明确为上下界，与英文一致。 / Matched the Chinese timer-bound wording to English. |

这些修订涉及 10 张卡、12 个字段，其中多处原本已用文字表达同一含义，本次改为显式符号以便独立复习，并非把所有格式差异都判作错译。

These changes affect 10 cards and 12 fields. Several equations were already described correctly in prose; explicit notation improves standalone review. Formatting differences were not automatically treated as mistranslations.

## 附属文字 / Supporting text

微课链接标题补为中英双份，共 673 个入口；往年预习主题、APKG 类型和范围提示、网页章节/主题标签、来源单位、34 类来源说明及卡片阅读器操作提示补为双语。原课件图片、文件名、程序代码和协议报文保留原样；中文题答负责解释它们，避免翻译改变原题或代码含义。

All 673 lesson-link labels now include Chinese and English titles. Historical topic labels, APKG type/scope notes, reader chapter/topic labels, source-location units, 34 provenance descriptions, and reader instructions are bilingual. Original figures, filenames, code and protocol transcripts remain unchanged; surrounding explanations provide the Chinese interpretation.

## 验证 / Validation

- 网页实际渲染全部 605 张，2,420 个题答字段无空项，1,876 处公式无 KaTeX 错误。 / All 605 cards rendered, with 2,420 nonempty language fields and no KaTeX errors across 1,876 formula occurrences.
- 两门课在 390 px 宽度下无页面横向溢出；检查了英语/中文/双语切换及先遮答、后显示两种答案。 / Both courses fit a 390 px viewport; language switching and answer reveal were checked.
- 两个 APKG 的实际数据库字段与主稿匹配；605 个笔记 GUID、牌组 ID 与 62 张图片保持。 / Actual APKG fields match the masters; note GUIDs, deck IDs and all 62 images are preserved.
- Markji 按原卡片 ID 更新，先对五张样本写入后回读，再进行全库同步与逐卡内容回读。 / Markji updates use existing card IDs, beginning with five write/read-back samples and followed by a full synchronization/read-back workflow.

本轮是双语完整性与显示核查，不是重新逐页审计全部原课件，也没有测试 Anki 客户端实际导入。Markji 的网页控制仍可能超时；服务端保存情况由 API 回读核对，不以一次浏览器操作成功与否推断。

This pass checks bilingual completeness and rendering, not every original course page or an actual Anki-client import. Markji browser control can time out; saved server content is checked through API read-back rather than inferred from a browser action.
