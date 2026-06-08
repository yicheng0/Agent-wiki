---
author: 别别人
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkzODk3MTIwMQ==&mid=2247489380&idx=1&sn=b2d68aac67c6e96d6f1ad3a6132c8aa3&chksm=c3b6ef10b72c50d4e992a718f8da0f4cf98042750cbea35a2d599cbb8874ba8f1bcb862cc4dd&mpshare=1&scene=1&srcid=0526A5GK9Z2ZL6vTIUeBQNe7&sharer_shareinfo=5e941b63a5a0840a7242a3358de3378e&sharer_shareinfo_first=05f50ea9d7edf970363dbdebdeb2f076#rd
saved: 2026-05-26 09:07:46
tags:
  - 笔记同步助手
id: 9020c0d6-01f0-4bab-9080-9c01780236a6
---

公众号名称：与AI同行之路

作者名称：别别人

发布时间：2026-05-26 00:06

前阵子跟一个做了七八年后端的老哥聊天,他说他用 Claude Code 大半年了,天天用,但总觉得没摸到门道。我让他描述一下日常怎么用,他说:打开终端,敲一句需求,等它回一段代码,粘进去,跑一下,不对再敲一句。

![[笔记同步助手/images/8ab8b1c840e428203abd610d60809772_MD5.jpg]]

我说哥,你这不是用 AI 编程,你这是把一个工作流引擎当微信对话框使了。

这话我也是有资格说的,因为我自己头小半年就是这么过来的。手动喂上下文,手动贴文件,手动复述项目背景,每开一个新会话都像第一次见面重新做自我介绍。技术上能用,但那个别扭劲儿,就跟拿黄油刀切牛排似的——切是能切下来,就是费劲得让人脸红。

转折点不是某个版本更新,工具本身一行代码没变。变的是我自己。我先翻到了一个网站,那个网站又链到另外几个,顺着摸下去,大概两个礼拜,我的 CLAUDE.md 能在每次会话自动带上项目背景了,hook 帮我自动格式化文件了,子代理开始替我审 PR 了。同一个工具,前后判若两人。

下面这 7 个网站,就是当时帮我把这条沟填平的。每个我都说清楚:它是啥,你能在上面找到什么,以及它教会我别处学不到的那一手。基本都是免费的。

​

---

## Claude Marketplaces —— 整个生态的实时目录

**网址:** https://claudemarketplaces.com/

![[笔记同步助手/images/cf0f59c4fd7a31f5af6170914b067b98_MD5.png]]

Claude Marketplaces 首页

`claudemarketplaces.com`,自称 Claude Code 插件、技能、MCP 服务器的头号目录,每月十七万开发者来逛。社区驱动,靠投票和质量筛,只有真有人装、仓库还活着的扩展才进得来。

打开首页那个搜索框,旁边写着六千七百多个技能、两千五百多个市场、八百多个 MCP 服务器。每个安装命令就一行,复制粘贴就能跑。

我看重它的点其实很朴素:这个生态变得太快了,任何一篇文章——包括我这篇——写完没几天就会过期。只有一个靠社区投票滚动更新的实时目录,才扛得住这个节奏。所以我把它当成"今天市面上有什么"的入口,而不是一篇攻略。

​

---

## Claude 101 —— 从没打开过到跑多代理的分级地图

**网址:** https://claude101.com/

![[笔记同步助手/images/87756dbd34bad1023ba3449bcfc6bbae_MD5.png]]

Claude 101 分级指南

`claude101.com`,一堆免费的、结构化的指南,把你从"我从来没打开过 Claude"一路领到"我在跑多代理工作流"。

它最聪明的地方是分了级。Level 1 是给纯小白的,什么 Claude For Dummies、怎么给新版 Opus 写提示词、怎么考个 Claude 认证。往上 Level 2 开始讲团队协作、设计、技能这些。再往上就是不让 Claude 拍马屁、让它说话像你而不像个 AI 这类进阶活儿,最后才到 Claude Code、Claude 电脑端。

我推荐它给团队里的新人,就是因为这个台阶设计得好。人最容易卡死的地方,是不知道自己现在站在哪一级、下一步该够哪儿。这网站等于把整条学习路径画成了地图,你照着爬就行。

