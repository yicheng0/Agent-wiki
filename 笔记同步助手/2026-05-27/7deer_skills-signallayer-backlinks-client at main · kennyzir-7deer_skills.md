---
author: unknown
source: GitHub
url: https://github.com/kennyzir/7deer_skills/tree/main/signallayer-backlinks-client
saved: 2026-05-27 20:51:32
tags:
  - 笔记同步助手
id: 70fd7679-9fce-414f-a22d-e6e1beb22918
---

> 通过 SignalLayer.io API 为任意网站创建外链投放 campaign，支持 drip/instant 两种速度模式。

## 功能

[](#功能)

-   ✅ **创建外链 campaign** - 只需提供网站 URL 和关键词
-   ✅ **查询状态** - 实时查看投放进度
-   ✅ **自动记录** - 所有 campaign 历史自动保存
-   ✅ **用户独立配置** - 每个用户使用自己的 API Key

## 快速开始

[](#快速开始)

### 1\. 安装

[](#1-安装)

将

signallayer-backlinks-client

文件夹复制到你的 OpenClaw skills 目录：

～/.openclaw/skills/signallayer-backlinks-client/

或在项目目录：

.your-project/.agent/skills/signallayer-backlinks-client/

### 2\. 配置 API Key

[](#2-配置-api-key)

(在这里SignalLayer.io ，配置key,无需充值，每天免费发50条)

告诉你的 Agent：

我的 SignalLayer API Key 是 sl\_xxxxxxxxxxxxxxxx

Agent 会自动保存到

memory/signallayer-api-user.md

### 3\. 创建外链 Campaign

[](#3-创建外链-campaign)

告诉你的 Agent：

给 https://example.com 发 200 条外链

## 工作流程

[](#工作流程)

用户请求 → Agent 读取 memory 中的 API Key → 调用 SignalLayer.io API → 创建 campaign → 记录到 memory → 向用户报告

## 参数说明

[](#参数说明)

| 参数 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| target\_url | 是 | \- | 目标网站 URL |
| brand | 是 | \- | 品牌名称 |
| keywords | 是 | \- | SEO 关键词 |
| quantity | 否 | 200 | 外链数量 |
| strategy | 否 | safety | safety(安全) / aggressive(激进) |
| speed | 否 | drip | drip(14天分批) / instant(即时) |

## 示例命令

[](#示例命令)

\# 基础用法
"给 openguessr.org 发 200 条外链"

\# 指定数量
"用 SignalLayer 投 500 条外链到 example.com"

\# 查看状态
"查看 SignalLayer 任务状态"

\# 配置 API Key
"我的 SignalLayer API Key 是 sl\_xxx"

## 获取 SignalLayer API Key

[](#获取-signallayer-api-key)

1.  访问 [https://app.signallayer.io](https://app.signallayer.io/)
2.  注册/登录账户
3.  在 Dashboard 获取 API Key

## 文件结构

[](#文件结构)

signallayer-backlinks-client/
├── SKILL.md                      # Skill 定义和工作流
├── SETUP.md                      # 安装配置指南
├── README.md                     # 本文件
├── scripts/
│   └── signallayer\_client.py     # 独立运行脚本
└── references/
    └── api.md                   # API 文档

## 独立脚本使用

[](#独立脚本使用)

不通过 Agent，也可以直接运行 Python 脚本：

# 配置 API Key
python scripts/signallayer\_client.py --configure

# 创建 campaign
python scripts/signallayer\_client.py \\
  --target "https://example.com" \\
  --brand "Example Brand" \\
  --keywords "keyword1,keyword2" \\
  --quantity 200

# 查询状态
python scripts/signallayer\_client.py --status "campaign\_id"

## 适用场景

[](#适用场景)

-   **SEO 外链建设** - 快速为网站建立高质量外链
-   **游戏站点推广** - 为游戏工具站创建外链矩阵
-   **内容网站** - 提升网站权重和搜索排名

## 相关技能

[](#相关技能)

本技能库中还有其他外链相关技能：

-   backlink-discovery
    
    \- 外链机会发现
-   backlink-intelligence
    
    \- 外链情报收集
-   seo-backlink-submitter
    
    \- 批量目录提交
-   seo-link-strategy
    
    \- 外链策略生成

## License

[](#license)

MIT

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/19c369cc_1779886291507?u=https%3A%2F%2Fgithub.com%2Fkennyzir%2F7deer_skills%2Ftree%2Fmain%2Fsignallayer-backlinks-client&s=obsidian)