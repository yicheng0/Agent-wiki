---
author: Excellent
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYzMzkwNjU1OQ==&mid=2247485018&idx=1&sn=4be4222b824e42b2cf1d47b96c23e4d1&chksm=f14333808baf745466056c6a1935b887bd7fe68591dea8f8847f439af9257811e4e2a8e66193&mpshare=1&scene=1&srcid=0526Ke7e166CO4xIuAABZtsQ&sharer_shareinfo=bb425fb7d01cc8ec890e3f6d75eeb3a5&sharer_shareinfo_first=bb425fb7d01cc8ec890e3f6d75eeb3a5#rd
saved: 2026-05-26 10:05:16
tags:
  - 笔记同步助手
id: 80f45133-9d07-4d54-93f4-0816b602b6ec
---

公众号名称：优码云AI

作者名称：Excellent

发布时间：2026-05-25 16:08

01

> 写在前面

这是一篇写给前端的AI Coding实战长文，你已经把界面、组件、工程化玩得挺熟，缺的多半只是一套跟AI配合的方法，下面从工具、Agent、还原、学习路线一直讲到团队转型，配了十几张图，方便边看边对照，内容偏长，建议先扫一眼下面的导读，按需跳读。

02

> 本文导读

第一、二章：转型机遇，以及把AI的基本概念一次说清（LLM、上下文、Agent、MCP、vibe和spec）。

第三章：设计稿转代码的工具链，Stitch、Figma、Pencil、Open Design都讲到。

第四章：Claude Code、Codex、Cursor三个Agent怎么选、怎么学。

第五章：把设计稿精准还原成页面的方法。

第六章：一条能照着走的学习路线。

第七、八章：团队怎么转，外加一个端到端实战案例。

03

> 章 前端工程师的AI Coding转型机遇

1.1 为什么是现在

2025年是AI编程真正成熟起来的一年。年初DeepSeek这类模型把推理成本压了下来，年中各种编程智能体（Agent）密集冒出来，到了年底，不少人已经习惯直接让AI大段大段地写代码。进入2026年，Claude Code、Codex、Cursor的周活跃开发者都到了百万甚至千万级别。对开发者来说，AI写代码已经从演示变成了每天都在用的工具。

这波变化对前端的冲击格外直接。界面这种东西，本来就容易用语言说清楚，也容易看出来做得对不对。设计稿转代码、生成组件、还原页面、调样式，这些活大模型上手很快，结果好不好也一眼能验证。所以前端常常是AI落地最快、见效最明显的方向。与其担心被取代，不如早点把自己变成会带着AI干活的人。

1.2 前端的底子，大半都能直接用上

有个常见的误区，觉得转AI得先补一大堆算法和数学。对前端来说没那么夸张，手上已有的不少经验可以直接迁移过去。先把这点想明白，能省掉不少焦虑和弯路。

异步和流式你早就熟了。写过async/await、踩过Promise和竞态的坑，调用大模型API、处理流式返回的token，用的是同一套思路。

调API是你的日常。AI工程里很大一块就是调接口、管密钥、解析JSON、处理重试，这些你天天都在做。

状态管理能平移。现在很火的Agent框架LangGraph，骨子里就是一台状态机，跟你用Redux、Zustand那套是相通的。

你知道什么叫好界面。大部分AI工程师做不出像样的UI，而后端能力和生产级前端都拿得下的人，2026年很稀缺，也很值钱。

验证这件事你最在行。截图对比、视觉回归、E2E测试，前端都有成熟做法。让AI能自己检查做得对不对，正好是用好Agent最划算的一招。

下面的导读，按需跳读。

本文导读

第一、二章：转型机遇，以及把 AI 的基本概念一次说清（LLM、上下文、Agent、MCP、vibe 和 spec）。

第三章：设计稿转代码的工具链，Stitch、Figma、Pencil、Open Design 都讲到。

第四章：Claude Code、Codex、Cursor 三个 Agent 怎么选、怎么学。

第五章：把设计稿精准还原成页面的方法。

第六章：一条能照着走的学习路线，含时间轴和薪资参考。

第七、八章：团队怎么转，外加一个端到端实战案例。

第一章前端工程师的 AI Coding 转型机遇

1.1 为什么是现在

2025 年是 AI 编程真正成熟起来的一年。年初 DeepSeek 这类模型把推理成本压了下来，年中各种编程智能体（Agent）密集冒出来，到了年底，不少人已经习惯直接让 AI 大段大段地写代码。进入 2026 年，Claude Code、Codex、Cursor 的周活跃开发者都到了百万甚至千万级别。对开发者来说，AI 写代码已经从演示变成了每天都在用的工具。

这波变化对前端的冲击格外直接。界面这种东西，本来就容易用语言说清楚，也容易看出来做得对不对。设计稿转代码、生成组件、还原页面、调样式，这些活大模型上手很快，结果好不好也一眼能验证。所以前端常常是 AI 落地最快、见效最明显的方向。与其担心被取代，不如早点把自己变成会带着 AI 干活的人。

1.2 前端的底子，大半都能直接用上

有个常见的误区，觉得转 AI 得先补一大堆算法和数学。对前端来说没那么夸张，手上已有的不少经验可以直接迁移过去。先把这点想明白，能省掉不少焦虑和弯路。

异步和流式你早就熟了。写过 async/await、踩过 Promise 和竞态的坑，调用大模型 API、处理流式返回的 token，用的是同一套思路。

调 API 是你的日常。AI 工程里很大一块就是调接口、管密钥、解析 JSON、处理重试，这些你天天都在做。

状态管理能平移。现在很火的 Agent 框架 LangGraph，骨子里就是一台状态机，跟你用 Redux、Zustand 那套是相通的。

你知道什么叫好界面。大部分 AI 工程师做不出像样的 UI，而后端能力和生产级前端都拿得下的人，2026 年很稀缺，也很值钱。

验证这件事你最在行。截图对比、视觉回归、E2E 测试，前端都有成熟做法。让 AI 能自己检查做得对不对，正好是用好 Agent 最划算的一招。

一句话定位

说到底，前端转 AI 用不着从头学一门手艺，更像是在你已有的工程能力上，加一套和 AI 配合的工作方法。

往后你拼的不再是打字快慢。重心会从亲手敲每一行，挪到把需求想清楚、把边界划好，再盯着 AI 把活干对、验收到位。

1.3 这份手册怎么读

这份手册写给前端已经比较熟练、但刚开始接触 AI 工具的人。内容从浅到深，尽量做到看完就能上手。建议这么读：

第二章先把后面反复出现的概念过一遍，比如 LLM、Token、上下文、Agent、MCP、vibe coding 和 spec-driven、上下文工程，给自己建一个词汇表。

第三章系统看一遍设计稿转代码的工具，Google Stitch、Figma、Pencil、Open Design 都会讲到，最后给选型建议。

第四章深入 Claude Code、Codex、Cursor 这三个 Agent，讲清楚各自能干什么、怎么学。这部分是日常生产力的核心。

第五章讲怎么把设计稿高保真地还原成页面，包括为什么会翻车，以及怎么靠结构化数据和视觉闭环做对。

第六章给一条能照着走的学习路线，含 30/60/90 天计划和资源清单。

