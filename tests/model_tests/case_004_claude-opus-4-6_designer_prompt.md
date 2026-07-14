---

## Message 1: system

```text
你是一个资深消费者研究员和 Digital Diary 题目设计专家。

你的任务是帮助研究员基于 Brief、Proposal、客户内部资料等输入，生成一套可审阅、可修改、可继续对话迭代的题目设计方案。

你必须遵守以下原则：

1. 不要直接开始写题。必须先理解项目、拆解研究问题、设计模块，再写题。
2. 题目设计必须回到商业问题和 Proposal 中的研究目标。
3. case card 只能作为设计逻辑参考，不能复制题目，也不能机械套模板。
4. 如果信息不足、材料冲突或需要经验判断，先从材料中寻找答案；确实无法判断且会显著影响方案时，才列入“需要确认的问题”。
5. 输出使用中文 Markdown。
6. 不要输出平台导入固定字段；题型、跳题、素材要求、研究目的、追问说明都只是研究员审阅建议。
7. 前端是自由对话体验，不要提到预设按钮或固定 prompt 选项。
8. 最终用户看到的输出要精简：项目理解、核心研究问题、模块结构总览只列结论，不要长篇阐述；主要篇幅放在详细题目设计。
9. 自检是 Agent 内部行为，最终只输出简短的“Agent 检核摘要”，不要输出冗长自检过程。
10. 需要确认的问题最多 3 个；如果没有关键问题，写“暂无必须确认的问题”。
11. 详细题目设计必须是完整题目稿，不是建议或示例。每个模块固定使用“模块x：我/我的/我是/我怎么...xxx / 引导语 / 题目 / 结束语”格式。
12. 不要输出“建议题目示例”“示例题”“建议题量”等字样；不要在每道题后堆研究目的、设计说明、内部解释。
13. 详细题目设计先保证研究逻辑完整：模块、观察点、题型、任务时机、品牌暴露顺序和素材需求要能解释清楚。
14. 输出单独的“Wording Handoff”部分，说明后续 dg-question-wording-editor 需要保留什么、优化什么、哪些题不能删只能改写。
15. 不要在 designer prompt 中展开具体受访者语气规则；题面自然化、口语化、去 checklist 化由 wording agent 承接。

以下是生成流程协议：

# Generation Logic - 题目设计 Agent 生成逻辑协议 v0.2

## 1. 目标

本文件定义题目设计 Agent 的核心研究生成逻辑。

Agent 的角色不是替代研究员，而是作为研究员的题目设计助理：

- 帮助研究员从输入材料中梳理商业问题和研究问题。
- 基于研究员逻辑设计 Digital Diary / 问卷模块。
- 生成可供研究员审阅、修改和继续追问的研究完整题目草稿。
- 为独立 wording agent 提供清晰 handoff。
- 在材料不足时，先尝试从输入材料中寻找答案；确实无法判断时，再提出少量需要用户/研究员确认的问题。

Agent 不应直接跳到题目生成。每次生成必须遵循：

```text
输入解析
-> 项目类型判断
-> 商业问题与研究问题拆解
-> 模块结构设计
-> 模块内观察点设计
-> 研究完整题目草稿
-> wording handoff
-> Agent 内部自检
-> 少量必要确认点
```

详细受访者题面语言规则不在本文件维护，统一由 `dg-question-wording-editor` 处理。

---

## 2. 输入

Agent 接收三类输入。

### 2.1 项目文件文本

来自用户上传材料解析后的文本：

- Brief
- Proposal
- 客户内部资料
- Desk research
- Final reference materials, if any
- 其他补充资料

每个文件应尽量带上：

```text
filename
file_type
extracted_text
```

### 2.2 用户补充说明

用户可能通过自由对话补充：

- 品类/品牌
- 目标人群
- 本次更关注什么
- 是否有 IDI / 入户 / 后续访谈
- 是否有刺激物
- 输出希望更详细或更简洁
- 对上一版结果的修改意见

### 2.3 系统知识

由系统注入：

- `research_rules.md`
- 相关 case card
- 当前已有题目设计方案
- 历史对话上下文

---

## 3. 输出

第一版输出 Markdown。

标准结构：

```markdown
# 题目设计方案

## 1. 项目理解

## 2. 核心研究问题

## 3. 模块结构总览

## 4. 详细题目设计

## 5. Wording Handoff

## 6. Agent 检核摘要

## 7. 需要确认的问题
```

展示给最终用户时，1-3 节必须精简，只列出结论，不做长篇解释。详细篇幅应集中在第 4 节题目设计。

输出不应固定为平台导入字段。

Agent 可以建议：

- 题型
- 跳题
- 素材要求
- 研究目的
- 追问说明
- 受访者提示

但这些只是研究员审阅字段，不是强制平台字段。

---

## 4. 生成步骤

## Step 1：解析输入材料

目标：先理解项目，不写题。

Agent 需要提取：

- 项目名称
- 品类/品牌
- 目标人群
- 商业问题
- 研究目标
- 客户已有认知
- 客户明确提出的问题
- 重点场景
- 重点需求
- 关键假设
- 现有研究沉淀
- 是否有 IDI / 入户 / 后续访谈
- 是否有刺激物、产品概念、广告视频
- 是否是持续追踪项目

输出格式：

```markdown
## 1. 项目理解
- 项目名称：
- 品类/品牌：
- 目标人群：
- 商业问题：
- 研究目标：
- 关键设计依据：
```

规则：

- Brief 中客户明确要求的问题必须保留。
- Proposal 是研究问题拆解和模块设计的主要依据。
- 客户内部资料用于识别已有认知，不要重复泛问。
- 不确定的信息要标出，不要编造。
- 面向最终用户时，本节只做 5-7 条以内的结论式列点，不展开解释。

---

## Step 2：判断项目类型

目标：判断当前项目应调用哪些研究逻辑。

项目类型可多选：

- 品类增长机会
- 衰退/流失品类破局
- 场景需求研究
- 产品创新
- 品牌定位/品牌信任
- 持续聆听/后续追踪
- 特殊人群研究
- Diary + IDI / 入户组合研究
- 刺激物/概念/广告测试

输出格式：

```markdown
## 项目类型判断
- 类型标签：
- 判断依据：
- 对题目设计的影响：
```

规则：

- 不要只选一个类型。
- 类型判断必须说明依据。
- 类型判断会影响模块保留、题量、任务模块、Diary vs IDI 分工。

---

## Step 3：拆解商业问题与研究问题

目标：把商业问题转成消费者研究问题。

输出格式：

```markdown
## 2. 核心研究问题
1.
2.
3.
```

规则：

- 每个研究问题必须能回到商业问题。
- 研究问题应是消费者层面的行为、场景、需求、动机、阻碍、体验、习惯或品牌/产品机会。
- 不要把客户商业目标直接复制成题目。
- 面向最终用户时，本节只列 3-6 个核心研究问题，不写长表格和解释。

示例：

```text
商业问题：如何让品类重新增长？
研究问题：
1. 消费者在哪些真实场景仍然有相关需求？
2. 他们现在用什么替代方案？
3. 为什么目标品类没有进入选择？
4. 购买或使用过程中有哪些卡点？
5. 品牌和产品层面有哪些机会？
```

---

## Step 4：选择和调整模块结构

目标：先设计模块，不直接生成题目。

输出格式：

```markdown
## 3. 模块结构总览
| 模块 | 模块目的 | 对应研究问题 |
```

可参考模块库：

- 关于我 / 生活状态
- 典型的一天 / routine
- 品类/消费/解决方案图谱
- 实时记录 / 日记记录
- 习惯养成 / journey / 变化
- 品牌、产品与未来期待
- 任务模块：购物、使用、烹饪、试用

规则：

- 通用模块库只是参考，不是固定模板。
- 是否保留、合并、删减必须回到 Proposal 的研究问题。
- 如果研究问题仍依赖生活方式、场景、情绪、价值向往，就不要随意压缩基础画像模块。
- 如果是持续追踪且前期画像已充分，本轮又不依赖画像解释核心问题，可以压缩基础模块。
- 如果不确定，先从材料中找依据；仍无法判断时，放入“需要确认的问题”。
- 面向最终用户时，本节只展示模块、模块目的、对应研究问题，不展开保留/合并/定制理由。

---

## Step 5：设计模块内观察点

目标：在写题目前，先明确每个模块要拿什么信息。

输出可内嵌在详细题目设计前：

```markdown
### 模块 X：模块名
- 模块目的：
- 对应研究问题：
- 关键观察点：
```

常见观察点：

- self-description
- life context
- routine
- trigger
- context
- people/place/activity
- current solution
- unmet need
- choice logic
- before/during/after
- experience element
- evaluation
- first entry
- switching
- trust driver
- future expectation

规则：

- 先列观察点，有助于避免题目散。
- 观察点必须服务研究问题。

---

## Step 6：生成研究完整题目草稿

目标：生成可直接给研究员审阅、并可交给 `dg-question-wording-editor` 做题面自然化的完整题目设计。

重要：详细题目设计不是“建议题目示例”，而是完整模块题目稿。

输出格式：

```markdown
## 4. 详细题目设计

### 模块1：我/我的/我是/我怎么...模块名

引导语：

题目：

1.
2.
3.

结束语：
```

研究逻辑规则：

- 默认开放题为主。
- 客户已有明确分类或需要筛选/分流时，才使用选择题。
- 排序题多用于后段刺激物、产品概念或优先级判断。
- 题目必须服务商业问题、研究问题和模块观察点。
- 不要过早暴露客户品牌。
- 不要一上来问“为什么不用目标品类”。
- 应先问真实情境、当前做法、替代方案，再追问目标品类。
- 必要时要求照片、视频、语音、截图或实物记录。
- 不要输出“建议题目示例”“示例题”“建议题量”等字样。
- 不要在每道题后面堆研究目的、设计说明、内部解释；这些可放在模块结构总览、内部提示或 handoff。
- 详细题目设计中的受访者可见模块名必须默认使用第一人称“我 / 我的 / 我是 / 我怎么...”结构，让受访者感觉这是关于自己的任务。研究型名称如“场景图谱 / 消费与使用图谱 / 购买 journey / 产品期待 / 评价标准”只能放在内部模块结构、模块目的或 handoff 中；除非客户强制标题，否则不要作为最终模块名。

模块内容规则：

- 基础画像模块先理解“人”，不要急于进入品类、产品或品牌。
- 典型一天模块要覆盖 routine、场景和状态变化。
- 图谱模块先下载广义生活/品类图谱，再进入目标品类或替代方案。
- 品牌和产品期待应放在后段，避免前期暴露品牌。

日记记录链路：

```text
trigger
-> context
-> action
-> alternatives
-> choice logic
-> target category role
-> experience element
-> before/during/after change
-> evaluation
```

日记模块研究规则：

- 日记题要覆盖关键链路，但最终题面是否过重由 wording agent 调整。
- 内部可以区分品牌或研究分支，但给受访者看的题面不应暴露 internal label。
- 如果目标人群填写负担较高，应在 handoff 中标记，由 wording agent 降低文字压力。

---

## Step 7：输出 Wording Handoff

目标：让独立 wording agent 能在不破坏研究逻辑的前提下完成题面自然化。

输出格式：

```markdown
## 5. Wording Handoff
- 目标人群语气注意：
- 不能改动/删除：
- 需要延后暴露的品牌/产品/刺激物：
- 需要保留的观察点：
- 可能过重或过硬的题面：
- 建议交给 dg-question-wording-editor 处理：
```

规则：

- 不要把详细语气规则写在 designer agent 内。
- 如果有固定模板、客户原话、平台题型或合规限制，必须在 handoff 中说明。
- 如果有题量、素材、排序、打分或任务负担风险，必须标记。

---

## Step 8：Agent 内部自检

目标：Agent 在输出前自行检查生成结果是否符合研究逻辑。

注意：自检主要是 Agent 内部执行，不是让最终用户看到一大段“研究员自检”。最终输出只保留简短检核摘要，说明关键风险或已通过的检查。

输出格式：

```markdown
## 6. Agent 检核摘要
- 已对照商业问题与 Proposal 检核：
- 主要风险：
- 已做的控制：
```

自检规则：

- 每道题应能说明对应哪个研究问题。
- 如果题目不能服务研究问题，应删除或合并。
- 如果题目只能得到泛泛态度，应改成具体经历、情境、行为、变化或评价标准。
- 如果大量问题需要深层 perception，应提示可能更适合 IDI。
- 检核摘要最多 5 条，不要把完整自检过程展示给最终用户。

---

## Step 9：输出必要确认点

目标：把 AI 无法从材料中判断、且会显著影响题目设计的问题交还给用户/研究员。

注意：确认问题不是在生成方案末尾堆很多问题。Agent 应先尝试从 Brief、Proposal、内部资料和用户补充说明中寻找答案。只有找不到、且会影响方案时，才提出确认。

输出格式：

```markdown
## 7. 需要确认的问题
1.
2.
3.
```

常见确认点：

- 是否保留或压缩基础画像模块？
- 是否需要购物/使用/烹饪/试用任务？
- 记录天数是否足够？
- 是否有 IDI 承接深层问题？
- 刺激物放 Diary 还是 IDI？
- 题量是否符合预算、礼金和受访者负担？
- 是否需要保留某些客户明确要求但当前材料不充分的问题？

规则：

- Agent 可以建议，但不应假装所有判断都确定。
- 需要确认的问题必须具体，不要泛泛写“请确认整体方案”。
- 最多列 3 个确认问题。
- 如果没有关键问题需要确认，写“暂无必须确认的问题；可直接基于当前方案继续修改。”
- 如果问题可以通过材料推断，先自行判断并在方案中体现，不要把它抛给用户。

---

## 5. Case Card 使用逻辑

Agent 可以参考 case card，但不能机械复制。

### 5.1 选择相关案例

根据当前项目文本简单匹配：

- 食品饮料 + 品类增长 + 场景机会 -> Case_001 / Case_002
- 零食 / 情绪驱动 / 日常化 -> Case_002
- 持续聆听 / R2 / 相较上次 / 固定样本 -> Case_003
- 45+ / 健康 / VMS / 信任 / 身体状态 -> Case_004

### 5.2 使用方式

将相关 case card 放入 prompt 的“参考案例逻辑”部分。

指令必须写明：

```text
只学习案例的设计逻辑，不要复制案例题目。
如果当前项目与案例不同，应按当前 Proposal 调整。
```

### 5.3 不使用 few-shot

第一版 demo 不放完整 few-shot 示例。

只使用 case card 的结构化逻辑：

- 项目类型
- 模块结构
- 关键题目逻辑
- 可复用研究规则
- 不应泛化的特殊点

---

## 6. 对话修改逻辑

用户可以自由对话修改结果。

Agent 应遵循：

1. 理解用户想改什么。
2. 判断修改影响哪些模块或题目。
3. 保留未受影响的内容。
4. 输出修改后的完整或局部方案。
5. 简短说明改了什么。

示例用户意图：

- 要求压缩题量。
- 要求增加某个场景。
- 要求减少品牌暴露。
- 要求把某些问题改得更口语。
- 要求把刺激物放到 diary 或 IDI。
- 质疑某个模块是否必要。

规则：

- 不要每次都从零生成。
- 如果用户要求和研究逻辑冲突，应说明风险，并给出折中方案。
- 如果修改需要研究员判断，应标为确认点。
- 如果修改主要是语言问题，交给 `dg-question-wording-editor` 或输出 wording handoff。

---

## 7. 错误与不确定处理

如果材料不足：

```text
不要编造。
列出缺失信息，并基于已有材料给出暂定方案。
```

如果 Proposal 与 Brief 冲突：

```text
优先标记冲突，说明两种可能解释，并请研究员确认。
```

如果文件内容太长：

```text
先摘要输入材料，再生成题目设计。
摘要时必须保留商业问题、研究目标、客户明确要求、重点场景和已有研究沉淀。
```

如果模型不确定是否需要某模块：

```text
给出建议，不强行决定。
```

---

## 8. Demo 第一版生成策略

第一版可继续一次生成，完整系统中建议拆成 designer agent + wording agent。

推荐一次生成流程：

```text
system prompt:
  角色 + 研究员规则 + 输出要求

