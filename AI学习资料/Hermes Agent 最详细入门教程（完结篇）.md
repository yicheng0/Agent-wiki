---
title: "Hermes Agent 最详细入门教程（完结篇）"
source: "https://x.com/XiaohuiAI666/status/2047175631277011181"
author:
  - "[[@XiaohuiAI666]]"
published: 2026-04-23
created: 2026-04-23
description: "大家好，我是程序员小灰。前两天我发布了《 Hermes Agent 最详细入门教程》的上篇内容，里面介绍了 Hermes Agent 的基本概念、与OpenClaw的对比、下载安装方法、配置方法等等。具体内容我放在了文末的链接当中。这一次我们书接上文，讲一讲 Hermes Age..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HGj9-IqaMAAM3Ns?format=jpg&name=large)

大家好，我是程序员小灰。

前两天我发布了《 Hermes Agent 最详细入门教程》的上篇内容，里面介绍了 Hermes Agent 的基本概念、与OpenClaw的对比、下载安装方法、配置方法等等。

具体内容我放在了文末的链接当中。

这一次我们书接上文，讲一讲 Hermes Agent 的启动方法、使用技巧、进阶应用、常见问题。

## 六、启动篇：验证安装成功

**1\. 启动 Hermes Agent**

配置完成后，直接运行下面命令就可以打开聊天界面：

```text
hermes
```

你会看到 Hermes Agent的欢迎界面：

