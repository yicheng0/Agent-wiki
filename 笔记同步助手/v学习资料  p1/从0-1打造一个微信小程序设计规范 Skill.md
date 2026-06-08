---
author: B端设计视界
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2MTY3ODMyMg==&mid=2247483934&idx=1&sn=710a0da38aae1bf3e4631f85079014d3&chksm=cfbfb188ef5b0cf68074fb89408a3da0a06e7f61170ee4a0c4bf1c48530b8a1688b878686178&mpshare=1&scene=1&srcid=0525rBX4KUEKmO8MQwhjNga8&sharer_shareinfo=154c9b540ebba916159d56a691934941&sharer_shareinfo_first=154c9b540ebba916159d56a691934941#rd
saved: 2026-05-25 09:05:49
tags:
  - 笔记同步助手
id: a401258a-2fc6-46c6-a5ef-f647a2cbc515
---

公众号名称：B端AI设计视界

作者名称：B端设计视界

发布时间：2026-05-05 20:00

# 之前的文章我写过，怎么把设计系统做成设计 Skill。

那个流程说实话挺费劲的—要整理 token、定义 schema、梳理 patterns，还要开 MCP 接口打通工具链。每一步都有门槛，每一步都要花时间对齐。不是不能做，但成本摆在那里，很多人看完觉得"有道理，但我做不来"。

这篇是续集，但不是"更复杂的教程"，而是—**同样的事情，现在已经变得非常简单了。**

**![[f017b2833d71fc26d17dc136039ba2ec_MD5.png]]**

刚好同事需要微信小程序的设计规范Skill，我们以此为例从0-1来拆解一下，如何打造一份设计规范skill～

---

  

## 首先，现在只需要一份原始文档

AI 进化之后，做设计 Skill 的起点变了。

不需要结构化的 token 文件，不需要提前定义 schema，不需要开 MCP。**只要你手头有一份整理好的设计规范原始文档，就可以开始了。**

我手头有的是什么？微信小程序相关的几份官方文档——**设计指南、WeUI 规范、****UI** **合规要求**—散落在不同页面，格式不统一。

```
核心三大源文件（必录）
小程序官方设计指南（主规范）
https://developers.weixin.qq.com/miniprogram/design/index.html
WeUI 视觉 & 组件规范（落地组件标准）
https://weui.io/
小程序 UI 审核规范 + 违规红线（避坑关键）
https://developers.weixin.qq.com/miniprogram/product/spec.html
补充增补内容
小程序适配规范（刘海屏、深色模式、胶囊按钮避让）
弹窗 / 授权 / 定位 / 隐私弹窗强制规范
导航栏、Tabbar、顶部标题栏强制交互规则
```

就这些够了，这意味着，设计规范 Skill 不再只是大团队、设计系统团队才能做的事情。即使是一个小团队，甚至个人设计师，也可以开始建立自己的规范 Skill。

---

  

## 现在30 分钟，手把手拆解打造设计skill的过程

### 01

### 第一步：整合原材料，输出一份 PDF

不要直接把链接扔给 AI，效果不太好。

正确做法是：先借助 AI 把几份官方文档的内容整合、提炼，输出成一份结构统一的 PDF。每个模块都套同一个格式：

```
【组件/场景】：【适用场景】：【官方标准规范】：【尺寸/参数】：【交互规则】：【强制要求】：【禁止设计】：【最佳实践】：
【组件/场景】：
【适用场景】：
【官方标准规范】：
【尺寸/参数】：
【交互规则】：
【强制要求】：
【禁止设计】：
【最佳实践】：
```

格式统一之后，AI 读起来更准，后面写出来的 Skill 质量会高很多。这一步是整个流程的地基。

![[f15ddf7fee1b8deaf486886da618a233_MD5.png]]

  

---

  

### 02

### 第二步：PDF 喂给 AI，让它写 Skill

把整理好的 PDF 发给 AI，指令只需要一句话：

> "请按照 Skill 的标准格式，把这份文档整理成一套完整的微信小程序设计规范 Skill，同时写一段预设人设 Prompt，让 AI 以这份规范为准来回答设计问题。"

![[6adff240944533c816991ddb342789ce_MD5.png]]

我同时发给了 Claude 和 Codex 对比，两个 AI 各自开始写，我没有介入。

15 分钟后，两份 Skill 都出来了。

![[00ed94b2e6d5c454f3a79ff79cea3e50_MD5.png]]

质量差距在细节上—Claude 的合规部分更完整，审核红线、边界情况覆盖得更系统，读起来更像可以直接用的专业文档。Codex 的结构干净，尺寸参数整理清楚，但对微信审核规则的感知相对浅，边界情况容易漏。

---

  

### 03

### 第三步：验证 Skill 质量

Skill 写完不是终点，得验证写得对不对。

