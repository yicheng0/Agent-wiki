---
author: 你说的完全正确
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247515145&idx=1&sn=330875a790c81cb381eddb75214e5273&chksm=cf1df22a6cdf768967b62a406dc661e731935265aa12304fcf7d1c13a2f073f0a91806a55bd2&mpshare=1&scene=1&srcid=0528rKjOOyGKJaibnmDoqpRb&sharer_shareinfo=3fdbdff42d3381c5283e4990e06f4bf3&sharer_shareinfo_first=3fdbdff42d3381c5283e4990e06f4bf3#rd
saved: 2026-05-28 09:17:50
tags:
  - 笔记同步助手
id: 12cfa5b3-3d32-4dd1-ab04-df881a3376af
---

公众号名称：AI寒武纪

作者名称：你说的完全正确

发布时间：2026-05-27 23:35

![[笔记同步助手/images/15c827e5ab91fc199af83feb3fa61ade_MD5.png]]

↑阅读之前记得关注+星标⭐️，😄，每天才能第一时间接收到更新

Claude写代码，测试报错，你解释哪里出问题，它修好了，又把别的地方搞坏。每次开新会话，同样的循环重来一遍。

Boris Cherny（Claude code创始人）最新采访爆料cc团队内部已经停止人为修复 Claude 的错误，他们现在让 Claude 自己修复它们

有一套配置能让Claude自动发现错误、自动修复、并且记住不再犯同样的错，Boris Cherny详细解释了这套配置。

![[笔记同步助手/images/d515312d6faaefe21861d1cf13cf71ba_MD5.png]]

  

---

### Claude为什么总犯重复错误

根本原因是Claude没有跨会话记忆。每次新会话都从零开始，昨天花20分钟修的bug，明天照样会出现。

CLAUDE.md能解决这个问题。Anthropic官方的使用指南里直接写了：每当Claude做错了什么，把它加进CLAUDE.md，让它知道不要再重复这个错误。

每次纠正完，在消息末尾加一句：更新你的CLAUDE.md，这样你就不会再犯这个错了。

Claude很擅长给自己写规则，问题是大多数人从来没让它这么做。

---

### 第一步：会自己成长的CLAUDE.md

CLAUDE.md应该随着每次错误不断扩充。不是写人格设定，而是写具体的、可执行的规则。

```
## 规则

- 绝对不要重构、重命名或清理无关代码
- 所有数据库查询走 services/，不要写在组件里
- 每次改完代码运行 npx tsc --noEmit
- 每次改完跑测试，失败了先修好再继续
- 提交前缀规范：feat:、fix:、docs:、refactor:、test:、chore:
- 绝对不用 enum，用字面量联合类型代替
- 绝对不要 force push，会覆盖共享历史
- 先跑 migration 再跑测试，顺序不能反

## 从错误中学到的

- 不要在 packages/ui 里装本该装在 apps/web 的包
- 不要把两种现有模式平均一下，选一种跟到底
- 不确定文件夹结构时，先查现有文件
- stop-loss 函数必须返回数字，不是布尔值（2026-05-12 生产环境出过问题）
```

关键是"从错误中学到的"这一节。每次纠正Claude之后，都加一句：更新CLAUDE.md，这样你就不会再犯这个错了。

坚持一个月，CLAUDE.md会积累下项目里Claude犯过的所有错误。错误率下降，因为Claude在开始工作之前会读一遍这份"不该做的事情清单"。

研究表明甜蜜点是12条规则、200行以内。超过这个范围，执行率会明显下降。

---

### 第二步：PostToolUse钩子，实时捕捉错误

钩子会在特定时机自动触发。PostToolUse在Claude写完或编辑完文件后立即运行，在问题扩散之前把它抓住。

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.ts)",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $file"
          }
        ]
      },
      {
        "matcher": "Write(*.ts)",
        "hooks": [
          {
            "type": "command",
            "command": "npx tsc --noEmit 2>&1 | head -20"
          }
        ]
      },
      {
        "matcher": "Write(*.tsx)",
        "hooks": [
          {
            "type": "command",
            "command": "npx eslint --fix $file"
          }
        ]
      }
    ]
  }
}
```

每个 .ts 文件：先用 Prettier 自动格式化，再做类型检查。每个 .tsx 文件：ESLint 自动修复。

Claude在同一轮对话里就能看到类型报错，立刻修掉再继续。

没有钩子的情况：Claude写完5个文件，你跑类型检查，3个文件共12个报错，你逐一解释。

有钩子的情况：每个文件写完就立刻检查，错误实时修复。

---

### 第三步：Stop钩子，质量门禁

这是最关键的钩子。Stop钩子在每次Claude说"我完成了"的时候触发，在Claude真正结束之前验证工作是否达标。

```
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "npm test 2>&1 | tail -5; echo \"Exit code: $?\""
          }
        ]
      }
    ]
  }
}
```

如果测试失败，Claude看到失败输出后会自动继续工作修复，不需要人工干预。

对于更复杂的验证，可以用 prompt 类型的钩子让Claude自己评估工作结果：

```
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "检查所有任务是否已完成。检查代码改动中是否有bug、遗漏的边界情况和测试覆盖。如果有未完成或有问题的地方，继续工作。如果一切正常，确认完成。"
          }
        ]
      }
    ]
  }
}
```

有一条关键规则必须记住：Stop钩子里一定要检查 stop\_hook\_active。

当这个值为 true，说明Claude已经因为前一个Stop钩子在继续工作，直接 exit 0 退出。不加这个检查，钩子会让Claude永远卡在循环里出不来。

---

### 第四步：PreToolUse钩子，错误发生之前就拦截

PreToolUse在Claude执行工具之前运行，用来过滤输入、阻止代价高昂的操作。

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(cat *log*)",
        "hooks": [
          {
            "type": "command",
            "command": "grep -n 'ERROR\\|WARN' $file | head -50"
          }
        ]
      },
      {
        "matcher": "Write(**/.env*)",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'BLOCKED: Cannot write to .env files' && exit 1"
          }
        ]
      }
    ]
  }
}
```