![图像](https://pbs.twimg.com/media/HGj_QqNaoAARrXr?format=jpg&name=large)

这说明一切正常，Hermes Agent已经在运行了。

你现在可以在终端里和它对话了。

如果你想继续上次的对话，可以用：

```text
hermes -c
```

这会加载上次会话的上下文，保持记忆连贯。

**2\. 验证安装**

Hermes Agent 提供了诊断命令：

```text
hermes doctor
```

这会做一个全面健康检查，检查配置、依赖、连接等是否正常。如果没有明显报错，说明安装成功。

```text
hermes version
```

查看当前版本号。

**3\. 测试飞书**

打开飞书，找到你的机器人，发一条消息：

![图像](https://pbs.twimg.com/media/HGj_q-3a8AA3lVR?format=jpg&name=large)

如果收到回复，说明消息网关工作正常。现在你可以从任何地方远程指挥 Hermes 干活了。

## 七、基础使用篇

**1\. Web UI**

在终端输入hermes dashboard就可以打开Web UI

![图像](https://pbs.twimg.com/media/HGkAKndbEAAfIIg?format=png&name=large)

不过我不太建议使用，官方 UI 体验较差。

![图像](https://pbs.twimg.com/media/HGkANXlbIAAM6Ta?format=jpg&name=large)

这里我推荐一个还比较好看的Web UI

![图像](https://pbs.twimg.com/media/HGkAjOxbgAA42Yo?format=jpg&name=large)

**安装步骤：**

```text
# 第一种方式
npm install -g hermes-web-ui

# 第二种方式
bash <(curl -fsSL https://cdn.jsdelivr.net/gh/EKKOLearnAI/hermes-web-ui@main/scripts/setup.sh)

# 启动
hermes-web-ui start
```

![图像](https://pbs.twimg.com/media/HGkA2WYboAA0DBu?format=jpg&name=large)

复制日志中的URL链接到浏览器即可打开。

**注意：** 这里可能会有一个坑，就是你安装完成后，输入hermes-web-ui start它会提示hermes-web-ui：未找到命令，这是因为环境变量未配置好，采用如下方式可以修复：

```text
# 找到npm路径
NPM_BIN=$(npm config get prefix)/bin

# 配置环境变量
echo "export PATH=$NPM_BIN:\$PATH" >> /root/.bashrc

# 激活配置
source /root/.bashrc
```

Github地址：[https://github.com/EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui)

**相关命令速查表**

![图像](https://pbs.twimg.com/media/HGkBBpPbQAAjzpk?format=png&name=large)

**2\. 核心命令一览**

![图像](https://pbs.twimg.com/media/HGkBIdobAAArXT4?format=png&name=large)

**3\. 对话界面内的斜杠命令**

进入对话后，输入 / 可以看到所有可用命令：

![图像](https://pbs.twimg.com/media/HGkBM1Ya0AA4oJF?format=jpg&name=large)

常用命令包括：

- /help：查看帮助
- /skills：查看技能列表
- /model：切换模型
- /clear：清空当前对话

**4\. 多行输入与中断任务**

**多行输入：**按 Ctrl+Enter 可以换行，输入多行内容。

**中断任务：**如果 Hermes Agent 正在执行一个任务，你想让它停下来，直接输入新消息按回车就行，它会中断当前任务响应你的新输入。

## 八、进阶篇：让它更懂你

**1\. 灵魂定义（SOUL.md）**

默认的 Hermes Agent 是一个通用 AI 助手，你可以通过 SOUL.md 文件定义它的"人格"，让它更符合你的喜好。

SOUL.md 的位置：~/.hermes/SOUL.md

这是一个纯文本文件，你可以直接编辑。示例模板：

```text
---
name: 务实工程师
---

# 思考模式
- 先验证后回答：不确定的事先查工具确认，不靠猜测
- 先计划后执行：复杂任务先列方案，确认再动手
- 交付即验证：做完一件事，主动给出验证方法

# 输出风格
- 结论先行，代码为主，少废话
- 高危操作必须预警

# 避免
- 谄媚
- 炒作用语
```

你可以让 Hermes Agent 帮你写 SOUL.md：

```text
帮我编辑 ~/.hermes/SOUL.md，定义你的风格：直接高效、不说废话、敢于反驳
```

或者让他从你的龙虾里面提取：

![图像](https://pbs.twimg.com/media/HGkBc_iacAA1alv?format=jpg&name=large)

**2\. 记忆系统简介**

Hermes Agent 的记忆系统有三层：

**第一层：内置记忆（默认开启）**

- MEMORY.md：Agent 的工作笔记，记录环境事实、项目惯例、踩过的坑
- USER.md：你的画像，记录偏好、沟通风格、工作习惯

这两个文件在每次会话开始时会自动注入到上下文，确保 Agent "认识你"。

**第二层：历史会话搜索**

所有历史对话都保存在 SQLite 数据库里，支持全文搜索。当 Agent 需要回忆几周前的讨论，它会搜索历史记录，精准找回相关内容。

```text
~/.hermes/state.db (SQLite) 
    ├── sessions — 会话元数据、Token 统计、计费信息 
    ├── messages — 单会话完整消息历史记录 
    ├── messages_fts — 用于全文检索的 FTS5 虚拟表 
    └── schema_version — 单行表，用于跟踪数据库迁移版本
```

**第三层：外部记忆插件（可选）**

支持 Mem0、Supermemory 等外部记忆服务，提供更强大的语义搜索和知识图谱能力。

**怎么让 Hermes Agent 记住你的偏好？**

直接明确告诉它：

```text
记住我的偏好：所有 Python 代码统一用 Python 3.11，不要用 
Python 3.12
```

这样更容易触发记忆写入。你也可以主动请求：

```text
把这个偏好写入你的长期记忆
```

**3\. 技能自我进化**

```text
hermes skills list
```

这是 Hermes Agent 最有想象力的设计。

当 Hermes Agent 完成一个复杂任务（比如调试一个 bug、搭建一个工作流），它会把解决过程提炼成一个可复用的技能文件，保存在 ~/.hermes/skills/ 目录。

下次遇到类似问题，它会直接调用这个技能，不用从头摸索。

你也可以主动引导它创建技能：

```text
把刚才的数据处理流程保存为一个 Skill，命名为 data-pipeline
```

查看已有的技能：

```text
hermes skills list
```

或者在对话里输入 /skills。

## 九、常见问题与排错

**1\. API Key 配置问题**

解决方案：打开 ~/.hermes/.env 文件，检查里面的 API Key 是否正确。如果有多余字符或格式问题，手动修正。

**2\. 飞书发消息无响应**

最常见的原因就是下图中没有选择Allow all direct messages

![图像](https://pbs.twimg.com/media/HGkFrP6aEAApchr?format=png&name=large)

解决方案：将~/.hermes/.env里面的属性 FEISHU\_ALLOW\_ALL\_USERS设置为true

![图像](https://pbs.twimg.com/media/HGkFv0Aa8AAxi1h?format=png&name=large)

**3\. 输入 hermes 提示命令找不到**

shell 配置没有加载

解决方案：

source ~/.bashrc # 或  source ~/.zshrc

如果还是不行，检查 Hermes Agent 是否正确安装在 PATH 里。

**4\. 输入内容填写错误想删除，却发现无法删除？**

![图像](https://pbs.twimg.com/media/HGkGKRNbsAAhqmZ?format=png&name=large)

这也是一个坑，我被坑的次数最多，是因为键盘不兼容引起的，按ctrl + del就可以删除了

## 十、写在最后

好了，以上我们介绍了 Hermes Agent 的基本概念、安装方式以及使用技巧。

这篇文章比较长，建议大家收藏下来，一步一步进行实操，慢慢消化吸收。

同时，如果大家希望对 Hermes Agent 有更深入的了解，也推荐大家看一看 Hermes Agent 的官方文档、Github源码，以及技能市场。

**官方文档：**

[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)

**GitHub 仓库：**

[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**技能市场：**

[hermes-agent.nousresearch.com/docs/skills](https://hermes-agent.nousresearch.com/docs/skills)

现如今，AI已经彻底颠覆了我们的工作和生活方式，希望大家都能把这款强大的AI工具用起来，一起抓住AI时代的红利！

也欢迎大家关注我 [@XiaohuiAI666](https://x.com/@XiaohuiAI666) ，学习更多有用的AI和副业经验。

没看过《Hermes Agent 最详细入门教程（上篇）》的朋友，可以点击这里阅读上篇内容：

[https://x.com/XiaohuiAI666/status/2046564780027396150](https://x.com/XiaohuiAI666/status/2046564780027396150)