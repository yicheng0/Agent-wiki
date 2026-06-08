---
author: ColaAI
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4MTAwMQ==&mid=2247484077&idx=1&sn=da8a75705c000b62f8d9b3dc57e2c4fd&chksm=cfde190d40e905c66ef1b7ea45bff0f4369f1f651fc436a15bfecd43673810027dc2ee8be81c&mpshare=1&scene=1&srcid=0524jpA2y1qdPdYMc8Xl4zQd&sharer_shareinfo=773dfea237c36603a80dda0f8c5cbfdb&sharer_shareinfo_first=773dfea237c36603a80dda0f8c5cbfdb#rd
saved: 2026-05-24 11:49:52
tags:
  - 笔记同步助手
id: ed6c0887-7ca1-4b98-b209-d446aea57ba3
---

公众号名称：ColaAI

作者名称：ColaAI

发布时间：2026-05-16 07:24

![[6e0b237d29bf71dc2ae6803a037acf5b_MD5.png]]

14个反爬检测全部通过。reCAPTCHA v3给出了0.9的分数——一个连真人都未必拿得到的分数。Cloudflare Turnstile直接放行。

这不是某个商业反检测浏览器的数据，而是一个刚上GitHub不久、开源免费、只用一行代码替换Playwright就能跑起来的Python库。

它叫CloakBrowser。如果你写过爬虫、做过自动化测试、或者哪怕只是被Cloudflare那个5秒等待页面恶心过——这篇文章你得看完。

![[5fe4d8e670e0383ff7a0363817d4acf4_MD5.png]]

一个让所有爬虫工程师集体破防的项目

​

搞过爬虫的人都懂一件事：现在的网页早就不是「请求一下HTML就能拿到数据」的时代了。

Cloudflare、Akamai、DataDome这些反爬服务商已经把检测做到了什么程度？它们能识别你的浏览器是不是「真的浏览器」、你的鼠标轨迹像不像人、你的TLS握手指纹和真Chrome能不能对上、甚至你Canvas画出来的图像哈希值和已知设备库里的能不能匹配。

传统对抗手段呢？基本失效了。

​

> playwright-stealth靠JS注入改属性,被识别;undetected-chromedriver靠配置改启动参数,被识别;puppeteer-extra插件层面的修补,统统被识别。
> 
> ​
> 
> 它们的问题是同一个:在JS运行时层面打补丁,反爬系统在C++渲染层就把你抓了。

去年圈内还有一个明星项目叫Camoufox,基于Firefox魔改,效果不错。但因为开发者健康原因,从2025年开始进入了长达一年的维护停滞——而这一年正是反爬技术升级最猛的一年。

Chromium这边几乎是一片荒原。

然后CloakBrowser出现了。

• • •

​

它到底牛在哪？一个数字说话

​

我先把官方的测试结果摆这里,大家自己感受一下落差有多大。

​

> 🎯 reCAPTCHA v3评分
> 
> ​
> 
> 原版Playwright:0.1分(妥妥的机器人)
> 
> CloakBrowser:0.9分(人类水平,服务端验证通过)

> ☁️ Cloudflare Turnstile挑战
> 
> ​
> 
> 原版Playwright:FAIL
> 
> CloakBrowser:PASS(非交互式直接自动解锁)

> 🔍 FingerprintJS指纹检测
> 
> ​
> 
> 原版Playwright:DETECTED(被识别)
> 
> CloakBrowser:PASS(数据正常返回)

还有bot.incolumitas.com的检测——原版Playwright失败13项,CloakBrowser只失败1项(还是WEBDRIVER规范本身要求保留的)。deviceandbrowserinfo.com上,原版有6个机器人标记,CloakBrowser是0个。

​

"

​

14个测试,通过14个。这不是「比同行强一点」,这是「换了一个赛道」。

• • •

​

它凭什么这么猛?核心思路只有一句话

​

传统反检测工具都在做一件事——在浏览器跑起来之后,用JS或者启动参数去「打补丁」掩盖马脚。比如改一下navigator.webdriver、改一下UA字符串、伪造一下plugins列表。

问题是,反爬系统也在进化。它们不再只看你浏览器报出来的那些属性,而是直接看渲染层的实际表现:

​

1​

你的Canvas画一张图,渲染出来的像素哈希值和真Chrome一致吗?

2​

你的WebGL Renderer字符串和你声称的硬件配置匹配吗?

3​

AudioContext生成的音频指纹是不是有JS拦截过的痕迹?

4​

你的TLS握手指纹(JA3、JA4)跟Chrome的实际网络栈一致吗?

JS层面再怎么打补丁,这些底层信号都改不了。这就是为什么所有JS注入式方案都正在被反爬系统快速识别——它们改的是「门面」,但反爬看的是「地基」。

​

> 💡 划重点
> 
> ​
> 
> CloakBrowser的做法是:直接改Chromium的C++源代码,做了16个底层补丁,然后重新编译成二进制。这意味着指纹是从「地基」开始就是干净的,反爬系统看到的就是一个真正的Chrome——因为它**真的就是**一个修改过的Chrome。

16个补丁覆盖了Canvas指纹、WebGL渲染器、音频处理、字体枚举、硬件并发数、GPU信息、WebDriver标识、Headless检测信号等等——基本就是反爬系统会查的所有指纹点。

• • •

​

用起来有多简单?一行代码

​

很多反检测方案,光是上手就够你折腾半天——要么换一个全新的API、要么要装一堆驱动、要么要自己编译。CloakBrowser的设计哲学完全不同:

​

> 你写的还是Playwright,只是换了一个import。

安装一句话:

​

> pip install cloakbrowser

第一次跑的时候,会自动下载它定制编译的Chromium二进制(约200MB,缓存到本地),后面就直接用。

代码长这样:

​

> from cloakbrowser import launch
> 
> ​
> 
> browser = launch()
> 
> page = browser.new\_page()
> 
> page.goto("https://protected-site.com")
> 
> browser.close()

就这。返回的browser对象是标准的Playwright Browser实例——你之前写的所有Playwright代码,改一行import就能直接用。

​

> ✗ 原版Playwright
> 
> ​
> 
> from playwright.sync\_api import sync\_playwright  
> pw = sync\_playwright().start()  
> browser = pw.chromium.launch()

> ✓ CloakBrowser
> 
> ​
> 
> from cloakbrowser import launch  
> browser = launch()

迁移成本几乎为零。这才是真正的「drop-in replacement」。

• • •

​

和现有方案比,差距有多大?

​

我把市面上几个主流方案的关键指标拉个清单,你一眼就能看出来差距:

​

> 📊 主流方案横向对比
> 
> ​
> 
> playwright-stealth
> 
> ​
> 
> reCAPTCHA分数0.3-0.5 ·补丁层级JS注入 ·维护已停滞 ·Chrome更新就坏
> 
> undetected-chromedriver
> 
> ​
> 
> reCAPTCHA分数0.3-0.7 ·补丁层级 配置参数 ·维护已停滞 ·只支持Selenium
> 
> Camoufox
> 
> ​
> 
> reCAPTCHA分数0.7-0.9 ·补丁层级C++(Firefox)·2025年起维护停滞
> 
> CloakBrowser ⭐
> 
> ​
> 
> reCAPTCHA分数 **0.9**·补丁层级 **C++(Chromium)**·积极维护中 ·原生Playwright API

几个关键点:

**Chromium不是Firefox。**Camoufox的核心问题是它基于Firefox——而你要爬的99%的网站都是按Chrome优化的,Firefox的TLS指纹一甩出来就是异类。CloakBrowser基于Chromium,TLS握手指纹直接和真Chrome一模一样。

**C++补丁不是JS注入。**这是本质区别。JS注入会留下痕迹——你重写了Function.prototype.toString,反爬系统一查就发现这函数被改过。C++补丁是编译进二进制的,反爬系统看不到任何运行时痕迹。

**能扛住Chrome更新。**JS注入的方案每次Chrome大版本更新都要重写,因为浏览器内部API一变,补丁就贴不上了。C++源码层的补丁不受影响,只需要在新版本Chromium上重新编译一次。

• • •

​

哪些人应该立刻试试?

​

这个工具不是万能的,但有几类需求,它就是当前最优解:

​

01​

数据采集类爬虫工程师

