---
author: unknown
source: GitHub
url: https://github.com/BigPizzaV3/CodexPlusPlus
saved: 2026-05-26 09:49:40
tags:
  - 笔记同步助手
id: d270fc70-8c87-4a45-93d2-846968af4322
---

[![[笔记同步助手/images/d8c773805f341a20d2271a4cda6f6ddb_MD5.png|Codex++ 图标]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/codex-plus-plus.png)

中文 | [English](/BigPizzaV3/CodexPlusPlus/blob/main/README_EN.md)

![[笔记同步助手/images/3e53290acff4c296b21b4aa95ba145fc_MD5.png|![Release]]](https://camo.githubusercontent.com/98e0787e3624c5b64dedb08238118995c988ae6b8bfc6dde8959e6f210a6a572/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f42696750697a7a6156332f436f646578506c7573506c7573) ![[笔记同步助手/images/bd35e3a5fae0eed1d6499cf0f26f71be_MD5.png|![Stars]]](https://camo.githubusercontent.com/6233eb954e859736b8889e2e782b64fa245fa056c5ec16601ea3a23c5da6feee/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f42696750697a7a6156332f436f646578506c7573506c7573) ![[笔记同步助手/images/62ae53e9fcb19c877d138b923f93f100_MD5.png|![License]]](https://camo.githubusercontent.com/b868fb41e6f8ff5a916a8a7c7732d05b0c8ff54ead1feeefe64a2621c4a8ca7c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f42696750697a7a6156332f436f646578506c7573506c7573) ![[笔记同步助手/images/e0935e3afa869e90c4e0f86c108be75c_MD5.png|![Rust]]](https://camo.githubusercontent.com/793530e4668aace641bcfdc4d0ad6dd8cd6cb17228902e407c595660f586c3ff/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d312e38352532422d6f72616e6765) ![[笔记同步助手/images/323359237163a1f2d7871ade75fe8aa2_MD5.png|![Tauri]]](https://camo.githubusercontent.com/a4859b22bde2782bc67b56618bee6483cd128da3592291125dc7df4ada231aaa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74617572692d322e782d323443384442)

Codex++ 是面向 Codex App 的外部增强启动器和管理工具。它不修改 Codex App 原始安装文件，而是通过外部 launcher 启动 Codex，并使用 Chromium DevTools Protocol 注入增强脚本。

## 快速使用

[](#快速使用)

从 [GitHub Releases](https://github.com/BigPizzaV3/CodexPlusPlus/releases) 下载最新版安装包：

-   Windows：
    
    CodexPlusPlus-\*-windows-x64-setup.exe
    
-   macOS Intel：
    
    CodexPlusPlus-\*-macos-x64.dmg
    
-   macOS Apple Silicon：
    
    CodexPlusPlus-\*-macos-arm64.dmg
    

安装后会有两个入口：

-   Codex++
    
    ：静默启动入口，不显示管理界面，只负责启动 Codex 并注入增强功能。
-   Codex++ 管理工具
    
    ：Tauri 控制面板，用于启动、检查、修复、更新、配置中转注入、管理增强功能和用户脚本。

Windows 安装包会创建桌面和开始菜单快捷方式。macOS DMG 会安装

/Applications/Codex++.app

和

/Applications/Codex++ 管理工具.app

。

## 赞助商

[](#赞助商)

[想显示在下方？](mailto:1727532@qq.com)

| 🏆 赞助商 🏆 | 介绍 |
| --- | --- |
| [![[笔记同步助手/images/21c20947c9e6d91639491126fe356efb_MD5.svg|JOJO Code]]](https://jojocode.com/) | [**JOJO Code｜Codex++ 官方中转站**](https://jojocode.com/)<br>感谢 JOJO Code 赞助了本项目！JOJO Code 是 Codex++ 官方中转站，面向日常开发和团队协作场景，提供稳定可用的 Codex API 接入体验，适合快速接入、长期使用和项目级工作流。 |
| [![[笔记同步助手/images/b71cb7031df5b7582e2c278340383c07_MD5.png|AIGoCode]]](https://aigocode.com/invite/CodexPlusPlus) | [**AIGoCode**](https://aigocode.com/invite/CodexPlusPlus)<br>感谢 AIGoCode 赞助了本项目！AIGoCode 是一个集成了 Claude Code、Codex 以及 Gemini 最新模型的一站式平台，为你提供稳定、高效且高性价比的AI编程服务。本站提供灵活的订阅计划，支持多风险，国内直连，无需魔法，极速响应。AIGoCode 为 CodexPlusPlus 的用户提供了特别福利，通过[此链接注册](https://aigocode.com/invite/CodexPlusPlus)的用户首次充值可以获得额外10%奖励额度！ |
| [![[笔记同步助手/images/bf06c8f07e1dc5c15e6c15cf2850c00a_MD5.png|PackyCode]]](https://www.packyapi.com/) | [**PackyCode**](https://www.packyapi.com/)<br>感谢 PackyCode 赞助了本项目！PackyCode 是一家稳定、高效的API中转服务商，提供 Claude Code、Codex、Gemini 等多种中转服务。PackyCode 为本软件的用户提供了特别优惠，使用此链接注册并在充值时填写"CodexPlusPlus"优惠码，首次充值可以享受9折优惠！ |
| [![[笔记同步助手/images/b991b249a9f4820c2c62394b6c295c65_MD5.png|APIKEY.FUN]]](https://apikey.fun/register?aff=CODEX) | [**APIKEY.FUN**](https://apikey.fun/register?aff=CODEX)<br>感谢 APIKEY.FUN 赞助了本项目！APIKEY.FUN 是一家致力于提供开放、稳定、高性价比的全球主流大模型的 AI 中转站。平台支持 Claude、OpenAI、Gemini 等热门模型的 API 中转服务，价格低至官方原价的 7%。通过专属链接[注册 APIKEY](https://apikey.fun/register?aff=CODEX)，可享受最高充值永久 95 折优惠。 |
| [![[笔记同步助手/images/2d6a3724867127cc960e17900b78cf72_MD5.png|RunAPI]]](https://runapi.co/register?aff=AWJq) | [**RunAPI**](https://runapi.co/register?aff=AWJq)<br>感谢 RunAPI 赞助了本项目！RunAPI 是高效稳定的 API OpenRouter 平替平台，一个 API Key 即可访问 OpenAI、Claude、Gemini、DeepSeek、Grok 等 150+ 主流模型，低至 1 折，极其稳定，可以无缝兼容 Claude Code、OpenClaw 等工具。 |
| [![[笔记同步助手/images/374d79fd34f45c0d00c3f273b9cd2803_MD5.svg|0029 云桥]]](https://www.0029.org/?promo=AFF11F) | [**0029云桥｜codex api中转站(gpt5.5 gpt-image-2)**](https://www.0029.org/?promo=AFF11F)<br>支持个人和企业接入。包月套餐/按量计费，Pro/Plus 号池，全站接口稳定可用，7×24 小时技术支持！ |
| [![[笔记同步助手/images/fb5c1cdbc3417efad88cefce68e9bac3_MD5.svg|RawChat]]](https://rawchat.cn/) | [**RawChat｜Codex 中转站**](https://rawchat.cn/)<br>老牌中转站，支持包月套餐。低倍率调用，高缓存命中，Pro/Plus 号池，全天专人维护。 |
| ![[笔记同步助手/images/d3f542989d23c9c8f37bdc0652216811_MD5.png|![VisionCoder]]](https://coder.visioncoder.cn/) | [**VisionCoder 开发平台**](https://coder.visioncoder.cn/)<br>感谢 VisionCoder 对本项目的支持。VisionCoder 开发平台是一个可靠高效的 API 中继服务提供商，提供 Claude Code、Codex、Gemini 等主流 AI 模型，帮助开发者和团队更轻松地集成 AI 功能，提升工作效率。VisionCoder 还为我们的用户提供 [Token Plan](https://coder.visioncoder.cn/) 限时活动：购买 1 个月，赠送 1 个月。 |

## 交流与支持

[](#交流与支持)

欢迎扫码加入 Codex++ 交流群，反馈问题、交流使用体验或提出新功能建议：

[![[笔记同步助手/images/8072f36196aa8c2f2f245637d3be21f0_MD5.jpg|Codex++ 交流群二维码]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/discussion-group-qr.jpg)

如果 Codex++ 帮到了你，可以请我喝杯咖啡，或者随手赞赏支持一下继续维护。

[![[笔记同步助手/images/99128e590b788b50a3dc354b555c01b5_MD5.jpg|支付宝赞赏码]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/sponsor-alipay.jpg) [![[笔记同步助手/images/918f5e2effbbc2ded4faa35b6946071c_MD5.jpg|微信赞赏码]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/sponsor-wechat.jpg)

## 主要功能

[](#主要功能)

-   Rust 后端和静默 launcher，启动时不依赖额外运行时。
-   Tauri + React 管理工具，支持深色/浅色切换。
-   外部 CDP 注入，不改
    
    app.asar
    
    ，不向 Codex 安装目录写入 DLL。
-   中转注入模式：支持多个中转配置，写入
    
    CodexPlusPlus
    
    provider，并可切回官方 ChatGPT 登录态。
-   传统增强模式：插件入口解锁、特殊插件强制安装、会话删除、Markdown 导出、项目移动、Timeline 等。
-   用户脚本独立管理，可在启动时注入自定义脚本。
-   Provider 同步：启动前同步本地会话 metadata，切换供应商后旧会话仍可见。
-   Zed 打开入口：识别远程 SSH 上下文后，可从 Codex 直接打开对应文件到 Zed Remote Development。
-   Upstream worktree 创建：可从
    
    upstream/<base-branch>
    
    创建新 worktree，创建前自动 fetch 远端分支，降低从陈旧本地 HEAD 派生导致的冲突风险。
-   GitHub Release 自动更新，管理工具和静默启动器都会检测可用更新。
-   Windows 单实例、无黑框启动、管理员权限清单、系统桌面路径识别。
-   macOS x64/arm64 分架构 DMG，静默入口隐藏 Dock 图标。

## 痛点与解决

[](#痛点与解决)

API Key 登录模式下，Codex 原生插件入口会提示需要登录 ChatGPT，导致插件功能无法正常使用：

[![[笔记同步助手/images/d7d0ce9c361b2e7df02c881b82c271e6_MD5.png|API Key 模式下插件入口不可用]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/pain-plugin-disabled.png)

Codex 原生会话列表只有归档入口，没有真正的删除按钮：

[![[笔记同步助手/images/1039dc34d477b78cfd093db1a9714813_MD5.png|原生会话列表缺少删除能力]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/pain-no-delete-button.png)

Codex++ 启动后会解锁插件入口，并在会话列表悬停时显示删除按钮：

[![[笔记同步助手/images/a9b488110c4055357346daa7d4c7b877_MD5.png|Codex++ 解锁插件入口并添加删除按钮]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/solution-plugin-and-delete.png)

顶部菜单栏会出现

Codex++

，可以查看后端状态并打开设置面板：

[![[笔记同步助手/images/f474ef8e8dc1859c14229139fe3514e6_MD5.png|Codex++ 后端状态指示灯]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/backend-status-indicator.png) [![[笔记同步助手/images/f8b8374f4790fea7750f8934f40bcb8b_MD5.png|Codex++ 设置面板]]](/BigPizzaV3/CodexPlusPlus/blob/main/docs/images/settings-panel.png)

## 中转注入

[](#中转注入)

中转注入适合已经在 Codex/ChatGPT 中完成官方账号登录，同时希望把模型请求转到自定义兼容 API 的场景。

在管理工具的“中转注入”页面：

1.  确认已经检测到 ChatGPT 登录状态。
2.  添加一个或多个中转配置，填写 Base URL 和 Key。
3.  选择当前配置并应用中转注入。
4.  启动
    
    Codex++
    
    。

Codex++ 会在

～/.codex/config.toml

中写入类似配置：

model\_provider = "CodexPlusPlus"

\[model\_providers.CodexPlusPlus\]
name = "CodexPlusPlus"
wire\_api = "responses"
requires\_openai\_auth = true
base\_url = "https://example.com/v1"
experimental\_bearer\_token = "sk-..."

如果需要回到官方登录态，在“中转注入”页面点击清除 API 模式即可移除

OPENAI\_API\_KEY

相关配置并切回官方 ChatGPT 登录模式。

## 增强功能

[](#增强功能)

增强功能在管理工具中统一开关。默认开启增强注入；关闭后不会注入 Codex++ 菜单和脚本。

如果启用中转注入模式，插件入口解锁和强制安装不再需要，界面会提示“中转注入模式下无需开启”。会话删除、导出、移动、Timeline、推荐内容和用户脚本等增强仍可继续使用。

## 推荐内容

[](#推荐内容)

推荐内容来自远程广告列表：

https://raw.githubusercontent.com/BigPizzaV3/Ad-List/main/ads.json
https://cdn.jsdelivr.net/gh/BigPizzaV3/Ad-List@main/ads.json

请求时会自动追加

?v=时间戳

绕开 CDN 旧缓存。推荐内容加载慢不会影响后端连接状态。

## 自动更新与安装包

[](#自动更新与安装包)

Codex++ 通过 GitHub Release 发布安装包。Windows 会生成 NSIS 安装程序，macOS 会生成 Intel x64 和 Apple Silicon arm64 两个 DMG。

管理工具的“关于”页可以检查并启动更新。静默启动器发现新版本时会拉起管理工具并进入更新提示。

## 数据位置

[](#数据位置)

-   Codex 配置：
    
    ～/.codex/config.toml
    
-   Codex 登录状态：
    
    ～/.codex/auth.json
    
-   Codex 本地数据库：
    
    ～/.codex/state\_5.sqlite
    
-   Codex++ 状态与日志：
    
    ～/.codex-session-delete/
    
-   Provider 同步备份：
    
    ～/.codex/backups\_state/provider-sync
    

## 常见问题

[](#常见问题)

### Codex++ 菜单没出现

[](#codex-菜单没出现)

确认是从

Codex++

入口启动，而不是原版 Codex。也可以打开管理工具的“诊断”和“日志”页面查看注入状态。

### 插件内显示后端连不上

[](#插件内显示后端连不上)

先在浏览器或 PowerShell 里测试：

Invoke-RestMethod \-Method Post \-Uri http://127.0.0.1:57321/backend/status \-Body "{}" \-ContentType "application/json"

如果接口正常，但插件仍显示超时，通常是 Codex 页面里的 CDP bridge 或脚本缓存问题。重启 Codex++，或在管理工具里查看日志中的

renderer.script\_loaded

、

bridge.request

、

bridge.response

。

### Upstream worktree 和 Codex 原生创建有什么区别

[](#upstream-worktree-和-codex-原生创建有什么区别)

Codex++ 的 Upstream worktree 功能等价于先更新远端分支，再执行：

git worktree add -b <new-branch\> <worktree-path\> upstream/<base-branch\>

这样新 worktree 从最新的远端跟踪分支开始，而不是从当前会话所在的本地 HEAD 开始。如果 Codex++ 无法安全识别当前 Codex 版本的原生 worktree 创建表单，请从 Codex++ 菜单中手动填写仓库路径、分支名、worktree 路径、remote 和 base branch。

### macOS 提示无法打开或已损坏

[](#macos-提示无法打开或已损坏)

当前安装包未签名/未公证时，macOS Gatekeeper 可能拦截。可以在“系统设置 - 隐私与安全性”中允许打开。正式分发建议配置 Apple Developer ID 签名和 notarization。

### macOS Intel 能用吗

[](#macos-intel-能用吗)

可以。Release 会分别提供

macos-x64.dmg

和

macos-arm64.dmg

。Intel Mac 下载 x64 包，Apple Silicon 下载 arm64 包。

## 开发

[](#开发)

# 前端检查
cd apps/codex-plus-manager
npm install
npm run check
npm run vite:build

# Rust 检查
cd ../..
cargo fmt --check
cargo test
cargo build --release

主要结构：

apps/
  codex-plus-launcher/          静默启动入口
  codex-plus-manager/           Tauri 管理工具
assets/inject/
  renderer-inject.js            注入到 Codex 渲染端的增强脚本
crates/
  codex-plus-core/              启动、注入、配置、更新、安装、桥接等核心逻辑
  codex-plus-data/              会话数据、导出、Provider 同步
scripts/installer/
  windows/CodexPlusPlus.nsi     Windows NSIS 安装包
  macos/package-dmg.sh          macOS DMG 打包

## 友情链接

[](#友情链接)

-   [LINUX DO](https://linux.do/)

## 说明

[](#说明)

Codex++ 是外部增强工具，不修改 Codex App 原始文件。Codex App 更新后，如果页面结构变化，可能需要更新注入脚本。

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/973cb0de_1779760178496?u=https%3A%2F%2Fgithub.com%2FBigPizzaV3%2FCodexPlusPlus&s=obsidian)