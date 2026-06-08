---
author: 苍何
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzU4NTE1Mjg4MA==&mid=2247498666&idx=1&sn=03ba9152db89838964a9e59799372eac&chksm=fcfecf652bc2f0c89d199353e45a3657a166dbe4913e99c2e435ccde4396ef6b20c80a70485d&mpshare=1&scene=1&srcid=0529mvzrcnKSEqi3ok6ALtQU&sharer_shareinfo=c5e9f61627e4bf6613b37631f0b6c752&sharer_shareinfo_first=c5e9f61627e4bf6613b37631f0b6c752#rd
saved: 2026-05-29 20:20:30
tags:
  - 笔记同步助手
id: 57eb9e10-1ff0-4927-990c-ef14f74c4b30
---

公众号名称：苍何

作者名称：苍何

发布时间：2026-05-29 18:39

这是苍何的第 540 篇原创！

大家好，我是苍何。

前天 CodexGuide 上线后，后台直接炸了。

![[笔记同步助手/images/834cb2cd2cf1f3439a2e4c5bab9d161b_MD5.png]]

问得最多的一个问题就是：国内怎么用 Codex？能不能不充 Plus？

说实话，我理解这个痛。

充值 Plus 本身就有门槛，还得搞定支付方式，折腾半天人都麻了。

所以我花了两天时间，把网上能找到的方案全试了一遍，踩了不少坑，最终总结出三种最靠谱的接入方法。

今天一次性分享给你，照着做就行。

> 教程也同步上线 CodexGuide 了，随时可以查阅。

![[笔记同步助手/images/5684fd40b980b79bc9df8f204c12e572_MD5.png]]

> 看在这么努力肝的份上，star 走起，哈哈哈。

![[笔记同步助手/images/c8b0ce2b446656e4075e1545de985e84_MD5.png]]

先说个前提，Codex 默认最稳的用法还是官方 GPT 账号登录。

接第三方 API 属于进阶操作，你得知道 `config.toml`、API Key、Base URL 这些东西是啥。

不懂也没关系，跟着下面一步步来就行。

# 三种方案怎么选

先给你一张表，对号入座：

| 方案 | 适合谁 | 优点 | 需要注意 |
| --- | --- | --- | --- |
| 手动配置 | 想理解底层原理的人 | 透明、可控、方便排障 | 要自己维护 `config.toml`，写错就不生效 |
| Codex++ | 用桌面 App，想图形化管理的人 | 有管理界面，配置一键写入 | 第三方工具，Codex 更新后可能需要适配 |
| CCX + CC Switch | 有多个供应商、需要协议转换的人 | 网关路由 + 一键切换供应商 | 组件多，需要理解端口和代理链路 |

讲真的，如果你是小白，直接看方案二就行，最省心。

如果你刚开始学 Codex，建议先看看我之前的 Codex 入门教程，再回来折腾第三方 API。

# 方案一：手动配置

这种方式有个缺点，没办法用 Codex APP 的插件功能。

想用插件的直接跳到方案二。

![[笔记同步助手/images/7c11592946c9dfe6dd3dbde44b332592_MD5.png]]

手动配置的核心就是改一个文件：

```
～/.codex/config.toml
```

改之前，先备份，养成好习惯：

```
cp ～/.codex/config.toml ～/.codex/config.toml.backup
cp ～/.codex/auth.json ～/.codex/auth.json.backup
```

![[笔记同步助手/images/3917374659b27bf58a569710885cb982_MD5.png]]

## 两类登录思路

| 思路 | 怎么理解 | 适合场景 |
| --- | --- | --- |
| GPT 登录 | 保留官方登录态，只改请求转发地址 | 想保留官方账号能力，同时用中转 |
| API Key 登录 | 用环境变量里的 Key，直接请求第三方 | 用 OpenAI API Key 或自建兼容服务 |

一个建议：别一次改太多东西。先只加一个 provider，跑通了再折腾多套配置。

![[笔记同步助手/images/e8dae260388baa5583e2c15df473cfd6_MD5.png]]

## GPT 登录态示例

也就是说，你的 Codex 得先登录 GPT 账号。

## 第一步，改配置文件：

打开 `～/.codex/config.toml`，加入下面的配置。

注意，字段和值要按你实际的服务来填：

```
model = "gpt-5-codex" #这里填你想要的模型
model_reasoning_effort = "high"
disable_response_storage = true
preferred_auth_method = "apikey"


[model_providers.ciyuan]
name = "ciyuan" # 填你的模型提供商名字或者中转站名字，这里以词元为例
base_url = "https://ciyuan.today/v1" # 填你的模型提供商的请求 URL
wire_api = "responses" # 这里不要变
env_key = "OPENAI_API_KEY" # 这里将会通过环境变量的方式注入并启动Codex APP
requires_openai_auth = false
```

几个容易踩坑的点：

-   `model_provider` 要和 `[model_providers.xxx]` 里的 `xxx` 完全一致，差一个字母都不行。
    
