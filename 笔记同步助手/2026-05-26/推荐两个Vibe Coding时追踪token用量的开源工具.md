---
author: 鲁工
source: 微信公众号
url: https://mp.weixin.qq.com/s/kskGYs_MI9r3dyI7S3vhQA
saved: 2026-05-26 17:17:35
tags:
  - 笔记同步助手
id: 01eb8fc1-85fb-4225-9128-9200850ac94d
---

公众号名称：AI编程实验室

作者名称：鲁工

发布时间：2026-05-26 16:46

大家好，我是鲁工。

之前写过一篇关于token用量讨论的短评：

[每天5亿token消耗，最大的痛苦是人跟...](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247485650&idx=1&sn=721f3f686370381ba372ef8798682d70&scene=21#wechat_redirect)

很多读者问，日常都是用什么工具来追踪Claude Code和Codex等Vibe Coding的token用量的，今天就专门推荐下。

今天推荐的两个开源工具都是咱们Vibe Coding群里经常讨论的，一个叫 ccusage，一个叫TokenTracker。各有特色，搭配着用基本能把token用量情况看清楚。

先说​ccusage​。定位很直接，就是把本地Coding Agent CLI的token用量和成本拉出来做报表。

我装的时候特意没全局安装，直接npx跑：

```
npx ccusage@latest
```

第一次跑会下载缓存，之后启动飞快。它会自动扫描机器上能识别的所有Coding CLI数据目录，默认输出daily报表。

![[笔记同步助手/images/0c94c4c0d6419039b7943400d3b9861d_MD5.png]]

目前覆盖15个工具：Claude Code、Codex、OpenCode、Amp、Droid、Codebuff、Hermes、pi-agent、Goose、OpenClaw、Kilo、Kimi、Qwen、GitHub Copilot CLI、Gemini CLI。

命令也很克制。daily看日报，weekly看周报，monthly看月报，session按会话分组。

ccusage整体气质比较像Unix时代的小工具，专注一件事并且做好。命令行、表格、JSON导出，没有web界面、没有menu bar，简简单单的。

项目地址：

https://github.com/ryoppippi/ccusage

第二个是TokenTracker。走的是另一条路径。除了ccusage支持的CLI之外，它还覆盖Cursor、Antigravity、Kiro、CodeBuddy、Grok Build、Roo Code、Zed Agent这些IDE类或VS Code插件类工具。

启动也一行：

```
npx tokentracker-cli
```

第一次跑它会自动注入hook到各家CLI配置文件，同步历史数据，起一个本地服务在localhost:7680，然后直接帮你打开浏览器。30秒看到token用量的dashboard。

![[笔记同步助手/images/0b7daec6f58f1c9649588e85dccf4954_MD5.png]]

dashboard做得还是比较精美的。GitHub风格的活动热力图、按模型拆分的成本饼图、按项目归因的柱状图，还有一个rate limit实时进度条覆盖Claude / Codex / Cursor / Gemini / Kiro / Kimi / Copilot / Antigravity 8个工具。

它原理是几种采集方式混着用：能下hook的（Claude Code、Codex、Gemini）走SessionEnd hook，剩下的（Cursor、Roo Code、Zed Agent、Goose 等）就被动读它们已经在写的SQLite或JSONL文件。

项目地址：

https://github.com/mm7894215/TokenTracker

ccusage和TokenTracker两个都依赖LiteLLM定价库，新模型上线1-3天内定价可能滞后。

## 感兴趣的读者可以试一下这两个工具，都是一行命令的事。

  

如果觉得有用，点个赞或者在看，也方便更多朋友看到。

感谢您阅读我的文章。我是鲁工，九年AI算法老兵，AI全栈开发者，深耕AI编程赛道。

\>/ 作者：鲁工

---

![[笔记同步助手/images/2e90650768a2be8a6fdbb660cf085249_MD5.jpg|cover_image]]

原创 鲁工 AI编程实验室

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/27d7e2fa_1779787053557?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FkskGYs_MI9r3dyI7S3vhQA&s=obsidian)