# Micro Course · CS5489 & CS5222

[打开学习网站](https://crazyshout.github.io/micro-course/) · [部署状态](https://github.com/CrazyShout/micro-course/actions/workflows/pages.yml)

先理解，再检索：章节导读、连续微课、双语例题与变式、先修链接、记忆卡片，以及梯度下降、k-means 和网络时延交互演示。

材料快照为 2026-09-15，卡片内容与覆盖核查更新于 2026-09-17：CS5489 30 节微课 / 325 张知识卡，CS5222 20 节微课 / 280 张知识卡。当前 Canvas 内容和往年 Extra Resources 分别标明；AI 讲解不代表教师已确认的考试范围。

## 使用

首页为连续微课；`cards.html` 为卡片阅读器；[课程信息与学习指南](https://crazyshout.github.io/micro-course/notices.html) 集中考核、提交、资料与运行提醒。13 张非知识卡迁出，旧网页链接跳转到对应条目。提示和答案可逐层展开，微课与卡片双向关联。支持英语口述训练、待复习标记及含图片 APKG 下载。

每张 Markji/APKG 卡的答案末尾提供对应微课链接，采用 `?lesson=ml10` 等直达地址。`guide.html?course=CS5489` 与 `guide.html?course=CS5222` 提供两门课各自的完整双语牌组介绍；Markji 简介栏保留短说明和介绍入口。

学习记录保存在当前浏览器，支持导出；没有跨设备或 Markji 自动同步。原课件的文件名与页码保留在出处说明中，Canvas 及历史仓库的完整原材料继续保存在本地 Course 资料库。

## 更新内容

`Course/codexing` 仍是主稿工作区。该仓库的 `docs/` 是生成后的公开网站；`content/` 保留本次导出的可读微课和卡片主稿。

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