第七章面向团队和公司，讲 AI Coding 怎么在组织里落地，包括 DDAD、上下文工程、度量和治理。

第八章和附录一个完整的实战案例，再加上提示词模板和全部参考链接。

第二章 AI Coding 基础概念扫盲

这一章把后面会反复用到的概念讲清楚。你不需要懂模型内部那套数学，但得有一套够用又准确的理解，才能用顺手、看得懂文档。

2.1 LLM、Token 和上下文窗口

大语言模型（LLM）做的事情，简单说就是根据前面的内容预测下一个词。它不会去执行你的代码，而是凭着从海量文本里学到的规律，生成最像样的文本，代码也是这么生成出来的。入门只要记住三个词。

Token（词元）。模型处理文本的最小单位，大概是半个到一个英文单词，或者一个汉字。算钱、算长度都按 token 来。

上下文窗口。模型一次能看到的 token 总量，输入加输出都算在里面。2026 年主流 Agent 普遍是 200K token，有些能开到 100 万。

上下文和记忆是两回事。模型默认不会跨会话记得你。每次对话它能用的，只有这次塞进上下文窗口里的内容。上下文工程就是冲着这件事来的。

上下文是耗材，得省着花

有个经验值：上下文用到七成左右，模型精度就开始往下掉；到八成五，容易开始胡编（也就是 hallucination）；过了九成，输出基本不稳了。

对应的做法是：用到五成以内可以放开手；五到七成留点神；七到九成主动用 /compact 压一压；过了九成就别犹豫，/clear 重开。

![[笔记同步助手/images/754ed4c193719456bcb7a3a10844d6f5_MD5.png]]

上下文是耗材：用得越满越容易出错（经验示意）

2.2 Prompt 和提示词工程

Prompt 就是你给模型的指令和背景信息。提示词工程不玄乎，核心就是把任务说清楚、能验证、有边界。针对前端，下面几条最值钱。

说具体。把目标、技术栈、文件路径、约束都写出来，比如移动端优先、用 Tailwind、别引入新依赖。

给例子。给一个想要的样子，再给一个反面例子，比讲一堆抽象要求管用得多。

让它先想后做。先要它给个方案或计划，你看过再放行去执行。

需要时指定输出格式。比如要 JSON、表格，或者指定的标签，方便你后面用程序处理。

把能验证的东西一起给它。测试、截图、期望结果都丢进去。一个任务只要 AI 能自己对照检查，完成质量会明显高一截。

2.3 三代工具：从补全到 Agent

把工具分代看一下，就能明白为什么 Claude Code、Codex 用起来和早期的 Copilot 差别那么大。

![[笔记同步助手/images/ea7dc2556950e5353ae1ba6436e61d5c_MD5.png]]

三代工具：你的角色从「写代码」变成「指挥与验收」

第三代最大的不同是它能自己动手。它可以直接碰你的文件系统和终端，通过 MCP 调各种工具，一个任务里跑几十甚至上千次工具调用，中间不用你一步步盯着。于是你的工作从敲代码，变成把意图说清、把边界定好、最后审一遍验收。

2.4 MCP 是什么

MCP 全称 Model Context Protocol，模型上下文协议，是 Anthropic 在 2024 年 11 月开源的一个标准。打个比方，它有点像 AI 应用的 USB-C 接口，用一套统一的方式让 AI 去发现并调用外部的工具、数据和资源，比如 Figma、GitHub、数据库、浏览器。

![[笔记同步助手/images/e618bf0ac7221a596fef75a110dd94c8_MD5.png]]

MCP 像 USB-C：一套标准把 N×M 的重复对接变成接上就能用

它解决什么。没有 MCP 的时候，N 个工具要分别对接 M 个模型，是 N 乘 M 的重复对接，很折腾。有了 MCP，大家讲同一种话，接上就能用。

三个角色。Host 是宿主（比如 Claude Code），Client 是客户端，Server 是服务器，负责暴露具体能力（比如 Figma MCP Server）。

对前端的意义。接上 Figma 的 Dev Mode MCP，AI 就能直接读到设计稿的图层树、变量、组件映射，而不用靠看截图去猜，生成的代码自然更准。这块第五章细讲。

2.5 Vibe Coding 和 Spec-Driven

这是 2025 到 2026 年最值得搞懂的一对方法论。弄明白了，你既能跑得快，又不至于翻车。

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="86" width="86" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>维度</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>Vibe Coding</span></span><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>（凭感觉写）</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>Spec-Driven</span></span><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>（按规格写）</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="86" width="86" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>做法</span></span></div></td><td data-colwidth="302" width="302" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提示、生成、再改，靠直觉快速试</span></span></div></td><td data-colwidth="302" width="302" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>先写一份机器能读的规格，当作唯一标准，再据此生成实现、测试和文档</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="86" width="86" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>好处</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>探索快、出原型快、门槛低</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>能复现、好协作、可追溯，规模大了也稳</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="86" width="86" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>风险</span></span></div></td><td data-colwidth="302" width="302" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>大约三个月后会撞上技术债的墙；同一句提示跑十次能出十个版本，人一多就乱</span></span></div></td><td data-colwidth="302" width="302" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>前期得花时间写规格，小活会显得有点重</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="86" width="86" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>适合</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>探索、做原型、个人小功能，团队五人以内</span></span></div></td><td data-colwidth="302" width="302" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>复杂系统、十人以上、受监管行业、要正式交付的</span></span></div></td></tr></tbody></table>

  

推荐的姿势

先用 vibe 去探索，等方向定下来，再用规格把它固化。

具体点说，原型阶段放开手快速试；想法成型后，把关键决策写进版本管理里的文档，再让 Agent 照着实现。

2.6 上下文工程

如果说提示词工程是写好一句指令，那上下文工程就是经营 AI 的整个工作环境：给它哪些文档、哪些规则、哪些工具、哪些记忆。这是用好 Agent 的核心，也是第七章团队转型的重点。

项目规则文件。像 CLAUDE.md、AGENTS.md、RULES.md，把项目架构、技术栈、代码规范、不能碰的地方都固定下来，让每次会话一开始就带着背景。

给得准，别给得多。关键是只放相关的东西。结构化数据，比如设计 token、组件映射，比一堆截图省 token，也更靠谱。

工具和记忆。需要什么工具就通过 MCP 接进来；靠记忆和规则文件，让上下文跨会话、跨项目接着用。

2.7 名词速查表

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>术语</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>一句话解释</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>LLM</span></span></div></td><td data-colwidth="518" width="518" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>大语言模型，按概率预测下一个词的生成式模型</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Token / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上下文窗口</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>token </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>是文本计量单位；上下文窗口是模型一次能看到的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> token </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上限</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Agent</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>（智能体）</span></span></div></td><td data-colwidth="518" width="518" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>能自己读写文件、跑命令、调工具、做验证的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>程序</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>模型上下文协议，</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>连外部工具和数据的统一标准</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Vibe Coding</span></span></div></td><td data-colwidth="518" width="518" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>凭感觉、靠提示快速生成和迭代</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Spec-Driven</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>以机器可读的规格为唯一标准的工程化开发</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上下文工程</span></span></div></td><td data-colwidth="518" width="518" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>经营</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工作环境的能力，包括规则、文档、工具、记忆</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Dev Mode</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>给开发者用的模式，提供测量、变量、代码和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> MCP </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>接入</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Design-as-Code</span></span></div></td><td data-colwidth="518" width="518" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计即代码，用可读的结构化文件描述设计，比如</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> .pen</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>DESIGN.md</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="173" width="173" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>BYOK</span></span></div></td><td data-colwidth="518" width="518" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Bring Your Own Key</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，自带模型密钥，不绑定单一厂商</span></span></div></td></tr></tbody></table>

  

