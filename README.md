# Micro Course · CS5489 & CS5222

[打开学习网站](https://crazyshout.github.io/micro-course/) · [部署状态](https://github.com/CrazyShout/micro-course/actions/workflows/pages.yml)

课程按老师的 Lecture / Chapter 组织：本讲导读、知识微课、配套 Tutorial、关联 Assignment 和回顾。先从 [CS5489 Lecture 2](https://crazyshout.github.io/micro-course/?course=CS5489&chapter=lecture-2) 或 [CS5222 Chapter 1](https://crazyshout.github.io/micro-course/?course=CS5222&chapter=chapter-1) 开始。

ML07 从课堂鸢尾花辨认任务逐步引出高斯分类；NET02 从多人上传文件解释共享链路。现有 50 节均采用连续文章；各篇围绕自己的任务展开，不套同一个故事。题目与实验按真实编号和任务讲解，图与双语答案就近展开。活动里的原卡预览不是新卡。

材料快照为 2026-09-15，教学整理更新于 2026-09-18：CS5489 30 节微课 / 329 张卡，CS5222 20 节微课 / 280 张卡。当前材料组织成 5 个 Lecture/Chapter、7 个配套活动、31 组原题或任务。历史 Extra Resources 单列，尚未确认的材料不冒充本学期或 QE 范围。

## 使用

首页是课程路线，`cards.html` 是卡片阅读器。每学完一节，可以用文末 2–5 张现有卡巩固；正式间隔复习由 Markji 完成。英文题答可展开，英语训练不代表中文串讲的全文翻译。

Tutorial 1–2 在各自对应课堂下；跨讲 Assignment 只维护一份、从相关讲次进入；Research Report 保留课程级入口。截止、评分与提交手续集中到 [课程信息栏](https://crazyshout.github.io/micro-course/notices.html)。已迁出的 13 张说明卡仍不进入知识卡组。

原 `?lesson=ml07`、`&unit=...`、`&task=...` 和 hash 链接保持。新的课堂入口为 `?course=CS5489&chapter=lecture-2`；任务入口为 `?activity=cs5489-tutorial-2`，可追加 `&item=<id>`。网页组织不改变原 Markji 卡片身份或学习记录。

学习自评保存在当前浏览器，可导出，没有账户或跨设备自动同步。编程、抓包和实验需实际完成；没有自动评分或网页复习排程。不使用 Anki/APKG。

## 维护

`Course/codexing` 是可编辑源，`docs/` 是生成的公开网站，`content/` 是选定的可读主稿副本。课堂组织与任务源在 `learning/curriculum/`，连续文章在 `learning/articles/`；练习、基础与原卡按 ID 引用，不复制第二套答案。

- [课堂与活动对应表](content/learning/curriculum/README.md)
- [已下载材料对应](content/learning/curriculum/materials-map.md)
- [教学讲述标准](content/learning/TEACHING_DESIGN.md)

在主稿中更新并核验后，在此仓库运行：

```sh
python3 tools/sync_from_course.py ../Course/codexing
python3 tools/validate_site.py docs
git diff --check
```

检查差异后只提交本轮文件，再推送 `main`。导出会替换工具管理的 `docs/`，不要直接修改生成页面。只发布选定学习内容与相关资源；完整原课件、API 状态、密钥及本机路径不公开。GitHub Actions 核对资源与关联后发布 `docs/`。

## 本地预览

```sh
python3 -m http.server 8767 --bind 127.0.0.1 --directory docs
```

网站资源随仓库提供，不依赖远端公式 CDN。第三方资源说明见 [NOTICE.md](NOTICE.md)。
