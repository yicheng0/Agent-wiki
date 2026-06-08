---
title: "Hermes 保姆级教程：从入门到精通，附 9 条变现路径"
source: "https://x.com/Jason23818126/status/2046055923094040818"
author:
  - "[[@Jason23818126]]"
published: 2026-04-20
created: 2026-05-25
description: "目前 Hermes Agent 热度爆棚，但作为小白还不知道怎么下手安装怎么办？别担心，本文从零带你深入浅出了解 Hermes 究竟比之前的 Openclaw 强在哪里，并手把手完成从安装部署到精通高阶玩法的全过程，最后还会附上 9 条实用的变现路径。一、Hermes 究竟强在哪..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HGSW2p7akAAEZgP?format=jpg&name=large)

目前 Hermes Agent 热度爆棚，但作为小白还不知道怎么下手安装怎么办？别担心，本文从零带你深入浅出了解 Hermes 究竟比之前的 Openclaw 强在哪里，并手把手完成从安装部署到精通高阶玩法的全过程，最后还会附上 9 条实用的变现路径。

## 一、Hermes 究竟强在哪里？—— 为什么值得从小白开始投入

在当前的开源 AI Agent生态中，Hermes Agent 是 Nous Research 推出的自改进 AI Agent 框架。项目在 GitHub 发布短短两个月内就积累了超过 10 万个Stars ，成为 2026 年最受关注的本地 Agent 之一。它本质上是 OpenClaw 项目的进阶版本，也是“Harness Engineering（缰绳工程）”概念的首次大规模产品化落地。

传统的 AI 工具（如 OpenClaw）需要用户手动编写超长的指令文件（例如 SOUL.md）、自己配置复杂规则、设计反馈机制，全靠人工一点点维护，稍有更新就容易崩盘。而 Hermes Agent 的核心优势在于它内置了一个完全自动化的“学习循环闭环”，让 Agent 真正“越用越聪明”：

- **记忆自动归档：**每次对话结束后，Agent 会主动判断哪些信息有价值，并自动写入本地 SQLite 数据库，建立 FTS5 全文索引。告别过去全靠人工记忆或上下文爆炸的问题，后续检索速度快、成本低。
- **自主创建 Skill（技能）：**当它帮你完成一项复杂任务后，系统会自动提炼操作步骤，生成 Markdown 格式的 Skill 文件，直接保存在 ~/.hermes/skills/ 目录。下次相同需求直接调用，无需重复描述。
- **技能自我进化：**如果你指出错误，它不仅本次修正，还会自动更新对应的 Skill 文件规则，实现真正的长期迭代。社区实测显示，使用 1-2 周后，重复任务的成功率可提升 30 %以上。
- **按需检索（告别卡顿）：**新对话时不再把几十万字历史全塞进上下文，而是根据当前话题进行全文检索，只提取相关片段。这让运行速度和 API 调用成本都大幅优化，尤其适合长线投研或多轮任务。
- **用户建模（它比你更懂你）：**内置 Honcho 模块，能从你的行为模式中推导工作习惯（例如你喜欢看数据、偏好精简结论、晚上 10 点后更活跃），后续回复会主动迎合你的风格，减少沟通摩擦。

**小白 Tips** ：OpenClaw 更像一个“万能网关”，集成广但需要你持续手动调教；Hermes 则更像一个“会成长的伙伴”，初期上手稍有学习曲线，但长期使用下来省心省力很多。适合想长期养一个“私人超级个体助手”的人。

## 二、入门阶段——安装部署与模型接入（30 分钟跑通基础）

Hermes 提供了三种主流安装方式，根据你的设备和需求选择即可。新手推荐先用本地或 Docker 快速测试。

1. **本地常规部署（推荐小白起步）**
- 适用于 macOS / Linux / WSL2。
- 打开终端，直接运行官方一键安装脚本：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

- Windows 用户需先安装 WSL2（推荐 Ubuntu 22.04），然后在 WSL 终端执行上述命令。
- 脚本会自动安装 Python、Node.js、Git 等依赖，并在用户根目录生成 ~/.hermes/ 核心文件夹（所有记忆、技能、配置都在这里，数据本地化，隐私安全）。

**2\. Docker 容器化部署（推荐不想污染本地环境的用户）**

```bash
docker pull nousresearch/hermes-agent:latest
docker run -v ~/.hermes:/opt/data nousresearch/hermes-agent:latest
```