第三章设计稿转代码工具链

把设计变成能用的前端，是 AI 见效最直接的场景。这一章先给一张全景图，再把你点名的 Google Stitch、Figma、Pencil、Open Design 逐个拆开讲，顺带补几个最近很火的工具，最后说选型。

3.1 全景图：三种路子

2026 年的设计转代码工具，大致是三种路子。选之前先想清楚自己要的是哪一种。

![[笔记同步助手/images/1771bb4fdf0d82e2534d2bc81d9db901_MD5.png]]

设计转代码的三种路子：先想清楚自己要哪一种

3.2 Google Stitch

Google Stitch 是 Google Labs 在 2025 年 Google I/O 上推出的 AI UI 设计工具，底层是 Gemini，目前免费。它的玩法很直白：用一句话或者一张图描述你想要的界面，Stitch 直接给你生成 UI，还能导出代码。

能做什么

底层模型。跑在 Gemini 2.5 Pro 上，文字和图片都能看懂。

一次出一堆。一次给你多套设计变体、多屏布局、Material Design 3 组件，还自带浅色和深色两版。

原型能点。生成的是可点击的原型，不是静态图，方便拿去做用户测试或者汇报。

代码能导。能导出 HTML/CSS 和组件级代码，也能导回 Figma 继续编辑，或者接进 Google AI Studio、Antigravity 去搭完整应用。

2026 年 3 月的大更新

2026 年 3 月，Stitch 从一个单屏生成器升级成了多屏原型工作台。现在能一次生成最多 5 个互相连通的屏幕，加上 AI 原生的无限画布、语音输入和一个设计 Agent，导出还支持 7 种框架的生产级代码，已经在正面对标 Figma 和一批 AI 设计创业公司了。

适合谁

会写代码但没什么设计功底的前端。Stitch 能给你一个有样式、有结构的起点和一份能改的代码，比对着空白 HTML 发呆强多了。

一句提醒：它的产物到不了资深设计师的水准，定位是一个不错的起点，后面还得你自己加工。

3.3 Figma：Dev Mode MCP、Figma Make、Code Connect

设计稿转代码，源头多半还是 Figma。2025 到 2026 年它在 AI 这边补齐了三块能力，前端值得重点掌握。

① Dev Mode MCP Server（强烈建议先学这个）

Figma 在 2025 年推出了官方的 MCP Server，把设计文件里的结构化内容通过 MCP 暴露给 AI 编程工具，包括 VS Code 里的 Copilot、Cursor、Windsurf、Claude Code 等等。它是高保真还原的地基。

它给的是结构化数据，不是截图。节点树、变体信息、布局约束、设计变量（design tokens）、资源引用都有，这些在截图里都看不到。

好处。因为能引用到具体的变量、组件、样式，生成的代码更准，也更省 token，做设计系统和组件化的时候尤其顺手。

双向打通。2025 年底开始还能把代码结果推回画布，设计和代码两头能对上。

② Code Connect（让 AI 用你自己的组件）

Code Connect 做的事，是把 Figma 里的设计组件，对应到你代码仓库里真实的那个组件。这层映射会通过 Dev Mode 进到 MCP 的返回里。这样 AI 不会另写一个按钮，而是直接调你项目里的那个 Button。想把 AI 的产物真正接进现有设计系统，这一步是关键。

③ Figma Make（一句话出应用）

Figma Make 在 Config 2025 上发布，2025 年 7 月正式可用。你用自然语言描述，它会生成一个基于 React 加 Tailwind CSS 的、能交互的真实原型，在 Code 标签里还能看和复制底层代码。它有个挺好用的点选即改：直接点预览里的某个元素，让 AI 只动那一块，比反复重写整段提示快多了。

价格和获取（2025 到 2026 的情况）

Dev 席位在 Professional 年付方案里大概 12 美元每月起，含 Dev Mode、Code 属性、MCP Server 访问和 FigJam。MCP 在测试期免费，以后可能改成按量付费。

Figma Make 所有用户都能用，但发布、私享、AI 额度、导入设计库这些高级能力，得看你的付费方案。

3.4 Pencil：在画布上写代码

Pencil（pencil.dev）是一款 Agent 驱动的设计工具，把 Figma 那种直观画布和 Claude 这类强模型接到了一起。你用自然语言下指令，AI 就在无限画布上实时生成可编辑的 UI，还能转成 React、Tailwind、Next.js 代码。

.pen 文件是纯 JSON。人能读，机器也能读，所以 AI 能把整个设计结构解析清楚再高保真转码，这也是它设计即代码理念的根。

Code on Canvas。AI 不是丢一段代码让你自己去跑，而是在画布上一个组件一个组件地搭出来，你能即时看到效果。

多 Agent 一起干。最多支持 6 个 AI Agent 在同一块画布上协同。

两种用法。既能当独立桌面应用专心做设计，也能集成进 VS Code、Cursor，在写代码的地方顺手设计。

价格。目前免费。

3.5 Open Design（nexu-io）：本地优先的开源工作台

Open Design（github.com/nexu-io/open-design）是最近社区里非常火的一个开源项目，GitHub 上大概 4.46 万 stars、5100 个 fork。它对标的是 Anthropic 的闭源产品 Claude Design，主打本地优先、开源替代。它跟别家最不一样的地方在于：自己不带模型，而是把你已经在用的编程 Agent，变成一台设计引擎。

它的定位和特性

本地优先、开源（Apache-2.0）、BYOK。应用、守护进程、技能运行时都跑在你本机，产物直接落到你的项目目录里，不用被迫走厂商的云。密钥自带，不绑定单一厂商。

跑在你现有的 Agent 上。支持 Claude Code、Codex、Cursor、Gemini CLI、OpenCode、Qwen、Copilot、Hermes、Kimi CLI 等主流 Agent 当后端。

19 个 Skills、71 套品牌级设计系统。靠可组合的技能和可移植的 DESIGN.md 设计系统来驱动。0.7.0 起，技能和设计系统在应用里一键就能装、卸。

什么形态都能出。Web、桌面、移动端原型，幻灯片、图片、视频，还有 HyperFrames（能交互的故事板），都做得了，支持沙盒预览和 HTML、PDF、PPTX、MP4 导出。

Critique Theater（设计陪审团）。5 个评委从可访问性、品牌契合度、做工等角度给草稿打分，只有 8 分以上才放行，相当于把设计评审做成了一道自动关卡。

Composio 连接器。通过 Composio 接上几百个 SaaS 工具，让生成出来的东西能吃到实时数据。

v0.7.0（2026 年 5 月 13 日）有什么新东西

这个版本三天里合了 107 个 PR，49 个人参与，主题是记忆加 UI 的一次大更新。

