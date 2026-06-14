---
author: 文/职场向上
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzAwOTY5NTU2MQ==&mid=2647652199&idx=1&sn=25504810051562a2d00947563882c9f9&chksm=823c844a165420bdeb0ece2a844e19088d2ba5bf862caa26848961cd35f63459e9c33272fcf8&mpshare=1&scene=1&srcid=06139B18RMFpAGaT8THo7Elz&sharer_shareinfo=67c475465472f990048d580975e80cc3&sharer_shareinfo_first=67c475465472f990048d580975e80cc3#rd
saved: 2026-06-13 00:56:00
tags:
  - 笔记同步助手
id: e6e15ef1-5a94-462e-a04e-9ac94cee794e
---

公众号名称：职场向上生长力

作者名称：文/职场向上

发布时间：2026-06-08 18:40

  

> 上一篇串了一遍流程，很多人反馈"大框架懂了，但每个环节到底怎么交互的？文档长什么样？代码怎么组织的？"这一篇，我们把镜头拉到最近一次真实开发——给团队内部的威胁情报平台加一个"按周统计分析"功能，从一句话需求到最终归档，每个环节的文档内容、交互细节、命令行操作、代码结构全部展开（有脱敏）。

## 一、需求背景：为什么要做这个功能

团队有一个内部威胁情报平台，核心功能是接收各渠道的 IOC（Indicators of Compromise，威胁指标），存储到数据库，供 SOC 分析员查询。

现有问题：分析员每周要手动统计"本周新增了多少 IOC"、“哪些类型最多”、“哪些来源贡献最大”。这个统计工作每周花 2-3 小时，而且容易出错。

需求：**加一个按周统计分析功能，自动生成周报，包含 IOC 数量趋势、类型分布、来源贡献排名、高危 IOC 高亮。**

这个需求的特点是：**后端逻辑明确，前端交互复杂，涉及多表联查和可视化图表**。正好适合用 SDD 流程来跑一遍。

## 二、阶段一：OpenSpec 需求对齐

### 2.1 2.1 启动 Claude Code，输入需求

打开终端，进入项目目录，启动 Claude Code：

```
cd ～/projects/threat-intel-platform
claude
```

进入 Claude Code 会话后，直接用一句话描述需求：

```
> 给情报平台加一个按周统计分析功能，自动生成周报
```

就这一句话。不需要写 PRD，不需要画流程图。这是 SDD 和传统开发最大的区别——**需求的起点是一句话，但终点是一份结构化规范**。

### 2.2 2.2 AI 自动生成四份核心文档

Claude Code 收到需求后，会调用 OpenSpec 的 propose 流程，自动在 `openspec/changes/weekly-analytics/` 下创建文档。你不需要手动创建目录或文件，AI 全部搞定。

这个过程中，Claude Code 会在终端显示它的操作：

```
我来为这个需求创建 OpenSpec 变更提案...

正在创建变更目录：openspec/changes/weekly-analytics/
正在生成 proposal.md...
正在生成 design.md...
正在生成 tasks.md...
正在生成 specs/weekly-analytics/spec.md...

变更提案已创建完成。请确认以下文档：
  - openspec/changes/weekly-analytics/proposal.md
  - openspec/changes/weekly-analytics/design.md
  - openspec/changes/weekly-analytics/tasks.md
  - openspec/changes/weekly-analytics/specs/weekly-analytics/spec.md
```

生成的文档结构：

```
openspec/changes/weekly-analytics/
├── proposal.md          ← 做什么：背景、目标、范围
├── design.md            ← 怎么做：技术方案、模块设计
├── tasks.md             ← 分几步：原子任务拆解
└── specs/
    └── weekly-analytics/
        └── spec.md      ← 做成什么样：功能规格定义
```

### 2.3 2.3 审核文档：在命令行里怎么操作？

AI 生成完文档后，会等你确认。这时候你可以用两种方式审核：