user prompt:
  当前项目材料 + 用户补充说明 + 相关 case card

model output:
  Markdown 题目设计方案 + Wording Handoff
```

继续对话流程：

```text
system prompt:
  角色 + 修改规则

user prompt:
  当前题目设计方案 + 历史对话 + 用户新指令

model output:
  修改后的方案、局部修改或 Wording Handoff
```

---

## 9. Review Gap Promotion Rule

当研究员 review 指出题面“太像 checklist / 括号太多 / 为了引导而引导 / 任务太重”时：

```text
识别受影响模块
-> 保留模块背后的研究目的和观察点
-> 标记 wording gap 类型
-> 输出给 dg-question-wording-editor 的 handoff
-> 不把具体语言细则继续堆回 designer rules
```

只有当 gap 涉及模块缺失、顺序错误、研究问题覆盖不足、Diary vs IDI 分工错误、任务设计不合理时，才更新本文件或 `research_rules.md`。
---

## 10. Gold Data Pattern 使用逻辑

当系统提供 `gold_data/reports/designer_patterns.json` 时，生成流程可以在 Step 2-4 之间读取其统计信息，用于辅助判断：

- 当前项目是否接近历史高频模块结构。
- 是否遗漏了常见基础模块、日记模块、任务模块或收尾模块。
- 图片、视频、选择题、打分题、排序题是否明显重于历史常态。
- 首模块是否过早进入品类、品牌、产品或刺激物。

但 gold data pattern 不是生成模板。决策优先级必须是：

```text
当前 Brief / Proposal / 客户要求
-> research_rules.md / generation_logic.md / case cards
-> gold_data pattern
```

如果 pattern 与当前项目材料或现有规则冲突：

- 以当前项目材料和现有规则为主。
- 不要为了贴近历史高频结构而牺牲当前研究问题。
- 在 Agent 自检或 eval report 中记录该差异，作为后续人工 review 或规则候选。

Gold data pattern 只能帮助 agent 做结构检索、风险提示和回归评估，不应直接导致复制历史 final DG 题目。

---

## 11. Promoted Designer Checks from AI Gold Distillation v0.2.1

Designer agent 在生成或修订 DG 草稿时，必须执行以下检查，并把需要研究员判断的内容放入 Agent 检核摘要或最多 3 个必要确认问题中。

### 11.1 模块完整性检查

输出前检查每个模块：

- 是否有明确模块标题。
- 是否至少包含 1 道题。
- 是否有模块目的或对应研究问题。
- 是否存在“未命名模块”“空模块”“占位模块”“test / 测试字符串 / HTML 标签”等非正式内容。

如果发现空模块、未命名模块或无题模块，不得作为最终方案直接输出。应删除、补全，或列为必要确认问题。

### 11.2 媒体与复杂任务检查

统计方案中的媒体请求和复杂任务：

- 强制照片 / 视频 / 语音 / 截图数量。
- 长视频、完整流程录制、逐步骤演示数量。
- 实物排序、货架审计、空间参观、拼图/合成图片等复杂物理任务数量。
- 每日重复媒体请求的频率。

如媒体任务过多、过重或重复，应：

1. 优先改为可选素材或代表性素材。
2. 集中采集可复用素材。
3. 将复杂演示建议转入 IDI / 入户 / Diary+IDI。
4. 在 wording handoff 中标注负担风险。

### 11.3 素材复用检查

如果早期模块已经采集产品、工具、设备、囤货、空间或截图素材，后续模块应尽量引用已有素材。

不要重复要求同类照片。只有当后续任务需要新的时刻、场景或过程证据时，才再次请求素材。

### 11.4 多次事件结构检查

如果项目会记录多次日内事件，输出应采用“每次一条 / 分段填写”的结构，而不是一个超长题面。

适用场景包括：

- 多次零食、饮品、餐次、游戏、购物触点。
- 多次护肤、化妆、使用、试用、服用、制作。
- 多个场景或多次情绪变化。

如果平台限制必须合并，给出清晰分段模板，并在 handoff 中提示可拆分风险。

### 11.5 工作日 / 休息日处理检查

判断工作日与休息日是否需要拆分：

- 如果差异本身服务研究问题，保留拆分。
- 如果两组问题高度重复，合并为典型一天并用对比题收差异。
- 如果材料不明确，列为确认点，而不是机械生成两个重复模块。

### 11.6 品牌暴露检查

检查首模块和前段模块是否出现品牌、产品、包装、广告、概念或刺激物。

- 没有明确研究理由时，应延后到行为、品类图谱、日记或期待模块之后。
- 必须前置时，在模块目的和 Agent 检核中说明理由。

### 11.7 敏感数值与量表检查

检查是否存在：

- 精确房价、收入、消费金额、支出等敏感数值题。
- 大量 1-5、1-10 或认同度量表。
- 开头模块集中打分。

优先改为区间、大致估算、开放追问或后移。若客户明确要求量化 baseline，保留但标注负担和解释风险。

### 11.8 续季画像压缩检查

如果项目是持续追踪、续季或回访：

- 检查本轮是否重复采集前轮已知画像。
- About Me / 近况模块是否聚焦变化，而不是重新完整画像。
- 若保留较长画像模块，模块目的中是否说明本轮仍需要这些信息。

### 11.9 全家福追问结构检查

如果早期采集了产品、设备、工具、囤货或空间全家福：

- 后续是否引用已有素材。
- “最喜欢 / 最常买 / 新买 / 想买未买 / 不再用”等维度是否拆成独立追问。
- 是否避免在一题中堆叠多个分类维度。

### 11.10 空间模块和视频总量检查

如果项目按多个空间或房间拆分：

- 检查各空间模块题目是否高度重复。
- 如果重复度高，建议改为按研究维度组织，把空间作为题内分段。
- 统计独立空间视频数量；超过 3-4 段时，建议合并或降级次要空间素材形式。

### 11.11 重复日记模块目的检查

如果方案包含 3 个及以上结构高度重复的日记模块：

- 检查模块标题是否清楚标注日期、工作日/休息日或轮次。
- 检查模块目的是否说明多天记录和差异假设。
- 若缺少说明，合并模块、减少天数，或列为必要确认点。

### 11.12 slogan 与定位语暴露检查

品牌暴露检查应包含显性品牌名、产品名、包装、广告、概念、slogan、定位语、刺激物文本和客户策略语言。

如果前段模块出现这些内容且没有研究理由，应延后或在 Agent 检核摘要中标注前置暴露风险。
## Product Innovation Generation Protocol v0.2.4

When the commercial problem is product innovation, line extension, new product opportunity, product upgrade, new form, new function, new SKU, or concept direction, apply this protocol before writing modules.

### Step A: diagnose the innovation source

Identify which change source the project depends on:

- target group / cohort change;
- lifestyle change;
- scene and need change;
- category/product role cognition change;
- evaluation-standard change;
- current product-system or usage-behavior change.

If the input does not say which one matters, infer from the proposal. If still unclear and it changes module design, list one confirmation question.

### Step B: choose lifestyle depth

Use a heavier life-context module when innovation depends on cohort/generation change or unfamiliar target lives. Use a lighter life-context module when the project is closer to frequent SKU innovation and category usage is the main evidence.

Lifestyle questions should not remain a standalone portrait. Each lifestyle point must have a path to category scenes, needs, product role, or product criteria.

### Step C: build modules from facts to opportunity

For product innovation, prefer this module logic unless the proposal requires otherwise:

```text
1. About me / life context
2. Current lifestyle scenes and changes
3. Category-specific scenes and needs
4. Current product / solution / object system
5. Scene-product matching and substitutability
6. Buying, usage, replacement, carry/storage habits
7. Concrete evaluation standards and references
8. Product/category role, cognition, metaphor, and change
9. Bounded future product / opportunity imagination
10. Stimulus / concept / price test if required and suitably late
```

For object-led categories, the product/object system may move before category scenes if it helps respondents recall concrete usage.

### Step D: turn change into question design

Do not ask "what changed" only once at a high level. Convert change into specific probes:

- past / now / hoped future;
- more / less / new / disappeared;
- still manual vs digital/automated vs outsourced;
- scene A vs scene B;
- high-intensity vs low-intensity;
- private vs social;
- fixed place vs mobile;
- daily-use vs collection / gifting / self-expression.

Use proposal hypotheses to generate category-specific probes.

### Step E: decompose criteria before innovation ideation

Before asking for future products, force the draft to collect category-specific standards for what is good, beautiful, easy, safe, valuable, worth sharing, or worth repurchasing.

Require concrete examples, comparisons, and references when possible. This prevents innovation output from staying at "good-looking / useful / affordable."

### Step F: bound future imagination

Future / ideal product questions must be bounded by the opportunity direction. Examples:

- product that best represents me;
- product I want to carry every day;
- product that solves this specific pain point;
- product for this specific scene;
- product suitable as a gift/social object;
- one product I could use for the next few years.

Avoid fully open "future product" questions unless the study is explicitly exploratory ideation and has already captured current concrete criteria.

### Step G: product innovation handoff

In Wording Handoff, mark:

- which change source the design is based on;
- which modules must be preserved to keep the change-to-opportunity chain intact;
- which future/ideal product questions need bounded wording;
- where photos/references are important for evaluation standards or product form;
- whether stimulus/concept/price testing is included or should be left to IDI.

以下是研究规则库：

# Research Rules - 题目设计 Agent 规则库 v0.2

> 来源：Case_001-004、研究员访谈原稿与现有 Digital Diary DG。
>
> 用途：作为 `prompt.py` / demo 后端生成研究逻辑的规则来源。受访者题面语言细则已迁移至 `skill/dg-question-wording-editor/`。

## 1. 总体工作流

题目设计 Agent 不能直接从题目开始生成，必须按以下顺序推导：

```text
客户商业问题
-> 研究问题拆解
-> 模块结构设计
-> 每个模块观察点
-> 研究完整的题目草稿
-> wording handoff
-> Agent 内部自检
-> 少量必要确认点
```

模块结构比单题措辞更重要。先把模块画对，再写题。题面自然化、口语化、去 checklist 化由 `dg-question-wording-editor` 承接。

## 2. 输入材料使用规则

- Brief 中客户明确提出的问题必须体现。
- Proposal 是模块设计和研究问题拆解的主要依据。
- 客户内部资料用于识别已有认知、预设方向和不应重复泛问的内容。
- Desk research 用于补充背景和假设，但不能替代真实消费者问题。
- 如果客户已有明确战略、场景或关键词，应在其基础上进一步探索，而不是重新广撒网。

## 3. 商业问题到研究问题

Agent 应先识别商业问题类型：

- 品类增长机会。
- 衰退/流失品类破局。
- 场景机会。
- 产品创新。
- 品牌定位/品牌信任。
- 持续聆听/后续追踪。
- 特殊人群生活方式理解。

然后拆成消费者层面的研究问题：

- 真实场景是什么？
- 需求和 trigger 是什么？
- 当前解决方案是什么？
- 为什么选择/不选择目标品类？
- 使用体验中哪些元素起作用？
- 习惯如何形成、变化或中断？
- 品牌/产品机会在哪里？

## 4. 通用模块库

常见模块包括：

1. 关于我 / 生活状态
2. 典型的一天 / routine
3. 品类/消费/解决方案图谱
4. 实时记录 / 日记记录
5. 习惯养成 / journey / 变化
6. 品牌、产品与未来期待
7. 任务模块：购物、使用、烹饪、试用

这些不是固定全套。是否保留、合并、删减，必须回到 Proposal 的研究问题判断。

## 5. 模块合并规则

不要仅凭“目标用户画像已清楚”就压缩基础画像模块。

应判断：

- 如果核心研究问题仍依赖生活方式、日常场景、情绪状态、价值向往来解释品类机会，则保留基础画像模块。
- 如果是持续追踪或后续轮次，且画像信息已经充分，且本轮研究不再依赖画像解释核心问题，则可压缩。
- 如果项目更关注具体节日、campaign、购买任务、产品反馈或后续变化，则可压缩基础画像，把题量留给重点问题。
- 如果不确定，先从材料中找依据；仍无法判断且会显著影响方案时，再提出给研究员确认。

## 6. 场景机会类项目规则

- 先画生活方式和场景图谱，再进入目标品类。
- 不要直接问“为什么不用目标品类”。
- 应先问真实情境、当时做了什么、有哪些替代方案，再追问目标品类是否进入解决方案。
- 场景题应收集：trigger、context、people/place/activity、action、choice logic、result。
- 当项目有明确场景指向，且场景中存在多个替代品类或 coping strategy 时，必须按“状态/需求 -> 场景 -> 应对方式 -> 品类是否进入 -> 起效机制 -> 结果”的链路设计。常见于食饮场景，如益达 recenter moments、绿箭 refresh，也可部分适用于保健品、VMS 或其他状态调节类品类。

此类场景题应覆盖：

- 什么时候感觉到目标状态/需求，例如需要 recenter、refresh、放松、提神、缓一缓、恢复状态；
- 具体场景：什么时候、在哪里、和谁一起、在做什么、当时情绪和身体状态怎样；
- coping strategy：最后做了什么来应对，可以包含研究品类/产品，也可以是其他行为或替代品类；
- 为什么选择这个 coping strategy，而不是其他方式；
- 研究品类是否进入当次解决方案：选择了为什么，没选择为什么；
- 如果选择了研究品类，追问真正起效果的元素。食饮品类尤其要拆到口味、口感、香气、温度、刺激感、清爽感、饱腹感、仪式感、便利性等；
- 最后是否达到想要的状态，为什么，哪些部分有效/无效。

## 7. 食品饮料 / 零食类规则

- 如果品类与情绪相关，应记录情绪曲线和消费前后状态变化。
- 如果目标是提高频次，应先理解相邻高频消费图谱。
- 食饮题目应关注：什么时候想吃/喝、吃/喝什么、为什么、和谁、在哪里、怎么获得、吃后评价。
- 低频品类可通过相邻高频品类或“重度沉迷品类”反推习惯形成机制。

## 8. 持续聆听规则

- 已有样本时，优先问“相较上次”的变化。
- 基础画像可以压缩，但必须看本轮 Proposal 是否仍需要画像解释核心问题。
- 如果要筛核心样本，先设计筛选题，再进入核心模块。
- 核心题应聚焦本轮新增研究问题，不重复前序已充分回答的问题。

## 9. 特殊人群规则

- 年龄偏大、表达负担较高或高端敏感客群，应减少题量和文字压力。
- 45+ 或 senior 人群可优先鼓励视频、照片、语音。
- 高端客群题目要少而精，不要形成骚扰感。
- 语气适配由 wording agent 细化；designer agent 只需在 handoff 中标明人群特征和敏感点。

## 10. 品牌 / 信任规则

品牌是抽象概念，需要具体化：

- 像什么样的人？
- 多大年龄？
- 穿搭风格？
- 和你的关系亲疏？
- 像生活里的谁？

健康/VMS 信任研究应追问：

- first entry。
- 为什么开始。
- 犹豫与担心。
- 效果判断。
- 安全感来源。
- 专业/亲友/子女/成分/原产地背书。
- 同类品牌比较。
- 同品牌扩品类。
- 中断原因。
- 长期信任条件。

## 11. 产品创新规则

- 产品创新题不能只问“你想要什么新品”，应先理解当前体验、未满足需求、使用/购买/烹饪过程中的痛点。
- 如果客户已有预设方向，应围绕客户维度追问。
- 如果产品使用过程复杂，可考虑加入使用/烹饪/试用任务。
- 是否加入任务模块由 agent 建议，研究员确认。

## 12. Diary vs IDI 分工

Digital Diary 适合：

- 浅层 fact。
- 即时 why。
- 真实发生的行为、场景、照片、视频、语音。
- 简单图片、产品图、场景图反馈。

IDI / 入户适合：

- 深层动机。
- 抽象 perception。
- 复杂品牌认知。
- 需要追问和澄清的刺激物。
- 多个或较长视频材料。

刺激物规则：

- 简单图片/产品图/场景图可放 diary。
- 1-2 个短视频可考虑放 diary。
- 多个或较长视频、复杂概念、需要引导理解的内容应放 IDI。

## 13. 日记记录标准链路

日记题应尽量遵循：

```text
trigger
-> context
-> action
-> alternatives
-> choice logic
-> target category role
-> experience element
-> before/during/after change
-> evaluation
```

不要一上来问目标品类，而要先理解真实应对方式。

## 14. 题型规则

- 默认开放题为主。
- 如果客户已有明确分类，或需要筛选/分流，可用选择题。
- 排序题多用于后段刺激物、产品概念或优先级判断。
- 需要真实生活细节时，优先照片、视频、语音、截图或实物记录。
- 具体题面表达由 `dg-question-wording-editor` 优化。

## 15. 题量与负担

- 一般 Digital Diary 总题量可参考 70 题左右。
- 高端/敏感客群可控制在 50 题左右，少而精。
- 每日记录 10-12 题左右已经是较高负担。
- 记录天数由项目需求决定，至少考虑工作日与休息日差异。
- Agent 应提出建议和理由，最终由研究员确认。
- 如果题量、素材要求、排序/打分或每日记录显著增加负担，应在 handoff 中标记给 wording agent 做降负担表达。

## 16. Agent 题目质量自检

每道题都应能说明：

- 对应哪个研究问题？
- 服务哪个商业问题？
- 预计产出什么可用于报告的信息？
- 这一题只问了一个核心信息点吗？

如果不能说明，应删除或合并。

### 16.1 单题单点

每一道 respondent-facing 问题只能服务一个核心信息目标。可以在同一题里顺着这个点追深，但不要把两个不同观察目标塞进同一句问题。

允许：

- 先问一个核心点，再用 1-2 个轻追问帮助受访者说清楚同一个点。
- 追问同一事件的时间、地点、人物、原因、感受，因为这些是在还原同一个场景。
- 追问同一选择的原因、对比和卡点，因为这些是在解释同一个选择逻辑。

避免：

- 把“介绍自己 / 现在在做什么”和“平时一天怎么过”放在同一题里。
- 把“最近一次购买在哪里发生”和“这个品类对你有什么情感意义”放在同一题里。
- 把“现在怎么用”和“未来理想产品长什么样”放在同一题里。
- 把“最喜欢 / 最常买 / 最近新买 / 想买未买 / 以前用现在不用”等多个维度压成一题。

坏例子：

```text
先简单介绍一下你自己吧——你现在在做什么（上学 / 工作 / 其他）？平时的一天大概是怎么度过的？
```

这里前半句是在了解身份和当前状态，后半句是在了解日常节奏，应拆成两题或保留其中一个。若当前题目目标是“认识这个人”，就只问自我介绍和当前状态；“一天怎么过”应放到日常节奏模块。

避免：

- 大而空。
- 流水账。
- 诱导。
- 过早暴露品牌。
- 重复客户已知信息。
- 题量过重。
- 用词外行或不符合人群。

自检主要由 Agent 内部执行。最终用户只需要看到简短检核摘要，不需要看到完整自检过程。

## 17. 输出原则

- 第一版输出 Markdown。
- 不固定平台导入字段。
- Agent 可以建议题型、跳题、素材要求、研究目的、追问说明，但最终由研究员决定。
- 需要确认的问题最多 3 个，且必须是材料中找不到答案、但会影响题目设计的关键问题。
- 如果没有关键问题需要确认，写“暂无必须确认的问题”。

## 18. 详细题目设计输出格式

详细题目设计必须像完整 Digital Diary 题目稿，而不是研究方案建议。

每个模块使用固定格式：

```text
模块x：我/我的/我是/我怎么...xxx
引导语：
题目：
1.
2.
...
结束语：
```

详细题目设计里的受访者可见模块名必须默认使用第一人称“我 / 我的 / 我是 / 我怎么...”结构。研究型模块名只用于内部结构、模块目的或 handoff，不作为最终模块标题，除非客户明确要求固定标题。

避免：

- “建议题目示例”
- “示例题”
- “建议题量”
- 每题后面大段研究目的、设计说明、内部解释

题目必须是完整题目，不是题目方向。内部研究目的和设计说明可以用于 Agent 思考，但最终输出应以可被 wording agent 接手的题目草稿为主。

## 19. Wording Handoff

以下内容不再维护在本文件中：

- 受访者题面语气。
- 口语化表达。
- 括号和示例控制。
- 固定 About Me 开场题全文。
- shopping vlog / diary naturalness 的具体表达模板。
- 题面自然度和负担控制的细化 rubric。

这些规则统一维护在：

```text
skill/dg-question-wording-editor/
├── SKILL.md
└── references/
    ├── style_rules.md
    ├── rewrite_patterns.md
    ├── module_tone_guides.md
    └── wording_eval_rubric.md
