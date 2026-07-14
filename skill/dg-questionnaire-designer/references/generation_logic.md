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