**方式一：让 Claude Code 帮你展示文档内容**

在终端直接说：

```
> 把 proposal.md 的内容给我看看
```

Claude Code 会读取文件并展示内容：

```
# 变更提案：按周统计分析功能

## 背景
SOC 分析员每周需要手动统计 IOC 数据，耗时 2-3 小时，容易出错。

## 目标
实现按周统计分析功能，自动生成周报，减少人工统计工作量。

## 范围
- 后端：新增周统计 API，支持按时间范围查询
- 前端：新增周统计页面，包含图表和数据表格
- 数据：基于现有 IOC 表进行聚合查询，不新增数据表

## 不做什么（边界）
- 不做实时统计（只做按周批量计算）
- 不做导出 PDF（后续迭代）
- 不做自定义时间范围（只支持自然周）
```

**方式二：另开终端窗口，用编辑器直接看**

```
# 另开一个终端窗口
vim ～/projects/threat-intel-platform/openspec/changes/weekly-analytics/proposal.md
```

或者用 VS Code：

```
code ～/projects/threat-intel-platform/openspec/changes/weekly-analytics/
```

### 2.4 2.4 提出修改：在命令行里怎么改？

审核后发现需要修改。**不需要手动编辑文件**，直接在 Claude Code 里用自然语言说：

```
> 范围不对，自定义时间范围必须做，分析员经常需要看"最近 30 天"而不只是自然周
```

Claude Code 会自动更新相关文档：

```
好的，我来更新 proposal.md 和 tasks.md...

已更新 proposal.md：
  - 范围新增：支持自定义时间范围查询
  - 删除"不做什么"中的"不做自定义时间范围"

已更新 tasks.md：
  - Task 2 新增 Step：实现自定义时间范围参数解析
  - Task 3 新增 Step：前端增加日期范围选择器

请确认修改是否符合预期。
```

再看另一个修改点：

```
> IOC 表的数据量有多大？如果是百万级，聚合查询会不会很慢？
```

AI 分析后给出建议：

```
IOC 表目前有 50 万条记录。按周聚合查询大约需要 3-5 秒。

建议：增加一个周统计汇总表，定时任务每天凌晨跑一次，
把结果写入汇总表，API 直接查汇总表，响应时间 < 100ms。

是否采纳这个方案？
```

你确认：

```
> 采纳，更新 design.md
```

### 2.5 2.5 任务拆解审核

tasks.md 的内容：

```
# 任务清单

## Task 1：后端 - 周统计核心逻辑
- [ ] Step 1.1：实现日期工具函数（获取指定周的起止日期）
- [ ] Step 1.2：实现 IOC 总量统计查询
- [ ] Step 1.3：实现类型分布统计查询
- [ ] Step 1.4：实现来源 TOP10 统计查询
- [ ] Step 1.5：实现高危 IOC 筛选逻辑
- [ ] Step 1.6：编写单元测试

## Task 2：后端 - API 接口
- [ ] Step 2.1：定义 API 路由和参数校验
- [ ] Step 2.2：实现接口逻辑，调用 Task 1 的核心函数
- [ ] Step 2.3：编写接口测试

## Task 3：前端 - 周统计页面
- [ ] Step 3.1：创建页面组件，搭建布局
- [ ] Step 3.2：实现周选择器组件
- [ ] Step 3.3：实现关键指标卡片
- [ ] Step 3.4：集成折线图（趋势图）
- [ ] Step 3.5：集成饼图（类型分布）
- [ ] Step 3.6：实现来源排名表格
- [ ] Step 3.7：实现高危 IOC 列表
- [ ] Step 3.8：联调后端 API
```

你觉得粒度可以，确认：

```
> tasks.md 没问题，确认进入下一步
```

**关键点**：这四份文档就是后续所有开发工作的"唯一真相源"。AI 写代码时，必须严格按照 tasks.md 的步骤来；审查代码时，必须对照 spec.md 来检查。