自动记忆库（Auto-memory store）。Agent 的上下文能跨会话、跨项目接着用，省得你每次重讲一遍品牌调性、受众和约束，思路类似 Claude Code 的全局记忆，但绑定到设计项目上。

Critique Theater Phase 7 加 6.2。评审面板加了状态机和回放，刷新不丢、断线能重连，被评审标记过的产物会作为真实项目资产留下来。

HyperFrames 支持画布里嵌 HTML。可以在画布模板里塞进真能交互的 HTML，端到端渲染出来，故事板不再只是摆样子。

响应式交付。平板和移动端自适应、2025 到 2026 的视口矩阵、DESIGN-HANDOFF 和 DESIGN-MANIFEST 导出。

其它。Designs 标签重做、预览里直接评论、Media 标签合并、HSL 调色、定时例行任务（让 Agent 无人值守地跑）、HTTP 206 分段加载、macOS Intel 构建和官方 Nix flake，还新增了 hud、loom、trading-terminal、WeChat 几套设计系统和一个 agent-browser 技能。

前端为什么该关注它

它把设计生成、自动评审、多形态导出、实时数据这几件事，串成了一条本地、开源、能自己定制的流水线，而且天然能接你正在学的 Claude Code、Codex、Cursor。

环境要求：macOS 11 以上（arm64 和 Intel 都行）、Windows 10/11、Linux 无头模式或者 Nix；从源码构建需要 Node 24.x 加 pnpm。Windows 安装包没签名，第一次启动会被 SmartScreen 拦一下。

3.6 其它值得知道的工具

除了上面四个，下面这些 2026 年也很热，按用途记个大概就行。

v0（Vercel）。把自然语言变成生产级的 React 加 Tailwind 组件，适合快速搭 UI 脚手架，跟 Vercel 生态绑得很深。

Bolt（StackBlitz）。在浏览器里做全栈编码，能看文件、改文件、装依赖，比 v0 更偏写代码。

Lovable。一句话生成全栈应用，UI、后端、数据库 schema、鉴权、部署一条龙，内建 Supabase，能一键部署、导出到 GitHub，做 MVP 特别快。

Locofy。把干净的 Figma 设计转成结构清楚、命名贴着图层、用 Flexbox 的 React 或 Next.js 组件，纯转码性价比高。

Anima。对设计还原得最贴字面，但大量用绝对定位，视觉对得上，代码偏向把截图重搭一遍，可读性一般。

Builder.io。强在把可视化 CMS 和设计转代码结合起来，适合内容运营和研发要一起干活的团队。

3.7 横向对比

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>工具</span></span></div></td><td data-colwidth="106" width="106" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>路子</span></span></div></td><td data-colwidth="163" width="163" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>输出</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>开源</span></span><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>/</span></span><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>本地</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>最适合</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Google Stitch</span></span></div></td><td data-colwidth="106" width="106" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提示转原型</span></span></div></td><td data-colwidth="163" width="163" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>HTML/CSS</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>7 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>种框架、导出</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>云</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>没设计功底、想快出多屏原型</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma Dev Mode MCP</span></span></div></td><td data-colwidth="106" width="106" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计转代码</span></span></div></td><td data-colwidth="163" width="163" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把结构化数据喂给</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>生成</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>本地服务</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>已有设计稿、要高保真还用自己的组件</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma Make</span></span></div></td><td data-colwidth="106" width="106" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提示转应用</span></span></div></td><td data-colwidth="163" width="163" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>React </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>加</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Tailwind</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>云</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>在</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>里快速做能点的原型</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Pencil</span></span></div></td><td data-colwidth="106" width="106" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计即代码</span></span></div></td><td data-colwidth="163" width="163" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>React/Tailwind/Next.js</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>桌面加</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> IDE</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>在画布上让</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>实时生成和改</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Open Design</span></span></div></td><td data-colwidth="106" width="106" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计即代码</span></span></div></td><td data-colwidth="163" width="163" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>HTML/PDF/PPTX/MP4</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、多端</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>开源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>(Apache-2.0) / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>本地</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>要本地可控、跑在自有</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Agent</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、带自动评审</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>v0 / Bolt / Lovable</span></span></div></td><td data-colwidth="106" width="106" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提示转应用</span></span></div></td><td data-colwidth="163" width="163" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>React </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>组件或全栈应用</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>云</span></span></div></td><td data-colwidth="144" width="144" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>从零快速出</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> UI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>或</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> MVP</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Locofy / Anima</span></span></div></td><td data-colwidth="106" width="106" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计转代码</span></span></div></td><td data-colwidth="163" width="163" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>React/Next.js</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>（</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>HTML/CSS</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>）</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>闭源</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>云</span></span></div></td><td data-colwidth="144" width="144" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>一键转组件</span></span></div></td></tr></tbody></table>

  

3.8 选型建议

已有 Figma 稿、要高保真。主路线就是 Figma Dev Mode MCP 加 Code Connect 加 Claude Code 或 Cursor，让 AI 读结构化数据、复用你的组件库，细节见第五章。

从零探索、先出个原型给人看。Google Stitch、Figma Make、v0、Lovable 挑一个，先把想法跑成能点的原型。

想本地可控、开源、不绑厂商。Open Design 加你现有的 Agent，适合对数据隐私、定制化、团队设计系统有要求的场景。

设计和代码想一份来源一起改。走 Pencil 或者 Open Design 的画布路子。

一个总原则。别指望一款工具通吃。务实的做法是原型用提示类工具，落地用 Dev Mode MCP 加 Agent，并且始终拿设计系统和组件库当唯一标准。

第四章 AI Coding Agent 完整学习路线

Agent 是日常生产力的核心。这一章先把三个主流工具横着比一遍，再分别讲怎么学，最后说怎么搭配着用，以及几个一直用得上的关键技能。

4.1 三个主流 Agent：Claude Code、Codex、Cursor

到 2026 年中，认真做这块的已经有七八家了，还包括 Google Antigravity、GitHub Copilot、Windsurf、Kiro 这些。但前端最该先拿下的就是这三家，它们的思路各不相同。

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="96" width="96" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>维度</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>Claude Code</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>OpenAI Codex</span></span></div></td><td data-colwidth="198" width="198" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>Cursor</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>形态</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>终端优先（</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>CLI</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>）</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>多形态：</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>CLI</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>IDE </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>扩展、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Web</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、云</span></span></div></td><td data-colwidth="198" width="198" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>编辑器优先（</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>VS Code </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>分支）</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>默认模型</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Claude Opus</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>（默认）、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Sonnet</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>（更省）</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>GPT-5.5 / 5.5 Pro</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>400K </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上下文</span></span></div></td><td data-colwidth="198" width="198" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>可选多家模型</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>强项</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>深度多文件改动、上下文大、最省</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> token</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>长时间自主任务、能在后台和云端跑、一口气几百次工具调用</span></span></div></td><td data-colwidth="198" width="198" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>在</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> IDE </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>里日常编码手感最顺</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上下文</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>200K </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>标准，部分支持</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 1M</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>约</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 400K</span></span></div></td><td data-colwidth="198" width="198" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>标称</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 200K</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，实际可用常被截断</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>价格</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个人约</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 20 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>美元每月起，团队偏贵</span></span></div></td><td data-colwidth="199" width="199" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个人约</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 20 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>美元每月起</span></span></div></td><td data-colwidth="198" width="198" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个人约</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 20 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>美元每月起，团队最便宜</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="96" width="96" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>最适合</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>架构级、深度多文件</span></span></div></td><td data-colwidth="199" width="199" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>自动化和后台任务</span></span></div></td><td data-colwidth="198" width="198" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>日常功能开发</span></span></div></td></tr></tbody></table>

  

