---
title: "Hermes Agent 最详细的入门教程（上篇）"
source: "https://x.com/XiaohuiAI666/status/2046564780027396150"
author:
  - "[[@XiaohuiAI666]]"
published: 2026-04-21
created: 2026-04-23
description: "大家好，我是程序员小灰。不知道有谁还记得，今年第一季度爆火的小龙虾（OpenClaw）项目？不可否认，小龙虾依然是一款强大的智能体工具，但由于存在种种弊端，它最终淡出了多数人的视野。就在这个时候，有一个全新的AI智能体框架在AI圈爆火了，这个AI智能体框架名为Hermes Age..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HGZwXUlakAAGyWf?format=jpg&name=large)

大家好，我是程序员小灰。

不知道有谁还记得，今年第一季度爆火的小龙虾（OpenClaw）项目？

不可否认，小龙虾依然是一款强大的智能体工具，但由于存在种种弊端，它最终淡出了多数人的视野。

就在这个时候，有一个全新的AI智能体框架在AI圈爆火了，这个AI智能体框架名为**Hermes Agent**，被国内玩家称为“爱马仕”。

![图像](https://pbs.twimg.com/media/HGZtpjobwAAlDXP?format=jpg&name=large)

许多人在后台问小灰，能不能出一篇关于Hermes Agent的教程，于是经过三天三夜的奋战，终于有了这篇长达7000字的教程。

建议大家先收藏、不迷路。

## 一、什么是Hermes？什么是Hermes Agent？

**1.什么是Hermes？**

在学习Hermes Agent之前，我们先来了解一下Hermes到底是什么。

**Hermes是一个AI大模型，由开源模型圈大名鼎鼎的实验室 Nous Research 所开发。**

它的名字取自希腊神话中的众神使者赫尔墨斯，背后的寓意是“信息的传递者”。

**2\. 什么是Hermes Agent？**

说完了Hermes，那Hermes Agent又是什么呢？

**Hermes Agent是Nous Research基于Hermes模型，研发的一套AI智能体框架。**

你可能用过 Cursor、Copilot 这类 AI 编程助手，也用过 ChatGPT、Claude 这种聊天机器人。但它们都有个共同的硬伤：**关掉窗口，它们就停工了。** 你想让 AI 半夜帮你跑个脚本？不行，你得自己开着电脑。

然而Hermes Agent不一样。它不是一个插件，也不是一个网页，它是一个**部署在你服务器上的 AI 分身。**

它可以实现 7x24 小时待命，你随时通过飞书、微信给它下指令，它帮你跑脚本、查日志、处理数据，然后把结果发回。

**3\. Hermes Agent 适合哪些人？**

那么，Hermes Agent适合哪些人来使用呢？目前该工具主要适合下面这四类人。

**独立开发者：**

让 Hermes 在服务器上 24 小时待命，随时通过 Telegram 下达任务。跑脚本、查日志、处理数据，不用开电脑。

**小团队：**

通过 飞书/微信 共享一个 Hermes Agent，处理运维监控、自动化任务，一人配置全员可用。

**自动化爱好者：**

用 cron 定时执行任务，用消息网关接收结果通知。比如每天早上自动生成市场日报，推送到微信。

**重视隐私的用户：**

完全本地部署，数据不离开你的服务器。可以选择本地模型，不依赖任何云端服务。

## 二、Hermes Agent与 OpenClaw 的区别

说完了Hermes Agent 的基本概念，或许会有朋友问：“Hermes Agent 和OpenClaw的作用听起来似乎差不多？两者到底有什么不同呢？”

**1\. 记忆：小龙虾像金鱼，爱马仕像老友**

龙虾每次新对话就像失忆，你上周刚说过「用 Python 3.11」，今天它又给你写 3.12，你得反复教。Hermes Agent 会把你的偏好永久记下来，重启也不会忘，甚至能回忆起几周前你们讨论过的方案细节。

**2.技能：小龙虾靠手动装，爱马仕靠自己学**

龙虾的技能生态丰富，但每个都要自己找、自己装、自己配，折腾半天。Hermes 走了另一条路——它干完一个复杂活，会在后台自动复盘，把解决过程提炼成一个可复用的技能文件，下次遇到类似任务直接调用。

比如它帮你调了一个 Bug，下次遇到同类 Bug 直接按套路来，不用你再教。你当然也可以主动让它存技能：“把刚才的数据清洗流程保存为 Skill”。

**3.隐私：小龙虾过云端，爱马仕守本地**

龙虾的不少 Skill 依赖第三方云端，你的数据要过别人的服务器。Hermes 完全跑在你自己的机器上，想用本地模型也行，数据一步都不出去。

**4.安全审批：小龙虾看不懂，爱马仕更聪明**

龙虾的授权弹窗经常是一串不明所以的数字和路径，你不清楚它到底要干什么，只能无脑批准。Hermes Agent 会智能判断指令风险等级，高危操作主动预警，低风险操作静默通过，审批体验更省心。

Hermes Agent与OpenClaw的异同，可以归纳为下面这张表：

![图像](https://pbs.twimg.com/media/HGZt8hybQAAYs_J?format=jpg&name=large)

总之，我们可以把小龙虾理解为**“**你问它答”的工具箱，是一只勤奋的“打工虾”；而爱马仕则是“教一次、记一辈子”的聪明员工，也是你的专属分身。

很多人现在两者并用，小龙虾负责执行（现成 Skill 多），爱马仕当大脑（越来越懂你）。

如果你之前养过虾，那么这里有一个好消息：借助下面的指令一键导入小龙虾的记忆、Skill、配置、API Key，可以让爱马仕实现“无痛迁移”。

```text
hermes claw migrate
```

## 三、准备篇：安装前需要什么

**1\. 系统要求**

Hermes Agent 支持以下环境：

- Linux
- macOS
- Windows （官方建议安装 WSL2）
- Android / Termux（这个后面再说，先把PC端的玩明白）

注意：Windows 环境目前问题还比较多，如果你用的是 Windows，建议安装 WSL2（Windows Subsystem for Linux）。安装方法很简单，在 PowerShell 里运行：

```text
wsl --install
```

重启电脑后，你就有了一个 Linux 环境。

安装 Hermes Agent 前只需要一个前提条件：**Git。**大多数系统已经自带了，如果没有，用以下命令安装：

```text
# Linux/WSL2
sudo apt install git

# macOS
brew install git

# Windows
# 官网下载：https://git-scm.com/download/win
# 全部默认，一路 Next。
```

**2\. 你需要准备的东西**

开始安装前，准备好以下材料：

**一台可以运行的电脑：**可以是你的本地电脑，也可以是一台云服务器/VPS。如果你想要 7x24小时待命，建议用服务器部署。

**API Key：**大模型API Key。推荐看我之前的一篇大模型白嫖指南，有大量免费模型可用，白嫖入门最方便。

**飞书/微信：**在 飞书 或 微信 里和 Hermes Agent 聊天，需要申请一个 Bot。

## 四、安装篇：一条命令搞定

**1\. 一键安装命令**

Hermes Agent 提供了自动安装脚本，会帮你搞定所有依赖（uv、Python 、Node.js 、ripgrep、ffmpeg），你只需要运行一条命令。

**Mac / Linux / WSL2 环境：**

打开终端，输入以下命令后回车：

curl -fsSL [https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh](https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh) | bash

![图像](https://pbs.twimg.com/media/HGZudXObEAATTtD?format=jpg&name=large)

注意：由于网络问题，有可能下载到99%的时候就失败了，别灰心，可以多重试几次。

![图像](https://pbs.twimg.com/media/HGbNq_FaoAAcHid?format=png&name=large)

根据我的测试，在国内的网络环境下，耗时最长可能在2-3个小时。

![图像](https://pbs.twimg.com/media/HGbUzXLaUAEdX_0?format=png&name=large)

看到这种界面你就离成功不远了！

![图像](https://pbs.twimg.com/media/HGbU4CKaMAAxYwV?format=png&name=large)

到这儿，你就成功了！！！

**Windows PowerShell 环境**（如果你坚持用原生 Windows）：

```text
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex

# 或者下载脚本后执行
.\install.ps1 -NoVenv -SkipSetup
```

耐心等待（愚公移山那种耐心），脚本会自动下载并安装所有依赖：

![图像](https://pbs.twimg.com/media/HGbVA0IaIAA5yZ4?format=png&name=large)

整个过程大概几十分钟吧，取决于你的网络速度。

![图像](https://pbs.twimg.com/media/HGbVEr8aUAAimAm?format=png&name=large)

到这里基本上就已经安装成功了。

![图像](https://pbs.twimg.com/media/HGbVH7QbsAA7zj0?format=png&name=large)

**2\. 安装后操作**

如果发现hermes命令无效，可以使用下面方法。

重新加载一下 shell 配置，让 hermes 命令生效：

```text
source ~/.bashrc    # 如果你用的是 bash

source ~/.zshrc     # 如果你用的是 zsh
```

然后验证一下安装是否成功：

```text
hermes version
```

如果看到版本号输出，说明安装成功。

**3\. 手动安装方式（可选）**

如果你想自己控制安装过程，或者想固定某个版本，可以用手动安装，手动安装之前需要安装好**Python 3.11** 和 **Node.js v22**

```text
# 克隆项目
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git

# 如果发现自己文件夹内容少了
git submodule update --init --recursive

# 然后进入目录
cd hermes-agent
```

![图像](https://pbs.twimg.com/media/HGbViNObgAAwERf?format=png&name=large)

```text
# 安装核心组件pip install -e "."
```

![图像](https://pbs.twimg.com/media/HGbVwera0AAesN6?format=jpg&name=large)

安装完成后执行 hermes version，验证是否安装成功

![图像](https://pbs.twimg.com/media/HGbV2HDbcAA6Xw8?format=png&name=large)

手动安装和自动安装的用法完全一样，适合想改源码或研究内部实现的同学。

## 五、配置篇：第一次启动

**1\. 运行配置向导**

安装好后，一般会自动弹出配置向导，如没有出现可以执行下面命令，它会一步步带你完成所有设置：

```text
hermes setup
```

你会看到一个交互式界面，有几个选项：

![图像](https://pbs.twimg.com/media/HGbWAuvaEAAt7xG?format=png&name=large)

选择 **Quick setup，**这是最简单的配置方式。

**2\. 选择模型提供商**

![图像](https://pbs.twimg.com/media/HGbWLNoaYAEXEBQ?format=png&name=large)

我还是比较钟爱智谱，选择[Z.AI](https://z.ai/)**，**然后填入API Key

![图像](https://pbs.twimg.com/media/HGbaSO2aUAAe6pD?format=png&name=large)

注意，这里有个坑，粘贴 Key 后不会显示任何内容，也不会提示；我之前就是以为没粘贴进去在这捣鼓半天......

**3\. 选择默认模型**

智谱免费赠送的 Token，一般仅适用于 glm-4.5-air 模型。

![图像](https://pbs.twimg.com/media/HGbaZClbwAAn6Dt?format=png&name=large)

**4\. 配置消息平台（可选）**

![图像](https://pbs.twimg.com/media/HGbadIvbsAAYIHD?format=png&name=large)

选择 **Set up messaging now，**然后选择你要接入的平台（比如 feishu）：

![图像](https://pbs.twimg.com/media/HGbaoOIb0AAuyq9?format=png&name=large)

选择扫码创建机器人：

![图像](https://pbs.twimg.com/media/HGbasl9bYAAGU1b?format=png&name=large)

扫码：

![图像](https://pbs.twimg.com/media/HGbavm4bEAAtu8L?format=png&name=large)

可以选择创建新的机器人，也可以选择之前玩龙虾的时候创建的机器人。

接下来配置 **authorized**，选择**Allow all direct messages：**

![图像](https://pbs.twimg.com/media/HGba3XHaAAAgqyJ?format=png&name=large)

保持默认配置：

![图像](https://pbs.twimg.com/media/HGba6gGaQAAUI2A?format=png&name=large)

这里直接回车就行：

![图像](https://pbs.twimg.com/media/HGba9Zwa8AAFz8j?format=png&name=large)

开启服务，输入**Y：**

![图像](https://pbs.twimg.com/media/HGbbAbKa8AAvq9v?format=png&name=large)

还是输入**Y，**开启对话：

![图像](https://pbs.twimg.com/media/HGbbVcNagAAVvuD?format=jpg&name=large)

如此一来，Hermes Agent 的配置工作完成了，下一步就是正式启动。

由于X的篇幅所限，Hermes Agent 的启动操作、使用技巧、进阶技术和常见问题，我们将在教程的下篇为大家详细讲解，敬请期待~~

也欢迎大家关注我 [@XiaohuiAI666](https://x.com/@XiaohuiAI666) ，学习更多有用的AI和副业经验。