## 三、阶段二：Superpowers 头脑风暴

OpenSpec 确认后，Superpowers 的 brainstorming 技能**自动触发**。你不需要手动调用任何命令，Claude Code 检测到 OpenSpec 提案已确认，会自动进入 brainstorming 流程。

### 3.1 3.1 苏格拉底式追问的实际对话

终端里会出现这样的交互：

```
[Superpowers: Brainstorming] 已自动触发

AI: 周报的数据来源是实时查询还是预计算？IOC 表目前有 50 万条
    记录，按周聚合查询大约需要 3-5 秒。如果前端要做实时切换
    不同周的数据，每次切换都要等 3-5 秒，体验会很差。

    方案 A：实时查询，简单但慢
    方案 B：预计算汇总表，快但需要定时任务维护
    方案 C：实时查询 + 缓存，第一次慢，后续快

    推荐方案 B，因为数据只需要每天更新一次。
```

你直接在命令行回复：

```
> 选 B，加汇总表
```

AI 继续追问：

```
AI: 好的。那汇总表的更新频率是每天凌晨一次，还是每小时一次？
    SOC 分析员通常在上午 10 点左右查看周报，如果凌晨 2 点
    跑定时任务，数据是到前一天 23:59 的，不影响。
```

```
> 每天凌晨 2 点跑一次就行
```

```
AI: 明白。接下来一个问题：高危 IOC 的定义是什么？是 CVSS 分
    数超过 7.0？还是标记为"critical"的？还是有其他标准？
```

```
> 按照我们平台现有的 severity 字段，severity >= 4 就算高危
```

```
AI: 好的。还有最后一个问题：周选择器的交互方式。你希望是：
    方案 A：下拉框选择年份 + 周数（如 2024-W23）
    方案 B：日期范围选择器（选择任意一天，自动定位到所在周）
    方案 C：左右箭头切换上一周/下一周

    推荐方案 B + C 组合，既灵活又方便快速切换。
```

```
> 就用 B + C
```

### 3.2 3.2 这个阶段产出什么？

每次问答后，Claude Code 会自动更新设计决策文档：

```
[Superpowers: Brainstorming] 已更新设计决策记录
  → docs/superpowers/specs/weekly-analytics/design-decisions.md
```

生成的决策记录：

```
# 设计决策记录

## 决策 1：数据查询策略
- 选择：预计算汇总表
- 原因：IOC 表数据量大（50 万+），实时聚合查询慢（3-5 秒）
- 方案：定时任务每天凌晨 2 点跑一次，结果写入 weekly_stats 表

## 决策 2：高危 IOC 定义
- 选择：severity >= 4
- 原因：与平台现有标准一致

## 决策 3：周选择器交互
- 选择：日期范围选择器 + 左右箭头切换
- 原因：灵活 + 快速切换
```

**这份决策记录的价值**：三个月后，有人问"为什么用汇总表而不用实时查询？"——不用翻聊天记录，看这份文档就行。

## 四、阶段三：Writing Plans — 任务细化到原子操作

Brainstorming 完成后，Superpowers **自动**进入 writing-plans 阶段。同样不需要你手动触发。

终端显示：

```
[Superpowers: Writing Plans] 已自动触发
正在细化 tasks.md，为每个 step 补充输入、输出、验收标准...
```

### 4.1 4.1 任务计划的实际产出

Claude Code 会把 tasks.md 中的每个 step 进一步细化：

```
# Task 1：后端 - 周统计核心逻辑

## Step 1.1：实现日期工具函数
- 输入：一个日期字符串（如 "2024-06-08"）
- 输出：该日期所在周的起止日期（start_date, end_date）
- 验收标准：
  - 输入 "2024-06-08"（周六），返回 ("2024-06-03", "2024-06-09")
  - 输入 "2024-01-01"（跨年），返回 ("2023-12-25", "2024-01-01")
  - 单元测试覆盖正常日期、跨月、跨年三种情况

## Step 1.2：实现 IOC 总量统计查询
- 输入：start_date, end_date
- 输出：该时间范围内的 IOC 总数（整数）
- 验收标准：
  - 查询语句使用 COUNT(*)，WHERE created_at BETWEEN start AND end
  - 空范围返回 0，不抛异常
  - 单元测试覆盖：有数据、无数据、跨月数据三种情况
```