高产团队是怎么用的

产出高的团队往往同时用两到三个：Cursor 做日常功能，Claude Code 做架构级改动，Codex 跑自动化和后台任务。

有独立测评显示，同一个任务 Claude Code 用掉的 token 大概是 Cursor 的五分之一。所以选型别只盯着月费，token 效率和上下文可靠度也得算进去。

![[笔记同步助手/images/2efcfa7b5c051f34a56165f6ba2223e7_MD5.png]]

三大 Agent 上下文窗口对比

![[笔记同步助手/images/a3580db4b4831eacbc307ae1d359080b_MD5.png]]

完成同一任务的 token 消耗：Claude Code 更省

4.2 Claude Code 学习路线（重点）

Claude Code 是 Anthropic 官方的命令行编程 Agent，2025 年 2 月发布，5 月正式可用。它能直接碰你的文件系统、终端，以及任何通过 MCP 暴露出来的工具。建议分三段学。

阶段 A：上手，大概一两天

装好、登进去。了解 npm 安装和原生二进制两种方式，搞定认证，把基本命令摸熟：claude、claude -p（一次性执行）、claude -c（继续上次）、claude -r（恢复会话）。

权限模式其实是工作流。弄清楚每步确认、自动接受、计划模式这几种，是怎么控制 AI 自主程度的。想通这点会有种豁然开朗的感觉。

接上 Git。让它读 diff、写提交信息、做分支操作。

阶段 B：工程化，大概一周

把 CLAUDE.md 写好。把项目架构、技术栈、命令、代码规范、不能碰的地方写进项目根目录的 CLAUDE.md，每次会话自动加载。先写个精简版，跑两周再按需补。

优先用 Plan 模式。让它先出方案，你真的逐行读一遍再批准执行，别图省事回一句看起来不错就放行。

管好上下文。该压就用 /compact，该重开就 /clear，按 2.1 节那几个阈值来。

阶段 C：进阶，按需学

接 MCP。把 Figma Dev Mode MCP、Playwright、数据库这些按需接进来。前端尤其要接 Figma 和 Playwright。

用 Subagents 和 Skills。把重复套路沉淀成可复用的技能和子代理。但记住先确认真有这个需求再加，别过度工程。

搞自动化。用插件（比如 Playwright 插件）和脚本，把评审、测试、视觉回归都自动跑起来。

官方资源

Anthropic 有免费课程 Claude Code in Action（在 anthropic.skilljar.com）和最佳实践文档（code.claude.com/docs）。大多数人花 8 到 11 小时基础学习就能上手。

4.3 OpenAI Codex 学习路线

Codex（2026 版）是一个由 GPT-5.5 和 5.5 Pro 驱动的统一 Agent，终端、IDE、Web、读屏这几个界面共用同一套执行模型，周活跃开发者有几百万。它最擅长的是那种长时间没人盯着的自主任务。

装好、初始化。用 npm install -g @openai/codex 安装，运行 codex 初始化，拿 ChatGPT 账号或者 API Key 登录，选一个文件夹或 GitHub 仓库，Codex 会把代码库预载进沙盒。

怎么派活。给它一个明确任务，比如修复文件名含特殊字符时 /diff 报错。它会在隔离环境里跑测试和 linter，然后把摘要、diff、日志和改动文件还给你，你审完批准就能提 PR。

目标模式（Goal mode）。在 App、IDE 扩展、CLI 里都能用，让 Codex 朝一个目标自己推进几个小时，甚至几天。

Agent Skills。把常用流程封装成技能，配置写在 ～/.codex/config.toml 里。

前端怎么用它。把批量重构、升依赖、补测试、跨文件改样式这类机械又费时间的活，丢给它在后台跑。

4.4 Cursor 学习路线

Cursor 是专门为 AI 协作做的 VS Code 分支，从传统 IDE 过渡过来几乎无缝。如果你现在还离不开图形化编辑器，从它起步最舒服。

迁移没成本。界面跟 VS Code 基本一样，插件、快捷键、主题都能直接搬过来。

核心能力。Tab 智能补全、Cmd-K 行内编辑、Agent 或 Composer 做多文件改动、用 @ 引用文件、文档、符号当上下文。

Rules。用 .cursor/rules 固化项目规范，作用跟 CLAUDE.md 差不多。

2026 的新东西。3.3 版（2026 年 5 月）加了能存住的多步计划画布，还有会自己分诊并修 bug 的 Bugbot。

4.5 搭配着用

别纠结哪个最好。一个比较务实的搭配是这样的。

日常开发用 Cursor，手感顺、看得见。

架构级、深度多文件用 Claude Code，上下文大、token 省。

后台自动化、长任务用 Codex，不用人盯，能自己跑测试提 PR。

做设计还原任一个 Agent 加 Figma Dev Mode MCP 加 Playwright MCP，详见第五章。

4.6 一直用得上的几个技能

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="192" width="192" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>技能</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>为什么重要</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>怎么做</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>规则文件</span></span></div><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>(CLAUDE.md / AGENTS.md / .cursor/rules)</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>让每次会话自带项目背景，输出更一致</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>从精简版起步，慢慢沉淀架构、命令、规范、禁区</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="192" width="192" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>先看方案再放行</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>避免</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>跑偏，主导权留在你手里</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>认真读它的计划，别敷衍着同意</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>管理上下文</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>防止精度下降和胡编</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>按七成、八成五、九成这几个点</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> compact </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>或</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> clear</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="192" width="192" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>让它自我验证</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>这是提升完成质量最划算的一招</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把测试、截图、期望结果一起给它</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>接</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> MCP</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把外部工具和数据接进来</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>前端必接</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Playwright</span></span></div></td></tr></tbody></table>

  

第五章把设计稿精准还原成页面

让 AI 把设计稿或者截图高保真地还原成页面，是前端用得最多、也最容易翻车的需求。这一章给一套能照搬的方法，把还原从碰运气变成有把握的工程。

5.1 AI 为什么会还原翻车

先弄清楚为什么会失败，才好对症下药。

截图丢了太多信息。一张图里没有图层结构、间距规则、设计变量、组件层级，也没有响应式约束，AI 只能靠猜。

提示太含糊就会发散。一句"做个登录页"，会逼着 AI 替你做几十个你没说的决定，而且每次决定还不一样。

细节它看不准。自定义图标、图表、精细间距、字体度量，光靠眼睛看容易有偏差。

没有验证环节。没有对照和回看的机制，AI 自己也不知道差在哪。

5.2 一条原则：给结构化数据，别只给截图

最靠谱的还原路径，是让 AI 拿到设计的结构化事实，而不是一张像素图。

拿 Figma 当唯一标准。通过 Dev Mode MCP 让 AI 直接读节点树、布局约束、设计变量、组件映射，这些在截图里都看不见。