-   `base_url` 只写到 `/v1`，千万别把 `/v1/responses` 整段写进去。
    
-   `wire_api = "responses"` 表示用 Responses API 形态请求，别改。
    
-   `requires_openai_auth = false` 表示不走官方登录态。
    

![[笔记同步助手/images/d9af69483cfd8e3921d9be71f75f751b_MD5.png]]

## 第二步，设置环境变量

打开终端，输入：

```
export OPENAI_API_KEY="这里填你的key"
```

![[笔记同步助手/images/28881b5aa43b18205fcdaaa14f35c194_MD5.png]]

## 第三步，从终端启动 Codex APP

这里有个坑，Mac 用户必须从终端启动，直接点图标可能读不到模型。

启动前先彻底关掉 Codex APP，然后终端输入：

```
open -a Codex
```

## 第四步，验证效果

打开 Codex APP，你就能看到模型已经切换成功了：

![[笔记同步助手/images/f486d7eeec6a9d336d379e31b73307d8_MD5.png]]

好家伙，直接起飞。

## API Key 登录示例

如果你用的是 API Key 方式，记住一个原则：密钥放环境变量里，别写死在配置文件。

```
export OPENAI_API_KEY="sk-your-api-key"
```

对应的 `config.toml` 配置：

```
model = "gpt-5.1-codex-max"
model_provider = "my-api-provider"

[model_providers.my-api-provider]
name = "My API Provider"
base_url = "https://example.com/v1"
wire_api = "responses"
env_key = "OPENAI_API_KEY"
requires_openai_auth = false
```

有一点要注意：如果你的上游只支持 Chat Completions，不支持 Responses API，光改配置是搞不定的，得用 CCX 这类网关做协议转换，后面方案三会讲。

## 修改鉴权文件

打开 `～/.codex/auth.json`，把 OPENAI\_API\_KEY 改成你模型服务商的 Key：

![[笔记同步助手/images/b3ff0c1de106d4a0e5c3b02d3e50b8dd_MD5.png]]

## 怎么验证配置成功

配完之后别急，先验证一下：

1.  完全退出 Codex，重新打开。
    
2.  让它执行一个只读任务，比如总结当前目录结构。
    
3.  如果报错，先检查 `model_provider` 名称、`base_url`、环境变量这几个地方。
    
4.  出现认证错误，先切回备份配置，别慌。
    

# 方案二：Codex++

如果你觉得手动改配置太折腾，Codex++ 了解一下。

它是一个图形化的管理工具，帮你一键搞定中转配置，不用手写 toml 文件。

而且，它支持插件功能，这是方案一做不到的。

![[笔记同步助手/images/d7d5b51b1f229d42d241a032dc98f4a7_MD5.png]]

适合这些人：

-   主要用 Codex 桌面 App 的。
    
-   不想手写配置文件的。
    
-   想随时切回官方模式的。
    

### 安装步骤

1.  打开 Codex++ Releases，下载安装包。
    

![[笔记同步助手/images/cd7b510697fe6d1854d74a8f22170d60_MD5.png]]

你会看到两个安装包：「Codex++ 管理工具」和「Codex++ app」，都要装。

![[笔记同步助手/images/f1318aea29d6c6313fe4620c753f1c31_MD5.png]]

2.  安装后打开「Codex++ 管理工具」。
    

首次打开如果弹这个错误，别慌：

![[笔记同步助手/images/11ad9f45b8633c9c0008d5f97d083f84_MD5.png]]

去「系统设置」-「隐私与安全性」，点「仍要打开」就行：

![[笔记同步助手/images/9494a4f701971f585e3015bb3b30dd1a_MD5.png]]

打开后进入管理界面：

![[笔记同步助手/images/fe71dbf54fb234c62e31d264c2363b98_MD5.png]]

同样的方式装好 Codex++ app，管理工具检测全绿就对了：

![[笔记同步助手/images/867909bff1b40b985cbc63a9c553b298_MD5.jpg]]

确认检测到 GPT 登录状态。

3.  添加中转配置。
    

选「供应商配置」- 添加供应商，填写你的 Base URL 和 Key。

注意，接入方式选「纯API」：

![[笔记同步助手/images/5b98236fd0b46b5f4edd240b7d2bd4dd_MD5.jpg]]

模型列表可以从上游自动获取，如果你配的是中转站，这里能选的模型就很多了：

![[笔记同步助手/images/bd88d38546467515841bb7c956c2c150_MD5.jpg]]

本质上这个工具就是帮你更方便地写入配置，省得手动改文件：

![[笔记同步助手/images/fb61b2dc986f1e1c3d32f614fb08d37d_MD5.jpg]]

保存后测试一下联通情况，没问题就直接用：

![[笔记同步助手/images/88a514a9dd75de5478709f81c560d163_MD5.jpg]]

4.  从 Codex++ 入口启动 Codex。
    