### 4.2 4.2 人类在这一步的操作

审核计划的合理性。在命令行里：

```
> Step 1.2 到 1.5 都是类似的聚合查询，能不能抽象一个通用的聚合函数？
```

Claude Code 分析后回复：

```
可以，但会增加一个中间抽象层。对于当前的 4 个统计维度，
各自的 SQL 查询逻辑差异较大（GROUP BY 字段不同、JOIN 条件不同），
强行抽象反而会增加复杂度。

建议保持当前拆分方式，每个 step 职责单一，便于测试和维护。
是否接受这个建议？
```

```
> 行，保持原样
```

**这一步的核心原则**：每个 step 必须是**原子的**——一个子代理调用就能完成，完成后可以立即验证。

## 五、阶段四：子代理执行 — 开发的核心环节

这是整个流程中最核心的环节。

### 5.1 5.1 启动执行：在命令行里怎么触发？

Writing Plans 完成后，Claude Code 会问你是否开始执行。你只需要：

```
> 开始执行
```

或者如果你想指定用子代理模式（Subagent-Driven Development）：

```
> 用子代理模式开始执行 tasks.md
```

Claude Code 会确认执行模式：

```
[Superpowers: Execution] 启动子代理驱动开发模式

执行计划：
  - Task 1：后端 - 周统计核心逻辑
  - Task 2：后端 - API 接口
  - Task 3：前端 - 周统计页面

每个 Task 将由三个子代理协作完成：
  1. Implementer（实现者）— 写代码 + 测试
  2. Spec Compliance Reviewer（规格审查员）— 检查是否符合规范
  3. Code Quality Reviewer（质量审查员）— 检查代码质量

开始执行 Task 1/3...
```

### 5.2 5.2 Implementer 执行 Step 1.1

Implementer 的工作方式是 **TDD**——先写测试，再写实现：

```
# Implementer 先写测试（TDD）
def test_get_week_start_end_normal_date():
    """正常日期：周六应该返回周一到周日"""
    start, end = get_week_start_end("2024-06-08")
    assert start == "2024-06-03"
    assert end == "2024-06-09"

def test_get_week_start_end_cross_year():
    """跨年日期：1月1日应该返回去年的最后一周"""
    start, end = get_week_start_end("2024-01-01")
    assert start == "2023-12-25"
    assert end == "2024-01-01"

# Implementer 再写实现
from datetime import datetime, timedelta

def get_week_start_end(date_str: str) -> tuple[str, str]:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date.weekday()  # 0=Monday
    start = date - timedelta(days=weekday)
    end = start + timedelta(days=6)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
```

终端显示执行过程：

```
[Implementer] Step 1.1：实现日期工具函数
    → 编写测试文件 tests/test_weekly.py...
    → 编写实现文件 analytics/weekly.py...
    → 运行测试：pytest tests/test_weekly.py -v
    ✓ 测试通过：3/3
```

### 5.3 5.3 Spec Compliance Reviewer 介入

Step 1.1 完成后，规格审查员**自动触发**：

```
[Spec Reviewer] 审查 Step 1.1...

    对照 tasks.md Step 1.1 要求：
    ✓ 输入：日期字符串 — 已实现
    ✓ 输出：起止日期元组 — 已实现
    ✓ 验收：正常日期 — 测试覆盖
    ✓ 验收：跨月 — 测试覆盖（隐含在跨年测试中）
    ✓ 验收：跨年 — 测试覆盖

    结论：通过
```