用 Code Connect 复用组件。让生成的代码去调项目里真实的组件和 token，别另起炉灶重写一套，从源头上保证一致。

跟设计 token 对齐。把颜色、间距、字号统一到 token 体系里，AI 出的东西自然就贴规范。

5.3 五源对齐

有个被实践验证过的高保真技巧：让 AI 交叉比对五个来源，五个都对上的时候，结果最接近像素级。

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="250" width="250" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>来源</span></span></div></td><td data-colwidth="442" width="442" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>作用</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>① </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计变量（</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>tokens</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>）</span></span></div></td><td data-colwidth="442" width="442" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>定下颜色、间距、字号、圆角的标准答案</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>② </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计元数据（节点和约束）</span></span></div></td><td data-colwidth="442" width="442" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>定下布局、层级、自动布局规则</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>③ </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计稿截图</span></span></div></td><td data-colwidth="442" width="442" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提供整体视觉参照</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>④ AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>生成的代码</span></span></div></td><td data-colwidth="442" width="442" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>待校验的实现</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>⑤ </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>实现渲染后的截图</span></span></div></td><td data-colwidth="442" width="442" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把实现拉回来跟前三个对</span></span></div></td></tr></tbody></table>

  

五个来源都对齐，基本就到像素级了。只要有一个对不上，就去定位差异、改掉、再比一遍。

5.4 视觉闭环：让 Playwright 帮你截图比对

这一步是把 AI 看不准变成 AI 能自查的关键。通过 Playwright MCP，Agent 可以自己开浏览器、点进页面、对每一页截图，再把实现截图和参照图放在几个视口下对比，自动改到视觉对上为止，全程不用你一张张手动对。

为什么管用。Anthropic 的最佳实践里说得很直接：让 Claude 能验证自己的工作，比如跑测试、对比截图、校验输出，是单点最划算的一招。

结构快照更省。Playwright MCP 能给出可访问性的结构快照，比直接发截图省 token，也更快更稳。

怎么落地。给 Claude Code 装上 Playwright 插件或者 MCP，让截图、对比参照、修改、再截图变成一个自动循环。

![[笔记同步助手/images/7b0bb39cf24877f85953ff05eb02ed68_MD5.png]]

精准还原的流水线：结构化数据负责对得准，视觉闭环负责改得对

5.5 高保真还原的提示词模板

下面这个模板按项目替换占位符就能用，完整版见附录 B。

还原任务提示词

角色：你是资深前端，目标是把指定的 Figma 帧一比一还原成生产级组件。

技术栈：React 加 TypeScript 加 Tailwind，复用 src/components 下已有的组件和 design tokens，别引入新依赖。

数据来源：优先用 Figma MCP 给的节点树、变量、组件映射，截图只当整体参照。

流程：先输出实现计划和组件拆分，等我确认；然后实现；再用 Playwright 在 375、768、1440 三个视口截图跟参照对比；最后列出差异并改到一致。

约束：移动端优先、语义化 HTML、可访问性达标、像素级对齐 token。拿不准的地方先问我，别自己瞎填。

5.6 还原质量检查清单

布局和间距：用的是设计 token 还是写死的数字？三档视口是不是都对？

颜色和字体：颜色、字号、行高、字重跟变量一致吗？深浅两种模式都覆盖了吗？

组件复用：调的是项目里现成的组件，还是又写了一套？

可访问性：语义标签、对比度、键盘可达、aria 属性都到位了吗？

交互状态：hover、active、disabled、loading、空态、错误态齐不齐？

资源：自定义图标、图片、图表用的是正确的资源，还是 AI 凑的近似品？

代码质量：lint、类型检查、测试过了吗？有没有重复样式？

5.7 从 Figma 到像素级：完整流程

把前面的方法串成一条能照着走的流水线。

第一步。在 Figma 里把变量和组件标好，配好 Code Connect，映射到代码里的组件。

第二步。在 Claude Code 或 Cursor 里接上 Figma Dev Mode MCP 和 Playwright MCP。

第三步。选中目标帧，用 5.5 的模板派活，先要计划再放行。

第四步。AI 读结构化数据生成代码，Playwright 多视口截图，按五源对齐校验，自动修正。

第五步。你照 5.6 的清单做人工终检，确认没问题再并进设计系统。

一句话心法

还原做得准，靠的是把猜测换成事实；改得对，靠的是把人工比对换成自动闭环。结构化数据负责对得准，视觉闭环负责改得对。

第六章完整学习路线规划

这一章给一条能照着走的成长路线，从会用 AI 工具，一直到能用 AI 做全栈、做 AI 应用。对有一年以上前端经验的人，整体大概 6 到 12 个月，看你投入多少、目标定多高。

6.1 总路线和时间

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="154" width="154" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>阶段</span></span></div></td><td data-colwidth="134" width="134" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>周期</span></span></div></td><td data-colwidth="211" width="211" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>目标</span></span></div></td><td data-colwidth="192" width="192" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>产出</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="154" width="154" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>阶段一</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> · </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>打基础</span></span></div></td><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 1 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 4 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>周</span></span></div></td><td data-colwidth="211" width="211" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工具用进日常前端工作</span></span></div></td><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>能用</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Cursor </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>或</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Claude Code </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>做功能、还原页面</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="154" width="154" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>阶段二</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> · </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工程化</span></span></div></td><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 2 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 4 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个月</span></span></div></td><td data-colwidth="211" width="211" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Agent </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工作流加上下文工程加自动化</span></span></div></td><td data-colwidth="192" width="192" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>CLAUDE.md</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、视觉闭环、可复用技能</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="154" width="154" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>阶段三</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> · </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>拓展</span></span></div></td><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 4 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 9 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个月</span></span></div></td><td data-colwidth="211" width="211" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>往全栈</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>应用走</span></span></div></td><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Python </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>加</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> LLM API</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>RAG</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Agent</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、作品集</span></span></div></td></tr></tbody></table>

  

![[笔记同步助手/images/928cbd56720ff23b1d58c564cd9e4cc6_MD5.png]]

前端转 AI 的学习时间轴，约 6–12 个月

6.2 阶段一：打基础

挑一个主力 Agent，建议先用 Cursor 过渡，再配一个 CLI（Claude Code），两边都跑通它改我审这个循环。

拿真实工单练手，让 AI 修 bug、加小功能、写测试，逼自己养成先看方案再放行的习惯。

把第二章的概念和提示词原则吃透，顺手建一个自己的提示词片段库。

完整做一次设计稿到页面的还原，用 Figma Dev Mode MCP 加截图闭环。

6.3 阶段二：工程化

给主力项目写 CLAUDE.md 或 .cursor/rules，把架构、命令、规范、禁区沉淀下来。

接 MCP：Figma、Playwright、数据库，把视觉回归、测试、评审都自动化。

练 vibe 加 spec 的混合打法，原型阶段快糙猛，定稿了写规格再实现。

再上第二个、第三个 Agent，形成日常、架构、后台的分工。

把重复套路沉淀成 Skills 或 Subagents，记得先确认需求真实再加。

6.4 阶段三：拓展

这一步能把你和只会前端的人拉开差距。好消息是前端经验在这里大量复用，异步、API、状态机都用得上。

Python 和基础（第 1 到 3 个月）。你已经会编程，这一步是学语法不是学概念，目标是把 Python 用熟。