​

---

## claude-code-ultimate-guide —— 一个法国人肝出来的开源宝库

**网址:** https://github.com/FlorianBruniaux/claude-code-ultimate-guide

![[笔记同步助手/images/7802be6778bb8638b2c4c29791c8ac96_MD5.png]]

claude-code-ultimate-guide 仓库

GitHub 上 Florian Bruniaux 维护的一个大仓库,四千五百多颗星,六百多次提交。从入门到高阶,带一堆能直接拿去用的生产级模板、智能体工作流指南,还有测验和速查表。开源协议是 CC-BY-SA-4.0。

我以前写 CLAUDE.md 全靠从零手搓,每个项目都重来一遍。这个仓库直接给了我一套模板,改一行——把语言换成我项目的——就跑起来了。

里头那个叫 `security-guardian` 的代理我印象最深。它会按 OWASP Top 10 那套去扫,给你指到具体哪一行、建议怎么改。有一次它在我一个 PR 里捞出三个问题,而那个 PR 我的人工 reviewer 是看过的、放行了。这事让我后背有点凉:不是说 AI 比人强,是人在重复劳动里注意力会塌,而它不会累。

​

---

## Anthropic Academy —— 做工具的人亲自教你怎么用

**网址:** https://anthropic.skilljar.com/

![[笔记同步助手/images/e395b19743e0aa9b03882cfa13b4bb06_MD5.png]]

Anthropic Academy 课程页

`anthropic.skilljar.com`,Anthropic 官方的培训平台,自主学习,完全免费。课程不多但都是正主出的:Claude 101、Claude Code 101、还有 Claude Cowork 入门。

我从那门 Claude Code 的课里捡到的最值钱的东西,是 Anthropic 内部团队自己在用的那套节奏——先探索,再规划,然后才写代码,最后提交。

这事说穿了不值钱,但没人点你你就是想不到。我以前的毛病是上来就"把这个 bug 修了",然后 Claude 信心十足地把错的问题给解决了。现在我会先让它"把这个模块相关的代码摸一遍",再让它"在动手前先把修复方案规划出来"。前面多花三分钟铺上下文,后面省下二十分钟返工。

做工具的人愿意花力气写一份正经教程教你怎么用好它,这在 AI 工具圈里其实挺少见的,Anthropic 这块做得地道。

​

---

## awesome-claude-code —— 一份有人替你做过判断的清单

**网址:** https://github.com/hesreallyhim/awesome-claude-code

![[笔记同步助手/images/2cd53e836c26bed82a235bf2228c7939_MD5.png]]

awesome-claude-code 仓库

GitHub 上 hesreallyhim 维护的仓库,四万四千多颗星。技能、hook、斜杠命令、代理编排器、应用、插件,都收。

市面上那种 "awesome-xxx" 清单你见多了,通病是一股脑塞五百个链接就完事,塞进去就再没人管。这份不一样,它是经过筛的——不合用的会被踢掉,留下的还打了标签告诉你实际拿来干嘛。

我顺着这份清单挖到了三个现在每天都在用、不然根本不会知道的东西:一个能实时显示 token 用量的状态栏,一个 Claude 跑完长任务会"叮"一声提醒我的 hook,还有一套现成的 CLAUDE.md 模板。光那套模板,每开一个新仓库就帮我省掉一个钟头的初始配置。价值就在这个"有人替你筛过"上头。

​

---

## ClaudeFast —— 官方文档还没来得及写的那部分

**网址:** https://claudefa.st/blog

![[笔记同步助手/images/062c28cc38750e6cddd80b70b67404a9_MD5.png]]

ClaudeFast 博客

`claudefa.st/blog`,一个技术博客,专门发 Claude Code 各种功能的深度指南,每周更,而且常常是官方文档都还没覆盖到的角落。每篇都标了对应的 Claude Code 版本号,这点很贴心,因为这工具迭代太快,不标版本的攻略基本等于过期食品。