### 5.4 5.4 Code Quality Reviewer 介入

规格审查通过后，质量审查员**自动触发**：

```
[Quality Reviewer] 审查 Step 1.1...

    ✓ 命名：函数名 get_week_start_end 清晰表达意图
    ✓ 类型：有类型注解
    ✓ 错误处理：输入格式错误会抛 ValueError（合理）
    ✓ 复杂度：O(1)，无性能问题
    ✓ 代码风格：符合项目规范

    结论：通过
```

两道审查都通过，Step 1.1 正式完成。终端显示：

```
✓ Step 1.1: 日期工具函数 — 完成
```

### 5.5 5.5 遇到问题时的命令行交互

执行到 Step 1.4（来源 TOP10 统计查询）时，Implementer 遇到了问题：

```
[Implementer] Step 1.4：实现来源 TOP10 统计查询
    ⚠ 遇到一个问题，需要确认

    IOC 表中 source 字段存储的是来源标识符（如 "virustotal"、
    "abuseipdb"），但来源的中文名称存在另一张 source_names 表中。

    方案 A：JOIN source_names 表，直接返回中文名称
    方案 B：只返回标识符，前端再做映射

    推荐方案 A，因为前端不应该关心数据映射逻辑。

    但有一个问题：source_names 表中可能没有所有 source 的映射
    （历史数据中有些来源已下线）。需要处理这种情况。
```

你在命令行回复：

```
> 选 A，没有映射的显示原始标识符就行
```

Claude Code 继续执行：

```
[Implementer] 好的，已更新实现...
    → 修改 analytics/weekly.py，LEFT JOIN source_names 表
    → 处理 source_name 为 NULL 的情况，fallback 到 source 标识符
    → 运行测试：pytest tests/test_weekly.py -v
    ✓ 测试通过：5/5

  [Spec Reviewer] 审查 Step 1.4...
    ✓ 通过（已处理缺失映射的情况）

  [Quality Reviewer] 审查 Step 1.4...
    ✓ 通过

  ✓ Step 1.4: 来源 TOP10 统计查询 — 完成
```

### 5.6 5.6 Task 完成后的进度汇报

```
[Task 1/3] 后端 - 周统计核心逻辑 — 完成 ✓

  ✓ Step 1.1: 日期工具函数 — 通过（测试 3/3）
  ✓ Step 1.2: IOC 总量统计查询 — 通过（测试 3/3）
  ✓ Step 1.3: 类型分布统计查询 — 通过（测试 4/4）
  ✓ Step 1.4: 来源 TOP10 统计查询 — 通过（测试 5/5）
  ✓ Step 1.5: 高危 IOC 筛选逻辑 — 通过（测试 2/2）
  ✓ Step 1.6: 单元测试补充 — 通过（测试 15/15）

  所有规格审查通过
  所有质量审查通过

开始执行 Task 2/3...
```

### 5.7 5.7 最终验收：在命令行里怎么确认？

所有 Task 完成后，Claude Code 会输出完整的变更摘要：

```
[Execution Complete] 所有任务已完成

# 变更摘要

## 新增文件
- analytics/weekly.py          — 周统计核心逻辑
- analytics/api.py             — API 接口
- analytics/models.py          — 汇总表模型
- analytics/tasks.py           — 定时任务
- pages/WeeklyAnalytics.vue    — 周统计页面
- components/WeekSelector.vue  — 周选择器组件
- components/StatsCards.vue    — 指标卡片组件

## 修改文件
- routes.py                    — 注册新 API 路由
- scheduler.py                 — 注册定时任务

## 测试结果
- 单元测试：42/42 通过
- 接口测试：8/8 通过
- E2E 测试：5/5 通过

## 遗留项
- 无

是否确认归档？
```

你确认：

```
> 确认归档
```

## 六、阶段五：OpenSpec 归档

### 6.1 6.1 归档操作：在命令行里怎么触发？

你确认后，Claude Code 自动执行归档：