LLM API 和提示词工程。直接调各家模型的 API，把函数调用、工具调用搞明白。

RAG（检索增强生成）。动手搭一个能用的检索问答系统。

Agent 框架。比如 LangGraph，骨子里是状态机，把你 Redux、Zustand 那套经验迁过来。

部署和作品集。把成果真正上线，攒下两三个能体现前端加 AI 组合的项目。

作品集怎么挑

挑能凸显你这个稀缺组合的：一个带 RAG 后端的流式聊天界面；一个带 React 仪表盘的 AI 代码评审工具；一个带实时可视化的多 Agent 系统。

6.5 技能树

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>层级</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>能力</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工具层</span></span></div></td><td data-colwidth="557" width="557" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Cursor</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Claude Code</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Codex</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>；</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma Dev Mode MCP</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Playwright MCP</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>方法层</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>提示词工程、上下文工程、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>vibe </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> spec </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>的取舍、视觉还原闭环</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工程层</span></span></div></td><td data-colwidth="557" width="557" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>规则文件、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>集成、自动化测试和视觉回归、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Skills </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Subagents</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>拓展层</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Python</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>LLM API</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>RAG</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Agent </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>框架、部署</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>软技能</span></span></div></td><td data-colwidth="557" width="557" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>拆需求、审方案、对</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>产出的判断和验收、团队协作</span></span></div></td></tr></tbody></table>

  

6.6 30、60、90 天计划

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>周期</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>重点</span></span></div></td><td data-colwidth="307" width="307" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>能交付的东西</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 1 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 30 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>天</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>让主力</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Agent </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>进日常，完整做一次设计还原</span></span></div></td><td data-colwidth="307" width="307" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>用</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>做完</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 5 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个以上真实工单，一个像素级还原的页面</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 31 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 60 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>天</span></span></div></td><td data-colwidth="250" width="250" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> CLAUDE.md</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、视觉闭环工程化</span></span></div></td><td data-colwidth="307" width="307" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>项目规则文件，接好</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Playwright</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，自动视觉回归</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>第</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 61 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>到</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 90 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>天</span></span></div></td><td data-colwidth="250" width="250" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>多</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Agent </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>分工，开始碰</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Python </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> LLM</span></span></div></td><td data-colwidth="307" width="307" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>沉淀</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> 3 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>个以上</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Skills</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，做完第一个</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> LLM API </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>小应用</span></span></div></td></tr></tbody></table>

  

6.7 资源清单

官方课程。Anthropic 的 Claude Code in Action（免费）、Introduction to MCP；OpenAI Codex 的官方文档和更新日志。

文档。code.claude.com/docs 的最佳实践、developers.figma.com 的 MCP 文档、modelcontextprotocol.io。

社区。GitHub 上的 Claude Code Ultimate Guide 这类开源学习仓库，还有 roadmap.sh 的 AI Engineer 路线。

动手项目。从把现有前端项目接上 AI 工作流开始，比光看教程有用得多。

第七章公司前端团队怎么转 AI Coding

个人会用 AI，和团队层面把 AI 变成稳定产能，是两码事。这一章写给带团队、或者要推动落地的人，讲方法、度量和治理。

7.1 团队转型难在哪

一致性。vibe coding 一个人写很爽，但多人协作时同一个需求出十种写法，技术债很快就堆起来了，大概三个月就会撞墙。

知识在脑子里。架构约定、规范、踩过的坑，没沉淀成 AI 能读的形式，AI 每次都得重新猜。

不敢规模化。团队担心 AI 产出的质量、安全和合规，没有验收闭环就不敢放开用。

工具各搞各的。每个人一套，缺统一的规则文件、MCP 配置和最佳实践。

7.2 DDAD：用文档驱动开发

2025 年逐渐成型的一种团队打法叫 DDAD，全称 Document-Driven AI Development，文档驱动的 AI 开发。核心是把最佳实践和约束写进 CLAUDE.md、RULES.md 这类文档里，让文档成为团队协作的底座。

转变在哪。开发者从写代码，转向打磨可执行的共识，更像是在指挥一支 AI 乐队。

收益。业界有实践报告说这种模式能明显提升交付效率，有的案例提到大概四成五。关键是把藏在人脑里的隐性知识变成显性的、AI 能复用的东西。

和 spec-driven 是一脉相承的。都是拿规格或文档当唯一标准，让上下文和底线跨会话、跨 Agent 都保持一致。

7.3 团队级的上下文工程

把第二章讲的上下文工程放大到团队规模，是转型的技术核心。

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="211" width="211" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>资产</span></span></div></td><td data-colwidth="288" width="288" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>内容</span></span></div></td><td data-colwidth="192" width="192" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>作用</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="211" width="211" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>CLAUDE.md / AGENTS.md / .cursor/rules</span></span></div></td><td data-colwidth="288" width="288" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>架构、技术栈、目录约定、命令、代码规范、禁区</span></span></div></td><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>每次会话自带团队背景，产出一致</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="211" width="211" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>RULES.md </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>或规范库</span></span></div></td><td data-colwidth="288" width="288" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>命名、提交、评审、安全红线</span></span></div></td><td data-colwidth="192" width="192" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>统一怎么做，少发散</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="211" width="211" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Skills </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>和模板</span></span></div></td><td data-colwidth="288" width="288" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把一个功能怎么标准化生产教给</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>，从领域建模到架构脚手架再到实现绑定</span></span></div></td><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>可复制的标准产能</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="211" width="211" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>配置</span></span></div></td><td data-colwidth="288" width="288" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>统一接</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Playwright</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、内部数据和服务</span></span></div></td><td data-colwidth="192" width="192" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>全员同一套能力，少踩坑</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="211" width="211" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计系统加</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Code Connect</span></span></div></td><td data-colwidth="288" width="288" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把设计映射到真实组件和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> token</span></span></div></td><td data-colwidth="192" width="192" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>还原时直接复用，保证一致</span></span></div></td></tr></tbody></table>

  

有些企业级工具（比如 Tabnine 的企业上下文引擎）会去学组织自己那套代码架构和规范，确保生成的代码符合内部的安全和合规要求。如果是自建，用上面这套文档体系加私有 MCP，也能做到类似效果。

![[笔记同步助手/images/2ea62e59a80965288579d32e4c6e4222_MD5.png]]

团队级上下文工程：把经验沉淀成 AI 能读的资产

7.4 落地四步

第一步，试点。找一个小而真实的项目，两三个意愿强的工程师，先写个精简的 CLAUDE.md，在真实生产里跑两周。

第二步，标准化。把试点里磨出来的规范、提示词、MCP 配置、还原流水线固化成团队资产。Skills 和 Subagents 等需求被验证了再加。

第三步，推广。做内部分享、结对，把规则文件和模板推到更多项目，再配一份 AI 工作流的内部文档和值班答疑。

第四步，度量和迭代。用指标验证收益，持续打磨文档和流程，具体看 7.5。

