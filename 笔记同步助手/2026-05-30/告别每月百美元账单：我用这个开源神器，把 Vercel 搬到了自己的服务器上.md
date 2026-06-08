---
author: Rollkey
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2MDYxOTkxMA==&mid=2247485192&idx=2&sn=cacfb2e710365faa1079a2d38baa9fe8&chksm=cf9ae47950d3803eacb311db06de5ae1b10d70bbb6210f494074034394ef46f34d668c031bff&mpshare=1&scene=1&srcid=05305HhTGUev08jNEbtfYiN4&sharer_shareinfo=2c80d741aaeffccd0f331078645c86ab&sharer_shareinfo_first=2c80d741aaeffccd0f331078645c86ab#rd
saved: 2026-05-30 11:54:25
tags:
  - 笔记同步助手
id: dac13e1f-e1a0-4c86-8313-06369e32a697
---

公众号名称：小学生意气用事

作者名称：Rollkey

发布时间：2026-05-30 07:00

![[笔记同步助手/images/6d927933b283e1d917cc626852648405_MD5.png]]

  

> 每次收到云平台账单，你是否也会心里一紧？ 流量超了，钱；函数调用多了，钱；项目多了，还是钱。 今天介绍的这个工具，能让你用 **每月不到 30 元** 的服务器，跑出同款体验。

---

## 从一个真实场景说起

想象一下这样的开发者日常：

你有几个独立项目，分别部署在 Vercel 和 Railway 上。某天月底打开账单，发现光这两个平台合计要 \*\*$80+\*\*，而这些项目的流量并不大。

这时你开始琢磨：明明买了一台 VPS 才 $6/月，为什么我还要给平台交这么多"智商税"？

**Coolify**，就是这个问题的答案。

---

## Coolify 是什么？

**Coolify** 是一个 **开源、免费、可自托管的 PaaS 平台**，你可以把它理解为：

> 把 Vercel + Heroku + Netlify 的体验，搬到你自己买的服务器上。

它托管在 GitHub，目前已超过 **55,000 Star**，是增长最快的基础设施工具之一。

```
GitHub 地址：https://github.com/coollabsio/coolify
```

你只需要一台 VPS，运行一行安装命令，就能得到一个功能完整的部署控制台：

```
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

没错，就这一行。

---

## 它能做什么？

### 🚀 一键部署，Git 推送即上线

连接你的 GitHub / GitLab / Bitbucket 仓库，每次 `git push`，Coolify 自动触发构建和部署。支持：

-   Next.js、Nuxt、SvelteKit、Remix 等前端框架
    
-   Node.js、Python、Go、PHP、Ruby 等后端语言
    
-   静态网站
    
-   任意 Dockerfile 项目
    

### 🔒 自动 SSL，域名绑定开箱即用

通过 Let's Encrypt 全自动签发和续期 HTTPS 证书，绑定自定义域名只需填写一个表单，背后的 Traefik 反向代理全部自动配置好。

### 🗄️ 数据库一键创建

在界面上点几下，即可创建并管理：

-   PostgreSQL
    
-   MySQL / MariaDB
    
-   MongoDB
    
-   Redis
    
-   ClickHouse
    

数据库直接跑在你的服务器上，完全私有。

### 📦 280+ 服务一键部署

包括但不限于：

-   **AI 工具**：Ollama（本地大模型）、Open WebUI
    
-   **自动化**：n8n、Activepieces
    
-   **分析**：Plausible Analytics、Umami
    
-   **后端**：Supabase、PocketBase、Appwrite
    
-   **博客/CMS**：Ghost、WordPress、Strapi
    

### 🖥️ 多服务器统一管理

一个 Coolify 控制台可以通过 SSH 管理多台服务器，所有部署状态、日志、监控集中查看。

### 🤖 Claude Code 集成（v4.0 新功能）

2026 年 5 月发布的 **v4.0** 带来了 **Coolify MCP Server**，可以直接在 Claude Code 中通过自然语言操作部署、查看日志、管理服务，AI 辅助运维从概念变成了现实。

---

## 和主流平台对比，省多少钱？

以一个中等规模的独立开发者为例，同时跑 3-4 个项目：

| 方案 | 月费 | 数据控制 | 扩展限制 |
| --- | --- | --- | --- |
| Vercel Pro + Railway | ～$40-80 | 数据在第三方 | 按用量计费 |
| Coolify + Hetzner VPS | ～$6-20 | 完全自有 | 服务器配置上限 |

**一年省下的钱，够再买几台服务器。**

---

## 真实用户怎么说？

> "我的账单从每月 ～$150 降到了不到$30，跑着完全相同的工作负载。" ——某开发者博客

> "自托管 Supabase + 用 Coolify 管理，根本不需要付任何 SaaS 订阅费。" ——Reddit r/selfhosted

---

## 适合谁使用？

✅ **非常适合：**

-   独立开发者 / 独立产品人
    
-   小型团队，项目数量多但流量不大
    
-   想要完整数据控制权的开发者
    
-   想搭建个人 AI 工具栈（Ollama、n8n 等）的技术爱好者
    

⚠️ **可能不适合：**

-   需要 SOC 2 / HIPAA 合规认证的企业项目
    
-   团队完全没有运维能力，出问题无人处理
    
-   需要极高可用性（五个九）的核心业务系统
    

---

## 如何开始？

**第一步：准备一台 VPS**

推荐 Hetzner Cloud（欧洲节点，性价比极高）或 DigitalOcean / Vultr 亚太节点。最低配置：2 核 CPU，2GB RAM。

**第二步：一行命令安装**

```
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

安装完成后，浏览器访问 [http://你的服务器IP:8000](http://你的服务器IP:8000) 即可看到管理界面。

**第三步：连接 Git 仓库，部署你的第一个项目**

整个流程，**30 分钟内搞定**。

---

## 写在最后

Coolify 代表了一种越来越主流的趋势：**把云平台的便利性带回到你自己的基础设施上**。

它不是要你回到刀耕火种的手动 SSH 时代，而是让你在拥有完整控制权的同时，享受和 Vercel 一样流畅的开发体验。

开源、免费、活跃维护、社区庞大——如果你还在为云平台账单烦恼，Coolify 值得花一个下午认真体验。

---

_项目地址：https://github.com/coollabsio/coolify_

_官方文档：https://coolify.io/docs_

  

---

![[笔记同步助手/images/c3bbdba7ed1fd8fe42219bcc92a6ef02_MD5.jpg|cover_image]]

Rollkey 小学生意气用事

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c9537621_1780113262210?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MDYxOTkxMA%3D%3D%26mid%3D2247485192%26idx%3D2%26sn%3Dcacfb2e710365faa1079a2d38baa9fe8%26chksm%3Dcf9ae47950d3803eacb311db06de5ae1b10d70bbb6210f494074034394ef46f34d668c031bff%26mpshare%3D1%26scene%3D1%26srcid%3D05305HhTGUev08jNEbtfYiN4%26sharer_shareinfo%3D2c80d741aaeffccd0f331078645c86ab%26sharer_shareinfo_first%3D2c80d741aaeffccd0f331078645c86ab%23rd&s=obsidian)