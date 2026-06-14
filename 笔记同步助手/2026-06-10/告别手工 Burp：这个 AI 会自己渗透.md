---
author: xiaoxxx
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2MzU2NDMzMA==&mid=2247487304&idx=1&sn=8fd241749c674a66f692f5838fb62724&chksm=cf499ef71b26db37a1197bb1f6a3f3ff7ee1766560a6c7e4022e4a1cc25115548bbb0c8e7bf1&mpshare=1&scene=1&srcid=06103WfJWsKe2v8YnB25NsWA&sharer_shareinfo=353365966571c65fa07e823988c11d06&sharer_shareinfo_first=353365966571c65fa07e823988c11d06#rd
saved: 2026-06-10 14:13:11
tags:
  - 笔记同步助手
id: 610c7ad6-284e-45c6-9371-e78579509fa3
---

公众号名称：稻草人安全团队

作者名称：xiaoxxx

发布时间：2026-06-10 12:00

法律声明：本工具仅供获得合法授权的安全测试使用，未经授权使用属于违法行为，使用者自行承担全部法律责任。

近期要agent的师傅越来越多，索性还是先开源，价值因人而异，不喜勿喷～

本人承诺：本次分享的内容和工具都不会做任何任何收费，不会去割韭菜，但是中国人骨子里的传统是“展示一代、装备一代、测试一代、研发一代”，考虑安全风险，本次开源的能力还是做了部分阉割，也希望各位大佬理解，后续会根据实际情况看是否继续做开源的优化。

题外话：关键能力早写完了，内部师傅也在试用，有一些产出，但不多。距离我构思的理想版本，我觉得能力还差很远。针对“skills开源”的话题和使用的朋友讨论了下，一致的结论都是让我不能给skills，给几个参考示列就行，在这里给个建议：使用的朋友去按照我给的模版让ai生成skills就行，我觉得效果也不会差～

回到正题：本次开源的能力如下（如果师傅们使用，辛苦用发财的小手点个star！！！）：

![[笔记同步助手/images/5fb731bc62ac7a5c4dd1ac19fb4677a0_MD5.png]]

我讲一下重点的几个功能使用：

1、智能对话，支持三种模式

1）批量模式：输入目标URL，自动执行全站渗透测试（爬虫→功能点分析→漏洞检测→报告）

2）实时模式：输入目标URL，边爬取边测试，发现功能点立即检测，实时输出结果

3）智能模式：自由对话，支持数据包分析、漏洞验证、危害证明、安全咨询等任意指令

![[笔记同步助手/images/96ea16202e84ed8118d59a4974f7dd07_MD5.png]]

使用案例：

1）用户问：“帮我对xxx进行渗透”

![[笔记同步助手/images/a641719965850a376438fee28bf5e585_MD5.png]]

2）用户问：“帮我判断这个数据包是否存在漏洞”

![[笔记同步助手/images/fb6c31033a51c83e74e7e82c706c3e2b_MD5.png]]

3）用户问：“这个数据包的参数xx存在xx漏洞，帮我进行危害证明”

![[笔记同步助手/images/bf2af03656e2debb4f13da72538b5df5_MD5.png]]

2、流量管理，支持所有的流量展示和筛选

![[笔记同步助手/images/13159c59325440ecbd6f54d76f281e5b_MD5.png]]

支持决策回放等

![[笔记同步助手/images/582acba6d825052801d25e10181cfa96_MD5.png]]

![[笔记同步助手/images/74aba3810cac221ec1ccf3d02a3bb3c2_MD5.png]]

3、支持burp插件，手动或者被动把要检测的数据包丢给agent

![[笔记同步助手/images/db1bb8b3e7b475050de855982fab497e_MD5.png]]

插件导入：

![[笔记同步助手/images/479a74126d1dbeda90105f930d6d3df6_MD5.png]]

4、支持自定义skills，考虑到实际的风险，skills最后用户自己去写

![[笔记同步助手/images/2f96c448507bf9e0b270aa353795489d_MD5.png]]

项目已经内置skills模版，按照模版填写即可：

![[笔记同步助手/images/740440f7b607e7a2f5eb5d81ef4853dd_MD5.png]]

其他功能不一一介绍了，各位大佬自行去体验。（本人也在找了个src的站点简单尝试了下，挖到了一个oss泄露和sql注入，我觉得很大一部分原因是这家src没啥难度）

另外，我近期花了些时间在agent的saas化上，进行了各种架构重构，比如说操作权限隔离、隧道流量隔离等，原因有二：

1、如果用户要对所在的内网环境系统做渗透，要支持流量可达

2、用户进行渗透，流量出口只能是自己的终端出口流量，不能是我的saas服务器

功能基本全部跑通，但是总感觉有点奇怪，也希望和大佬们深入交流～

项目地址： https://github.com/xiaoxxx-src/ScareAISec

希望所有朋友多转发点赞，让我有继续优化开源版本能力的动力，谢谢大家！！！

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c629ddf7_1781071990440?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MzU2NDMzMA%3D%3D%26mid%3D2247487304%26idx%3D1%26sn%3D8fd241749c674a66f692f5838fb62724%26chksm%3Dcf499ef71b26db37a1197bb1f6a3f3ff7ee1766560a6c7e4022e4a1cc25115548bbb0c8e7bf1%26mpshare%3D1%26scene%3D1%26srcid%3D06103WfJWsKe2v8YnB25NsWA%26sharer_shareinfo%3D353365966571c65fa07e823988c11d06%26sharer_shareinfo_first%3D353365966571c65fa07e823988c11d06%23rd&s=obsidian)