7.5 度量和 ROI

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>维度</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>可以看的指标</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>效率</span></span></div></td><td data-colwidth="557" width="557" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>需求交付周期、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>PR </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>合并时长、设计还原工时、每个任务的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> token </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>消耗</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>质量</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>缺陷率、视觉回归通过率、返工率、可访问性达标率</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>采纳</span></span></div></td><td data-colwidth="557" width="557" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>参与的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> PR </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>占比、活跃使用人数、规则文件覆盖了多少项目</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="134" width="134" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>体验</span></span></div></td><td data-colwidth="557" width="557" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工程师满意度、上手时间、重复劳动少了多少</span></span></div></td></tr></tbody></table>

  

一个提醒：先量出基线再推广，不然没法证明收益。第一批度量优先挑 AI 收益明显的前端活，比如设计还原、样式重构、补测试。

7.6 风险和治理

代码质量。把先看方案再放行、自动测试、视觉回归设成合并的硬门槛，AI 产出一样要走 code review。

安全合规。明确数据和密钥不进提示，私有代码用本地或企业版工具，敏感场景可以选本地优先的方案，比如 Open Design 那种自带密钥、本地运行的。

别堆技术债。约定不能随便加新依赖，要求复用现成的组件和 token。

可追溯。把规格、决策文档和变更记录都留好，受监管行业尤其要做到。

7.7 角色会怎么变

转型做得好的团队，工程师的价值会往上走：从亲手敲实现，转到定义意图和约束、设计上下文、审阅验收、把控架构和质量。前端不会消失，而是变成既懂体验、又能高效带着 AI 干活的人。这正好是稀缺、也值钱的位置。

第八章一个端到端的实战案例

用一个例子把前面的方法串起来：把一个 Figma 营销落地页做成生产组件。假设技术栈是 React 加 TypeScript 加 Tailwind，已经有现成的设计系统。

场景和目标

设计师交来一个 Figma 文件，里面有 Hero、特性卡片、价格表、FAQ 和页脚。要求是像素级还原、复用现有组件、三档视口自适应、可访问性达标，并且一个工作日内交出能评审的 PR。

一步步怎么走

① 准备上下文。确认 CLAUDE.md 里写清了技术栈和组件库路径，在 Figma 里配好变量和 Code Connect 映射。

② 接工具。在 Claude Code 里接上 Figma Dev Mode MCP 和 Playwright MCP。

③ 先探索。让 AI 先生成整页草稿，快速判断组件拆分合不合理。

④ 再固化。把组件拆分、命名、交互状态写成一份简短规格，当作这次实现的标准。

⑤ 实现加闭环。选中各帧，照第五章的模板派活。AI 读结构化数据生成代码，Playwright 在 375、768、1440 截图，按五源对齐校验，自动改。

⑥ 终检。照 5.6 的清单人工复核可访问性、状态、资源、代码质量，跑 lint、类型、测试。

⑦ 交付。提 PR，CI 跑视觉回归当合并门槛，评审过了再并进设计系统。

![[笔记同步助手/images/43d09f739a753d23705824eaf360d4a0_MD5.png]]

端到端实战：从 Figma 到上线的七步

为什么这么做能成

结构化数据保证对得准，视觉闭环保证改得对，规则文件保证风格一致，自动门槛保证质量可控。

整个过程你都在当指挥：定意图、设边界、审方案、验结果。这也正是转型之后的主要工作形态。

附录 A 名词表

<table style="border-collapse: collapse"><tbody><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>术语</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(46, 94, 140); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-weight: bold; color: rgb(255, 255, 255); font-size: 13px"><span>解释</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Agent / </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>智能体</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>能自己读写文件、跑命令、调工具、做验证的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>程序</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>MCP</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>模型上下文协议，</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>接外部工具和数据的统一标准</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Dev Mode</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>给开发者用的模式，提供测量、变量、代码和</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> MCP</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Code Connect</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>把</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> Figma </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>组件对应到代码仓库里真实组件的能力</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Design-as-Code</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>设计即代码，用结构化文件描述设计，比如</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> .pen</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>、</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>DESIGN.md</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>HyperFrames</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Open Design </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>的可交互故事板，能在画布里嵌真实</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> HTML</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Critique Theater</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Open Design </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>的自动设计评审，多个评委打分，</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>8 </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>分以上才放行</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>BYOK</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>自带模型密钥，不绑定单一厂商</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Vibe Coding</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>凭感觉、靠提示快速生成和迭代</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>Spec-Driven</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>以机器可读规格为唯一标准的工程化开发</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>上下文工程</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>经营</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>工作环境，包括规则、文档、工具、记忆</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>DDAD</span></span></div></td><td data-colwidth="509" width="509" style="background-color: rgb(238, 243, 248); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>文档驱动的</span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span> AI </span></span><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>开发，团队落地的一种打法</span></span></div></td></tr><tr style="text-align: center"><td data-colwidth="182" width="182" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>RAG</span></span></div></td><td data-colwidth="509" width="509" style="border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span style="font-size: 13px; color: rgb(0, 0, 0)"><span>检索增强生成，给模型外接一个知识库</span></span></div></td></tr></tbody></table>

  

附录 B 提示词模板

B1 设计稿高保真还原

模板

你是资深前端。把选中的 Figma 帧一比一还原成生产级组件。技术栈是 React 加 TypeScript 加 Tailwind，复用 src/components 和 design tokens，别加新依赖。

优先用 Figma MCP 给的节点树、变量、组件映射，截图只当整体参照。先输出组件拆分和实现计划，等我确认；实现后用 Playwright 在 375、768、1440 截图跟参照对比，列出差异改到一致。要移动端优先、语义化、可访问性达标。

B2 重构现有页面、还技术债

模板

在不改变视觉和行为的前提下重构这个组件：把重复样式抽成 token、去掉写死的数字、补齐类型和交互状态。先给重构计划和风险点，等我确认；改完跑 lint、类型、测试，再附上 diff 摘要。

B3 补测试和视觉回归

模板

给这个组件补单测和 Playwright 视觉回归用例，覆盖空态、加载、错误、禁用这些状态和三档视口。先列测试清单，确认后再实现，保证全部通过。

B4 项目规则文件骨架

CLAUDE.md 精简骨架

项目概述：一句话说清产品和技术栈，比如 React 加 TypeScript 加 Tailwind。

目录和约定：关键目录、组件库路径、命名规范。

常用命令：安装、启动、测试、构建、lint。

代码规范：风格、提交规范、优先复用、别随便加依赖。

禁区：不能改的目录和文件、安全红线，比如密钥不进提示。

验收：合并前必须过 lint、类型、测试、视觉回归。

---

![[笔记同步助手/images/3591480644c2c3f26af478afe7ab3305_MD5.jpg|cover_image]]

Original Excellent 优码云AI

修改于

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/78eecdad_1779761107116?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzYzMzkwNjU1OQ%3D%3D%26mid%3D2247485018%26idx%3D1%26sn%3D4be4222b824e42b2cf1d47b96c23e4d1%26chksm%3Df14333808baf745466056c6a1935b887bd7fe68591dea8f8847f439af9257811e4e2a8e66193%26mpshare%3D1%26scene%3D1%26srcid%3D0526Ke7e166CO4xIuAABZtsQ%26sharer_shareinfo%3Dbb425fb7d01cc8ec890e3f6d75eeb3a5%26sharer_shareinfo_first%3Dbb425fb7d01cc8ec890e3f6d75eeb3a5%23rd&s=obsidian)