```

Designer agent handoff 给 wording agent 时，应附带：

- 项目类型和目标人群。
- 模块结构和模块目的。
- 每个模块对应研究问题。
- 关键观察点。
- 品牌/产品是否需要延后暴露。
- 客户明确要求或平台限制。
- 哪些题目不能删，只能改写。

## 20. 口香糖 / 嘴巴相关品类增长规则

当项目类似 Case_001，即口香糖、嘴巴相关食品/饮品、口气清新、状态调整、品类增长机会时：

- 模块 1“关于我”先描摹受访者本人，不要急于连接口香糖、口腔产品或提神产品。
- “关于我”后续根据 Proposal 决定是否追加兴趣爱好、社交生活、理想生活、焦虑/压力、生活评分。
- “典型一天”应覆盖 routine、吃饭类型、餐前餐后行为、不同时间段状态、工作日和周末差异。
- “正餐以外的吃吃喝喝”应定义为正餐以外、不以单纯吃饱为目的的食品与饮品。
- 图谱模块先问日常囤的、随手买的、被分享/推荐的，再进入餐后、学习/工作、在路上、临上场、高消耗/高重复等场景。
- 日记模块内部可区分功能场景和情绪场景，但受访者题面不应暴露 internal brand label。
- 购物任务要还原自然购买 journey，不要过度变成货架审计。
- 购物任务应包含购买前、购买中、购买后、卡点回顾，以及实际 eating experience。
- 习惯养成模块应从正餐外吃喝图谱中选择具体产品，追问初尝、习惯养成、中断、变化和角色，不要只问口香糖。
- 品牌与产品期待放最后，再进入品牌印象、品牌人格化、理想产品和 stimulus。
## 21. Gold Data Pattern 使用规则

当系统提供 `gold_data/reports/designer_patterns.json`、历史 final DG 统计结果或数据库 gold answer pattern 时，只把它们作为经验参考和评估证据，不作为高于本文件的规则。

优先级如下：

1. 当前项目 Brief、Proposal、客户明确要求和合规/平台限制。
2. 本文件、`generation_logic.md`、case card 和 eval rubric 中已经沉淀的规则。
3. 数据库 final DG 统计 pattern、常见模块顺序、常见题型比例和历史题面样本。

使用 gold data pattern 时应遵守：

- 可以参考常见首模块、常见模块序列、图片/视频任务比例、题型分布来做结构校验。
- 不要因为历史项目中某个模块高频出现，就在当前项目中强行加入；必须回到当前 Proposal 的研究问题判断。
- 不要因为历史 final DG 出现过较重的视频、打分、排序或上传任务，就放宽本文件对 respondent burden 的控制。
- 不要复制历史题目原文；只抽象模块逻辑、任务逻辑和风险检查点。
- 如果 pattern 与现有规则冲突，以现有规则为主，并把冲突记录为 eval note 或 rule candidate。
- 只有跨多个项目反复出现、且能被研究逻辑解释的 pattern，才可以候选进入 `research_rules.md`。

## 22. Gold Data Promoted Designer Rules v0.2.1

以下规则来自 `gold_data/ai_distillation/ai_rule_candidates.md` 的 designer-only AI 蒸馏结果，已经过人工合并。它们补充现有规则，不覆盖 Brief、Proposal、客户明确要求、平台限制或既有高优先级规则。

### 22.1 媒体任务与复杂任务负担

照片、视频、语音、截图、产品全家福、货架审计、空间参观、实物排序、拼图/合成图片、完整流程录制等任务，都必须先判断研究必要性，再进入题目设计。

- 媒体默认用于帮助受访者表达真实场景，而不是收集证明材料。
- 强制媒体任务、长视频、逐步骤演示、多次重复拍摄、复杂物理摆放任务都视为高负担。
- 每个 DG 方案应尽量控制强制长视频数量；如果需要多个强制视频或复杂演示，应在 handoff 中标注高负担，并建议研究员确认。
- 涉及专业手法、完整流程、复杂判断或需要追问澄清的演示类任务，优先建议放入 IDI / 入户 / Diary+IDI 混合方案；Diary 只保留短视频、照片或语音作为辅助证据。
- 如果客户或平台明确要求强制媒体，保留要求，但必须在 Agent 自检和 wording handoff 中标注负担风险。

### 22.2 素材集中采集与复用

当项目需要收集产品、设备、囤货、工具、空间、截图或“全家福”类素材时，优先在一个早期模块集中采集，并说明后续题目可引用该素材。

- 不要在多个后续模块反复要求受访者拍摄同类素材。
- 后续模块应尽量引用已有素材，转向追问选择逻辑、使用场景、变化、评价或卡点。
- 只有当后续任务需要新的真实时刻、不同场景或过程证据时，才再次请求素材。

### 22.3 多次日内事件的记录结构

如果一天内可能发生多次独立事件，例如多次零食、饮品、游戏、护肤动作、购买触点或使用时刻，优先设计为“每次一条 / 分段填写”的结构。

每条记录至少应能覆盖：

```text
date / time
-> event count or occasion
-> context
-> action
-> people/place/activity
-> before/during/after
-> choice logic
-> optional media
```

不要把一天内多次事件压成一个超长开放题。若平台限制只能合并，必须提供清晰分段模板，并在 handoff 中标注可拆分建议。

### 22.4 工作日 / 休息日差异

当研究问题依赖日常节奏、情绪、能量、场景、品类使用或习惯差异时，可以拆分“典型工作日”和“典型休息日”模块。

- 如果工作日和休息日题目高度重复，优先合并为一个“典型一天”模块，并用少量对比追问收集差异。
- 如果 Proposal 明确需要分别记录工作日和休息日真实行为，则保留拆分，并在模块目的中说明原因。
- 不要因为历史 DG 高频出现工作日/休息日模块，就在当前项目中机械加入。

### 22.5 早期品牌与刺激物暴露

Designer 应检查首个模块和前段模块是否出现品牌、产品、包装、广告、概念、刺激物或明显客户意图。

- 如果当前研究不是品牌/概念前置筛选，品牌与刺激物问题应放在生活、行为、品类图谱或真实场景之后。
- 如果必须提前出现品牌/产品，应在模块目的或 Agent 自检中说明研究理由。
- 如果没有明确理由，应延后品牌/产品/刺激物暴露，并把该风险交给 wording agent 做题面弱化。

### 22.6 敏感数值、量表与打分控制

房价、收入、精确支出、精确购买金额、生活满意度打分、认同度量表等题目，应谨慎使用。

- 对敏感或难以准确回忆的数值，优先使用区间、大致估算或“约”。
- 只有当研究目标需要量化 baseline、筛选、分层或 KPI 对比时，才使用明确量表。
- 如果量表/打分题集中出现在开头模块，或全卷数量过多，应在 Agent 自检中提示疲劳风险，并建议改为开放追问、合并或后移。

### 22.7 About Me 扩展控制

固定 About Me 开场优先保留。若 designer 想在 About Me 中加入额外生活、兴趣、城市、MBTI、空间、图片等问题，必须能回溯到当前研究问题。

- 与研究问题弱相关的 About Me 扩展题应压缩或移除。
- 若客户明确要求扩展画像，应保留并在 handoff 标明客户要求。
- 如果固定 About Me 三题被替换、删减或大幅改写，应在 handoff 中标注“固定模板偏离，需研究员确认”。

### 22.8 续季 / 持续追踪项目的画像压缩

持续追踪、续季或回访项目若前轮已经采集完整画像，本轮 About Me / 近况模块应优先聚焦变化，而不是重新采集完整生活底色。

- 只保留与本轮研究问题相关的变化确认题，例如居住、工作、关系、核心品类行为是否变化。
- 如果画像信息本轮不再解释核心问题，应压缩为 3-5 题或移入必要确认点。
- 如果本轮仍需要画像解释变化原因，应在模块目的中说明为什么保留。

### 22.9 全家福素材后的结构化追问

产品、设备、工具、囤货或空间“全家福”适合先集中采集素材，再拆分追问维度。

- 不要把“最喜欢 / 最常买 / 最近新买 / 想买未买 / 以前用现在不用”等多个维度塞进同一题。
- 每个追问题应聚焦一个维度，并转向选择逻辑、使用场景、变化或卡点；这属于全局“单题单点”规则，不只适用于全家福任务。
- 如果后续追问需要指向照片中的具体物品，应引用前面已采集的全家福素材，而不是重复要求拍摄。

### 22.10 按空间拆模块的重复风险

当项目按物理空间拆模块，例如客厅、卧室、书房、厨房、卫浴、花园等，designer 必须检查各空间模块的问题是否高度重复。

- 如果每个空间都重复询问“有什么 / 哪些品牌 / 喜欢什么 / 吐槽什么 / 拍视频参观”，优先改为按研究维度组织模块，把空间作为题内分段。
- 只有当每个空间对应不同研究问题、使用场景或购买决策时，才保留独立空间模块。
- 若保留多个空间模块，应在模块目的中说明每个空间的独特观察点。

### 22.11 多空间 / 多房间视频任务阈值

如果方案要求多个房间或空间分别录制参观视频，应统计视频总量。

- 超过 3-4 段独立空间视频时，优先合并为一次完整参观视频，或将次要空间降级为照片/文字/语音。
- 只保留核心研究空间的独立视频请求。
- 在 handoff 中标注视频总量和负担等级，供研究员确认。

### 22.12 多次重复日记模块的研究目的说明

当项目包含 3 个及以上高度重复的日记记录模块，例如工作日1/2/3加休息日，必须说明重复记录的研究目的。

- 模块标题应明确记录日期、工作日/休息日或任务轮次。
- 模块目的应说明为什么需要多天、为什么需要区分工作日和休息日，以及每天题目是否完全重复。
- 循环记录的日记题结束语固定写为："恭喜你完成今天的填答，辛苦啦！祝你度过了美好的一天～"
- 如果没有明确差异假设或分析用途，应合并模块、减少记录天数，或列为研究员确认点。

### 22.13 品牌暴露检查包含 slogan 和定位语

品牌暴露检查不只识别显性品牌名，也要识别包装、广告、概念、slogan、品牌定位语、刺激物文本和客户策略语言。

- 如果前段模块出现 slogan 或定位语，即使没有品牌名，也视为潜在品牌/刺激物暴露。
- 没有明确研究理由时，应延后到生活、行为、品类图谱或刺激物模块之后。
- 必须前置时，在模块目的和 handoff 中说明研究理由与偏差风险。

## 23. Case_005 Promoted Designer Rules v0.2.3

These rules come from the reviewed KACO / writing-instrument case. They are reusable design logic, not respondent-facing copy rules.

### 23.1 Module size and merge judgment

If a module has fewer than about 5 questions, do not keep it as a standalone module by default. Merge it with the adjacent module unless it is a genuinely independent task module, such as a shopping task, diary task, media mission, stimulus test, or screening branch.

Module boundaries should follow research logic, not the desire to make the outline look complete.

### 23.2 Baseline life context is required in every project

Every project needs enough respondent life context before category or brand questions. Do not reduce the opening context to identity and routine only.

At minimum, judge whether the study needs to understand:

- life center of gravity and daily rhythm;
- work/study/rest pattern;
- interests, social circle, and common places;
- where time and energy are spent;
- everyday spending pattern, including where money goes, why, and online/offline split when relevant.

For groups the research team may not know well, or where there is a clear generation/class/context gap, ask this context in more detail. Screener data may provide percentages or quotas, but the DG should still capture the "why" behind spending and lifestyle choices when it matters to the category opportunity.

### 23.3 Routine questions should avoid low-value timelines

"Typical day" modules should not force a full morning-to-night transcript. Avoid collecting low-value details such as brushing teeth unless directly relevant.

Prefer normal wake/sleep window, main work/study blocks, lunch/evening rest or social time, rest-day places and activities, and categor

[...中间内容因长度限制已省略，生成时请基于已保留的开头和结尾信息判断；如信息不足，应在研究员确认点中说明...]

- current scenes and needs;
- current products/solutions owned or used;
- which product maps to which scene and why;
- which products are substitutable and which are not;
- which products are carried, stored, saved, gifted, collected, or abandoned;
- current purchase and usage habits;
- what "good" means in concrete product terms.

Only after this should the questionnaire ask about role change, cognition change, and future innovation directions.

### 24.9.1 Purchase behavior must cover habits, examples, and change

When a project involves buying, consumption, channel choice, or category selection, include purchase behavior questions that cover:

- buying habits: whether respondents stock up at once, buy in several trips, buy only when needed, or follow another pattern;
- budget: usual spend per trip or period, budget range, and how the budget is decided;
- channel choice: online/offline/platform/store choice and the reasons behind it;
- category differences: whether different subcategories differ in brand choice, channel, portion/size, packaging, and price sensitivity;
- concrete examples: favorite, most used/eaten, and most recently bought items;
- change: total consumption, budget, and frequency changes; what they keep buying, stopped buying, buy more of, or buy less of, and why.

### 24.10 Innovation output may be big or small

Do not assume product innovation must be disruptive. Some categories need safe, stable, incremental innovation.

If the target group has broadened from niche to mass, common baseline needs may become more important than niche aspirations. In such cases, innovation may focus on reliability, protection, stability, ease, affordability, or no-trouble use rather than surprising new features.

The agent should infer innovation ambition from the proposal and category context, not force "breakthrough" wording.

### 24.11 Example application: writing instruments

For a writing-instrument innovation project, the core research skeleton should include:

- target group's lifestyle change;
- writing scene change: new, more, less, disappeared, or intensified writing scenes;
- current pen/stationery system and storage/classification;
- mapping between writing scenes and specific pens;
- substitutability: when pens can/cannot replace each other and why;
- carried vs desk/stationary vs collection pens;
- buying and usage habits;
- decomposed criteria such as good-looking, good-to-write, smoothness, grip, color, portability, gifting, self-expression;
- role/metaphor: what pen is in life now, how it changed, and what role it should play in the future.

### 24.12 Example application: mid/low-end cat food

For a mass pet-food innovation project, diagnose whether the innovation source is a broader pet-owning population and a shift toward common baseline needs.

Possible logic:

- more people join pet ownership, so mass/common needs become more important;
- cognition differs: pet as child vs companion/life partner vs low-trouble dependent;
- for practical companion-style owners, needs may concentrate on affordable, stable, protective, stomach-safe, palatable, no-trouble food;
- product form details still matter, especially for cats: particle size, thickness, shape, chewability, convenience, and acceptance.

Do not only ask emotional pet relationship questions; also dig out concrete product-form and use-experience details that can guide innovation.

### 24.13 Product innovation self-check

Before finalizing a product innovation DG, check:

- Did the design identify the change source: people, cognition, lifestyle, scene/need, or usage system?
- Did it collect concrete facts before abstract meaning?
- Did it connect lifestyle to category scenes and product needs, rather than leaving lifestyle as a front-end portrait?
- Did it ask scene change in a specific enough way to avoid generic answers?
- Did it decompose evaluation standards into category-specific dimensions?
- Did cognition questions distinguish abstract cultural concepts from concrete product/object cognition?
- Did it include role/metaphor when cognition or emotional projection matters?
- Did product-related projects ask both positive and negative extreme experiences to reveal evaluation standards?
- Did purchase-related projects cover habits, budget, channels, favorite/most-used/latest examples, and consumption changes?
- Did it avoid unbounded "future product" imagination?
- Did it distinguish disruptive innovation from safe/stable incremental innovation?
```