Claude要读一个1万行的日志文件？钩子先过滤，只给它50行错误。Claude要写 .env 文件？直接拦截，操作根本不会发生。

---

### 第五步：自动重试模式

对于需要多次尝试的任务，可以加上重试次数限制：

```
修复这些失败的测试。最多尝试3次。

每次尝试之后：
1. 跑测试
2. 如果通过，完成
3. 如果失败，读错误信息，换一种思路
4. 如果3次都失败，说明你尝试了什么、还有什么没修好

不要尝试同一个修法两次。
```

配合第三步的Stop钩子，这构成一个自我修复的闭环：Claude写代码，测试运行，失败了就读错误重新来，直到通过或者耗尽尝试次数。

必须设置次数上限。没有上限，Claude可能陷入无限重试，烧掉大量token。

---

### 第六步：跨会话记忆

钩子解决单次会话内的错误。记忆系统解决跨会话的重复错误。

```
# 查看Claude已记住的内容
/memory

# 手动添加规则
/memory add "这个项目用 pnpm，不是 npm"
/memory add "auth 模块在5月15日重构了，新模式在 src/lib/auth/v2/"
```

开启 Dreaming 功能后，Claude会在后台处理历史会话、自动积累持久知识，不需要手动添加。

三层组合：CLAUDE.md 捕获项目级规律，/memory 捕获会话级学习，Dreaming 每晚自动整合。

---

### 完整配置，可以直接复制

```
{
  "permissions": {
    "allow": [
      "Read", "Glob", "Grep", "LS", "Edit", "MultiEdit",
      "Write(src/**)", "Write(tests/**)",
      "Bash(npm test *)", "Bash(npx tsc *)", "Bash(npx prettier *)",
      "Bash(npx eslint *)", "Bash(git add *)", "Bash(git commit *)"
    ],
    "deny": [
      "Read(**/.env*)", "Write(**/.env*)",
      "Bash(rm -rf *)", "Bash(git push *)"
    ],
    "defaultMode": "acceptEdits"
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.ts)",
        "hooks": [
          { "type": "command", "command": "npx prettier --write $file" },
          { "type": "command", "command": "npx tsc --noEmit 2>&1 | head -20" }
        ]
      },
      {
        "matcher": "Write(*.tsx)",
        "hooks": [
          { "type": "command", "command": "npx prettier --write $file" },
          { "type": "command", "command": "npx eslint --fix $file" }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash(cat *log*)",
        "hooks": [
          { "type": "command", "command": "grep -n 'ERROR\\|WARN' $file | head -50" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "npm test 2>&1 | tail -10; echo \"Exit: $?\"" }
        ]
      }
    ]
  }
}
```

---

### 配置前后的对比

配置之前：

-   • Claude写代码，你跑测试，4个失败
    
-   • 你逐一解释每个失败
    
-   • Claude修了3个，顺带又引入1个新bug
    
-   • 你再次解释
    
-   • 每个功能来回45分钟
    
-   • 同样的错误明天还会出现
    

配置之后：

-   • Claude写代码，钩子自动格式化并检查每个文件
    
-   • Claude说完成，测试自动跑
    
-   • 测试失败，Claude读错误继续修
    
-   • CLAUDE.md 阻止昨天的错误重演
    
-   • 记忆系统阻止上周的错误重演
    
-   • 每个功能10分钟，大部分时间不需要盯着
    

\--end--

最后记得⭐️我，每天都在更新：如果觉得文章还不错的话可以点赞转发推荐评论

/...@作者：你说的完全正确（YAR师）

---

![[笔记同步助手/images/d678e69ff7b6d8c7869406dfa275eca4_MD5.jpg|cover_image]]

原创 你说的完全正确 AI寒武纪

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/8865eab9_1779931068440?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3MTkxMjYzOA%3D%3D%26mid%3D2247515145%26idx%3D1%26sn%3D330875a790c81cb381eddb75214e5273%26chksm%3Dcf1df22a6cdf768967b62a406dc661e731935265aa12304fcf7d1c13a2f073f0a91806a55bd2%26mpshare%3D1%26scene%3D1%26srcid%3D0528rKjOOyGKJaibnmDoqpRb%26sharer_shareinfo%3D3fdbdff42d3381c5283e4990e06f4bf3%26sharer_shareinfo_first%3D3fdbdff42d3381c5283e4990e06f4bf3%23rd&s=obsidian)