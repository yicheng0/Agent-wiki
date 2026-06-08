---
author: wsleepybear
source: 微信公众号
url: https://mp.weixin.qq.com/s/Fxjebfb0l1rP_OkIDa2YdQ
saved: 2026-05-27 23:51:18
tags:
  - 笔记同步助手
id: f376c9dc-be0b-464f-94a8-05ea8e3ee744
---

公众号名称：Git Trend

作者名称：wsleepybear

发布时间：2026-04-22 17:09

![[笔记同步助手/images/1262e03328d09cbd66770ac59bb1ceee_MD5.png]]

一个熟练的逆向工程师拿到 APK 之后干什么？反编译、看结构、追调用链、把 API 接口整理成文档。这个过程靠经验——知道 jadx 快但 Fernflower 在 lambda 和泛型上更准，知道 ProGuard 混淆后要从字符串常量入手，知道 Retrofit 注解永远不会被混淆。

android-reverse-engineering-skill 做的事情很直接：**把这套经验编码成 Claude Code 插件**。装好之后一句 `/decompile path/to/app.apk`，Claude Code 按 5 个阶段走完整个流程——从依赖检查到 API 文档输出。

> **项目卡片**
> 
> -   **项目**：android-reverse-engineering-skill\[1\]
>     
> -   **状态**：v1.0.0 / 3500+ Stars / 2026 年 2 月创建
>     
> -   **一句话判断**：不是新逆向工具，而是把逆向方法论打包成 Claude Code Skill，让 AI 执行结构化分析流程
>     

> 它是什么，不是什么

先说清楚它不做什么：**不包含新的反编译引擎**。底层靠 jadx、Fernflower/Vineflower、dex2jar 这些成熟工具。

项目本身的代码量很小——4 个 bash 脚本、5 份参考文档、1 个 SKILL.md。我翻完整个仓库后觉得，SKILL.md 里定义的工作流和混淆代码导航策略才是真正有信息量的部分。脚本只是胶水层。

> 安装和触发

安装走 Claude Code 的插件机制：

> ```
> /plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill
> /plugin install android-reverse-engineering@android-reverse-engineering-skill
> ```

安装后，你可以用斜杠命令触发：

> ```
> /decompile path/to/app.apk
> ```

也可以用自然语言触发，比如"反编译这个 APK""提取这个 app 的 API 接口""追踪 LoginActivity 的调用链"。

前置依赖只有 **Java 17+** 和 **jadx**。Fernflower 和 dex2jar 是可选的，但对复杂代码反编译质量有明显提升。插件自带 `check-deps.sh` 做环境检测，输出是机器可读的：

> ```
> INSTALL_REQUIRED:jadx
> INSTALL_OPTIONAL:vineflower
> ```

装缺失依赖直接跑 `install-dep.sh jadx`，它会自动识别你的系统（Linux/macOS）和包管理器（apt/brew/pacman），优先装到 `～/.local/`，不需要 sudo。

![[笔记同步助手/images/442165275daeaae43b2cc325711117a8_MD5.png]]

> 5 阶段工作流：核心价值所在

SKILL.md 定义了 5 个阶段，每一步都写得很具体：

**Phase 1 — 依赖检查与安装**：运行 `check-deps.sh`，缺什么装什么。`install-dep.sh` 自动处理系统识别和包管理器选择，sudo 不可用时打印手动安装命令。

**Phase 2 — 反编译**：`decompile.sh` 支持 APK、XAPK、JAR、AAR 四种格式。三个引擎可选：

-   `jadx`（默认）：速度快，能处理资源文件
    
-   `fernflower`：Java 代码质量更高，适合 JAR/AAR 库
    
-   `both`：两个引擎并行跑，输出对比报告
    

XAPK（APKPure 等平台使用的分包格式）也能自动处理——解压后逐个反编译内部的 APK 文件。对混淆代码可以加 `--deobf` 参数启用 jadx 的反混淆。