我在它那儿解开过一个困扰我好几天的怪事。当时我装了二十多个技能,结果发现有几个死活不生效,翻官方文档翻不出原因。后来在 ClaudeFast 上看到一篇,讲 Claude Code 有个限制加载到系统提示里的技能数量的预算设置,我装太多超了上限,有些技能就被悄悄削掉了,连个报错都没有。我把预算调了调、把真正常用的技能排到前面,一切就顺了。

这种东西你在官方文档里是找不到的,因为当时压根还没被写进去。

​

---

## r/ClaudeCode —— 一线开发者真刀真枪的现场

**网址:** https://www.reddit.com/r/ClaudeCode/

![[笔记同步助手/images/2123d99b59db64187e3166f11f232460_MD5.png]]

reddit

前面六个偏"资料",这第七个是"人"。`reddit.com/r/ClaudeCode`,目前 Claude Code 用户里最大、最活跃的社区,每周几千号贡献者,把第二名的 AI 编程代理子版块甩出去一大截。

关键是,它不是个报障答疑的客服论坛。开发者在这儿发的是工作流、是配置文件、是跑分、是实战复盘——那种"我这么搭了一套,踩了哪些坑,最后快了多少"的帖子。文档教你"应该怎么做",这里让你看到"别人到底是怎么做的、做完什么效果"。

我自己的习惯是把它当雷达。新功能出来,官方文档往往还在路上,但社区里已经有人连夜试过、把翻车和真香都贴出来了。这种来自一线的、带着体温的信息,是任何一份静态文档给不了的。

​

---

## 多数人卡在哪儿

写到这儿你大概看出来了,这 7 个网站串起来不是孤立的:Marketplaces 告诉你有什么,Claude 101 和 Anthropic Academy 告诉你怎么入门进阶,awesome-claude-code 替你筛过料,ultimate-guide 给你能直接抄的模板,ClaudeFast 补上官方文档的盲区,最后 r/ClaudeCode 让你看见一线开发者真实在怎么折腾。

我见过太多人的成长曲线长一个样:装上 Claude Code,学几个基础命令,可能再挂一台 MCP 服务器,然后……就这么用上好几个月,停在原地。

而那些真正捅破窗户纸的人,往往就是花了一个周末,从"基础阶段"挪到了"配置阶段"。一旦跨过去,会话开始自动带上下文,代理开始审你的代码,hook 开始强制执行你的规范——然后他们的干活速度,就跟之前不在一个量级了。

工具一直在那儿,门道也一直在那儿。差的只是有没有人把那扇门指给你看。这 7 个网站,就是我当年的那几扇门。

​

---

## 网址清单,方便你收藏

-   • Claude Marketplaces:https://claudemarketplaces.com/
    
-   • Claude 101:https://claude101.com/
    
-   • claude-code-ultimate-guide:https://github.com/FlorianBruniaux/claude-code-ultimate-guide
    
-   • Anthropic Academy:https://anthropic.skilljar.com/
    
-   • awesome-claude-code:https://github.com/hesreallyhim/awesome-claude-code
    
-   • ClaudeFast:https://claudefa.st/blog
    
-   • r/ClaudeCode:https://www.reddit.com/r/ClaudeCode/
    

---

_本文配图为上述网站 2026 年 5 月的实时截图,生态更新很快,以各站当前内容为准。_

  

---

![[笔记同步助手/images/a19811aba10c50cb5b5d1203db911606_MD5.jpg|cover_image]]

Original 别别人 与AI同行之路

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/a7a2dc0a_1779757664881?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkzODk3MTIwMQ%3D%3D%26mid%3D2247489380%26idx%3D1%26sn%3Db2d68aac67c6e96d6f1ad3a6132c8aa3%26chksm%3Dc3b6ef10b72c50d4e992a718f8da0f4cf98042750cbea35a2d599cbb8874ba8f1bcb862cc4dd%26mpshare%3D1%26scene%3D1%26srcid%3D0526A5GK9Z2ZL6vTIUeBQNe7%26sharer_shareinfo%3D5e941b63a5a0840a7242a3358de3378e%26sharer_shareinfo_first%3D05f50ea9d7edf970363dbdebdeb2f076%23rd&s=obsidian)