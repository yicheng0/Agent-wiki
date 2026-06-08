---
author: 开源星探
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247506277&idx=1&sn=a2aa37f829bb846d2cde004e39abe6b3&chksm=c1852f61c0913d363e01f28402d9d721379890617121ca390c7b0d72740915750b58742c4e57&mpshare=1&scene=1&srcid=0607rD4UFKZTT9E1eY5U3ibY&sharer_shareinfo=0399597838760ea8a774e16d26e5e7df&sharer_shareinfo_first=e2abb1188e2d3de4e70645d60d658054#rd
saved: 2026-06-07 13:39:30
tags:
  - 笔记同步助手
id: c907954f-ec1f-435b-b3a4-3d5989e13b42
---

公众号名称：开源星探

作者名称：开源星探

发布时间：2026-06-07 08:36

视频制作行业正在经历一场革命。

过去，要做出一支像样的产品宣传视频或者知识解说视频，你需要专业的剪辑师、动画师、配音员，可能还要花几万块钱找外包团队。

即使是小团队自己做，也得精通AE、Pr这些复杂的工具，光学习成本就高得吓人。

而且，这一切成本和门槛都还是建立在人工操作的基础上的。

就在这个时候，Open Design 团队干了一件大事。他们用了3天时间，写了3万行代码，把视频制作这件事彻底改写了，而且照样是开源的。

![[笔记同步助手/images/9d99421e73ce05784a0485c18ddda052_MD5.png]]

现在，你只需跟你的 AI Agent 说句话，或者粘贴一个公众号文章链接，它就能直接给你生成一支动态的 MP4 视频。而且，这个过程完全在你本机上运行，没有云端渲染费用，也不绑定任何厂商。

这就是 **html-video** —— 一个把HTML变成视频的革命性工具。

![[笔记同步助手/images/2f0cbd428d74da896555fe99391e4d7f_MD5.png]]

### 什么是html-video？

html-video 是 Open Design 团队官方研发的开源项目，它的核心理念很简单：**在你的电脑上，把 HTML 变成视频**。

你不需要是专业的剪辑师，也不需要是动画专家。你只需要：

1.  1\. 描述一个视频（或者直接粘贴一个文章链接/GitHub仓库）
    
2.  2\. 让你的 Agent 来处理
    
3.  3\. 导出真实的 MP4 视频
    

这个过程中，Agent会自动帮你：

-   • 选择合适的渲染引擎
    
-   • 挑选最匹配的视频模板
    
-   • 填入你的内容
    
-   • 渲染出高质量的视频
    

而且，所有这些都在你的本地机器上完成，不用上传到任何云端，也没有单次渲染费用。

### 核心亮点：为什么html-video不一样？

#### 1、基于Hyperframes框架

html-video 不是从零开始的。它的默认渲染引擎是 Hyperframes，这是一个成熟的 HTML+CSS+GSAP 框架，专门用来做动态HTML动画。

而整个项目的架构思想，其实和 Open Design 在设计领域的产品是一脉相承的。

而且，这个架构是可插拔的。现在默认用的是Hyperframes，未来Remotion、Motion Canvas、Manim这些引擎都会一一接进来。加一个新引擎，所有模板、所有agent、整条工作流就都自动用上了。

#### 2、21套顶级HTML视频模板

html-video 内置了21个精选、许可清晰的视频模板，每一个都是经过精心设计的。

![[笔记同步助手/images/d7b6b7e5a61feae1eae2b926c284aec9_MD5.png]]

这些模板不是随手凑的一堆，而是覆盖了各种常见的使用场景：

-   • **数据可视化**：纽约时报风格的动态折线图、瑞士网格数据卡，适合「数字涨上去了」类叙事
    
-   • **标题与特效**：故障艺术标题、动感排版、打字机光标，适合开场爆点
    
-   • **主视觉与电影感**：极光液态渐变背景、漏光电影感画面、暖色颗粒杂志风
    
-   • **产品宣传**：15秒/30秒多场景产品宣传片
    
-   • **解说骨架**：决策树解说、Takram有机动效
    

每个模板都有清晰的分类和标签，agent 可以根据你的意图自动匹配最合适的模板。

更重要的是，这些模板都可以在 Open Design 中找到，保持了设计系统的一致性。

#### 3、分页预览、分页编辑、帧文字编辑

传统的视频制作工具，你改一点东西就得重新渲染整个视频，等上半天才能看到效果。html-video 完全改变了这个工作流。

它支持：

-   • **分页预览**：每一帧都可以单独预览，不用等整个视频渲染完
    
-   • **分页编辑**：每一帧都可以单独编辑，想改哪帧改哪帧
    
-   • **帧文字编辑**：直接在界面上修改每帧的文案，所见即所得
    

而且，它支持多种视频尺寸：

-   • 横屏 16:9
    
-   • 竖屏 9:16
    
-   • 方形 1:1
    
-   • 小🍠 4:5
    

你可以根据发布平台随时切换尺寸，不用重新制作。

#### 4、自动识别本地6种Code Agent

html-video 最厉害的一点是，它可以自动识别你电脑上已经安装的 coding agent。目前支持14个主流的 agent：

-   • Open Design (Vela)
    
-   • Windsurf CLI
    
-   • Trae CLI
    
-   • Claude Code
    
-   • Cursor Agent
    