- 关键参数 -v ~/.hermes:/opt/data 会把容器内数据映射到宿主机，即使容器删了，记忆和技能依然保留。

**3\. VPS 云服务器部署（适合 24 小时不间断运行）**

- 推荐低配 Ubuntu 22.04 LTS 服务器（单核 CPU + 1GB 内存就够），Hetzner、DigitalOcean 等平台月费约 5 美元。
- SSH 登录后，直接粘贴执行上面的本地一键安装脚本即可。
- **额外 Tips** ：部署后用 screen 或 tmux 后台运行，避免 SSH 断开后进程退出。

**4\. 运行状态自检与排障**

- 安装完成后输入 hermes version，看到版本号即成功。
- 运行 hermes doctor 执行系统诊断，检查 OpenAI SDK、Rich 等组件是否就绪（全部打勾即可）。
- 常见问题补充：如果报 Python 或 Node 版本冲突，建议先卸载系统自带旧版本；网络问题可加 --proxy 参数或切换镜像源。

**5\. 初次运行与自动配置向导接入（最核心一步）**

- 在终端输入 hermes 回车，进入 Quick Setup 向导。
- LLM 后端推荐新手先选 DeepSeek、Kimi 或 OpenRouter 免费模型（免费额度高，够前期反复测试）。
- 熟练后用 hermes model 命令切换到 Claude 3.5 Sonnet、GPT-4o 或 Nous Portal 高阶模型。
- 测试命令：hermes chat -q "Hello! What tools do you have available?" —— 如果正常列出工具列表，整个入门流程就跑通了。