​

尤其是要爬电商、社交媒体、新闻聚合、招聘网站这类用了Cloudflare/DataDome的目标。以前要花一半时间和反爬周旋,现在可以专心写业务逻辑。

02​

做AI Agent的开发者

​

如果你在做能自动浏览网页的AI助手——OpenAI的Operator、Claude的Computer Use这类——后端浏览器一定要扛得住反检测,不然agent还没开始干活就被弹CAPTCHA。

03​

做自动化测试的QA

​

在线上用真用户身份做端到端测试时,有些测试场景会被自家公司的反爬系统误杀——CloakBrowser可以解决这个尴尬。

04​

做SEO/SEM监测的

​

大批量抓取搜索引擎结果、监测关键词排名、追踪竞品价格——这类场景几乎每天都在和反爬斗智斗勇。CloakBrowser能极大降低被ban率。

• • •

​

几个不能不说的真相

​

吹了这么多,也得说几句冷静话。

​

### ① 它不是万灵药

反爬是一场永远不会结束的军备竞赛。源码级补丁比JS注入级难检测,但「难检测」≠「无法检测」。Cloudflare、Akamai这些大厂每天都在升级算法,一年后CloakBrowser能不能保持现在的成功率,谁也不敢打包票。

​

### ② 平台支持还不全

目前只支持Linux x86\_64。macOS arm64(M系列芯片)还在路上,Windows更是远期计划。如果你用Mac开发,要么换Docker要么等等。

​

### ③ 200MB的二进制文件

第一次安装会拉一个约200MB的定制Chromium二进制——这是C++补丁路线的必然代价。它不像JS方案那么轻量,但比起一个被ban掉的爬虫,这点磁盘空间和带宽根本不算事。

​

### ④ 仓库还很年轻

GitHub上star数还在32左右,只有6次提交。看得出来作者把精力都花在底层那16个C++补丁上了,周边的文档、测试、社区还在建设中。早期使用者会享受到第一波红利,但也要承担「这个项目万一不维护了怎么办」的风险。

​

> ⚠️ 法律和道德提示
> 
> ​
> 
> CloakBrowser本身只是一个浏览器,使用合法。但你用它做什么,责任在自己。爬取公开数据不违法,但破解付费内容、绕过反爬抓取个人隐私、做羊毛党刷单——这些事再好的工具也不会让你逃过法律。

• • •

​

最后一句话

爬虫这个领域,过去5年的主旋律是反爬技术疯狂升级、自动化工具集体破防。很多老牌方案进入了维护停滞,新的商业方案动辄一个月几百美元的订阅费。

CloakBrowser的出现给Chromium生态填上了一个空白:用开源、免费、零迁移成本的方式,提供了一个能打的源码级反检测浏览器。

"

​

一行import换掉Playwright,就拿到了一个真正能打的反检测浏览器。

这件事本身,就是2026年开源世界最有意思的事之一。

如果你正好在被反爬折磨,直接去试一下:

> pip install cloakbrowser

项目地址:github.com/CloakHQ/CloakBrowser

用之前先在仓库点个star,顺便也帮作者一把——这种作者一个人扛起来的硬核开源项目,值得被更多人看见。

> 如果觉得这篇有用
> 
> ​
> 
> 点个「关注」,转发给你认识的爬虫朋友  
> 关注我,继续聊那些值得早知道的开源项目

---

![[66095e32d2ec5d1df815355e08eb7ed1_MD5.jpg|cover_image]]

Original ColaAI ColaAI

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/a824a177_1779594590791?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2NTA4MTAwMQ%3D%3D%26mid%3D2247484077%26idx%3D1%26sn%3Dda8a75705c000b62f8d9b3dc57e2c4fd%26chksm%3Dcfde190d40e905c66ef1b7ea45bff0f4369f1f651fc436a15bfecd43673810027dc2ee8be81c%26mpshare%3D1%26scene%3D1%26srcid%3D0524jpA2y1qdPdYMc8Xl4zQd%26sharer_shareinfo%3D773dfea237c36603a80dda0f8c5cbfdb%26sharer_shareinfo_first%3D773dfea237c36603a80dda0f8c5cbfdb%23rd&s=obsidian)