**Phase 3 — 结构分析**：读 `resources/AndroidManifest.xml`，识别主 Activity、四大组件、权限声明，梳理包结构。SKILL.md 指导 Claude Code 去找 `api`、`network`、`repository` 这些命名的包——通常 API 调用就藏在那里，然后判断项目用的是 MVP、MVVM 还是 Clean Architecture。

**Phase 4 — 调用链追踪**：这是整个工作流中最有方法论含量的部分。从入口点出发，沿 Activity → ViewModel → Repository → API Service 的路径追踪执行流，处理 Dagger/Hilt 依赖注入的绑定关系。

![[笔记同步助手/images/f48f609598aff32655297a59b0ac44b3_MD5.png]]

对混淆代码，SKILL.md 给出了一个实用的导航策略：ProGuard/R8 把类名方法名压成 `a.b.c`，但**字符串常量、Android 框架类名、Retrofit 注解、URL 不会被混淆**。所以方法是从可读的 URL 和注解入手，通过 grep 交叉引用定位混淆类之间的关系。`call-flow-analysis.md` 里举了一个完整例子：从 `"auth/login"` 这个字符串找到 Retrofit 接口 `c.a.b.d`，再一路 grep 到 `LoginActivity`。

**Phase 5 — API 提取与文档化**：`find-api-calls.sh` 用正则扫描五种 HTTP 客户端模式——Retrofit 的 `@GET`/`@POST` 注解、OkHttp 的 `Request.Builder`、Volley 的 `StringRequest`、`HttpURLConnection`、以及 WebView 的 `loadUrl`。支持按类型过滤：

> ```
> find-api-calls.sh sources/ --retrofit   # 只看 Retrofit
> find-api-calls.sh sources/ --auth       # 只看认证模式
> find-api-calls.sh sources/ --urls       # 只看硬编码 URL
> ```

每个端点按固定模板输出：HTTP 方法、路径、Base URL、参数、请求体、响应类型、调用链。

> 脚本工程质量

翻完四个 bash 脚本，几个值得提的设计：

-   `set -euo pipefail` 统一兜底，退出码有明确语义——0 成功、1 失败、2 需要手动操作
    
-   `install-dep.sh` 覆盖 Linux（apt/dnf/pacman）和 macOS（brew），无 sudo 时回退到 `～/.local/` 用户本地安装
    
-   Fernflower 处理 APK 时自动走 dex2jar 中转（DEX→JAR→Fernflower），对使用者透明
    
-   XAPK 自动解压并逐个反编译内部 APK，保留 `manifest.json` 备查
    

> 用之前的判断

这套工具的边界很清晰：**静态分析、Java/Kotlin 层面、需要 Claude Code**。它不碰 Frida hook、不处理 native .so 库、没有增量缓存（每次全量反编译）。Fernflower 走 dex2jar 中转，复杂 APK 的转换可能丢信息。

适合用它的人：安全研究员做授权渗透测试、恶意软件分析师快速摸清 app 行为、CTF 选手跑 Android 题。前提是你已经在用 Claude Code——这不是一个独立工具。

android-reverse-engineering-skill 的思路其实可以推广到其他领域：不造新工具，而是把领域知识编码成 AI 可执行的流程。4 个脚本 + 5 份文档，本质上是一份"逆向工程操作手册"的工程化实现。如果你已经在用 Claude Code，装上它相当于多了一个知道按什么顺序 grep 的逆向助手。它不会替代熟练的逆向工程师，但能帮你快速建立对目标 app 的结构认知，省掉大量重复性的阅读工作。

---

如果这篇对你有用，建议点个关注。我会持续把 GitHub 上值得用的 AI 工具拆成「最短上手闭环 + 坑点清单 + 可复用配置」，让你少走弯路。

### 引用链接

\[1\]android-reverse-engineering-skill: _https://github.com/SimoneAvogadro/android-reverse-engineering-skill_

---

![[笔记同步助手/images/9857405677772e4b5ae60c503285e220_MD5.jpg|cover_image]]

原创 wsleepybear Git Trend

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/3b74d9f2_1779897075251?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FFxjebfb0l1rP_OkIDa2YdQ&s=obsidian)