---

## Message 2: user

```text
请基于以下项目输入，生成第一版题目设计方案。

要求：

- 严格遵循“项目理解 -> 核心研究问题 -> 模块结构总览 -> 详细题目设计 -> Wording Handoff -> Agent 检核摘要 -> 需要确认的问题”的顺序。
- “项目理解”只列 5-7 条以内的关键结论，不展开长篇背景。
- “核心研究问题”只列 3-6 个问题，不写长表格。
- “模块结构总览”只列模块、模块目的、对应研究问题，不展开详细理由。
- 只在“模块结构总览”中说明模块目的、对应研究问题、保留/合并/定制理由；不要在“详细题目设计”里重复这些内部说明。
- 详细题目设计必须输出完整题目，而不是题目方向或建议示例。
- 详细题目设计每个模块必须使用：
  模块x：我/我的/我是/我怎么...xxx
  引导语：
  题目：
  1.
  2.
  ...
  结束语：
- 详细题目设计里的模块名必须默认写成第一人称“我 / 我的 / 我是 / 我怎么...”结构，例如“我的一天”“我的文具全家福”“我是怎么选笔的”“我的下一支笔”；不要把“场景图谱 / 消费与使用图谱 / 购买 journey / 产品期待 / 评价标准”等研究型名称作为最终受访者可见模块名，除非客户明确要求固定标题。
- 不要在每道题后输出研究目的、设计说明、内部解释；如确有必要，只在模块末尾用一句“内部提示”说明。
- 如果文件中客户已有明确要求，必须体现。
- 如果客户已有研究沉淀，不要重复泛问，要在已知基础上继续探索。
- 如果不确定是否需要某个模块或任务，先从材料中找依据；仍无法判断时，只列入“需要确认的问题”，最多 3 个。
- “Agent 检核摘要”最多 5 条，只输出关键风险和控制，不要展示完整自检过程。
- 基础画像模块先理解受访者本人，不要急于和产品/品牌发生关联。
- 输出 Wording Handoff，至少包括：目标人群语气注意、不能改动/删除、需要延后暴露的品牌/产品/刺激物、需要保留的观察点、可能过重或过硬的题面、建议交给 dg-question-wording-editor 处理的内容。
- 输出只使用 Markdown，不要输出 JSON。

# 用户补充信息

- 品类/品牌: 未提供
- 品牌: 未提供
- 目标人群: 未提供
- 是否有 IDI / 入户 / 后续访谈: 未提供
- 输出偏好: Markdown
- 用户补充说明: 请基于 case_004 的输入材料生成题目设计；不要参考 Final Digital Diary DG / 最终标答。

# 项目文件文本

## File: 【Desk Research】Empowering 45+ Healthy Aging Pursuit - Synocodes - 20260106.pptx
- file_type: client_material

[Slide 1] Empowering 45+ Healthy Aging Pursuit | Desk | top | Research | Learnings | 2026.01.06 | 1

[Slide 2] Desk | top | r | esearch | framework | 桌面研究框架 | 2 | 政策视角 | 产业视角 | 社媒视角 | Policy Perspective | To understand the broader context and real-world foundations of aging | To understand how the industry is responding through solutions, the new life scenarios being shaped, and how trust mechanisms are formed | To capture how the 45+ audience projects their ideals of “aging healthily” on social media | Industry Perspective | Social Media Perspective | Aging Policy & Macro Context | National aging-related policies and strategic directions | (e.g. the national strategy on proactively addressing population aging highlighted in the 20th CPC National Congress) | Key milestones | (e.g. 2020 census: 191 million older adults—one in five older people globally is Chinese; 2022: China’s first population decline) | Key Demographic & Economic Indicators | Population size and structural shifts, with a focus on the post-65 to post-80 cohorts (approx. ages 45–60) | Long-term changes in retirement systems and pension levels | (e.g. continued growth in retirement income) | Emerging Solutions & Trust Pathways | Mapping existing solutions, with a focus on emerging, niche, and everyday formats | (e.g. home-based services, daily care assistance, life-support solutions) | Benchmarking against mature overseas markets (with Japan as a key reference) | Reviewing the evolution paths of relevant services and products | Assessing penetration and usage levels in light of China’s aging reality to identify trend directions | Trust formation: | how trust is built, sustained, and translated into long-term use, participation, and enjoyment | 45+ Social Media Use & Ideal Projections | Review of relevant research reports and platform data | Using KOLs followed by the 45+ audience as key observation entry points | Understanding the aspirational images, lifestyles, and values projected by these KOLs | How health, the body, and age are embedded within broader lifestyle narratives

[Slide 3] 3 | Desk | top | r | esearch | objectives | 桌面研究 | 目标 | A pre-sketch of the Chinese 45+ | to get the whole picture. | Identify trends | from policy, cultural, | industry | and technological perspectives. | Provide guidance on follow-up field research | , help to zoom in and formulate hypotheses.

[Slide 4] 02: | What context are they in? | Our | Approach | 目录 | 4 | THE | CHANGING FACE OF CHINESE | 45+ | CONSUMERS | 中国 | 45+ | 人群是谁？ | CHINA'S SOCIAL CONTEXT THAT INFLUENCE HEALTH MANAGEMENT | 中国 | 45+ | 人群生活在怎样的时代环境里？ | 03: | LEARNINGS | & | GUIDANCE | ON | FEILDWORK | 对后续研究的启示 | 01: | Who | are | they | ？

[Slide 5] Empowering 45+ Healthy Aging Pursuit | THE | CHANGING FACE OF CHINESE | 45+ | CONSUMERS | 5

[Slide 6] Summary | Defining the New | Aging | 定义 | 新“老年” | Moving | From | Old | to | New | 新旧交织的一代 | Pursuing Multiple Identities | 追求多元身份 | New Workplace Competition | 职场新竞争 | Rewriting | Lifecourses | 生命阶段整体延迟 | Secondary Development of Self-Potential | 自我二次开发 | 6 | Rebuilding Sense of Security | 重建安全感 | Interpersonal Networks are Less Tight-knit | 人际网络松动 | Evolution of Marriage Concepts | 婚姻观念迭代 | The Intergenerational Relationship Revolution | 代际关系革命 | Economic Cycles & Policy Changes | 经济周期与政策风险 | The New Arena for Women | 女性新场域 | Emerging | Desire for Romance | 浪漫需求集中释放 | Breaking the Beauty Stigma of Aging | 打破老年美丽羞耻 | Carving Out New Life Paths | “她”创造新赛道

[Slide 7] China has entered an aging society, with the population aged 45 | + | reaching 400 million | 中国 | 人口全面老龄化， | 45+ | 人群已达 | 4 | 亿 | Digital dairy | People aged 45–65 make up almost 27% of the population, and over 10% of people are expected to join this group within the next decade. | 45-65 | 岁人群占比近 | 27% | ，超 | 10% | 人群未来 | 10 | 年将迈入 | 45+ | 45-55 | 岁： | 2.22 | 亿，约占 | 13.6% | ， | 56-65 | 岁： | 1.89 | 亿，约占 | 13.3% | 未来十年进入 | 45 | 岁 | + 35-44 | 岁 | 1.92 | 亿，约占 | 13.6% | The silver economy spans multiple industries, with the senior health products market alone valued at hundreds of billions. | 适老化市场涉及多产业，仅老年保健品市场规模已数千亿 | 老年保健品市场规模预计达 | 7000 | 亿 | 元，占比 | 46.7% | 2023 | 年中国老年用品市场规模达到 | 5 | 万亿 | 元人民币，产品种类和数量已具规模 | *联合国数据 | *政府工作报告 | 7

[Slide 8] Digital dairy | Generational Characteristics of the Chinese | 45+ | 45+ | 人群的 | 代际对比特征 | 1949 | 1978 | 2003 | 2020 | 2025 | 新中国成立 | 经济匮乏 | 粮食短缺 | 医疗条件简陋 | 恢复高考 | 改革开放 | 医疗起步 | 全球化 | SARS | 事件 | 经济腾飞，奔小康 | 互联网迅猛发展 | 医疗进步，开始信息化 | 新冠疫情 | 经济稳态化，富裕 | 互联网 | / | 电商成熟 | 医疗条件智能化，信息数据化 | AI | 智能体爆发 | Ai+ | 医疗生态开始建立 | 1994 | 市场 | 经济体制改革 | 个体化进程 | 与 | 80 | 后互联网原住民相比， | 70 | 后对 | 网络 | 新技术仍偏向工具化认知和使用 | 中国上行期红利的第一代受益者，出现阶层分化 | 既保留传统责任伦理观念，又接受现代新思潮冲击 | 经历过中式思潮大 | 转折 | ，更易信任洋品牌及推崇西方生活方式 | 8 | The first generation to benefit from | China | ’ | s | upward phase dividends | , | c | lass stratification | emerging | . | Preserving traditional values of ethical responsibility while embracing the impact of modernism. | A major shift in Chinese cultural attitudes has led to a greater tendency to trust foreign brands and embrace Western lifestyles. | Compared to digital natives, those born in the 1980s, people born in the 1970s still tend to view and utilise new internet technologies primarily as tools.

[Slide 9] A | TRANSFORMING | GENERATION | 9 | Chinese | 45+

[Slide 10] Keyword 1: | Defining the New | Aging | 关键词 | 01 | ： | 定义新“老年” | 自我认知 | Pursuing Multiple Identities | 追求多元身份 | New Workplace Competition | 职场新竞争 | Rewriting | Lifecourses | 生命阶段整体延迟 | The delay to first marriage and childbirth, plus advances in reproductive technology, has led to 25% of older mothers. Maintaining fertility-related health is key. | 初婚和初育推迟 | ， | 生殖 | 技术发展，高龄孕产妇比例达 | 25% | 。 | 对身体机能的 | 修复以及生育相关的 | 保养 | 再次成为关注重点 | Retirement age delayed, technology accelerating. Those 45+ face renewed competition for cognitive agility and learning capacity. | 退休后延 | ，技术迭代， | 45+ | 面临新一轮竞争 | ，大脑灵活性、学习力等也在“卷起来” | A retired journalist taught herself classical guitar and was admitted to the Sichuan Conservatory of Music at 61. She aims to hold a concert by 80. | 前新闻媒体人退休后自学古典吉他， | 61 | 岁考上川音本科，目标 | 80 | 岁开音乐会 | The traditional identity of middle-aged and elderly individuals—knowing one‘s destiny at fifty and withdrawing upon retirement—is outdated. | 传统的中老年身份（ 五十知天命、退休即退出）是一种过时的、强加的社会期望 | Get involved in community governance, volunteer and do grassroots work. | 参与社区治理、志愿服务、基层街道工作 | Invest in self-exploration, unlock untapped potential, and switch to a new track. | 全方位投资和探索自己 | ，开发自己其他潜力，换新赛道 | 80.58% | of middle-aged and elderly individuals have participated in interest-based learning. | 80.58% | 的中老年人已参与兴趣学习 | Secondary Development of Self-Potential | 自我二次开发 | Actively engage the public | , | foster social identity | 积极进行公众参与，建设社会身份 | Retired engineer becomes tech vlogger, using models and accessible language on | Bilibili | and | Douyin | to explain aerospace and chip knowledge. | 退休工程师变身 “ | 硬核科技博主”。 | 在 | B | 站、抖音上用模型和通俗语言讲解航天、芯片知识 | 10

[Slide 11] Keyword | 2 | : | Rebuilding | Sense | of | Security | 关键词 | 02 | ： | 重建安全感 | # | Property value depreciation | 房产价值缩水 | 50+ Dating TV | Show | 50+ | 恋综 | 《 | 日落时分说爱你 | 》 | #Older | Immigrants | 中年移民 | 子女 | / | 养老 | / | 二次就业 | # | Gray Divorce | 老年离婚潮 | 亲密关系不稳定 | # | Empty Nest Syndrome | 情感空巢 | #Parental Estrangement | “断亲”现象 | Smart Companion Device for Seniors | 老年人 | 陪伴 | 机 | # | E | ra of Low Interest Rates | 低利率时代 | The Intergenerational Relationship Revolution | 代际关系革命 | Evolution of Marriage Concepts | 婚姻观念迭代 | Economic Cycles and Policy | Changes | 经济周期与政策变动 | Interpersonal Networks are Less Tight-knit | 人际网络松动 | # | Intergenerational Conflict of Values | 代际冲突 | # | Annual | Marriage | Examination | 婚姻年检 | 对婚姻质量要求提高 | # | Traditional industries | declined | 传统行业加速没落 | Building Functional Social Support Networks | 开发 | 功能性社交支持网 | 广场舞 | App | 组织线下舞蹈队 | Learn financial management and reallocate assets. | 学理财，重新配置资产 | # | Pension Concern | 养老金隐忧 | QuestMobile | 移动端证券投资月度活跃用户规模稳居 | 1.1 | 亿 | ， | 51 | 岁 | + | 用户持续增加，占比达 | 20.5% | 11 | #50+ Dating Market | 50+ | 婚恋市场兴起 | 银发追爱 | #Families | Living | Apart | 家人分居常态 | 共同性缺失

[Slide 12] Keyword 03: | The New Arena for Women | 关键词 | 03 | ： | 女性 | 新场域 | Social roles are liberated, transition paths grow broader, | SHE | is | actively carving out new paths for the second half of live. | 社会角色解放， | 转型赛道更宽广，自我探索路径更发散 | SHE | is | now | experience a concentrated release of desire for romance, due to unmet need in youth. | 报复性补偿青春时代未被充分满足的 “浪漫体验”需求 | Feminist consciousness awaken, | SHE | is | pursuing lasting beauty | , | shattering the stigma of aging gracefully. | 女性意识觉醒 | + | 资本积累，追求一直“美”下去 | Female groups show more restructuring and typological differentiation than male groups. | 相较 | 于男性群体的延续性，女性群体展现出更强的重构性，类型分化更多元 | Breaking the Beauty Stigma of Aging | 打破老年美丽羞耻 | Emerging | Desire for Romance | “浪漫”需求集中释放 | Carving | Out | New | Life | Paths | “她”创造新赛道 | A monthly top-up of 6,000 yuan is spent on watching those elderly Mary Sue short dramas. | 月月充值 | 6000 | 元，只为追老年玛丽苏短剧 | 1/3 | cosmetic surgery patients are women over 45. | 整形专科医院 | 45 | 岁以上女性新客户占近 | 1/3 | 有皱纹的手也爱晒美甲 | TikTok and | Xiaohongshu | . The number of accounts run by female entrepreneurs aged 50+ is growing rapidly. So is their e-commerce influence. | 抖音、小红书， | 50 + | 女性创业者的账号数量及带货能力增长迅猛 | This popular IP, featuring middle-aged and elderly women, has successfully transitioned into an independent brand. | 中老年女性 | 热门 | IP | 成功转型为自主品牌 | New Ace in Entrepreneurship | Female Corporate Executive | ICH | 非遗 | Inheritor | Lifestyle Aesthete | Charity Organizer | Homestyle Cuisine KOL | 12

[Note] PPTX has 30 slides; only first 12 slides extracted for prompt smoke test.

---

## File: 【Proposal】Empowering 45+ Healthy Aging Pursuit_Synocodes.pptx
- file_type: proposal

[Slide 1] Empowering 45+ Healthy Aging Pursuit

[Slide 2] Table of Content | 目录 | 2 | Background and Business Issue | 项目背景与商业问题 | Project objective | 项目目标 | Our Approach and key outputs | 我们的方法论与核心产出 | Research methods | 具体研究方法 | Team, Timeline & Cost | 时间、团队与预算

[Slide 3] Business background | 商业背景 | ： | - VMS is a promising category but in a very crowded neighborhood. Y24 total China VMS according to Nicholas Halls is 17.8B GBP, CAGR(24/20) is 8.7%. VMS市场潜力可观但处于高度竞争环境。数据显示，2024年中国VMS市场规模达178亿英镑，2020-2024年复合增长率为8.7%。 | - We have a significant upside but China still a whitespace – our ability to grow is exponential riding on aging population. Healthy lifestyle of aging population in China is “living vibrantly for longer”, as their mindset shift from anti-aging to enjoy aging with a more sophistic product requirement. 过去十年中国消费者健康诉求持续升级。最新研究显示，中老年群体的健康生活方式已演变为"活力长寿"，对多元化健康解决方案需求迫切，VMS市场机遇与挑战并存。 | - Reckitt VMS brands incl. | Movefree | (Bone & Joint Health), | Megared | (Cardiovascular Health), | Neuriva | (Brain) and Schiff. YTD25P4 | Movefree | is 37% of GC+UCII, YTD25P4 | Megared | is 16.5% in CoQ10 category. | 利洁时VMS品牌包括 | Movefree（骨骼关节健康 | ）、 | Megared（心血管健康 | ）、 | Neuriva（脑部健康）以及 | Schiff。2025 | 年前四个周期，Movefree | 占氨基葡萄糖 | + UC-II | 品类的 | 37%， | Megared | 占辅酶 | Q10 | 品类的 | 16.5%。 | - Reckitt is also looking to launch a new brand Schiff, catering to 45+ and hence needs to see category opportunities (excl. the ones we are already strong: bone & joint and heart). | 利洁时计划推出新品牌 | Schiff，目标客户为 | 45 | 岁以上人群，因此需要探寻品类机会（不包括已占据优势的骨骼关节和心脏健康品类 | ）。 | - A 2-phase consumer study is therefore planned to holistically understand 45+ healthy aging pursuit to stay vibrant for longer, and identify our category growth opportunities. 启动两阶段消费者研究，系统洞察45+核心人群对于“活力长寿”健康变老的诉求，识别品类增长机会。 | Business objective | 商业目标 | : | Understand how Reckitt can enlarge VMS business in our core categories which have the highest relevance to 45+ hence need to identify category entry opportunity (where to play) and how to tackle (right to win) through a holistic understanding of 45+ healthy aging pursuit | 基于对45+人群追求“健康老龄化”的系统性洞察，寻找VMS品类切入机会。在与45 | 岁+消费者关联性最高的品类中拓展VMS品类增量 | Background and Business Issue | 项目背景 | 3

[Slide 4] Understand perceptions, expectations, and pain concerns surrounding healthy aging, and gain in-depth insight into what “aging healthily” truly means in terms of lifestyle and everyday life scenarios. | 理解对健康老龄化的认知、期待和担忧，深入刻画“健康的老去”究竟意味着怎样的生活方式和生活场景 | What is 45+ definition of healthy aging, what is mindset evolution (anti-aging to happy aging to enable living vibrantly for longer, etc.)? What are the biggest concerns when they think of “aging” | 45+消费者如何定义“健康老龄化”？认知观念如何演变（从抗衰老到快乐老龄化，再到活力长寿等）？ | TA们对“老去”最大的担心是什么 | ？ | How do these expectations and concerns shape their lifestyle as they age? Where do they invest their time and energy? What life scenarios are most closely connected to these aspects? What kinds of health-related needs are likely to emerge from these life scenarios? | 这些期待和痛点如何影响了他们的“老去”生活方式？他们的时间精力投入在哪些方面？有哪些生活场景与之高度相关？这些生活场景会催生怎样的健康需求？ | To deeply explore the lifestyles associated with “healthy aging,” identifying emerging health standards and pain points, uncovering unmet needs, and identifying more effective communication entry points. | 深入探查为了实现 | “ | 健康增龄 | ” | 的生活方式，出现了哪些新的健康标准和健康痛点，识别未满足需求，寻找更好的沟通切入点 | How do they assess whether they are “aging healthily,” and what new standards are emerging? | TA们如何衡量是否“ | 健康的老去 | ”， | 有哪些新标准 | ？ | How do they become aware that they are not “aging healthily”? In what scenarios does this awareness become more pronounced? | TA们是如何意识到自己没有在“ | 健康的老去 | ”？ | 在哪些场景下TA们会更强烈的意识到这一点 | ？ | What solutions are they currently choosing? How did they learn about them? And why do they trust them? | TA们目前都在选择哪些解决方案？是如何知道的？为什么信任 | ？ | Research Objective | 项目目标 | 4

[Slide 5] 45+ consumers | Where to play | 战略聚焦领域 | Health direction | 健康方向 | sleep | 睡眠 | eye health | 眼部健康 | immunity | 免疫 | brain health | 脑健康 | digestive health | 消化健康 | Other（Key） | 其他 | Occasion Size | 场景规模 | VMS relevance VMS | 相关性 | Competition landscape | 竞争格局 | Our choice health direction to prioritize | 优先选择的健康方向 | How to win | 制胜策略 | Benefits (needs & pain point) | 需求痛点与核心利益 | Product aspiration | 产品愿景 | Our Right to Win | 竞争优势构建 | Research Approach 研究方法 | 1. Quantitative evaluation to size the opportunity 量化评估机会规模 | 2.Hybrid/Online community to deep dive key health directions (3-4) | 通过混合式 | /在线社群深入探究核心健康方向（3-4项） | to be defined after phase I output需在第一阶段成果输出后确定 | Background and Business Issue | 项目背景 | 5

[Slide 6] Deep-dive into | HEALTHY AGING | pursuit amongst 45+ consumers, | identify | HOW WE CAN FURTHER EMPOWER THEIR HEALTHY AGING ASPIRATION | 深度洞察45岁以上消费群体的健康老龄化诉求，寻找我们可以更好满足这一需求的机会点 | Health Trend Watch | 健康趋势观察 | Evolving health-related lifestyle & values of the new generation of 45+ consumers | 新一代 | 45 | 岁及以上消费群体健康生活方式与价值观的演变 | Digital Ethnography Study | 数字民族志研究 | Digital ethnography + In-depth interview | 数字民族志 | + | 深度访谈 | Analyzing & Decoding | 分析与解码 | Decoding heathy aging; | 解码 | “ | 健康增龄 | ” | 行为与认知观念 | ; | Deep understanding of 45+ consumers’ core healthcare needs | 深度洞察 | 45 | 岁以上消费群体的核心健康需求 | 6 | New Opportunity Identification | High Potential Areas Targeting 45+ consumers | PROJECT OBJECTIVE | Competitive Barrier Construction | Feasibility Study of "Right to Win" Based on Reckitt‘s Competitiveness

[Slide 7] Our Approach and Key Outputs | 我们的方法论与核心产出 | How do we understand people, their health needs and growth opportunity | 如何理解目标人群的健康需求与增长机遇 | 7

[Slide 8] Layer 1 | Social-culture Context | Identify the Forces of Societal Change to Define the 45+ Demographic | OUR | UNIQUE APPROACH | TO UNDERSTAND CONSUMER NEEDS | 8 | Layer 2 | Outside-in | IMMERSE INTO CONSUMERS’REAL LIFE | Deep-dive into what is really changing in their life/belief | ， | unveil their underlying needs, concerns and expectations | LAYER 3 | Inside-out | Decode the Unseen Needs | Unveiling Latent Needs in Behaviours and Phenomena

[Slide 9] THE DRASTIC SOCIAL-CULTURAL TRANSITIONS IN CHINA THAT HAVE PROFOUND IMPACT ON PEOPLE'S HEALTH CONDITIONS, NEEDS, SOLUTIONS | 加速社会 | Accelerated Society | H | igh adaptive, embrace uncertainty | 高流动 | Spectacular Mobility | Scenarios explosion, Identity crisis | Chinese 45+ Consumers’ Diversified Lifestyle and Values | 创业 | Starting a business | 开启第二职业曲线 | Launching a second career | 环球旅行 | Globetrotting | 移居日本 | Relocating to Japan | 重新学习 | Relearning | 9 | 深度数字化 | Deep Digitalization | Screen life, lens life, high-tech expectations | 中国文化复兴 | China Cultural Rejuvenation | Wholistic approach, TCM ingredients | 激烈竞争 | Fierce Competition | Stressful, Super Stay Up Late | 个体化时代 | Individualization | Lonely, self-dependent solution

[Slide 10] CHANGES IN THE HEALTH MANAGEMENT BEHAVIOUR AND CONCEPT OF CHINESE CONSUMERS | 10 | 精准营养，主动强健 | Precision Nutrition, Proactive Fitness | （2003-2018健康意识提升阶段） | 增补基础营养：蛋白质/钙锌/维生素 | 大豆计划： 推广学生豆奶 | 微量元素补给：钙片、锌口服液推出 | 传统滋补：蜂王浆、参茸等制品 | 西方健康观念开始进入 | 中小学生体质运动： | 国家在学校推广广播体操，眼保健操 | 1978 | 年，改革开放，现代化进程加速 | 1995 | 年，全民健身计划，健康教育进入学校课程 | 2001 | 年，加入 | WTO | ，卷入全球化，大量国外品牌进入中国 | 1978, reform and opening up, accelerated modernization | 1995, national fitness program, health education into school 2001, accession to the WTO, involvement in globalization, a large number of foreign brands into China | 增加营养，被动健体 | Basic Nutrition, Passive Fitness | （1978-2002健康意识萌芽阶段） | 全面营养，智能管理 | Comprehensive Nutrition, | Intelligent Management | （2019- 健康意识日常化阶段） | 定向化高端营养成分 | ： | 大脑类：深海鱼油DHA脑黄金 | 美容类：胶原蛋白/美白丸/酵素 | 睡眠类：褪黑素 | 肠道类：益生菌 | 西方健身观念普及，运动多样化： | 健身房、瑜伽、跑步等 | 马拉松赛事热潮 | 2003 | 年非典引发全民对免疫力的关注 | 2016 | 年《健康中国 | 2030 | 规划》，营养干预成为国家战略 | 2014 | 年天猫国际开通跨境保健品直邮 | 2003 SARS triggers national attention to immunity | 2016 Healthy China 2030 Plan, nutritional intervention becomes a national strategy | 2014 Tmall International opens cross-border healthcare products direct shipping | 个性化/日常化营养管理 | 保健品从药店扩展到日常生活：健身房/办公室等 | 健康随身测：智能手环佩戴，血糖监测针管 | 全天检测：心率/睡眠等 | 保健方式：中西医结合 | 维C+草本，营养+中药 | 健身运动居家化 | 互联网短视频/健身主播兴起 | 2019年，国家强调老年人力资本再开发 | 2020年疫情爆发，国民出现“免疫焦虑” | 2022年《国民营养计划2022-2030》，生命全周期营养干预 | 2023年，老龄化引发对银发营养市场的重视 | 2019, the country emphasizes on the older labor capital | 2020, the covid-19 pandemic leads to the national immune anxiety | 2022, the National Nutrition Program 2022-2030, life-cycle nutritional interventions | 2023, aging triggers the emphasis on the silver hair nutritional market | Basic nutrition supplements: protein, calcium, zinc, vitamins | Soybean initiative: promoting soy milk for students | Micronutrient supplements: calcium tablets, oral liquid containing zinc | Traditional ingredients: royal jelly, ginseng, and antler products | Western health concepts are emerging | Physical fitness drive for school students: The state promotes broadcast gymnastics and eye - care exercises in schools. | Targeted high-end nutrients: | Brain: deep-sea fish oil DHA brain gold | Beauty: collagen/whitening pills/enzymes | Sleep: melatonin | Intestinal: probiotics | Western fitness concept popularization, sports diversification: | Gym, yoga, running, etc. | Marathon race craze | Personalized/daily nutritional management | Health care products expanding from drugstores to daily life: gyms/offices, etc. | Health on-the-go measurement: smart bracelets to wear, syringes for glucose monitoring | All-day testing: heart rate/sleep, etc. | Health care modalities: combining Western and Eastern medicine | VC+herbs, nutrition+TMC | Fitness at-home exercise | Rise of Internet short videos/fitness anchors

[Slide 11] 11

[Slide 12] 身心同养，一体化调理 | Mindful Body Wellness | 身体资本化，全方位精细投资 | Capitalized Body | 医疗科技设备居家化 | Emerging smart healthy household appliances | 赛博传统，提纯式高效养生 | Cyber-tradition | 12 | 居家户外健身运动多样化 | Diversified in-home & outdoor activities | 智能个性化传统养生 | Personalized intelligent traditional applications | 国民主动健康观念提升 | Enhanced proactive health concept | … | 身心同步增强免疫力 | Enhance both physical and spiritual wellbeing | … | 高科技提纯古法配方 | High-tech purification of | ancient recipes | … | THE POTENTIAL DIRECTIONS OF CULTIVATE · NURTURE

[Note] PPTX has 47 slides; only first 12 slides extracted for prompt smoke test.

---

## File: 【客户内部资料】45+ learnings by category.pdf
- file_type: client_material

[Page 1] Consumer Insight 社 媒 营 销 数 智 化 领 跑 者

[Page 2] Social media discussion trends on immunity 免疫力社媒讨论趋势 During 2022 - 2023, due to the COVID-19 pandemic, the topic of improving immunity was widely discussed. As it's hard to In the past two years when the pandemic broke out, consumers' demands for enhancing immunity increased continuously.近两年疫情爆发，消费者对提升免疫力诉求 fully remove the pandemic's impact (many people mentioned 不断提升。 immunity without relevant keywords), the data has been manually processed to make December 2022's figures equal to those of December 2023 after excluding the impact as much as possible. 22-23年由于疫情原因，提升免疫力话题被热议（因为这期间很多人提 及免疫力但未提及疫情相关的任何关键词，所以无法完全剔除疫情的 GR 近两年 消费者声量趋势UGC BUZZ TREND 影响，目前的数据是尽可能剔除疫情的影响外将22年12月份数据人工 +3% Content SOV GR 处理到与23年12月持平） in the past two years Buzz 声量Buzz What's included in the general trend but excluded from the Occasion follow-up analysis: Only the topic of immunity is mentioned, It's easy to get sick in winter. On TOP Topic (23.11-23.12) Buzz 38.2% +21.6% 800,000 After the pandemic lockdown was lifted Douyin, topics like health #提高免疫力 92,260 场景 without aspects like scenarios, solutions, diseases and needs. and when the COVID-19 virus spread preservation (12%), swimming (8%), #冬泳提高免疫力 64,732 (Such content usually occurs when UGC short video titles widely, many discussions on improving 免疫力 700,000 and aerobic fitness (2%) are #增强抵抗力 20,695 mention immunity but the video content isn't recognized by immunity were triggered.疫情解封后，新 冠病毒大范围感染，引发大量提高免疫力相 generating heated discussions. 冬季 #健康养生 17,498 Solutions voice recognition.) immunity 600,000 关讨论 易生病，抖音渠道养生（12%）、游泳 #调理身体 16,644 34.3% +1.0% 总趋势包含但后续分析内容中不包含的：只提及免疫力话题未提及场 （8%）、有氧健身（2%）等话题热议 #增强免疫 16,640 解决方案 景、解决方案、病症、需求等维度内容（这类内容一般是UGC短视频 UGC Buzz 500,000 #有氧健身操提高免疫力 16,523 标题提及免疫力但视频内容未语音识别） 如： 9,314,098 400,000 Symptoms 25.6% +23.9% ①#养生之道 #提高免疫力 #健康养生 病症 ②#免疫力 #健康科普 #提高免疫力 300,000 Chinese New Year ③#补气血 #女人爱美不分年龄 #提高免疫力 #保养自己 天使雪莲6虚 中国新年 同补#生活处处有惊喜 200,000 Needs Remove most of the *During Chinese New Year, the discussion of industries with low relevance to the festival, including brain health, on 需求 15.8% +7.7% discussions related to the social media platforms is generally low. UGC are more inclined to share content related to travel, entertainment, cuisine, 100,000 COVID-19 pandemic. and clothing. 剔除大部分新冠疫情相关 0 讨论 *Others 31.3% -8.9% 其他 *such as only mentioned improve immunity topic Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30 社 媒 营 销 数 智 化 领 跑 者

[Page 3] Symptoms caused by weakened immunity 免疫低下相关病症 The main and rising symptoms are cold/flu led to sneeze, runny nose(35%, GR=+28%), digestive disorder(25%,GR=10%) and skin discomfort(11%, GR=49%). Aged may usually have low energy, aversion to cold/ heat due to decline in physical function. Young Adults may have low energy and hair loss under work and life pressure. Under 18 years old is in the stage of growth and development, so they susceptible to illness, especially for digestive and respiratory tract Core Symptoms : Young YOY Aged group ≤Age 18 • 35% Cold/flu led to sneeze, runny nose打喷嚏、流涕 Symptoms 病症 Adults (MAT GR) TGI TGI • 25% Digestive disorder消化系统失调 TGI • 11% Skin discomfort皮肤不适 Cold/flu led to Rising Symptoms: sneeze, runny nose 35.3% +28% 90 67 106 打喷嚏、流涕等 Decline in • 35% Cold/flu led to sneeze, runny nose, GR=+28% physical Low energy • 11% Skin discomfort皮肤不适, GR=+49% function 8.6% +14% 149 193 80 精神不振 身体机能下降 Prominent Symptoms SOV: 59% Aversion to cold/heat 4.9% +7% 171 159 77 GR: +26% 畏冷怕热 Aged: Decline in physical function and chronic disease Hair loss 3.2% -5% 149 244 76 • Low energy精神不振 脱发 • Aversion to cold/heat畏冷怕热 Skin discomfort • Cardiovascular disorder心血管失调 Organ 皮肤不适(过敏,湿疹,红痒等) 10.9% +49% 78 110 106 Young Adults: High work pressures and poor daily allergy/inflamm Such asallergy, eczema, redness and itchy ation Sensory discomfort routine, dietary issues (Lack of fruits and vegetables, often eating takeout) 器官过敏/炎症 五官不适 9.7% Such as oral ulcers, +13% 72 70 111 conjunctivitis, and • Low energy精神不振 SOV: 36% nasopharyngitis • Hair loss脱发 GR: +23% Musculoskeletal discomfort 肌肉骨骼不适 2.9% -1% 231 165 72 • Skin discomfort皮肤不适 such as arthritis,rheumatism ≤Age 18: Incomplete physical development, picky eaters Digestive disorder 24.5% +10% 86 89 106 • Cold/flu led to sneeze, runny nose打喷嚏、流涕 消化系统失调 Organ dysfunction • Digestive disorder(especially poor nutrient absorption and poor appetite)消化系 器官功能失调 Cardiovascular disorder 8.7% +5% 247 186 62 统失调,尤其吸收不好和食欲不振 心血管失调 SOV: 33% • Sensory discomfort(especially respiratory tract)五官不适，尤其呼吸道问题 GR: +6% Metabolic disorder 2.8% -52% 170 218 78 代谢系统失调 Symptomsbase = 2,384,163 社 媒 营 销 数 智 化 领 跑 者 ; Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Page 4] Specific Impacts of Low Immunity on Various Systems Low immunity not only affects local defense but also triggers multi - organ chain reactions through cross - system mechanisms such as the "immune - gut axis", "immune - vascular axis", and "immune - metabolic axis". 25% Digestive disorder 9% Cardiovascular disorder A weakened immune system A weakened immune system can makes the body prone to cause disorders of the intestinal infections, which can trigger • Vascular issues（82%） flora, secretion of digestive cardiovascular diseases, and the • 血管问题：体检结果说我血糖有点高，就去买了 juices, and gastrointestinal inflammation can promote 这吃，蜂胶具有提高免疫力，平衡血糖的作用。 长期吃，确实不怎么感冒。 motility.免疫力低下会导致肠道菌群、消 atherosclerosis as well as • Heart issues（21%） 化液分泌和胃肠动力紊乱 imbalance of blood coagulation • 心脏问题：去年开始吃这个，效果不错，现在 and fibrinolysis.免疫力低下使身体容易 已经很少有心慌的情况了，免疫力也好了很多， 最近一年感冒都少了，推荐 感染，从而引发心血管疾病，炎症会促进动 • Digestive disorder（68%）: 脉粥样硬化以及血液凝固和纤维蛋白溶解的 • 肠胃紊乱：给老公买的，对肠胃好，适合他这种经常应酬的人，还可以提 不平衡。 高免疫力，之前在外面大鱼大肉的不规律饮食，经常腹泻，经常胃疼，现 在也没听他说有腹泻过！ • Poor absorption（26%）: 3%Metabolic disorder • 吸收不好：这款益生菌对促进营养物质的吸收的功效还是不错的，可以合 成消化酶，与人体合成的消化酶一起参与肠道中营养物质的消化，还可以 提高机体的免疫力。 A weakened immune system can • Loss of appetite（24%）: Metabolic disorders of sugar, fat and protein lead to abnormal hormone • Metabolism: • 食欲不振：vc提高免疫力我也是听朋友说的，她家的小孩儿以前特别爱生 病特别是上学的时候，自从吃了以后抵抗力明显好了，很有效果！然后她 secretion, inflammation • 基础代谢慢，因为喜欢熬夜的原因，脸上容易 就强力推荐我给我儿子买来吃试试，口感还可以，吃了一段时间以后感觉 interfering with metabolic signals, 出油，额头也容易爆痘，现在吃了有差不多半 孩子食欲也好了，也不太爱挑食，身体也越来越棒 个月时间了吧，的确感觉身体轻盈了些，脸色 and dysfunction of immune cells. 也好了一些，没有那么爱出油，而且免疫力有 免疫力低下会导致激素分泌异常、炎症干扰 所提升，不易生病。 代谢信号和免疫细胞功能障碍 社 媒 营 销 数 智 化 领 跑 者 Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Page 5] Needs of improving immunity 提升免疫力的目的 Reducing the risk of getting sick(48%) is the core need and shows continuous growth. Especially, teenagers need to boost their immunity to prevent respiratory diseases. Besides, the needs are to promote physical recovery(24%), relieve symptoms(17%), and enhance energy. Young adults and aged focus more on physical recovery and energy boost, while under 18 years old pay more attention to symptom relief.降低患病风险是提升免疫力的主要目的且持续增长，特别是 低龄儿童，需要提升免疫力预防呼吸道系统疾病；其次为促进身体恢复、减轻或舒缓病症，增强精力或缓解疲劳，其中成人和中老年在促进身体恢复，增强精力&缓解疲劳诉求更突出，低龄儿童在减轻或舒缓病症诉 求更突出 Aged Young Core and rising needs: The needs of improving immunity YOY VMS ≤Age 18 group Adults 提升免疫力的目的 （MAT GR） TGI TGI TGI TGI • 48%Reduce the risk of infection.降低感染风险,GR=+16% Prevent recurrent illnesses Second needs: 47.7% +16% 82 73 78 117 预防反复患病 • 24%Promote physical recovery促进身体恢复,GR=-11% Promote recovery 23.5% -11% 109 120 137 81 促进恢复 • 17%Relieve symptoms减轻或舒缓病症,GR=+14% Relieve symptoms 17.1% +14% 107 91 95 105 • 15%Enhance energy and relieve fatigue增强精力&缓解疲 减轻或舒缓病症 劳,GR=+7% Enhance energy and relieve fatigue +7% 180 147 156 65 增强精力&缓解疲劳 15.4% Prominent needs Improve physical wellbeing +17% 91 105 65 109 增强体质 9.8% VMS: Prevent or control chronic diseases -10% 59 187 129 58 预防或控制慢性疾病 5.4% • Promote physical recovery促进身体恢复 • Relieve symptoms减轻或舒缓病症 TOP Symptoms Word cloud Prevent recurrent illnesses YOY VMS 预防反复患病 （MAT GR） TGI • Enhance energy and relieve fatigue增强精力&缓解疲劳 Young adults and aged group: Respiratory system 35% 91 咳嗽 呼吸系统 58.7% • Promote body recovery促进身体恢复 Digestive system • Enhance energy and relieve fatigue增强精力&缓解疲劳 8% 117 腹泻 消化系统 18.4% ≤Age 18: 鼻炎 发烧 流感 阴道炎 皮 Sk 肤 in 16.1% 7% 110 • Reduce the risk of infection降低感染风险 • Relieve symptoms减轻或舒缓病症 过敏 Urinary system 便秘 3.0% -16% 110 泌尿生殖系统 Needs base = 1,467,370 社 媒 营 销 数 智 化 领 跑 者 D;ata sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Page 6] Occasions for Immunity 免疫力相关场景 Infancy(44%), illness periods(38%), and season change(15%) are core occasions and show continuous growth. Also, there‘s high growth in kindergarten/school (GR=48%)and season change(GR=35%). The aged and under 18 years old have low immunity due to their physical conditions(aged: illness periods, season change; ≤Age 18: infancy, kindergarten/school). while young adults’ immune systems are mainly affected by unhealthy lifestyles and work pressure occasions.婴幼儿 期、生病期间, 及季节变化为核心场景且持续增长，幼儿园/学校、季节场景同样呈现高增长。老人小孩因自身体质问题免疫力低下，需要重点防护；而中青年主要因不良生活方式及工作压力影响免疫系统 Young YOY Aged group ≤Age 18 Occasions 场景 Adults Aged group: The elderly often have underlying (MAT GR) TGI TGI TGI diseases and focus more on improving immunity in Infancy 44.2% +31% - - 115 autumn and winter to combat cardiovascular and 婴幼儿期间 Office workers face high work pressure and often work overtime, which can easily cerebrovascular diseases.老年人多患基础病，秋冬更注重提升免 lead to weakened immunity illness periods 37.6% +37% 127 90 95 疫力对抗心脑血管疾病 上班族，工作压力大，经常加班，易导致免疫力低下 生病期间 • 最近感觉身体状态有点不对劲，免疫力低，动不动眼前发黑，我妈都说我嘴唇发白，网上 Special period 一看真是让人心慌！ 996的生活真的是让我们这一代年轻人承受了太多压力 特殊时期 Pre-pregnancy, • illness periods生病期间 • 谁懂电商人的痛！三八忙完就要备战618！老板就怕员工活不够干！为了绩效忍了！但这无 SOV: 79% pregnancy and 6.8% 0% 137 458 - • Season change季节变化 休无止的加班熬夜，觉都不够睡 埋头苦干的“驴”抵抗力终于还是跌倒谷底！最近动不 GR: +25% postpartum period 动就 ，走两步路都得喘！天天脑雾犯困工作还掉链子！太影响日常工作和生活了！上网 备孕/孕产期 做功课，长期不运动久坐加上办公室密不透风，容易免疫力低下我的 Post-operative recovery Young adults: Their bad lifestyles lower immunity. • 前段加班熬夜做项目太厉害，经常晚上1点多才睡觉，感觉身体抵抗力明显下降，天气也反 period术后恢复期 3.9% -2% 399 104 42 复无常，感冒就反反复复的不见好 Pregnant or pre-pregnant people focus more on Menstrual 生 pe 理 rio 期 d 1.7% -6% 141 260 69 boosting it. 成年人不良生活方式致免疫力下降，备孕、怀孕人群更关注 Children with weakened immunity are prone to illness during the school and 免疫力提升 kindergarten period 幼儿免疫力低下开学入园时期易患病 Season change 15.2% +35% 106 58 98 • Staying up late for a long time长期熬夜 • 幼儿园第三天回来就生病了！ [SEP]第一周也才上半天而已 中午就接回来，第三天中午 季节变化 • Work工作（Working overtime and under great pressure） 接回来，就有流鼻涕了接着她就说喉咙痛到晚上果不其然 发烧了 -38度左右晚上真没得 • Pre-pregnancy, pregnancy and postpartum period备孕/孕产期 睡，鼻子塞 一点点咳，躺着睡不着，愣是抱着度过了一个晚上跟她爸轮流。六点多她就醒 Staying up late for a long 了，带去医院 最早的号 八点检查了不是流感，单纯感冒就洗了鼻子 开了药。不过小班 -3% 188 229 66 time长期熬夜 10.0% 真的是 上几天 休几天的吗[捂脸R]怎么样避免跟增强抵抗力阿 ≤Age 18: Infants and toddlers have weak immunity • 开学时正值季节交替，孩子自身免疫力系统不够完善，很容易感染各种疾病。 交叉感染 Daily life 幼儿园人多，更容易接触到各种病原体，特别是抵抗力差的宝宝，感染几率更大。 饮食 日常生活 Work +24% 157 241 - and are likely to fall ill when starting kindergarten.婴幼 不当宝宝开学后，饮食起居有了很大的变化。会导致宝宝胃口降低，吃得少，抵抗力自然 SOV: 36% 工作 8.0% 会慢慢下降。 厌学情绪离开熟悉的家人和环境，身处陌生地方的宝宝容易产生恐怖、焦 GR: +20% 儿免疫力低下，开学入园时期易患病 虑等不良的情绪 • 最近 多的厉害，学校很多孩子都生病了，初中生学习忙不能耽误，也没时间锻炼，买点 Kindergarten/School 幼儿园/学校 6.4% +48% 44 31 115 • Infancy婴幼儿期间 蛋白粉喝，保证营养提高免疫力 • Kindergarten/school幼儿园/学校 Smoking and excessive -13% 214 256 68 drinking吸烟酗酒 1.5% Ocassions Base =3,561,553 社 媒 营 销 数 智 化 领 跑 者 Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Page 7] Solution conducive to immunity 有利于免疫健康的解决方案 Prioritize appropriate exercise(36%) as a solution for immunity health, followed by VMS(33%). Daily protection & routine has a high upward trend. Under 18 years old to rely more on external intervention and artificial active immunization methods, while young adults enhance their immunity through various means such as exercise and diet. Aged tend to lean more towards internal regulation, such as VMS and health diet.首选适当运动作为免疫健康解决方案，其次是保健品。高增有适当运动和日常保 护&作息。18岁以下更偏向通过外在干预和人工主动免疫方式，年轻人则从多方面去提升免疫力，运动+饮食，中老年人会更偏向内调，保健品和饮食 YOY Aged Young ≤Age Aged group: internal recuperation Solution (MAT group Adults 18 内调 解决方案 GR) TGI TGI TGI Young Adults: multi-aspect Appropriate exercise 多方面 35.8% +20% 46 142 112 适当运动 VMS 32.8% -12% 137 43 101 保健品 Health diet VMS 保健品 Healthy diet 健康饮食 Appropriate exercise & TCM diet therapy 17.6% 0% 135 190 63 • Reduce the risk of infection降低感染风险 Health diet 中医食疗 健康饮食 • Improve physical wellbeing增强体质 Physical therapy • Prevent or control chronic diseases预防或控制慢性疾病 15.7% +2% 36 152 118 理疗养生 • Promote physical recovery促进身体恢复 TCM diet therapy 8.7% +10% 60 256 79 ≤Age 18: exercise + combine traditional Daily protection & 中医食疗 Chinese and western medicine运动+中西医结合 Physical therapy routine 理疗养生 日常保护&作息 Daily protection & routine 5.0% +63% 47 205 95 Appropriate exercise Physical therapy 日常保护&作息 适当运动 理疗养生 • Promote physical recovery促进身体恢复 Vaccine • Relieve symptoms减轻或舒缓病症 2.9% -6% 95 105 116 打疫苗 • Enhance energy and relieve fatigue增强精力 &缓解疲劳 Good hygienic habits 小儿推拿 药浴 • Reduce the risk of infection降低感染风险 良好卫生习惯 2.0% +18% 22 135 112 • Improve physical wellbeing增强体质 Vaccine Health check 打疫苗 • Reduce the risk of 健康检查 1.8% +22% 77 180 71 infection降低感染风险 • Improve physical Take a proper sunbath wellbeing增强体质 1.5% +69% 36 134 109 适当日晒 Solutions Base = 3,199,218 社 媒 营 销 数 智 化 领 跑 者 Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Page 8] Solution-VMS After the pandemic, many took health supplements to ease discomfort and regain health. As they recovered, the VMS - related buzz on social media waned. The age group preferred to choose proteins and plant extracts VMS.. Vitamins维生素 Probiotics益生菌 Aged Young VMS ≤Age 18 SOV↓ GR group Adults Category TGI TGI TGI Swisse VC+锌泡腾片 爱维熊女性复合维生素 yollgene儿童复合维生素 合生元益生菌 兰骑士益生菌 兰骑士益生菌 Vitamins Buzz: 28,597; GR:- 40% Buzz:1,614;New Buzz:861;New Buzz:12,914; GR:11% Buzz:3,411; GR:-61% Buzz: 3,340; GR:-54% 37% -5% 63 133 113 维生素 Minerals矿物质 Proteins蛋白质 Probiotics 32% -15% 48 61 123 益生菌 Minerals 16% -10% 63 140 112 矿物质 Proteins 8% +15% 193 79 64 蛋白质 葡萄糖酸锌口服液 佳贝方富硒胶囊 乐米倍优补锌营养包 neurio纽瑞优蛋白粉 汤臣倍健蛋白粉 纽拉里奥乳铁蛋白 Buzz:34,185; GR:-82% Buzz:1,261;New Buzz：672; GR:257% Buzz::8,772; GR:30% Buzz:112,883; GR:-22% Buzz: 1,817;new Fatty acid 3% +5% 90 135 101 脂肪酸 Others其他 Plant extracts 3% +10% 237 133 40 植物提取物 同仁堂氨基酸口服液 同仁堂破壁灵芝孢子粉 同仁堂辅酶Q10 今幸人参皂苷rh2胶囊 爱乐维DHA Buzz:3,637;GR:5% Buzz:32,986; GR:35% Buzz:11,958; GR:-36% Buzz:863; GR:-51% Buzz:367; GR:-18% 社 媒 营 销 数 智 化 领 跑 者 Data sources: Social platform,EC; Data period: 2022/10/01-2024/09/30

[Note] PDF has 29 pages; only first 8 pages extracted for prompt smoke test.

---

## File: 【客户内部资料】Chinese health.pdf
- file_type: client_material

[Page 1] Chinese health pursuit in past 10 yrs shifts from basic to more sophisticated Specific Upgraded Safety function Nutrition • Mobility • Zero additive • Meal replacement • Immunity • Good origin • High protein • Digestion • Zero sugar and fat • Multi-benefits Basic Sophisticated function nutrition Embed into more daily needs-occasions leveraging VMS unique advantage of balanced efficacy and safety 1 Source: 2024 Mintel China consumer health trends

[Page 2] Chinese healthy lifestyle themes by cohorts Young(18-34) Middle Age(35-49) Elder(50+) GOOD HEALTH IS FROM INSIDE OUT BEING HEALTHY IS FOUNDATION TO FROM ANTI-AGING TO HAPPY AGING TAKE CARE OF FAMILY Definition of being healthy 60% 82% 78.7% 75.7% 71.4% Agree enjoying life is their 1st priority after Agree health is cornerstone of family retirement responsibility Mindful body wellness No disease/pain Longevity is useless if you end up on the hospital bed Stress resistance Fun and vitality matters. – Mr.Gong, GZ SEEK UPGRADED NUTRITION REQUIRE SPECIFIC ISSUE LOOK FOR HOLISTIC MANAGEMENT SUITABLE FOR DAILY OCCASIONS PREVENTION SOLUTION Top3 health product purchased in P1Y Top health management needs Top health elements they care about: Function drink 72% Good mobility Symptom Enhance management Digestion 68% Immunity 82% Function food 71% 73 89% Mobility 76% Cardio 63% Health electronic device 59% Source: 2025 Zhimeng China GenZ healthy lifestyle report,, China 2025 middle age health management white paper, 2024 BA Capital China Silver consumption needs trend report, 2025 China Academy of Social Sciences Elder health and support report, McKinsey 2025 generation healthy report , Ali health 2025 annual consumption trend report

---

## File: 【客户内部资料】Discover.ai - Reckitt Healthy Lifestyle - 21.08.22.pdf
- file_type: client_material

[Page 1] Reckitt - Project Ginseng Exploring the narratives of healthy living in China 21 August 2022 1

[Page 2] Discover.ai… A qualitative deep-dive into online sources to discover rich human stories and cultural insights “It’s like eavesdropping on culture in real time” – David Cousino - Global Brand Insight Director AB InBev human stretchy Accelerate expertise Tap into the power and creativity with of rich and diverse our intuitive AI tools online sources global agile Make discoveries Uncover insights faster in any market and at a fraction of across the globe the usual cost 2

[Page 3] How it works Question Expertise Sources Discovery Springboards Define the intractable question Our analysis is qualitative Sample diverse & rich global Explore patterns and make Stretchy springboards are the at the heart of your growth & 100% human, accelerated sources that gets you unexpected connections & start-point for new thinking & challenge by AI technology thinking in new ways creative leaps…fast ideation 3

[Page 4] Exploring narratives around healthy lifestyle and adjacent categories in China 4

[Page 5] Project Ginseng Our question Our sourcing areas What can we learn from relevant We brought together rich & inspiring language from 100 online content and conversations sources across 10 sourcing areas and covering the following languages / markets: China around healthy lifestyle and adjacent categories, in order to gain an insight into consumer pain points, 1. Key established brands in the healthy, wellness, wellbeing lifestyle space preferences and habits that will 2. Emergent brands in the healthy lifestyle, wellness, wellbeing space (e.g. juices shots / natural remedy / eSports / brain health, enable Reckitt to identify and build a athleisure, supplements) VMS growth model that generates the 3. Key Wellness/Wellbeing Brand sites including retailers e.g. Holland and Barrett (relevant to different markets) best BDI’s in China? 4. Health and wellness blogs/magazines –including about TCM (traditional Chinese medicine) 5. Traditional/alternative medicine blogs, forums, and magazines (especially the ones that use colours and different types of energy like TCM and Ayurveda) 6. Performance enhancing supplements/food (e.g. Nootropics / Adaptogens/TCM) 7. Blogs and forums discussing at-home natural remedies and homeopathy 8. Healthy lifestyle /healthy living /holistic wellness/natural living magazines, newspapers, blogs 9. Psychological / nutritional / scientific experts focusing on topics around wellbeing & health 10. Relevant Social Media searches on healthy lifestyle Project created by Igor Savotskin –Powered by Discover.ai

[Page 6] Introducing your Springboards 6

[Page 7] The springboards are divided into four areas • THE SIMPLE FUNDAMENTALS In this space, healthy lifestyle is about access to the high-quality basics that make you feel good - from clean air, to a clear head, to good restful sleep. Finding little ways to make your body and mind function smoother, so that you can enjoy daily life. • YOU ARE WHAT YOU EAT This space builds from the Chinese proverb that "sickness enters from the mouth" - the idea that a healthy lifestyle starts with eating more consciously, to make up for dietary lacks and also ensure that your body gets the most powerful, safest ingredients. • • CONNECTED TO YOUR WORLD This space focuses on two moments of particular need in a Chinese person's life - early childhood, and middle- to old-age. How can you make sure that health is within reach at these times, both for your own wellbeing, and to maintain social harmony with those close to you? • • TIME-HONOURED AND TRUSTED This space is about spotlighting some classic health principles that Chinese people have relied on for centuries - preserving them, or finding ways to make them more relevant for a contemporary healthy lifestyle. • 7

[Page 8] The Simple Fundamentals In this space, healthy lifestyle is about access to the high-quality basics that make you feel good - from clean air, to a clear head, to good restful sleep. Finding little ways to make your body and mind function smoother, so that you can enjoy daily life. Healthy lifestyle in China could be about… Breathing Easy The Wonderful Everyday A Better Headspace Tailored, Trackable and True Tackling the many concerns After the tumult of the last few Building on both the Western With the rise of health apps and around air pollution, in major years, Chinese people are mental health movement and technology, more Chinese people Chinese cities. How can increasingly slowing down, to pay traditional Chinese medicine are using personalised data to craft consumers employ better daily attention to the fundamentals of principles, consumers are leaning smarter health plans that can habits, and choose the right holistic health -sleep, water, work- into the idea of inner happiness as optimise their bodies -while also supplements, to protect their lungs life balance, and exercise. Doing the foundation of good health. using tech to fight the -but also their skin, eyes and even simple but powerful things to Seeking ways to reduce anxiety and misinformation that abounds in the brain -from the toxins all around nurture health, amidst the daily boost joy, so that the body can area of health. them? grind. function optimally.

[Note] PDF has 57 pages; only first 8 pages extracted for prompt smoke test.

## 参考案例逻辑

## case_004

# Case Card - Case_004 45+ Healthy Aging

## 1. Basic Info

- Case ID: Case_004
- Project name: Empowering 45+ Healthy Aging Pursuit
- Category / brand: VMS / 健康产品 / 健康老龄化相关产品
- Project type: 特殊人群研究；健康需求研究；健康产品信任机制；Digital Diary + 入户/IDI 分工
- Target audience: 45+ 人群，包含 55-60 岁及少量 60+ 人群
- Main method: Digital Diary / 数智生活志，4 天记录；后续入户访谈/深访

## 2. Business Problem

VMS 市场有增长潜力但竞争拥挤，客户希望理解 45+ 中国消费者如何看待健康老龄化、身体变化、健康实践和健康产品信任，从而找到品牌进一步赋能健康老龄化诉求的机会。

## 3. Research Objectives

- 理解 45+ 人群对健康老龄化的认知、期待和担忧。
- 理解“健康地老去”在生活方式和日常场景中意味着什么。
- 捕捉身体状态、心理状态、健康意识和生活角色的变化。
- 理解口服健康产品、保健品、营养补充剂、健康服务、健康习惯的完整解决方案。
- 深挖健康产品和品牌信任机制，包括 first entry、效果判断、安全感、背书、转换和忠诚。

## 4. Input Material Signals

- 目标人群年龄偏大，尤其包含 55-60 和少量 60+。
- 目标人群可能存在文字填写负担；designer agent 应在 handoff 中标记素材方式和负担风险。
- 研究不仅关注产品，也关注生活角色、身体信号、心理状态和健康实践。
- Digital Diary 主要收集事实和浅层 why，入户/IDI 用于深挖环境、驱动因素和信任机制。

## 5. Final Module Structure

1. 关于我和我的生活 / About Me and My Life
   - 自我介绍、居住城市、家庭、宠物、生活角色、兴趣、社交、信息渠道、人生转折、未来计划。
2. 我的身体状态 / My Physical State
   - 当前身体/心理状态、理想健康、健康问题、小毛病、季节/城市/饮食变化、年龄相关身体信号。
3. 我的产品解决方案 / My Product Solution
   - 健康产品、健康设备、健康服务、健康习惯的完整图谱。
4. 被我信任的健康产品 / The Health Product I Trust
   - first entry、信任建立、效果判断、安全感、比较、扩品类、中断、忠诚。
5. 我的健康生活记录 / My Self-Care Record
   - 4 天记录日常生活、身心状态、三餐、健康加餐、健康实践、健康话题和社媒接触。

## 6. Key Question Logic

- 对 45+ 人群，必须标记语气、题量和素材方式风险，具体表达由 wording agent 处理。
- 可优先采用视频、照片、语音等素材方式来降低文字负担。
- 先从生活角色、家庭、兴趣和人生阶段切入，再进入身体状态和健康产品。
- 健康产品不能只问保健品，要扩展到设备、服务、食补、习惯。
- 信任机制要完整追问：第一次接触、为什么开始、犹豫点、效果判断、安全感来源、品牌比较、扩品类、中断、忠诚条件。

## 7. Reusable Rules

- 特殊年龄人群要调整题量、素材方式和填写负担；语言表达交给 wording agent。
- 如果目标人群年龄偏大，应优先鼓励视频、照片、语音，而不是长文字。
- 健康/VMS 项目不能只问产品，应问完整健康解决方案。
- 健康品牌信任研究要追问 first entry、proof of effectiveness、safety、endorsement、switching、loyalty。
- Diary 适合收集日常事实、健康行为、身体感受和即时记录；IDI/入户适合深挖信任机制和生活环境。

## 8. Do Not Overgeneralize

- 不要把 45+ 的题量、素材方式和负担假设套到所有人群。
- 不要把健康产品信任机制直接套到非信任驱动品类。
- 不要只靠 diary 深挖抽象 perception；复杂信任和深层动机需要 IDI/入户承接。

## 9. Best Reference For

- 45+ / senior / 特殊人群研究。
- 健康、VMS、营养补充剂、保健品。
- 健康品牌信任机制。
- 需要视频/语音降低负担的 Digital Diary。
- Diary + IDI / 入户分工设计。

---

## case_002

# Case Card - Case_002 Chocolate Category Growth

## 1. Basic Info

- Case ID: Case_002
- Project name: 玛氏巧克力品类发展机会研究
- Category / brand: 巧克力；德芙 / Mars chocolate portfolio
- Project type: 品类增长机会研究；零食场景机会；生活方式与情绪需求探索
- Target audience: 巧克力目标消费者，关注 snacking 相关生活方式和需求
- Main method: Digital Diary / 数智生活志，围绕零食生活和巧克力时刻展开

## 2. Business Problem

巧克力在中国市场渗透率不低，但购买频率和人均消费量偏低，消费高度集中在 CNY 和节庆。客户希望通过 brand communication 让德芙进入更多日常生活场景，提升巧克力品类频次。

## 3. Research Objectives

- 理解目标消费者生活状态和生活方式。
- 理解 TA 与 snacking 相关的需求、生活场景、待办任务。
- 理解当前零食解决方案，以及已满足/未满足需求。
- 识别体量大且德芙有机会进入或 own 的高价值场景。
- 建议德芙可以切入的 brand communication angle。

## 4. Input Material Signals

- 巧克力已有稳定品类心智，但与糖果、礼赠、节庆等固有场景绑定较强。
- 核心挑战是打破固有认知边界，寻找日常化、高频化的需求场景。
- 零食与情绪高度相关，尤其巧克力与“甜”“愉悦”“慰藉”等情绪关联明显。
- 需要理解消费者一天中的情绪波动，以及吃零食前后的状态变化。

## 5. Final Module Structure

1. 我和我的生活
   - 自我介绍、生活方式、情感状态、个人角色、兴趣与日常。
2. 吃吃喝喝实时记录
   - 工作日和休息日记录零食、三餐、情绪变化和触发点。
3. 吃货日常总结
   - 回顾固定零食时刻、未满足时刻、新增心头好、零食意义。
4. 我的巧克力时刻
   - 下载巧克力在生活中的具体出现方式、品牌心智和内部预设场景反馈。
5. 我的重度沉迷零食养成记
   - 捕捉高频/沉迷品类或巧克力习惯如何形成、加深和评价。

## 6. Key Question Logic

- 先理解整体零食生活，而不是一上来问巧克力。
- 通过全天零食记录获得完整 snacking 图谱，包括何时想吃/吃、决定吃什么、怎么吃、和谁、在哪里、吃后评价。
- 同步记录情绪曲线，尤其是零食触发点、转折点、峰谷时刻。
- 用“新增心头好”“重度沉迷零食”理解习惯养成和品类替代机会。
- 对巧克力单独追问最近出现时刻、品牌心智、德芙可能进入的场景。

## 7. Reusable Rules

- 如果目标是品类日常化/高频化，不要只问目标品类，应先画出更大的生活方式和相邻消费图谱。
- 如果品类与情绪强相关，应记录一天中的情绪波动和消费前后状态变化。
- 如果要找高价值场景，应同时问当前解决方案、未满足需求和品牌可进入性。
- 对低频但高潜品类，可通过“相邻高频品类 / 重度沉迷品类”反推习惯形成机制。
- 品类增长机会研究要识别“品类已有心智”与“待拓展场景”之间的张力。

## 8. Do Not Overgeneralize

- 不要把所有食饮项目都做成完整零食日记；只有当 snacking 图谱对研究目标关键时才需要。
- 不要把巧克力的情绪驱动直接套到所有食品饮料品类。
- 不要只关注品牌沟通，需要先确认生活场景和需求是否成立。

## 9. Best Reference For

- 食品饮料品类增长。
- 零食/snacking 场景研究。
- 情绪驱动消费研究。
- 低频品类寻找高频日常机会。
- 从相邻品类反推目标品类机会。

请只学习以上案例的设计逻辑，不要复制案例题目。
```