-   • Codex CLI
    
-   • Hermes
    
-   • Gemini CLI
    
-   • Grok Build
    
-   • Qwen Code
    
-   • OpenCode
    
-   • GitHub Copilot CLI
    
-   • Aider
    
-   • Anthropic Messages API
    

这些 agent 会在你的 PATH 上自动探测，你只需要在 studio 的顶栏一键切换就可以了。没有本地 agent 也没关系，你可以直接使用官方 AMR 接入，或者配置 Anthropic API key，studio 直接走 Messages API。

而且，studio 默认把 Open Design (Vela) 排在最前面——一次登录、多种模型、成本更低——然后回落到第一个可用的 agent，保证你永远有一个能用的后端。

#### 5、已接入MiniMax

视频没有声音是不完整的。html-video 已经接入了 MiniMax，你可以一键给视频加上背景音乐和旁白。

在 Settings → Audio 里填入 MiniMax API key，然后在每个项目的 Soundtrack 面板：

-   • **背景音乐**：描述一种情绪（比如「舒缓的电影感氛围，缓慢推进」），MiniMax 会生成一段器乐
    
-   • **旁白**：输入文案，MiniMax 会朗读出来（TTS）
    

两者都会通过 ffmpeg 混进导出的 MP4，音乐还会自动压低到人声之下，还支持可选的淡入淡出效果。

### 快速上手

在开始之前，你需要先安装几个依赖：

| 依赖 | 最低版本 | 检查方式 |
| :-- | :-- | :-- |
| Node.js | 20+ | `node --version` |
| pnpm | 9+ | `pnpm --version` |
| ffmpeg | 任意较新版本 | `ffmpeg -version` |
| Chromium（或 Playwright 浏览器） | — | `npx playwright install chromium` |

默认渲染引擎用无头 Chromium 录制带动画的 HTML，再用 ffmpeg（libx264）编码为 MP4。如果没有系统安装的 Chromium，可以装 Playwright 内置的。

安装和运行都很简单：

```
pnpm install
pnpm -r build
node packages/cli/dist/bin.js studio  # 在 http://127.0.0.1:3071 打开 studio
```

然后在浏览器里打开 http://127.0.0.1:3071，你就可以看到 html-video 的 studio 界面了。

在 studio 里，你可以：

1.  1\. 挑一个模板（或者直接描述视频/粘链接）
    
2.  2\. 跟 agent 对话
    
3.  3\. 逐帧改文案
    
4.  4\. 加配乐
    
5.  5\. 导出 MP4
    

就这么简单。

支持三种输入方式：

-   • **网页文章**：抓取并扁平成 Markdown。像微信公众号这种服务端渲染的页面开箱即用。
    
-   • **GitHub 仓库**：通过公开 API 拉取简介、顶层结构、README——很适合做「解读某开源项目」的视频。
    
-   • **只给一句话**：描述主题，agent 从零写内容。
    

无论哪种来源，它都会成为视频真正依据的素材——不是套模板时的摆设。

agent 会读取抓来的内容，自己决定需要几个场景，写出一份 content-graph 故事板：要点变成帧，要点之间的关系（这个承接那个、这个对比那个）变成边，再把所选模板的视觉风格逐帧应用上去。

### CLI工具

除了图形化的 studio，html-video 还提供了可脚本化的 CLI 工具：

```
node packages/cli/dist/bin.js doctor  # 探测已安装的 agent + 引擎
node packages/cli/dist/bin.js search-templates --intent "github stars race" --top 3
```

这对于想把 html-video 集成到自己 CI/CD 流程中的团队来说非常有用。你可以写个脚本，每天自动生成项目进度视频，或者自动把新发的博客文章转成视频。

### 写在最后

html-video 给我们展示了一种全新的视频制作方式。它不是要取代专业的剪辑师，而是要让每一个人都能轻松地制作出高质量的视频。

而且，这一切的成本都极低——你只需要一台电脑，不需要任何专业设备，也不需要给任何云端服务付费。

Open Design 团队用了3天时间写了3万行代码，给我们带来了这样一个革命性的工具。这就是开源的力量——一群聪明人聚在一起，就能改变世界。

如果你对这个项目感兴趣，不妨去 GitHub 上看看，给它一个 Star，或者直接上手试试。

GitHub地址：https://github.com/nexu-io/html-video

![[笔记同步助手/images/d71a6c29149a3520e6101b34e0d696de_MD5.gif||20]]

如果本文对您有帮助，也请帮忙点个 赞👍 + 在看 哈！❤️

**在看你就赞赞我！**

![[笔记同步助手/images/43fecf6d2ad8ac56602b0310aa6415da_MD5.gif||60]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9aa8c404_1780810767705?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwMjQ0NzI0OQ%3D%3D%26mid%3D2247506277%26idx%3D1%26sn%3Da2aa37f829bb846d2cde004e39abe6b3%26chksm%3Dc1852f61c0913d363e01f28402d9d721379890617121ca390c7b0d72740915750b58742c4e57%26mpshare%3D1%26scene%3D1%26srcid%3D0607rD4UFKZTT9E1eY5U3ibY%26sharer_shareinfo%3D0399597838760ea8a774e16d26e5e7df%26sharer_shareinfo_first%3De2abb1188e2d3de4e70645d60d658054%23rd&s=obsidian)