这里两个 AI 的处理方式完全不同。

![[a441a33e28f9923a7fdfaf38631ce437_MD5.png]]

**Claude：自己写例子验证。**

Claude 写完 Skill 之后，自己构造了设计场景和代码示例，对照规范逐条检查——这个规则写清楚了吗？这个参数在例子里对得上吗？禁止项有没有覆盖到？它在自我校验 Skill 本身的质量，不需要我介入，自己跑完交卷。

**Codex：需要手动验证。**

Codnet 的内容本身没大问题，但验证这步它不做。需要我自己拿规范和例子对照逐项 review，本质上还是人工核查。

---

  

### 04

### 第四步：实战验证，跑一个真实项目

光靠自我校验不够，还需要拿真实项目验一遍。

![[6f866fe07c4f489bff54452e7a92bebe_MD5.png]]

我用一个**社区咖啡店微信小程序**做了验证——首页推荐、菜单点单、会员积分、订单查询，覆盖了列表、卡片、表单、弹窗、底部导航这些最典型的场景。

![[d0f1f19f57fb4a94cb8aa60894f2d319_MD5.png]]

结果：**Skill 覆盖率 92%**。剩下 8% 是咖啡馆品牌定制部分（积分动画、主题色），在 Skill 基础上额外补充定义即可。

---

  

#### 05

#### 第五步：打包分享，一句话的事

Skill 验证完，想分享给团队或朋友，不需要手动整理文件。

直接告诉 AI：

> "帮我把这个 Skill 打包到桌面。"

它会自动把所有规范文档、模板结构、预设 Prompt 打包成一个文件夹，放到你桌面上，发给谁都行。

![[8425746ba3039ad4c04de38f52f6322a_MD5.png]]

---

---

  

## 为什么与上次相比会变简单？

### 前后对比

<table style="border-collapse: collapse"><tbody><tr><td data-colwidth="103" style="color:rgb(0, 0, 0); font-weight:bold; text-align:center; border: 1px solid #ddd; padding: 6px 10px"><br></td><td data-colwidth="262" style="color:rgb(0, 0, 0); font-weight:bold; text-align:center; border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">上一次</span></span></div></td><td style="color:rgb(0, 0, 0); font-weight:bold; text-align:center; border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">这一次</span></span></div></td></tr><tr><td data-colwidth="103" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">起点</span></span></div></td><td data-colwidth="262" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">结构化设计系统</span></span></div></td><td style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">原始设计规范文档</span></span></div></td></tr><tr><td data-colwidth="103" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">前置工作</span></span></div></td><td data-colwidth="262" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">整理 token、schema、</span></span></div><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">patterns、开 MCP</span></span></div></td><td style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">整合文档成 PDF</span></span></div></td></tr><tr><td data-colwidth="103" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">验证方式</span></span></div></td><td data-colwidth="262" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">手动</span></span></div></td><td style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">Claude 自动自我校验</span></span></div></td></tr><tr><td data-colwidth="103" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">总用时</span></span></div></td><td data-colwidth="262" style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">数天</span></span></div></td><td style="color:rgb(0, 0, 0); border: 1px solid #ddd; padding: 6px 10px"><div style="color: rgb(0, 0, 0)"><span><span style="font-size: 16px; color: rgb(0, 0, 0)">30 分钟</span></span></div></td></tr></tbody></table>

不是流程被简化了，是 AI 的理解能力上来了。

以前 AI 读不懂松散的原始文档，必须先人工结构化成它能处理的格式——token、schema、patterns，本质上是在替 AI 做"消化"的工作。

现在 AI 自己能消化了。你给它原始材料，它自己提炼结构、填充规范、输出 Skill，还能回头验证自己写的对不对。

**中间那些折腾人的步骤，是 AI 能力不够时的补丁。补丁不需要了。**

---

  

## 写在最后

如果你上次看过那篇文章，觉得流程太复杂没有动手——现在可以试了。

这份微信小程序设计 Skill 我已经整理好了，

**关注公众号，发送「Skill」，直接分享给你～**

---

![[46dd5d9392088ee3dbe6b00e6a6804a3_MD5.jpg|cover_image]]

Original B端设计视界 B端AI设计视界

修改于

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/28320573_1779671145460?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MTY3ODMyMg%3D%3D%26mid%3D2247483934%26idx%3D1%26sn%3D710a0da38aae1bf3e4631f85079014d3%26chksm%3Dcfbfb188ef5b0cf68074fb89408a3da0a06e7f61170ee4a0c4bf1c48530b8a1688b878686178%26mpshare%3D1%26scene%3D1%26srcid%3D0525rBX4KUEKmO8MQwhjNga8%26sharer_shareinfo%3D154c9b540ebba916159d56a691934941%26sharer_shareinfo_first%3D154c9b540ebba916159d56a691934941%23rd&s=obsidian)