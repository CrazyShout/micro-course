# Micro Course · CS5489 & CS5222

[打开学习网站](https://crazyshout.github.io/micro-course/) · [部署状态](https://github.com/CrazyShout/micro-course/actions/workflows/pages.yml)

从一个问题开始，顺着例子学懂，再用 Markji 巩固。先试读两篇连续文章样板：[ML07 · 咖啡与高斯分类](https://crazyshout.github.io/micro-course/?lesson=ml07)、[NET02 · 咖啡店共享网络](https://crazyshout.github.io/micro-course/?lesson=net02)。正文采用单列阅读，双语题答可展开，图与交互放在解释难点的位置。其余 48 节保留原分步微课，待样板试读后再推广。

材料快照为 2026-09-15，教学整理更新于 2026-09-18：CS5489 30 节微课 / 329 张知识卡，CS5222 20 节微课 / 280 张知识卡。当前 Canvas 内容和往年 Extra Resources 分别标明；AI 讲解不代表教师已确认的考试范围。

## 使用

首页为连续微课；`cards.html` 为卡片阅读器；[课程信息与学习指南](https://crazyshout.github.io/micro-course/notices.html) 集中考核、提交、资料与运行提醒。13 张非知识卡迁出，旧网页链接跳转到对应条目。提示和答案可逐层展开，微课与卡片双向关联。每节先学2–5张首轮重点卡，其余按专题分次进入；网页用于预览，Markji负责正式复习。支持英语口述训练、待复习标记；Python空白骨架与人工DNS样例帮助第一次动手。

每张 Markji 卡的答案末尾提供对应微课链接，采用 `?lesson=ml10` 等直达地址。`guide.html?course=CS5489` 与 `guide.html?course=CS5222` 提供两门课各自的完整双语牌组介绍；Markji 简介栏保留短说明和介绍入口。

学习记录保存在当前浏览器，支持导出；没有跨设备或 Markji 自动同步。原课件的文件名与页码保留在出处说明中，Canvas 及历史仓库的完整原材料继续保存在本地 Course 资料库。

## 更新内容

`Course/codexing` 仍是主稿工作区。该仓库的 `docs/` 是生成后的公开网站；`content/` 保留本次导出的可读微课和卡片主稿。两篇文章的源位于 `Course/codexing/learning/articles/`，通过 ID 引用现有双语练习、基础与专题；不要另外复制一套答案。公开副本在 `content/learning/articles/`。

在本仓库运行：

```sh
python3 tools/sync_from_course.py ../Course/codexing
python3 tools/validate_site.py docs
git add docs content
git commit -m "Update course learning materials"
git push origin main
```

先在 Course 中更新微课与卡片、运行其生成和核验脚本，再导出到此处。导出会替换由工具管理的 `docs/`，因此网页内容应优先在原主稿中修改。此过程按清单选取资源，排除原材料目录、API 同步状态、密钥与本机路径。

GitHub Actions 在 `main` 更新时检查链接、卡片关联和资源哈希，通过后只发布 `docs/`。Pages 的发布来源配置为 GitHub Actions。修改部署方式前可参考 [GitHub 官方说明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 本地预览

```sh
python3 -m http.server 8767 --bind 127.0.0.1 --directory docs
```

然后在浏览器打开终端显示的地址。网站资源均随仓库提供，不依赖远端公式 CDN。第三方资源说明见 [NOTICE.md](NOTICE.md)。