```
[OpenSpec: Archive] 正在归档变更 weekly-analytics...

  → 移动 openspec/changes/weekly-analytics/ → openspec/archive/weekly-analytics/
  → 更新 openspec/specs/threat-intel-platform/weekly-analytics.md
  → 记录设计决策到 openspec/archive/weekly-analytics/decisions.md

归档完成。
```

### 6.2 6.2 归档后的目录结构

```
openspec/
├── archive/
│   └── weekly-analytics/
│       ├── proposal.md          ← 原始提案
│       ├── design.md            ← 最终技术方案
│       ├── tasks.md             ← 任务清单（已全部勾选）
│       ├── decisions.md         ← 设计决策记录
│       └── specs/
│           └── weekly-analytics/
│               └── spec.md      ← 功能规格
├── changes/                     ← 空，等待下一个需求
└── specs/
    └── threat-intel-platform/
        ├── core.md              ← 核心功能规格
        └── weekly-analytics.md  ← 新增：周统计功能规格
```

### 6.3 6.3 归档的价值

三个月后，新需求来了：“加一个按月统计功能”。你可以在 Claude Code 里直接说：

```
> 参考 openspec/archive/weekly-analytics/ 的方案，加一个按月统计功能
```

Claude Code 会读取归档文档，参考已有的设计方案、任务结构、决策记录，快速生成新的变更提案。**不用重新设计、不用重新讨论、不用重新拆任务。**

**归档让每次开发的成果变成可复用的资产，而不是一次性产物。**

## 七、完整流程的命令行交互汇总

为了让你一目了然，这里把整个流程中**你需要在命令行里敲的内容**汇总如下：

### 7.1 你需要敲的内容

| 阶段 | 你敲的内容 | 说明 |
| --- | --- | --- |
| 启动 | `claude` | 进入 Claude Code 会话 |
| 需求输入 | `给情报平台加一个按周统计分析功能，自动生成周报` | 一句话描述需求 |
| 审核文档 | `把 proposal.md 的内容给我看看` | 让 AI 展示文档 |
| 提出修改 | `范围不对，自定义时间范围必须做` | 自然语言修改 |
| 确认方案 | `选 B，加汇总表` | 回答 AI 的追问 |
| 确认计划 | `tasks.md 没问题，确认进入下一步` | 审核任务拆解 |
| 启动执行 | `开始执行` | 触发子代理执行 |
| 中途决策 | `选 A，没有映射的显示原始标识符就行` | 回答执行中的问题 |
| 最终确认 | `确认归档` | 触发归档 |

### 7.2 你不需要做的事

-   不需要手动创建目录或文件
    
-   不需要手动编写文档
    
-   不需要手动运行测试
    
-   不需要手动执行代码审查
    
-   不需要手动归档
    

**一句话总结：你只需要用自然语言和 Claude Code 对话，所有的工程操作都由 AI 完成。**

## 八、人效对比：SDD 和传统开发差在哪？

不同项目的复杂度不同，绝对耗时没有参考意义。真正有意义的是**人类投入占比**和**流程带来的质量保障**。

### 8.1 人类在各阶段的投入占比

整个流程可以分为两大类活动：

**人类主导的阶段**（AI 等你决策）：

-   需求范围确认：你说"要什么"，AI 生成文档等你审核
    
-   方案取舍：AI 给出 2-3 个方案，你做选择
    
-   计划审核：AI 拆解任务，你判断粒度是否合理
    
-   最终验收：AI 汇报结果，你确认是否达标
    

**AI 主导的阶段**（你等 AI 执行）：

-   文档生成：AI 按模板生成 proposal、design、tasks、spec
    
-   代码实现：AI 按 tasks.md 逐 step 写代码
    
-   测试编写与运行：AI 写测试、跑测试、修 bug
    
-   双阶段审查：AI 自动做规格审查和质量审查
    
-   归档整理：AI 整理文档、更新规范
    

