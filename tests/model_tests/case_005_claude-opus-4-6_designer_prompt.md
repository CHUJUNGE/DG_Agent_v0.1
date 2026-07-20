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

16. 当项目涉及特定人群、生活方式、代际/圈层变化、非刚需品类机会或需要先理解“这个人”时，About Me / 了解一个人模块不是轻量 warm-up，必须在进入品类或产品前覆盖：
   - 自我介绍、关键词、代表性图片；
   - 生活空间 / room tour；
   - 生活重心、生活节奏；
   - 消费习惯：大头消费，以及哪些非刚需但特别愿意花钱；
   - 兴趣爱好及相关场景；
   - 社交圈，以及自己在社交圈里的角色，例如跟随者、发起者、组织者、倾听者；
   - 生活痛点：可用 1-10 轻量打分，并追问扣分扣在哪里。
   如果因为题量必须压缩，也只能合并表达，不能整体删除这些观察点；若材料明确说明不需要生活方式理解，才可在 Agent 检核摘要中说明删减理由。

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
- 重复打卡信息（事件名称、重复频次、单位）
- 必填图片/必填视频意图
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
- 重复打卡信息（事件名称/频次/单位）：
- 必填图片/必填视频要求：
- 可能过重或过硬的题面：
- 建议交给 dg-question-wording-editor 处理：
```

规则：

- 不要把详细语气规则写在 designer agent 内。
- 如果有固定模板、客户原话、平台题型或合规限制，必须在 handoff 中说明。
- 如果有题量、素材、排序、打分或任务负担风险，必须标记。
- 如果模块需要用户重复几日、几次或按事件持续记录，必须保留事件名称、重复频次和单位，供后续 `dg-question-type-setter` 标注为 `打卡题`。
- 如果图片或视频是必填，不要只写成泛泛的“素材要求”；必须明确标记为“必填图片”或“必填视频”。如果只是可选补充，明确写为可选，避免后续误标必填。

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
- 大量 1-10 打分题或认同度量表；平台打分题只使用 1-10，不生成 1-5 打分。
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
- 只有当研究目标需要量化 baseline、筛选、分层或 KPI 对比时，才使用明确量表；平台打分题只使用 1-10，不生成 1-5 打分。
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

### 23.2.1 Lifestyle research needs enough depth for specific cohorts

When the project is about a specific cohort, lifestyle, life-stage, generation, subculture, or unfamiliar target group, do not treat lifestyle as a light warm-up. Lifestyle becomes a core research object and must be detailed enough to understand the person beh

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

以下是研究员 Word 文档沉淀规则，不得截断，优先级高于普通压缩规则：

# Research Design AI Agent Rules

Source: `研究设计AI Agent.docx`.

These rules are distilled from researcher-authored guidance. They are high-priority design rules and must be injected into designer prompts without truncation. Do not rely on compressed `research_rules.md` to preserve these points.

## 1. Lifestyle / Understanding A Person

For projects about a specific cohort, lifestyle, generation/subculture change, non-essential category opportunity, or any brief that depends on understanding "who this person is" before category/product questions, the opening person-understanding module must be detailed enough. It is not a light warm-up.

### Must-Have Observation Points

Cover these before moving into category/product questions:

- Self-introduction, keywords, and representative images.
- Living space / room tour.
- Life center of gravity and life rhythm.
- Spending habits: major spending buckets, and which non-necessities the respondent is especially willing to pay for.
- Interests, hobbies, and related scenes.
- Social circles and the respondent's role in them, such as follower, initiator, organizer, active participant, listener, connector, or observer.
- Life pain points: use a light 1-10 score when useful, then ask where points are deducted.

If the questionnaire must be shorter, combine these observation points into fewer respondent-facing questions, but do not delete them altogether. If the project material clearly says person/lifestyle understanding is not needed, state the reduction reason in the Agent check summary.

### Additional Lifestyle Points For Deeper Studies

Add these when the project is more lifestyle-led or cohort-led:

- Cohabitants, including family, roommates, partners, and pets; for pets, ask their role in life, not only ownership.
- Leisure time arrangement and how free time is divided across rest, interests, socializing, learning, entertainment, and self-care.
- Information channels and how information differs by channel, such as Xiaohongshu, Douyin, Bilibili, friends, communities, offline stores, or professional sources.
- Preferred content and narrative taste, such as dominant-CEO romance, strong-female-lead stories, healing content, practical tutorials, niche aesthetics, or other content types that reveal values and fantasy.
- Life turning points, such as moving cities, changing jobs, relationship changes, health events, study/work transitions, or any transition the respondent sees as important.
- Ideal life image, or a person/creator/peer who seems to be living the respondent's ideal life.
- Future life expectations: what they think may change in 3 years or 5 years, and what they hope will stay the same.

### Reusable Question Patterns

Use or adapt these patterns when suitable:

- "首先，让我们多了解一下你吧！色彩、MBTI、星座、关键词……可以用任何你觉得能代表自己的方式来介绍自己！欢迎多多分享照片，向我们展示真实的你～"
- "和我们聊聊你的学业/工作吧！包括你所在的专业/行业、每天具体要做的事情（如果你有副业，也介绍一下吧！）"
- "可以拍一段小视频，带我们'云参观'一下你的居住空间吗？比如宿舍/家里的整体布局、你每天待得最久的地方，你最用心打理的一个角落。"
- "请描画一下你最近典型的一天吧！通常几点起床、几点休息？从早到晚，一天大概都在忙些什么？"
- "工作日和周末，你的节奏有什么不同？具体说说。"
- "和我们分享一下你的兴趣爱好吧！哪些是长期坚持的，哪些是近期才开始的？"
- "这些活动大概多久一次？通常会有哪些不同的玩法/形式？"
- "你有哪些社交圈子？和不同社交圈子的人在一起分别做些什么？不同社交圈子对你的意义和价值分别是什么？"
- "你在社交圈里通常是什么样的角色？是发起活动的人、非常活跃的参与者，还是别的角色？为什么？认识新朋友对你来说重不重要？为什么？"

## 2. Product Innovation Projects

For product innovation projects, do not jump directly to ideal products or concepts. First diagnose the change source and build the logic from concrete life/behavior to abstract opportunity.

### Change Sources To Check

Product innovation may come from:

- New lifestyle.
- New life scenes or finer scene segmentation.
- Completely new scenes, such as new hobbies or new social circles.
- More segmented old scenes, such as commuting becoming different for different occupations or lifestyles.
- New cognition.
- Changed evaluation standards, such as what counts as good to use, good to write, good to eat, healthy, festive, fun, premium, reliable, or worth sharing.
- Changed cognition of a category, concept, or cultural image.

### Concrete Before Abstract

Do not ask cognition without behavior. Cognition and behavior belong together. Use a "specific first, abstract later" sequence:

```text
concrete behavior / scene / experience
-> change and reason
-> category/product role
-> cognition or metaphor
-> future expectation or opportunity
```

Usually ask behavior before cognition.

## 3. How To Ask New Life Scenes

Ask change in the lifestyle / "about me" / typical day section when relevant:

- Which interests are played more or less now?
- Which social circles are more or less active now?
- Which scenes are fully new?
- Which old scenes have new forms?
- How have leisure life and social life changed over the past 2-3 years, and what impact did those changes have?

For fast-moving consumer goods, fragmented low-price categories, or categories that happen repeatedly in daily life, use continuous diary/check-in tasks to capture scenes. Examples include coffee drinking scenes, gum-chewing scenes, writing scenes, snack scenes, and other repeated low-involvement behaviors.

## 4. Deep Dive Scene Chain

For scene-led projects or diary records, use this chain:

```text
when the respondent felt the state/need
-> concrete scene: when, where, with whom, doing what, emotional/body state
-> chosen coping strategy: what they did, why they chose it
-> whether the research category/product was chosen
-> if chosen, why; if not chosen, why not
-> what elements worked if the product/category was chosen
-> whether the respondent reached the desired state, and why
```

For food and beverage categories, "what worked" should be decomposed into concrete experience elements such as taste, texture, aroma, temperature, freshness, fullness, stimulation, convenience, atmosphere, and ritual.

Do not force the target category into every scene. Let respondents describe the actual coping strategy first, then ask whether the research category entered and why.

## 5. Asking Theme-Specific Scene Change

When the study is about a specific cultural, seasonal, or lifestyle theme, ask concrete scene change directly:

- What new activities or scenes have appeared?
- Whether old activities now have new forms.
- How this year/period compares with last year/previous periods.
- Who decides the arrangement and why.
- Who brought the change.
- How the change affects the feeling of the theme.

Example pattern:

- "请把 2026 年春节当成一段生活纪录片，给我们讲讲你是怎么过这个年的：在哪里、和谁一起、分为哪几个阶段、每天大致在做什么？"
- "这些安排是怎么决定的？为什么这么安排？谁在主导？和去年相比，有没有什么不同？为什么？"
- "这几年你家有没有一些新的过年方式出现？比如全家旅行、新式年夜饭、新娱乐方式、开发新爱好等。这些变化是谁带来的？这些变化让'过年'的感觉有什么不一样？"

## 6. Cognition Questions

### Abstract Or Cultural Concepts

When the object is not a concrete product, but a cultural image, social concept, theme, or created concept, ask:

- What do you think counts as X?
- What is X to you?
- What is the first image that comes to mind when X is mentioned? Why?
- What sounds, tastes, smells, objects, or emotions do you associate with X?
- Has X changed? Why?
- Has your expectation of X changed? Why?

Use this pattern for topics such as CNY / Spring Festival, 二次元, "慢人", health concepts, wellness concepts, or other non-object ideas.

### Concrete Products Or Objects

When the object is concrete, use metaphor and relationship questions:

- What is it like?
- What objects would you mentally or physically place it together with?
- What role does it play in life?
- If it were a person, how old would it be, what personality, occupation, and clothing style would it have?
- What is its relationship with "me": close, distant, dependent, companion-like, decorative, occasional, or something else?

Always ask why after metaphor questions.

## 7. Experience Standards

To understand what respondents mean by good/bad, ask extreme experiences before abstract criteria:

- Best experience.
- Happiest experience.
- Most satisfying / most comfortable / most useful moment.
- Worst experience.
- What makes them unhappy.
- What missing element makes the experience unacceptable.

Tie the probes to category-specific sensory or use details:

- For writing instruments: smoothness, grip, sound on paper, control, appearance, emotional feeling, and the moment of writing.
- For coffee or food/drink: taste, aroma, texture, temperature, mouthfeel, refreshment, fullness, scene, and feeling.

Encourage respondents to make the experience concrete through five senses and real scenes instead of abstract adjectives.
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
- 用户补充说明: 请基于 case_005 的输入材料生成题目设计；不要参考 Final Digital Diary DG / 最终标答。

# 项目文件文本

## File: 【Proposal】协助KACO 打造国民级笔类大单品 -MindSight - 260701.pdf
- file_type: proposal

[Page 1] 协助KACO 打造国民级笔类大单品 MindSight 心智观策 2026.06

[Page 2] 目录 Content 01 02 03 04 项目背景 MindSight思考 研究路径 服务团队 及目标 与预期产出 与独特方法 与预计排期 Project Backgrounds MindSight Perspectives & Research Approach & & Objectives Expected Outputs Signature Methods Team, Estimated Timeline, and Cost

[Page 3] 目录 Content 01 02 03 04 项目背景 MindSight思考 研究路径 服务团队 及目标 与预期产出 与独特方法 与预计排期 Project Backgrounds MindSight Perspectives & Research Approach & & Objectives Expected Outputs Signature Methods Team, Estimated Timeline, and Cost

[Page 4] 项目背景 1. 品牌近年通过礼盒升级与 IP 联名实现了一定突破，并沉淀出若干经典产品线。但随着书写 工具赛道整体竞争加剧，现有增长路径的天花板逐渐显现。 2. 企业关注文具爆品品类的变化，如过去几年的秀丽笔和近期的爆闪马克笔，希望找到下一 个非刚需但市场规模不小的爆品品类。

[Page 5] 项目目标 商业目标 在笔类市场进入存量竞争、基础书写需求持续被电子化与 AI 分流的背景下， 协助 KACO 研判未来三年，具备国民级大单品潜力的新品类/新产品方向，支撑品牌长期增长。 研究目标 1. 理解目标人群的生活方式、兴趣场景、书写需求与文具消费逻辑 2. 理解书写场景、书写行为及书写价值的变化，识别未来的机会空间 3. 理解用户对笔的品类认知、选择逻辑与价值期待，重新定义未来笔类产品的机会方向 4. 识别具备国民级大单品潜力的机会方向，并转化为产品创新概念原型

[Page 6] 目录 Content 01 02 03 04 项目背景 MindSight思考 研究路径 服务团队 及目标 与预期产出 与独特方法 与预计排期 Project Backgrounds MindSight Perspectives & Research Approach & & Objectives Expected Outputs Signature Methods Team, Estimated Timeline, and Cost

[Page 7] 05/10后学生、年轻白领等核心人群都在发生代际变化 2025年上半年， 2024 年，全国普通高中在校生约 2922 万人 8个文具品牌与60个IP 普通/职业本专科在校生约 3891 万人 共发生70起联名合作 2025 届高校毕业生预计达到 1222 万人 平均每月约5起 行业增长放缓、赛道竞争加剧，我们面对「人 × 书写 × 笔」三重挑战 挑战1 挑战2 挑战3 代际变化、人群分化，需要重新理解目标用户 书写被分流，基础书写持续被电子化与AI替代 笔类新品爆炸，产品易陷入短期消耗逻辑 “学生”“白领”不再是一种人：不同教育路径、 记录、整理等基础信息处理任务，正在被数字工具与 供给端：新品爆炸，产能过剩，利润空间被进一步挤压 兴趣圈层、行业状态带来更细分的需求 AI承接，书写场景被进一步压缩和筛选 2026年中国青年报社社会调查中心对1334名受访者的调查 中国笔类产能已达约 1000亿支规模，相 当于全世界人均可使用 15支笔 2025年晨光年研发投入 约2亿元，新品从产线 到全国零售终端仅需7天 公立高中、职高、国际高中学生的生活方式/场景截然不同 消费端：买得多、换得快、闲置率高 05/10后学生成长于AI、短视频、兴趣圈层和内容种 94.5%受访者有过提笔忘字的情况 草环境中，学习、消费和表达方式已不同于80/90后 相较2017年同类调研（72.5%），占比明显提升 在低客单、高上新的 消费环境下，笔成为 97.2% 46.5% 99.8% 2025年晨光财报显示，传统核心业务营收同比下降5%， “低决策成本的尝鲜 书写工具（笔）的销量减少3.61%， 品”，社媒上涌现大 量相关讨论 未成年人互联网普及率 未成年人利用互联网复习 基础教育智慧黑板布设率 学生文具的销量大幅下降近10% 数据来源：教育局数据；角研社；腾讯新闻；国信证券；中国报告大厅；共青团中央维护青少年权益部、中国互联网络信息中心；中国青年报社社会调查中心；2025年晨光财报 得力"黄油小熊"单个IP联名的SKU数量达100+款

[Page 8] 思考1：重新理解「人」，洞察新生代目标用户，识别可放大的共性需求 国民级机会不是简单覆盖“学生/白领”等大标签，而是既要洞察人群内部不断细分的新需求，也要识别能够跨人群迁移、持续放大的共性需求 以05/10后新一代学生为样本， 在女性优势市场基础上， 以圈层先锋人群作为趋势信号， 理解代际变化下的新需求 进一步挖掘男性用户的增量机会 识别未来大众需求 过去学生对笔的需求集中在顺滑、耐写、便宜， 在持续深耕女性优势市场的同时，进一步探索男性用 手帐、写字等圈层未必代表大众市场，但往往更早显现 今天学生需求极度个性化细分，颜值、IP联名 户等尚未被充分开发的人群机会，寻找新的增长空间 新的审美偏好与价值期待，可作为未来趋势的前置信号 10后学生用笔来代表自己 蓝色系、美拉德色系 周边笔袋、笔挂、可改造挂件等 抽象写生/速写成为更多人的低成本爱好 微缩模型勾线笔 从“一支主力笔用到底”到“多支笔服务不同的场景与心情” 质感/手感细分、机械结构与把玩乐趣、黑科技与功能性 “学术好运开挂桌” 手作水晶笔

[Note] PDF has 28 pages; only first 8 pages extracted for prompt smoke test.

## 参考案例逻辑

## case_003

# Case Card - Case_003 Wonton Continuous Listening

## 1. Basic Info

- Case ID: Case_003
- Project name: 思念-用户持续聆听 / 馄饨品类相关研究
- Category / brand: 冷冻食品；馄饨 / 云吞 / 抄手等
- Project type: 持续聆听；R2 后续追踪；基础题目复用；核心问卷聚焦
- Target audience: 固定样本组中的冷冻食品消费者，进一步筛选馄饨高频使用者
- Main method: Digital Diary / 数字日记本，基础题目 + 品类核心题目

## 2. Business Problem

冷冻馄饨品类在电商平台增长明显，客户希望理解消费者为何选择馄饨、偏好基于哪些维度、不同渠道和营销活动如何影响决策，并为后续产品和传播提供方向。

## 3. Research Objectives

- 从固定样本组中识别馄饨高频使用者。
- 理解消费者为什么选择馄饨，而不是其他冷冻食品或餐食解决方案。
- 理解馄饨的皮、馅、汤底、烹饪方式、品牌、渠道等偏好。
- 追踪从上次填写到现在的生活、兴趣、工作、情绪和冷冻食品消费变化。
- 理解冷冻馄饨购买平台变化、新品尝试、信息获取和烹饪诀窍。

## 4. Input Material Signals

- 这是持续聆听项目，不是完全从零开始。
- 已有固定样本，因此基础画像可更关注“相较上次的变化”。
- 项目会分为泛问卷和核心问卷，核心问卷聚焦具体品类问题。
- 样本设计上需要从 50 人中筛出约 25 个馄饨高频使用者。

## 5. Final Module Structure

1. 基础模块一：我和我的生活
   - 聚焦家、工作、兴趣爱好、情绪状态相较上次是否变化。
2. 基础模块二：吃吃喝喝实时记录
   - 记录工作日和休息日的一日三餐、三餐外饮食、情绪变化。
3. 冷冻食品消费与筛选
   - 最近购买过哪些冷冻食品、购买渠道、是否涉及馄饨。
4. 馄饨核心题目
   - 食用原因、偏好维度、馅料/种类、品牌、购买平台、烹饪方式、新品尝试、信息来源、未来期待。

## 6. Key Question Logic

- 持续聆听项目不重复完整画像，而是问“相较上次填写，有没有变化”。
- 基础题目用于维护样本生活背景和饮食图谱。
- 核心题目聚焦馄饨品类：为什么吃、怎么吃、买什么、在哪里买、怎么评价、如何变化。
- 用选择题识别冷冻食品购买范围和渠道，再进入开放追问。
- 最后通过新品想象和产品期待收集创新方向。

## 7. Reusable Rules

- 持续追踪项目应优先问变化，而不是重新完整画像。
- 如果已有固定样本，基础模块可以压缩，但是否压缩仍要回到 Proposal 的研究问题判断。
- 如果需要从泛样本筛核心样本，应先设计筛选题，再对符合条件的人进入核心模块。
- 品类核心题应覆盖：选择原因、偏好维度、替代品类、产品体验、品牌/渠道、变化、新品尝试、未来期待。
- 对具体食品品类，可重点追问口味、口感、形态、烹饪方式、包装、价格、购买平台。

## 8. Do Not Overgeneralize

- 不要把“基础模块压缩”套到所有项目；只有持续追踪或已有画像时才适合。
- 不要把馄饨品类的皮/馅/汤底结构直接套到其他食品。
- 不要忽视筛选逻辑；持续聆听中核心题常常只适合部分样本。

## 9. Best Reference For

- 持续聆听项目。
- R2/R3/R4 后续追踪。
- 从泛样本筛选核心样本。
- 冷冻食品/具体食品品类专项题。
- “相较上次”变化型题目设计。

请只学习以上案例的设计逻辑，不要复制案例题目。
```