注意，要从 Codex++ 启动，不是原版 Codex：

![[笔记同步助手/images/42ea609ed33ab0e505c9ded1dc0cbf65_MD5.jpg]]

重启后，你就能看到 Codex 已经用上了自定义的模型供应商，可选模型一下子多了起来：

![[笔记同步助手/images/251a61f08e10754d8e2dc5931677d097_MD5.jpg]]

插件也能直接用了，这才是完整体验：

![[笔记同步助手/images/193e221a5da2c3fba637c7a99a34f77b_MD5.jpg]]

你还别说，这个方案是我目前用下来最丝滑的，强烈推荐。

### 如果想回滚怎么办

-   在管理工具里清除 API 模式，切回官方配置就行。
    
-   如果 Codex 更新后 Codex++ 不好使了，等它适配就行，不影响原版使用。
    

# 方案三：CCX + CC Switch

这个方案适合重度玩家，把「网关」和「切换工具」拆开了：

-   CCX：API 代理网关，负责协议转换和路由。支持 Claude、OpenAI、Codex、Gemini 等多种入口。
    
-   CC Switch：桌面管理工具，一键切换不同供应商配置。
    

![[笔记同步助手/images/5db07a63df4f859a89ea4cee6d271476_MD5.png]]

什么时候用这个方案？你有多个国产模型 API、多个中转服务、多个 Key，或者上游只支持 Chat Completions 需要转换成 Responses API 的时候。

### 第 1 步：部署 CCX

用 Docker 一行命令搞定：

```
docker run -d \
--name ccx \
-p 3000:3000 \
-e PROXY_ACCESS_KEY=your-proxy-access-key \
-e APP_UI_LANGUAGE=zh-CN \
-v $(pwd)/.config:/app/.config \
crpi-i19l8zl0ugidq97v.cn-hangzhou.personal.cr.aliyuncs.com/bene/ccx:latest
```

启动后浏览器打就能看到了。

### 第 2 步：添加上游渠道

在 CCX 管理界面里添加你的渠道：

1.  选择上游服务类型。
    
2.  填 API Key 和 Base URL。
    
3.  配置模型映射和路由规则。
    
4.  用自带的测试功能确认能通。
    

这里有个关键点：Codex 需要 Responses API 入口。如果上游只有 Chat Completions，CCX 会帮你做协议转换，这也是用它的核心原因。

### 第 3 步：安装 CC Switch

命令行安装：

```
npm install -g cc-switch
```

初始化：

```
cc-switch init
```

初始化时填入 CCX 的地址作为中转入口。

![[笔记同步助手/images/5db07a63df4f859a89ea4cee6d271476_MD5.png]]

### 第 4 步：切换配置并启动

一行命令切换供应商：

```
cc-switch use <配置名>
```

然后重启 Codex 就生效了。

切换后建议打开 `～/.codex/config.toml` 核对一下：

-   `model_provider` 是不是你刚选的。
    
-   `base_url` 是不是指向 CCX。
    
-   Key 有没有不小心写进公开仓库（这个很重要）。
    

# 常见踩坑汇总

最后放一张排错表，遇到问题先对照看：

| 现象 | 先检查什么 |
| --- | --- |
| 切换后没生效 | 是否完全重启了 Codex，`model_provider` 名称是否一致 |
| 报认证错误 | API Key 是否有效，环境变量是否被当前 shell 继承 |
| 报接口路径错误 | `base_url`是否只写到 `/v1`，别重复拼 `/responses` |
| 国产模型无响应 | 上游是否支持 Responses API，不支持就得用 CCX 转换 |
| 插件配置不见了 | 切换工具是否覆盖了配置，有没有提前备份 |

说实话，三种方案我都跑通了，日常用的最多的还是方案二 Codex++，省心。

如果你是那种手里有好几个 Key、好几个供应商的重度用户，方案三更适合你。

好了，今天的分享就到这里。

如果这篇教程帮到你了，点个赞让我知道，我后续会继续更新更多 Codex 的实战玩法。

有问题直接评论区问，我看到都会回。

---

![[笔记同步助手/images/9d35dfee1a82f0f2ba3a0a4db3d2ac3d_MD5.jpg|cover_image]]

Original 苍何 苍何

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/324d1bd6_1780057227111?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU4NTE1Mjg4MA%3D%3D%26mid%3D2247498666%26idx%3D1%26sn%3D03ba9152db89838964a9e59799372eac%26chksm%3Dfcfecf652bc2f0c89d199353e45a3657a166dbe4913e99c2e435ccde4396ef6b20c80a70485d%26mpshare%3D1%26scene%3D1%26srcid%3D0529mvzrcnKSEqi3ok6ALtQU%26sharer_shareinfo%3Dc5e9f61627e4bf6613b37631f0b6c752%26sharer_shareinfo_first%3Dc5e9f61627e4bf6613b37631f0b6c752%23rd&s=obsidian)