**一个直观的比喻**：整个流程中，人类的时间花在"开车时看路、做判断"，AI 的时间花在"踩油门、打方向盘"。你不需要踩油门，但你必须看路。

### 8.2 和传统开发的对比

假设一个同等复杂度的功能，传统开发方式下：

| 环节 | 传统方式 | SDD 方式 |
| --- | --- | --- |
| 需求文档 | 人写，1-2 小时 | AI 生成，人审核 15 分钟 |
| 技术方案 | 人写，1-2 小时 | AI 生成，人审核 10 分钟 |
| 代码实现 | 人写，3-6 小时 | AI 写，人决策 15 分钟 |
| 测试 | 人写（或不写），1-2 小时 | AI 自动写 + 跑，0 人工 |
| 代码审查 | 人审，1 小时 | AI 双阶段自动审查，0 人工 |
| 返工 | 需求偏差导致，1-2 小时 | 规范驱动，几乎无返工 |
| 文档归档 | 人写（或不写），30 分钟 | AI 自动归档，2 分钟确认 |

**核心差异不是"谁更快"，而是"人类的时间花在哪"。**

传统方式下，人类的时间大量花在**执行**上——写代码、写测试、写文档。SDD 方式下，人类的时间集中在**决策**上——确认范围、选择方案、审核结果。

执行是可重复的、可自动化的。决策是需要业务判断的、不可替代的。SDD 的本质就是把人类从可自动化的工作中释放出来，专注于不可替代的决策。

### 8.3 质量保障的差异

比时间更值得关注的是质量：

-   **传统方式**：测试覆盖率取决于开发者是否勤快，代码审查取决于 reviewer 是否认真，文档取决于团队是否有这个习惯
    
-   **SDD 方式**：测试是强制的（TDD 在子代理内部执行），审查是强制的（双阶段审查自动触发），文档是强制的（OpenSpec 流程自动生成）
    

**SDD 的价值不是"更快"，而是"更可靠"。** 每一步都有文档、有审查、有测试、有归档。质量不依赖个人习惯，而是内嵌在流程中。

## 九、写在最后

这一篇把镜头拉到了具体的代码级别和命令行操作级别。核心收获：

**第一，SDD 的价值不是"AI 帮你写代码"，而是"AI 帮你把模糊的需求变成精确的规范，再把精确的规范变成可验证的代码"。** 每一步都有文档、有审查、有测试、有归档。

**第二，人类的角色不是"监工"，而是"决策者"。** 你不需要逐行看代码，但你需要在关键节点做选择——范围、方案、取舍。AI 负责执行和文档化。

**第三，命令行交互极其简洁。** 整个流程中，你敲的都是自然语言，不需要记任何命令。Claude Code + OpenSpec + Superpowers 会自动处理所有的工程操作。

**第四，归档是被严重低估的环节。** 没有归档，每次开发都是从零开始。有了归档，你的开发经验会不断积累，团队的知识会不断沉淀。

**第五，不要纠结绝对耗时。** 不同项目、不同复杂度，耗时差异很大。真正有意义的是流程带来的质量保障和人类时间的重新分配——从"执行者"变成"决策者"。

如果你也在用 Claude Code + SDD 流程做开发，欢迎在评论区分享你的案例。

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9af5b4c8_1781283359224?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzAwOTY5NTU2MQ%3D%3D%26mid%3D2647652199%26idx%3D1%26sn%3D25504810051562a2d00947563882c9f9%26chksm%3D823c844a165420bdeb0ece2a844e19088d2ba5bf862caa26848961cd35f63459e9c33272fcf8%26mpshare%3D1%26scene%3D1%26srcid%3D06139B18RMFpAGaT8THo7Elz%26sharer_shareinfo%3D67c475465472f990048d580975e80cc3%26sharer_shareinfo_first%3D67c475465472f990048d580975e80cc3%23rd&s=obsidian)