![图像](https://pbs.twimg.com/media/HGElifrbUAAB2zX?format=jpg&name=large)

![图像](https://pbs.twimg.com/media/HGEmG6Qa4AAQi5O?format=jpg&name=large)

**常用命令速查（入门必备）：**

- hermes —— 开启对话模式
- hermes model —— 切换/查看模型
- hermes tools —— 配置可用工具
- hermes gateway —— 启动消息网关
- hermes setup —— 重新配置向导
- hermes doctor —— 系统诊断
- hermes migrate openclaw —— 从 OpenClaw 迁移数据（支持自动导入历史技能和配置）

## 三、进阶阶段——三层记忆机制与底层参数调优（让它真正记住你）

入门跑通后，就该让 Hermes “懂你”了。这部分是 Hermes 区别于其他 Agent 的核心竞争力。

**1\. 三层本地记忆架构（纯本地，无云端泄露）**

- 会话记忆：SQLite + FTS5 全文索引，记录原始对话和工具调用结果，适合快速追溯具体细节。
- 持久记忆：长期观察你的行为模式（代码习惯、工具偏好、作息规律、情绪触发点等）。Honcho 模块甚至能推理出“你报错时容易急躁”，从而自动调整回复语气。
- Skill 记忆：存放在 ~/.hermes/skills/下的 Markdown 文件，记录具体任务的执行规范和步骤。

**如何给它立人设？**

- 编辑 ~/.hermes/SOUL.md 文件，写入：“我是做 AI 趋势投研和 Web3 个体的，习惯看数据、结论要精简直接、回复请多用列表”。保存后重启对话即可。
- 更智能方式：在聊天中多纠正它，然后说：“根据我们今天的对话，自动调整并更新 SOUL.md”。它会自己总结你的偏好并写入。

**2\. 模块化模型配置（省钱+高效实操技巧）**

打开 ~/.hermes/config.yaml，将不同任务分层：

- 核心逻辑（记忆策划、技能提炼、复杂投研）→ 用 Claude Opus / GPT-4o 等强推理模型。
- 基础执行（网页搜索、文本格式化、简单汇总）→ 用 OpenRouter 免费/低价模型。

实测效果：这种分层配置可将长期 API 费用降低 50%-70%。建议新手先用免费模型练手，熟悉后再升级。

**进阶 Tips** ：定期运行 hermes status 查看内存占用和技能使用统计，及时清理不常用记忆，避免磁盘膨胀。

## 四、高阶阶段——技能系统、通讯平台接入与自动化流转（让它真正帮你赚钱干活）

只有大脑还不够，得让它“动手”并 24 小时在线。

1. **自动进化的 Skill 系统（最实用部分）**
- 出厂自带 40+ 常用技能，但最强大是它自己生成的。
- 示例：输入“帮我抓取 Hacker News 首页的 AI 新闻，并总结成中文摘要 + 投研亮点”。完成后它会自动生成 Skill 文件。
- 官方 Skills Hub（[agentskills.io](https://agentskills.io/) 兼容）允许一键安装社区优秀技能。以前在 Claude Code、Cursor 写的技能文件，直接复制到 ~/.hermes/skills/ 即可无缝复用，实现跨平台规则共享。
- 高阶玩法：用 hermes skills list 查看已有技能，用 hermes skills edit <name> 手动微调，再让它自我进化。

**2\. 跨平台网关配置（手机随时指挥）**

- 飞书接入（国内最方便）：运行 hermes gateway setup 选飞书，创建企业自建应用，填 App ID 和 App Secret 即可。所有上下文本地同步。
- Telegram 接入：找 [@BotFather](https://x.com/@BotFather)，获取 Token，运行 hermes config set TELEGRAM\_BOT\_TOKEN your-token，然后启动网关。
- 支持多平台同时接入，手机上发指令，电脑 /VPS 上继续执行，记忆完全一致。

**3\. MCP 协议与自动化流转（真正的生产力爆发）**

- **Model Context Protocol (MCP)**：标准化协议，可直接调用 6000+ 外部服务（无需额外适配）。支持 stdio（本地无网络开销）和 HTTP/SSE 两种方式。

示例接入 GitHub（安全配置）：

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "你的Token"
    allowed_tools: ["read_repo", "list_issues"]  # 只开放读取，屏蔽修改权限
```

- **定时调度（Cron）**：编辑 ~/.hermes/cron/tasks.yaml，设置每日早间自动追踪 AI/Web3 新闻并推送到 Telegram。

示例：

```yaml
tasks:
  - name: daily_ai_tracking
    schedule: "0 9 * * *"
    command: "总结今日AI趋势和Web3投研热点，用列表输出"
    platform: telegram
    chat_id: "your-chat-id"
```

- **多 Agent 并发编排（delegate\_task）：**主 Agent 可并行拉起最多 3 个子 Agent 实例，分别负责数据检索、文档分析、社区汇总，最后主节点客观合成报告。大幅缩短复杂任务时间（例如预测市场项目深度投研）。

**高阶 Tips**：结合 MCP + Cron + 多 Agent，可搭建全自动“AI 投研流水线”，每天睡醒就有新鲜报告，很适合个体搞钱场景。

## 五、生态导航与资源汇总

Hermes 虽然年轻，但社区活跃度很高 ：

- 官方英文文档：[https://hermes-agent.nousresearch.com/docs/](https://hermes-agent.nousresearch.com/docs/)
- 中文社区文档：[https://hermes-doc.aigc.green/](https://hermes-doc.aigc.green/)
- Awesome 资源：[https://github.com/0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
- 官方技能商店：[https://hermes-agent.nousresearch.com/docs/skills](https://hermes-agent.nousresearch.com/docs/skills)
- 生态地图（80+ 工具可视化）：[https://hermes-ecosystem.vercel.app](https://hermes-ecosystem.vercel.app/)
- 橙皮书（花叔深度解读）：[https://www.huasheng.ai/orange-books/hermes-agent/](https://www.huasheng.ai/orange-books/hermes-agent/)

## 附：9 条变现路径

1. 代安装与排障服务（闲鱼/小红书接单，远程帮小白部署，一单几十到上百）
2. 工作流定制（帮电商/投研团队写自动抓取、排版脚本，收费几百到上千）
3. 卖现成技能包（打包常用 Markdown Skill，虚拟产品零成本多卖）
4. 做自动化内容账号（定时任务自动搜集新闻、改写发帖，赚流量分成）
5. 做付费数据社群（24h 监控行业数据，自动推送，收包月费）
6. 技能分发赚提成（上传到技能平台，按调用次数分成）
7. 自动化任务脚本（监控打折、重复点击等省时省力）
8. 企业内部工具开发（接入公司数据库/代码库，做外包项目）
9. 做培训和社群陪跑（开小班教安装+高阶用法，提供长期答疑）

看完这篇，有没有感觉 Hermes 比想象中好上手多了？

我是 [@Jason23818126](https://x.com/@Jason23818126) ，摸鱼局长，主要分享 AI 趋势及干货、个体搞钱路径和 Web3、美股赛道投研。

想一起用 AI 工具少走弯路、早点上车搞钱的，欢迎关注我，一起 Stay lazy, stay early 🦞

（喜欢就点个关注或转推，非常感谢各位~ ）