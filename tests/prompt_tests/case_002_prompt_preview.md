# Prompt Preview - case_002

- Selected cases: case_002, case_001
- Input files: 5
  - 【Brief】玛氏巧克力.docx (brief, 878 chars)
  - 【Proposal】玛氏巧克力品类发展机会研究.pptx (proposal, 5719 chars)
  - 【客户内部资料】2023 Demand Space China Chocolate.pdf (client_material, 5988 chars)
  - 【客户内部资料】Category Growth Brainstorming_0422.pdf (client_material, 2568 chars)
  - 【客户内部资料】KWP - FMCG Quarterly Penetration Report 25Q1_250425.pdf (client_material, 6349 chars)

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
11. 详细题目设计必须是完整题目稿，不是建议或示例。每个板块固定使用“板块x：xxx / 引导语 / 题目 / 结束语”格式。
12. 不要输出“建议题目示例”“示例题”“建议题量”等字样；不要在每道题后堆研究目的、设计说明、内部解释。

以下是生成流程协议：

# Generation Logic - 题目设计 Agent 生成逻辑协议 v0.1

## 1. 目标

本文件定义题目设计 Agent 的核心生成逻辑。

Agent 的角色不是替代研究员，而是作为研究员的题目设计助理：

- 帮助研究员从输入材料中梳理商业问题和研究问题。
- 基于研究员逻辑设计 Digital Diary / 问卷模块。
- 生成可供研究员审阅、修改和继续追问的题目设计方案。
- 在材料不足时，先尝试从输入材料中寻找答案；确实无法判断时，再提出少量需要用户/研究员确认的问题。

Agent 不应直接跳到题目生成。每次生成必须遵循：

```text
输入解析
-> 项目类型判断
-> 商业问题与研究问题拆解
-> 模块结构设计
-> 模块内观察点设计
-> 题目生成
-> Agent 内部自检
-> 少量必要确认点
```

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

## 5. Agent 检核摘要

## 6. 需要确认的问题
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

## Step 6：生成题目

目标：生成可直接给研究员审阅、并可进一步放入 Digital Diary 的完整题目设计。

重要：详细题目设计不是“建议题目示例”，而是完整板块题目稿。

输出格式：

```markdown
## 4. 详细题目设计

### 板块1：模块名

引导语：

题目：

1.
2.
3.

结束语：
```

题目规则：

- 默认开放题为主。
- 客户已有明确分类或需要筛选/分流时，才使用选择题。
- 排序题多用于后段刺激物、产品概念或优先级判断。
- 题目必须具体、中性、自然、贴合人群。
- 不要过早暴露客户品牌。
- 不要一上来问“为什么不用目标品类”。
- 应先问真实情境、当前做法、替代方案，再自然追问目标品类。
- 必要时要求照片、视频、语音、截图或实物记录。
- 不要输出“建议题目示例”“示例题”“建议题量”等字样。
- 不要在每道题后面堆研究目的、设计说明、内部解释；这些可以作为 Agent 内部思考，但最终题目稿要以受访者可读的题目为主。
- 题目要自然、开放、有陪伴感；不要用过多例子限制受访者回答。
- 示例只在帮助理解时使用，并用“比如/如”等轻提示，不要写成封闭选项。

模块内容规则：

- 基础画像模块先理解“人”，不要急于进入品类、产品或品牌。
- 典型一天模块要开放描画 routine、场景和状态变化，不要写成机械时间表。
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

日记模块表达规则：

- 日记题要完整，但不要写成过重的事件调查表。
- 内部可以区分品牌或研究分支，但给受访者看的题面应尽量自然，不要暴露 internal label。
- 如果目标人群填写负担较高，应鼓励语音、图片、视频，降低文字压力。

---

## Step 7：Agent 内部自检

目标：Agent 在输出前自行检查生成结果是否符合研究逻辑。

注意：自检主要是 Agent 内部执行，不是让最终用户看到一大段“研究员自检”。最终输出只保留简短检核摘要，说明关键风险或已通过的检查。

输出格式：

```markdown
## 5. Agent 检核摘要
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

## Step 8：输出必要确认点

目标：把 AI 无法从材料中判断、且会显著影响题目设计的问题交还给用户/研究员。

注意：确认问题不是在生成方案末尾堆很多问题。Agent 应先尝试从 Brief、Proposal、内部资料和用户补充说明中寻找答案。只有找不到、且会影响方案时，才提出确认。

输出格式：

```markdown
## 6. 需要确认的问题
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
- 可复用规则
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

第一版不做复杂 multi-agent。

推荐一次生成流程：

```text
system prompt:
  角色 + 研究员规则 + 输出要求

user prompt:
  当前项目材料 + 用户补充说明 + 相关 case card

model output:
  Markdown 题目设计方案
```

继续对话流程：

```text
system prompt:
  角色 + 修改规则

user prompt:
  当前题目设计方案 + 历史对话 + 用户新指令

model output:
  修改后的方案或局部修改
```

以下是研究规则库：

# Research Rules - 题目设计 Agent 规则库 v0.1

> 来源：Case_001-004、研究员访谈原稿与现有 Digital Diary DG。
>
> 用途：作为后续 `prompt.py` / demo 后端生成逻辑的规则来源。

## 1. 总体工作流

题目设计 Agent 不能直接从题目开始生成，必须按以下顺序推导：

```text
客户商业问题
-> 研究问题拆解
-> 模块结构设计
-> 每个模块观察点
-> 具体题目与追问
-> Agent 内部自检
-> 少量必要确认点
```

模块结构比单题措辞更重要。先把模块画对，再写题。

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
- 语气必须匹配人群：年轻人可轻松，年长者更礼貌清楚，圈层人群用准确黑话。

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

## 15. 题量与负担

- 一般 Digital Diary 总题量可参考 70 题左右。
- 高端/敏感客群可控制在 50 题左右，少而精。
- 每日记录 10-12 题左右已经是较高负担。
- 记录天数由项目需求决定，至少考虑工作日与休息日差异。
- Agent 应提出建议和理由，最终由研究员确认。

## 16. Agent 题目质量自检

每道题都应能说明：

- 对应哪个研究问题？
- 服务哪个商业问题？
- 预计产出什么可用于报告的信息？

如果不能说明，应删除或合并。

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

详细题目设计必须像最终 Digital Diary 题目稿，而不是研究方案建议。

每个板块使用固定格式：

```text
板块x：xxx
引导语：
题目：
1.
2.
...
结束语：
```

避免：

- “建议题目示例”
- “示例题”
- “建议题量”
- 每题后面大段研究目的、设计说明、内部解释

题目必须是完整题目，不是题目方向。

内部研究目的和设计说明可以用于 Agent 思考，但最终输出应以受访者可读的题目为主。

## 19. 受访者题目语言规则

- 题目要自然、开放、有陪伴感。
- 不要把问题写得过度像表格或调查任务。
- 不要给太多例子限制受访者回答。
- 示例只在帮助理解时使用，并用“比如/如”等轻提示。
- 引导语要帮助受访者进入状态，结束语要自然承接下一模块。
- 前期模块不要过早暴露品牌或产品意图。

## 20. 口香糖 / 嘴巴相关品类增长规则

当项目类似 Case_001，即口香糖、嘴巴相关食品/饮品、口气清新、状态调整、品类增长机会时：

- 模块 1“关于我”先描摹受访者本人，不要急于连接口香糖、口腔产品或提神产品。
- “关于我”应覆盖自我介绍、学业/工作、居住空间、兴趣爱好、社交生活、理想生活、焦虑/压力、生活评分。
- “典型一天”应开放描画 routine、吃饭类型、餐前餐后行为、不同时间段状态、工作日和周末差异。
- “正餐以外的吃吃喝喝”应定义为正餐以外、不以单纯吃饱为目的的食品与饮品。
- 图谱模块先问日常囤的、随手买的、被分享/推荐的，再进入餐后、学习/工作、在路上、临上场、高消耗/高重复等场景。
- 日记模块内部可区分功能场景和情绪场景，但受访者题面不应暴露 internal brand label。
- 购物任务要还原自然购买 journey，不要过度变成货架审计。
- 购物任务应包含购买前、购买中、购买后、卡点回顾，以及实际 eating experience。
- 习惯养成模块应从正餐外吃喝图谱中选择具体产品，追问初尝、习惯养成、中断、变化和角色，不要只问口香糖。
- 品牌与产品期待放最后，再进入品牌印象、品牌人格化、理想产品和 stimulus。
```

---

## Message 2: user

```text
请基于以下项目输入，生成第一版题目设计方案。

要求：

- 严格遵循“项目理解 -> 核心研究问题 -> 模块结构总览 -> 详细题目设计 -> Agent 检核摘要 -> 需要确认的问题”的顺序。
- “项目理解”只列 5-7 条以内的关键结论，不展开长篇背景。
- “核心研究问题”只列 3-6 个问题，不写长表格。
- “模块结构总览”只列模块、模块目的、对应研究问题，不展开详细理由。
- 每个模块必须说明模块目的、对应研究问题、保留/合并/定制理由。
- 详细题目设计必须输出完整题目，而不是题目方向或建议示例。
- 详细题目设计每个板块必须使用：
  板块x：xxx
  引导语：
  题目：
  1.
  2.
  ...
  结束语：
- 不要在每道题后输出研究目的、设计说明、内部解释；如确有必要，只在板块末尾用一句“内部提示”说明。
- 如果文件中客户已有明确要求，必须体现。
- 如果客户已有研究沉淀，不要重复泛问，要在已知基础上继续探索。
- 如果不确定是否需要某个模块或任务，先从材料中找依据；仍无法判断时，只列入“需要确认的问题”，最多 3 个。
- “Agent 检核摘要”最多 5 条，只输出关键风险和控制，不要展示完整自检过程。
- 题目语言要自然、开放、有陪伴感；不要用过多具体例子和选项限制受访者回答。
- 基础画像模块先理解受访者本人，不要急于和产品/品牌发生关联。
- 输出只使用 Markdown，不要输出 JSON。

# 用户补充信息

- 品类/品牌: 巧克力 / 零食
- 品牌: 德芙 / Mars
- 目标人群: 巧克力目标消费者
- 是否有 IDI / 入户 / 后续访谈: 未提供
- 输出偏好: Markdown
- 用户补充说明: 无

# 项目文件文本

## File: 【Brief】玛氏巧克力.docx
- file_type: brief

Market Research Brief – 玛氏巧克力品类发展机会研究
Client：Mars Global Brand Insights Team
Agency：Synocode
Business & Brand Background
巧克力在中国市场的年度渗透率上线城市为70%左右，低线城市为50%+/-
相较于年度渗透率，在中国巧克力品类的主要挑战有两方面
巧克力品类的购买频率较低，主要集中在CNY及节庆
巧克力品类的人均消费量较低，为全球成熟市场的5%
中国巧克力市场主要由玛氏占据，玛氏在中国巧克力市场的份额超过50%
Business Objective
提升巧克力品类消费频次，通过brand communication，让德芙关联到更多日常生活场景，提高目标消费者在日常生活中对巧克力的兴趣，让巧克力和德芙成为其他更高频的零食或饮料（如咖啡、酸奶等）那样、与生活方式高度相关的品类和品牌
Research Objective
理解巧克力目标消费者的生活状态及生活方式
理解TA与snacking相关的需求、生活场景、待办任务
理解TA目前的解决方案、当前解决方案中的已满足和未满足需求
建议体量大且德芙potentially可以own的高价值场景
建议德芙可以切入的 brand communication angle(s)
Next Step
NDA签署
Download玛氏目前已知的与巧克力和snacking场景相关的消费者洞察，download德芙的品牌定位信息和主要传播素材，为项目设计导入所需的品类、品牌、消费者信息
Check美团营销地图账号，尽量开通
Align project design, quotation, co-PR plan
KO project ASAP – before May end, and try best to get initial feedback before Jun-end to enable Client internal sharing to leadership team

---

## File: 【Proposal】玛氏巧克力品类发展机会研究.pptx
- file_type: proposal

[Slide 1] 玛氏巧克力品类发展机会研究 | 研究计划书 | 上海华因极数科技发展有限公司 | 2025-0 | 6

[Slide 2] 目录 | 项目 | 背景 | 及商业目标 | 01 | 项目目标 | 02 | 03 | 时间 | 、团队及预算 | 0 | 5 | 研究路径与核心产出 | 具体研究方法 | 04

[Slide 3] Background and Business Objective | 项目背景及商业目标 | Business background | 商业背景： | 1. | 巧克力在中国市场的年度渗透率上线城市为 | 70% | 左右，低线城市为 | 50%+/- | 2. | 相较于年度渗透率，在中国巧克力品类的主要挑战有两方面 | - | 巧克力品类的购买频率较低，主要集中在 | CNY | 及节庆 | - | 巧克力品类的人均消费量较低，为全球成熟市场的 | 5% | 3. | 中国巧克力市场主要由玛氏占据，玛氏在中国巧克力市场的份额超过 | 50% | Business objective | 商业目标： | 提升巧克力品类消费频次，通过 | brand communication， | 让德芙关联到更多日常生活场景，提高目标消费者在日常生活中对巧克力的兴趣，让巧克力和德芙成为其他更高频的零食或饮料（如咖啡、酸奶等）这样的与生活方式高度相关的品类和品牌

[Slide 4] 理解巧克力 | 目标消费者的生活状态及生活方式 | 理解 | TA | 与 | snacking | 相关的 | 需求、生活场景、待办任务 | 理解 | TA | 目前的解决方案、当前解决方案中的 | 已满足和未满足需求 | Project | Objective | 项目目标 | 建议德芙可以切入、且有品牌独占潜力的沟通角度 | IMPLICATION | 02 | 建议体量大、德芙 | 有机会 | 进入并占领的高价值场景 | IMPLICATION | 01

[Slide 5] Our Approach and Key Outputs | 我们的方法论与核心产出 | How do we understand people, their health needs and growth opportunity | 如何理解目标人群的健康需求与增长机遇 | 研究路径和核心产出

[Slide 6] 思考：一瓶“药水”，如何被可口可乐重新定义成为 | No.1 | “快乐水” | 可口可乐 从药用饮料转为“快乐水” | 可口可乐结合彼时时代的社会矛盾和情绪张力，借助圣诞节这一重大仪式重塑快乐内涵 | 19 | 世纪末 | 20 | 世纪初，美国贫富分化加剧 | 工业化 | / | 城市化进程，社会价值观冲突凸显 | 社会不平等和社会问题丛生 | 健康诉求发生变化 | … | 可口可乐不再是药用饮料，而是 | 传递善意与快乐的“快乐水” | 重塑圣诞老人形象 | 可口可乐的标志红 | 圣诞老人代表仁慈、善良、快乐等意象 | 红色圣诞老人成为世界性圣诞节符号 | 仪式场景 | 将可口可乐与代表善意与快乐的 圣诞老人相结合，锐化品牌联想，使可口可乐成为圣诞节的一种全球性文化符号，让消费者 | 在快乐时刻或者需要快乐的情绪触点 | ， | 即刻唤醒对可口可乐的品牌记忆，形成消费惯性 | 社会情绪 | 可口可乐从“提神醒脑，喝可口可乐”转为 | “快乐、轻松喝可口可乐” | 品类重新定义 | 压力感 | 紧张感 | 对立感 | 疲劳感 | … | 1931 | 年，可口可乐红 | - | （红色）圣诞老人诞生 | “理想的补脑药” | 1931 | 年之前，（绿色）圣诞老人 | “快乐时刻”

[Slide 7] 思考：一块“饼干”，如何被奥利奥重新定义成为“玩伴” | / | “快乐搭子” | 社会结构变化 | 二战时期女性地位提升和二战后的“婴儿潮”兴起，女性和儿童的消费力释放 | 宏观经济趋势 | 20 | 世纪三十年代初，美国经济大萧条，后在开始逐步复苏，在 | 60 | 年代走向 | “ | 大通胀 | ” | 定位“ | 大众化 | ”亲民路线，用朗朗上口的命名为消费者提供简单易得的美味和快乐，打败更早做白加黑饼干的 | Hydrox | 顺应大势 | Hydrox | ：用元素氢和氧的英文 | hydrogen | 和 | oxygen | 命名 | OREO | ：两个「 | O | 」形饼干夹着奶油「 | cream | 」，即 | O-re-O | ，同时三音节读起来顺口 | 回应新消费人群诉求 | 聚焦 | 女性 | ：发现有很多女性喜欢把奥利奥分开来吃， | 创造了“扭一扭，舔一舔” | 饼干仪式 | 聚焦 | 儿童 | ：增加 | “ | 泡一泡 | ”, | 将牛奶和奥利奥食用场景联系，增加 | 营养附加 | 价值的 | 同时完形了奥利奥的 | 趣味性 | 饼干应该放在盘子里，作为高雅精致的下午茶来吃 | 品类传统认知 | 打破传统 | 竞品的宣传海报：强调自己的 | 原创 | 和正统，配合优雅精致的下午茶插画 | 奥利奥的宣传海报：强调 | “ | 扭一扭、舔一舔、泡一泡 | ” | 的动作，饼干从精致场景中 | “ | 解脱 | ” | 出来，成为 | 休闲乐趣 | 的选择

[Slide 8] 巧克力在中国消费者心中有明确消费特性及场景，品类进一步发展如何打破固有认知边界 | 巧克力已有 | 稳定品类心智 | 与休闲零食大类中的 | 糖果 | 品类强绑定 | 益普索 | x | 小红书 | | | 食品饮料行业洞察报告（ | 2024 | ） | 2023 | 京东糖巧趋势洞察白皮书 | 灵感「补给站」 | —— | 零食行业用户洞察报告（ | 2023 | ） | 礼赠 | 为巧克力 | 消费主要场景 | * | 京东超市 | 2023 | 年《巧克力消费趋势洞察报告》 | 新年 | + | 巧克力 | 520+ | 巧克力 | 年货节 | 是巧克力消费最为集中的节庆，消费额排各大节日之首。其次是圣诞、元旦，以及情人节、 | 520 | 。 | 从商品单价来看， | 年货节、情人节巧克力价格最高 | ，消费品质更胜一筹。 | * | 来源： | 2023 | 京东糖巧趋势洞察白皮书 | 其他场景 | …… | 哄娃神器 | 办公室零食 | 低血糖急救 | 运动充能 | Why? | 价格不高不低刚好合适 | 包装精致有仪式感 | 含糖量高，有幸福感 | 分量合适适合分享 | ……

[Slide 9] 因此我们需要 | ： | 为巧克力找到新的需求场景 | Redefine | Chocolate | 重新定义「 | 巧克力 | 」 | D | emand | Creation | 创造 | 「巧克力」 | 需求 | 解锁并打破巧克力的 | 固有消费属性 | （解决什么需求、出现在哪些场景） | 识别背后的成因逻辑 | 找到 | 巧克力在品类之外的潜力 | Unlock | Chocolate | Usage | 巧克力不是“巧克力”？ | 巧克力不是“零食”？ | 巧克力不是只能吃的东西？ | … | “吃 | 德芙 | 就好了” | 锚定占位 | “巧克力”如何满足？ | 切中心脉 | 识别并占据生活中那些 | 未命名 | 的 | （未 | 被任何解决方案触达 | ） | 消费者自己也尚未察觉但 | 真实存在的需求 | & | 可能产生需求的场景 | Uncover | Social | Tension | 时代在呼唤什么 | ？如何回应？ | 个人在诉求什么？如何唤起？ | 当下最大的情绪公约数是什么？ | …

[Slide 10] 首先， | 人类学与社会学 | 深度研究 | 方法 | 能够结构性理解社会痛点 | ， | 前瞻时代尚未显现的潜藏趋势 | 在当下及未来较长时间内，中国社会普遍的 | 价值观念、社会心态及理想生活范式 | 如何？ | 如何穿越中国社会沉浮变化的表象，把握 | 当下及未来的情绪风向标 | ？如何定位 | 最核心的情感张力和诉求 | ？ | 需要结合宏观社会文化背景、中观社会环境变迁及微观个体生活， | 回归真实消费者和他们的日常中。 | 世界格局重塑 | 全球资本、信息，商品、文化等都在经历格局重塑，国家主动创造战略机遇 | 传统文化复兴 | 高度流动性 | 家庭形式多元 | 价值观念极化 | 虚拟现实交融 | 内卷竞争加剧 | 公共参与生态民主 | 世界格局重构 | 全过程人民民主 | , | ， | 鼓励公共参与和表达，包容多元 | 价值观 | 消费市场深度变革 | 行业变局，奠定消费模式的基本框架，消费方式和理念日益变迁 | 产业发展重新定向 | 经济换挡增速放缓，产业规则重塑，发展重点转向绿色与可持续，关注人与自然和谐共处 | 智能科技急速发展 | 数字化时代，元宇宙技术兴起，加快职业发展、生活方式的 | 重塑 | 意义感缺失 | 社会性孤独 | 认同感危机

[Slide 11] 定量 | 定性 | 以 | 人类学 | 与 | 社会学 | 为方法论核心 | Anthropology and sociology as the methodological foundation | 以 | 数据科学 | 与 | AI | 人工智能 | 为技术核心 | Data science and AI as the technological core | 华因极数 | InsightY | 消费者洞察系统 | Synocodes Insight Why Consumer Insights System | （ | InsightY | ） | “ | 九州知数 | TM | ”- | 华因极数数字生活志数据库 | TM | Digital Enhanced Ethnography Panel | (D.E.E.P.) | 消除定性与定量研究先天不足 | 打造智慧融合的尖端优势 | Eliminate inherent limitations of qualitative and quantitative research | Forge cutting-edge advantages through intelligent integration | 华因极数 | SYNOCODES | 深度融合定性定量研究双优势 | Deep integration of the dual advantages of qualitative and quantitative research | 建立 | D.E.E.P.+ | InsightY | 数智化定性消费者研究系统 | Establish the D.E.E.P.+ | InsightY | digital-intelligent qualitative consumer research system | 从非结构化数据到智能，再到决策 | From DIKW to DIKWP | 其次，华因极数在深度研究方法之上 | 提供了独特 | 的 | 「 | 类定量 | 」 | 及 | 「 | 洞察资产化 | 」 | 价值

[Slide 12] 华因极数InsightY系统，深刻高效地洞察消费群体 | 数智化追踪 | Digital Intelligence Tracking | 数智化管理 | Digital Intelligence Management | 数智化收集 | Digital Intelligence Data Collection | 数智化分析 | Digital Intelligence Analysis | InsightY | 系统 | 自研对话流形式数记APP | 定性数据低成本快速收集 | Self-developed Dialog-Driven "Shuji" APP: Enables Cost-Effective Rapid Collection of Qualitative Data | 通过综合D.E.E.P.或打造定制D.E.E.P. | 提供长时追踪洞察 | Delivers long-term tracking insights through integrated D.E.E.P. or customized D.E.E.P. development | 集合深度学习技术 | 自研非结构数据分析工具，快速提取洞察 | Integrated deep learning technologies with self-developed unstructured data analysis tools for rapid insight extraction | 定性数据后台看板 | 沉淀为品牌真实数据资产 | Custom qualitative data dashboard development to accumulate authentic brand data assets | 华因极数InsightY消费者洞察系统 | InsightY Consumer Insights System | In | sightY帮助品牌： | 链接 | 任何人 | 在 | 任何时间 | 讨论 | 任何话题 | 与 | 任何地点 | Anyone | Anytime | Any topic | Anywhere

[Note] PPTX has 34 slides; only first 12 slides extracted for prompt smoke test.

---

## File: 【客户内部资料】2023 Demand Space China Chocolate.pdf
- file_type: client_material

[Page 1] China Portfolio Strategy Workshop August 6, 2023

[Page 2] PRELIMINARY – still to be aligned with stakeholders Snacking Category Vision | Working to build an overall Category Growth Approach and externalize our strategies Objectives • Develop a Snacking Category Vision that covers wider Snacking landscape incl. category definition and role we play in each segment • Simplified version of demand spaces, adding future trends and shopper considerations to build "Snacking Growth drivers" • Integrated with Portfolio Strategy work to ensure frameworks are aligned • Translated into concrete growth strategies, measurable, quantifiable and deployable with customers Copyright © 2019 Mars Wrigley Confectionery — Confidential 2

[Page 3] Scope of Learning | Over 50,000 respondents were interviewed representing 600K+ consumption events WHAT WHEN CAPTURED DEEP DIVES • ~20 min Online Modular • 20% of sample collected in Holiday Season Survey • 80% in non-holiday Total Snacks Chocolate Fruity Confections • China was collected as COVID Zero Tolerance eased • 50,174 respondents (~9,000 per market, 4,000 for KSA)* • 603,235 recorded Ice Cream/Frozen December January February consumption events Gum + Mints Snack Bars Novelties WHERE WHO Holiday Regular Consumption • Adults (18+) and Teens (14-17) responding for themselves • Parents of children aged 7-13 US UK China Regular Consumption Holiday • Must have consumed relevant categories in past day Regular Consumption Saudi Mexico Germany Arabia 3

[Page 4] Snacking Definition: Based on Category Behavior Analysis revealed that categories cluster based on predominantly meal or non-meal consumption. Non-meal categories were included fully along with “snacking” consumption for categories that have significant or notable meal usage. These traditional snacking categories were fully included For these categories only non-meal consumption regardless of their relationship to a meal occasions were included* FULLY INCLUDED CATEGORIES NON-MEAL INCLUDED Fresh sweet baked goods Cereal / granola Snack bars Bread, buns, croissants, rolls, biscuits Crackers Sandwiches / instant soup Packaged sweet baked goods Vegetables Fruit snacks Fast food / street food Jello / pudding Dips and savory spreads Nuts / seeds / dried beans / trail mix / snack mix Meat snacks Salty popcorn Frozen snacks Packaged cookies / biscuits / wafers Cheese Salty snacks Yogurt Sweet popcorn Healthy Drinks Ice cream and frozen treats Fruit & Applesauce Non-chocolate / fruity candy Indulgent Drinks (coffee/tea based) Mints Gum Note: All categories were localized by market Chocolate A consumption occasion is deemed a non-meal occasion if the respondent selected that they had the item “immediately after a regular meal (e.g., as a dessert)” or “Between regular meals” Copyright © 2023 Mars Snacking Confectionery — Confidential 4

[Page 5] The 5 Snacking Needstates were built from the local level to create a consistent framework globally Healthier Intent Fuel Relax Connect Enjoy More nutritious, Energizing, Reduce stress, Sharing with Fun to eat, great guilt-free, lower satisfies hunger, provide a mental others, rewarding, taste, provide sugar, and lower higher in protein, break, improve great for feelings of joy and in calories gives you a boost mood celebrating delight Note: While the naming is consistent for the 5 needstates across markets, the profile for each will be slightly different based on the uniqueness of each country. Copyright © 2023 Mars Snacking Confectionery — Confidential 5

[Page 6] The framework was defined based on the intersection of Needstates & Occasions NEEDSTATES Healthier Intent Fuel Relax Connect Enjoy Morning in Home and OOH S N Daytime at O Home I S A C C O Evening at Home Daytime and Evening OOH The Snacking Landscape serves as a unified, people-centric framework Morning = Before breakfast & at breakfast time Daytime = Between breakfast and lunch; At lunch time or immediately after; Between lunch and dinner Evening = At dinner time or immediately after; After dinner Copyright © 2023 Mars Snacking Confectionery — Confidential 6

[Page 7] Global Snacking Demand Landscape | 8 Market Demand Spaces Share of Snacking Occasions (%) NEEDSTATES Healthier Intent Fuel Relax Connection Enjoy Morning in Bright & Ready Home and 9% OOH S Daytime at Share the Joy N Home 11% O I S Healthier Intent Fuel Me Up Relax & Unwind A 20% 20% 16% C Cozy Evening C Evening at Delicious Fun O Together Home 7% 6% Daytime and Mood Boost OOH Evening OOH 11% Morning = Before breakfast & at breakfast time Global represents a combined view of the US, UK, Germany, China, Mexico and Daytime = Between breakfast and lunch; At lunch time or immediately after; Between lunch and dinner Saudi Arabia, weighted based on the size of Snacking in each market. Evening = At dinner time or immediately after; After dinner 7

[Page 8] China Snacking Demand Landscape | 15 Market Demand Spaces Share of Snacking Occasions (%) NEEDSTATES Healthier Intent Fuel Relax Connection Enjoy Morning in Bright & Ready (10%) – In Home Fuel Me Up (6%) Home and - Morning Anywhere OOH Bright & Ready (4%) – Out of Home Share the Joy (8%) - Media S Daytime at Relax & Unwind (12%) N O Home Healthier Fuel Me Up (10%) – Daytime Healthier I S Intent (15%) Intent (5%) - Daytime & Evening At Share the Joy (11%) A - Out of Home - Non-Media - In Home C Home C O Evening at Relax & Unwind (3%) Cozy Evening Delicious Fun (3%) Home - Evening Together (4%) Fuel Me Up (4%) Mood Boost OOH (6%) - Alone/Partner Daytime and - Daytime & Evening Evening OOH Out of Home Mood Boost OOH (7%) - Family/Friends/Coworkers Morning = Before breakfast & at breakfast time alone with others at home outside of (their) home with media Daytime = Between breakfast and lunch; At lunch time or immediately after; Between lunch and dinner Evening = At dinner time or immediately after; After dinner 8

[Note] PDF has 41 pages; only first 8 pages extracted for prompt smoke test.

---

## File: 【客户内部资料】Category Growth Brainstorming_0422.pdf
- file_type: client_material

[Page 1] Chocolate Category Growth

[Page 2] AGENDA: - Category Context and Business Insights (Jessie) 30min - China Pleasure Study and Category growth case studies (Sunny) 30min - Brainstorming 30min

[Page 3] Chocolate China Changing our Mindset Copyright © 2022 Mars Snacking —Confidential

[Page 4] Where we are & Mindset change: From brand to category growth What is the drivers and barriers of Chocolate? vs. other markets Objectives of the session How to grow the China Chocolate category? What other categories and market do? 4

[Page 5] Category View I Chocolate category has a history of meaningful growth Mars Leads Category Stellar Growth Category Turbulence COVID and Post Growth Category RSV(Bil USD) | Total market incl. offline & online & snack chain &Club, excl. offline bulk and wedding • Changing channel dynamics (SC, Club and Int. dCom) • Small players (Meiji, Lindt, Godiva and NuoFan) emerge 3.3 • MW turnaround • Chocolate War journey • Int. players entering China • MW enters China 2.0 • Local / compound chocolate dominate 0.7 CAGR: 19% CAGR: 5.0% 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 Retail sales Gr% -1% -7% 3% 2% -3% -3% 10% 6% 16% 7.3% Offline + Trad. Offline only Offline +Trad. dCom dCom + Uncovered Data source: Nielsen, ROMA, and Team intelligence

[Page 6] MW view I You increased business 3+x the business, and we want to talk how to accelerate faster! MW Chocolate NSV (M USD) Growth Journey Stellar Growth Struggle Back to glory 1200 1,032 942 1000 887 902 866 811 825 826 808 771 800 723 716 676 528 600 402 377 334 400 CAGR: +17% P10Ys CAGR: +1.8% 200 0 Y2008 Y2009 Y2010 Y2011 Y2012 Y2013 Y2014 Y2015 Y2016 Y2017 Y2018 Y2019 Y2020 Y2021 Y2022 Y2023 Y2024 NSV Gr% 12.9% 6.6% 31.3% 28.0% 19.9% 6.8% -4.7% -12.4% -0.9% 7.7% 7.1% -2.2% 9.8% 1.7% 4.5% 9.5% Data source: Finance 6

[Page 7] What got us here won’t get us there…. 3.8% -0.6% GDP growth Inflation 2024-28 February 2025 7

[Page 8] Brand focus Category focus ✓ Benchmarking versus other ✓ Benchmarking vs other Snacking categories Chocolate competitors ✓ Maximize Chocolate category consumption opportunities and ✓ Maximizing brand opportunities then identify the best brand to (e.g. Win with CXM in seasons) capture them 100% ✓ Call out category targets and ✓ Call out Brand targets (e.g. 3x related brand missions brand xyz) ✓ A category lead (think Alyona) ✓ Teams set up by brands / cells Copyright © 2022 Mars Snacking —Confidential 8

[Note] PDF has 41 pages; only first 8 pages extracted for prompt smoke test.

---

## File: 【客户内部资料】KWP - FMCG Quarterly Penetration Report 25Q1_250425.pdf
- file_type: client_material

[Page 1] FMCG & Cross Category T&S categories penetration grew in 25Q1; Nuts, Crispy and Biscuits showed strong IH penetration growth +/- vs. +/- vs. YA Penetration % - 25Q1 - IH – K-E YA Penetration % - MAT25Q1 - IH – K-E 0.9 T&S 0.2 T&S 96.7 99.6 0.4 Chocolate 1.6 Chocolate 41.1 66.2 0.2 FC 1.1 FC I 44.3 71.8 H 3.5 Nuts 2.6 Nuts 66.8 88.4 2.4 Crispy Snack 1.0 Crispy Snack 65.2 89.3 2.4 Biscuit 0.9 Biscuit 80.1 96.8 -0.2 Ice Cream -0.9 Ice Cream 9.0 52.4 +/- vs. +/- vs. YA Penetration % - 25Q1 - OOH – K-D YA Penetration % - MAT25Q1 - OOH – K-D O GUM GUM 1.0 3.4 17.5 34.3 O H -0.1 MINT 2.2 MINT 11.0 26.2 1.8 Chocolate 2.4 Chocolate 31.7 49.2 Source: Kantar World Panel | IH Panel | 25P3 | Key-E City; Out Of Home Panel | Key-D City | 25P3 7 T&S: Chocolate; Chewing Gum ; Mints; FC; Packaged Nut; Crispy Snack; Biscuit; Ice Cream; Jelly

[Page 2] Confectionery & MW Q1’25 Penetration: Confectionery continues to grow in all categories but mint; MW penetration grew in Choc and Gum Total Category: Mars Wrigley: All gained penetration but Mint OOH OOH is the main source of penetration growth Y245 Q1 Penetration Change vs. YA Y25 Q1 Penetration Change vs. YA 1.9 1.4 1 0.5 0.5 0.3 0.1 -0.1 -0.1 -0.2 Choc IH Choc OOH Gum OOH Mint OOH FC IH Choc IH Choc OOH Gum OOH Mint OOH FC IH Penetration 19.9 18.6 13.3 4.2 2.5 Penetration 42.9 31.7 17.5 11.0 44.3 Scope: OOH K-D city, IH K-E city Copyright © 2022 Mars Snacking —Confidential

[Page 3] Confectionery & MW MAT Penetration: Confectionery and MW maintained growth across all categories, however momentum slowed down in Q1 ’25 FMCG, IH, K-E, MAT25P3 | Chocolate & Gum & Mint, OOH, K-D, MAT25P3 Chocolate (IH & OOH) Gum (OOH) +2.0 +1.6 64.6 66.2 +5.1 +3.4 46.7 +4.4 +2.4 30.8 34.3 42.3 49.2 38.3 +0.4 +0.9 28.5 39.3 +3.8 +2.7 32.9 25.2 27.8 23.5 30.5 +3.6 +2.4 27.1 Chocolate_IH MW_IH Chocolate_OOH MW_OOH GUM_OOH MW_OOH 23Q1 23Q2 23Q3 23Q4 24Q1 24Q2 24Q3 24Q4 25Q1 23Q1 23Q2 23Q3 23Q4 24Q1 24Q2 24Q3 24Q4 25Q1 Mint (OOH) FC (IH) 70.3 70.8 +0.9 +1.1 +3.8 +2,2 24.0 20.7 71.8 26.2 9.5 +2.1 +1.0 8.1 8.4 8.3 +0.1 +0.2 10.5 Mint_OOH MW_OOH 8.5 FC_IH SKT 23Q1 23Q2 23Q3 23Q4 24Q1 24Q2 24Q3 24Q4 25Q1 23Q4 24Q1 24Q2 24Q3 24Q4 25Q1 Source: Kantar World Panel | IH Panel | 25P3 | Key -E City | FMCG; Out Of Home Panel | 25P3 | Key-D City | Chocolate & Gum & Mint 9

[Page 4] Confectionery & MW CHOCOLATE (manu): MW led growth; Ferrero and Meiji showed fast recruitment; Others declined driven by Nuofan and KDV Chocolate, IH, K-E, 25P3 | Chocolate, OOH, K-D, 25P3 IN HOME PENETRATION OUT OF HOME PENETRATION 25Q1 MAT25Q1 25Q1 MAT25Q1 Pen% Pen ± GR Pen% Pen ± GR Pen% Pen ± GR Pen% Pen ± GR 41.1 0.4 1% 66.2 1.6 2% 31.7 1.8 6% 49.2 2.4 5% 19.1* 0.7 4% 39.3* 0.9 2% 18.6 1.4 8% 32.9 2.4 8% 6.9 0.3 4% 14.4 0.5 3% 5.5 0.8 17% 10.9 1.7 18% 1.8 0.2 9% 4.9 0.6 15% 2.1 0.5 30% 4.6 1.1 32% 1.5 0 -3% 3.9 -0.1 -3% 1.2 -0.1 -11% 2.9 0.0 0% 1.1 -0.1 -8% 3.1 -0.0 0% 1.4 0.2 22% 3.2 0.5 20% Others 24.3 -0.5** -2% 45.4 1.5 3% 14.9 0.2 1% 28.1 1.2 5% *Mars Snacking K-D, 25Q1 penetration:19.9, +0.5pt; MAT25Q1 penetration: 40.5%, +0.6pt **: 25Q1： KDV (-0.4 pt), Nuofan （-0.5 pt) 10 Source: Kantar World Panel | IH Panel | 25P3 | Key-E City; Out Of Home Panel | 25P3 | Key-D City | Chocolate

[Page 5] Confectionery & MW CHOCOLATE (brands): Dove led penetration growth; FRR Rocher IH and Kinder OOH showed fast recruitment Chocolate, IH, K-E, 25P3 | Chocolate, OOH, K-D, 25P3 IN HOME PENETRATION OUT OF HOME PENETRATION 25Q1 MAT25Q1 25Q1 MAT25Q1 Pen% Pen ± GR Pen% Pen ± GR Pen% Pen ± GR Pen% Pen ± GR 41.1 0.4 1% 66.2 1.6 2% 31.7 1.8 6% 49.2 2.4 5% 12.8 0.8 7% 27.8 0.9 3% 13.1 1.4 12% 24.4 2.3 11% 4.2 0.1 2% 11.3 0.4 4% 4.5 0.3 7% 10.4 0.8 8% 4.1 0.3 8% 8.1 0.2 2% 2.8 0.3 12% 6.9 1.1 19% 3.1 0 0% 8.0 -0.2 -3% 2.6 0.2 9% 6.1 0.7 12% 2.4 0.1 3% 7.5 0.2 3% 2.5 0.5 25% 5.5 1.2 28% Others 28.6 -0.4 -1% 51.7 1.7 3% Others 19.7 0.7 3% 34.4 1.6 5% Source: Kantar World Panel | IH Panel | 25P3 | Key-E City; Out Of Home Panel | 25P3 | Key-D City | Chocolate Copyright © 2021 Mars Wrigley —Confidential 11

[Page 6] Channel IH Traffic (Confectionery): MW CHO and Skittles outperformed in Snack Chain; MW CHO led in Mini and EC while Skittles lagged Chocolate & FC, IH, K-E, 25P3 Chocolate FC IH IH Traffic* MAT MAT 25Q1 GR MAT25Q1 GR 25Q1 GR MAT25Q1 GR Share% Share% Cat MW Cat MW Cat MW Cat Skittles Cat Skittles Cat Skittles Total Outlets 100% 100% 1% 4% 3% 2% 100% 100% 0% -4% 1% 1% Hypermarket 17% 21% -7% -7% -4% -3% 12% 18% -7% -3% -5% -2% Large Super 17% 21% -5% 2% -1% 1% 15% 17% -14% -5% -11% -8% Small Super/Mini 22% 24% 4% 9% 7% 8% 26% 26% 2% 0% 4% -5% CVS 5% 5% -10% -3% -4% -4% 5% 6% -18% 7% -5% 11% Traditional Trade 4% 4% -5% 4% -3% -3% 6% 8% -10% -36% -7% -7% Snack Store 5% 3% 77% 105% 80% 98% 7% 7% 51% 103% 69% 175% E-commerce 16% 10% 4% 9% 6% -1% 14% 6% 16% -19% 9% -11% Gifting Acceptance** 9% 5% 3% 7% 6% -3% 8% 6% 5% 18% 6% 20% Others 6% 5% -6% 3% -7% -5% 7% 6% -12% -25% -11% -8% Source: Kantar World Panel | IH Panel | 25P3 | Key-E City *Traffic=Penetration% * No. of HHs * Frequency Others includes free mart, whole sales. direct sales etc. **Gifting Acceptance refers to product value gaining from gifting and work unit 17

[Page 7] Channel OOH Traffic (confectionery): MW CHO led in Super, TT and Snack Store; Gum and Mint lagged in TT, snack store and online Chewing Gum , Mint & Chocolate, OOH, K-D, 25P3 Chocolate Chewing Gum Mint OOH OOH OOH Traffic* MAT MAT MAT 25Q1 GR MAT25Q1 GR 25Q1 GR MAT25Q1 GR 25Q1 GR MAT25Q1 GR Share% Share% Share% CAT MW Cat MW Cat MW Cat MW Cat MW Cat MW Cat MW Cat MW Cat MW Channel 100% 100% 9% 13% 14% 15% 100% 100% 7% 5% 13% 11% 100% 100% -2% -5% 6% 13% Hypermarket 3% 3% -2% -14% 7% 2% 2% 2% 16% 20% 26% 38% 2% 2% -8% -56% -20% -48% Supermarket 18% 20% 27% 30% 28% 33% 13% 12% 15% 8% 23% 22% 12% 15% 25% 25% 22% 39% CVS 30% 32% 0% 1% 6% 6% 28% 28% -4% -1% 3% 4% 30% 32% -6% 1% -3% 8% Traditional Trade 30% 31% 10% 17% 15% 15% 47% 48% 7% 4% 16% 12% 39% 42% -9% -15% 7% 17% Snack stores 8% 5% 37% 36% 44% 41% 3% 3% 72% 56% 98% 87% 6% 3% 35% 28% 54% 53% Online 4% 2% -18% 8% -8% 6% 1% 1% -16% -24% 5% -1% 3% 1% -20% -29% -13% -28% Other channels 8% 7% 7% 17% 11% 21% 6% 6% 18% 17% 2% 1% 7% 6% 4% -1% 13% 3% Source: KWP OOH Panel, 25P3, Key-D City *Traffic=Penetration% * No. of HHs * Frequency Others includes free mart, whole sales. direct sales etc. 18

## 参考案例逻辑

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

---

## case_001

# Case Card - Case_001 Gum Occasion Study

## 1. Basic Info

- Case ID: Case_001
- Project name: Mars Gum Occasion Study
- Category / brand: 口香糖；益达 Extra、绿箭 Doublemint
- Project type: 品类增长机会研究；衰退/流失品类破局；场景需求研究；双品牌策略研究
- Target audience: 18-40 Urban Striver，覆盖学生、白领、蓝领等
- Main method: Digital Diary / 数智生活志，6 天追踪，包含工作日和休息日

## 2. Business Problem

口香糖品类长期下行，客户希望找到重新增长和破局的机会：

- 口香糖为什么不再被频繁选择？
- 消费者在什么场景下仍然可能需要口香糖？
- 益达和绿箭分别应如何进入真实生活场景？
- 品牌和产品层面是否还有可放大的机会？

## 3. Research Objectives

- 理解口香糖在真实生活中的使用/未使用场景。
- 拆解益达 Recenter / 好状态 的真实情绪结构和生活触发点。
- 拆解绿箭 After Meal / Fresh & Clean 的真实餐后卡点。
- 理解口香糖与其他“进入嘴巴”的食品/饮品之间的竞争关系。
- 捕捉口香糖习惯如何形成、中断、变化。
- 识别品牌、产品、购买路径、使用体验中的机会。

## 4. Input Material Signals

- 客户已有大量品类和品牌研究沉淀，不能从零泛问。
- 益达已有战略方向：Recenter / 好状态。
- 绿箭已有战略方向：After Meal / Fresh & Clean。
- 品类问题不只是传播问题，也涉及代际文化断裂、生活方式变化、真实购买卡点和使用习惯流失。
- 需要同时关注功能场景和情绪场景。

## 5. Final Module Structure

正式 DG 的详细题目设计采用固定板块格式：

```text
板块x：xxx
引导语：
题目：
1.
2.
...
结束语：
```

1. 关于我 / About Me
   - 建立消费者生活底色、压力来源、价值向往和日常节奏。
2. 我典型的一天 / My Typical Day
   - 记录 routine、用餐、状态变化、off-center / re-center 时刻。
3. 我正餐以外的吃吃喝喝 / Everyday Mouth-Related Item
   - 下载更广义的“嘴巴解决方案”图谱，而不只问口香糖。
4. 我的 6 天日记 / 6-Day Diary
   - 每日记录功能场景和情绪场景，捕捉 trigger、context、choice logic、体验和结果。
5. 购物任务 / Shopping Task
   - 捕捉真实购买路径、渠道、犹豫、卡点和放置位置。
6. 嘴巴习惯养成 / Mouth Habit Formation
   - 理解长期习惯、变化和跨品类替代。
7. 我期待的品牌与产品 / Brands & Products I Look Forward To
   - 进入品牌和产品机会，理解未来期待。

## 6. Key Question Logic

- “关于我”不应和产品/品牌直接发生关联，重点是描摹受访者本人：自我介绍、学业/工作、居住空间、兴趣爱好、社交生活、理想生活、焦虑/压力、生活评分。
- “我典型的一天”应开放地让受访者描画 routine、吃饭类型、餐前餐后行为、不同时间段状态、工作日和周末差异，不要写成机械时间表。
- “我正餐以外的吃吃喝喝”定义为：正餐以外、不以单纯“吃饱”为主要目的的食品与饮品。先下载广义图谱，再问口香糖是否出现。
- 不直接问“为什么不用口香糖”，而是先问真实场景中发生了什么、做了什么、是否有吃喝进入解决方案，再追问口香糖是否出现。
- 对益达，围绕“状态不佳 / 不自在 / off-center”设计题目，追问 before-during-after 的状态变化。
- 对绿箭，围绕“餐后 / 嘴巴不舒服 / 需要清新”设计题目，追问是否想到清新、用什么解决、为什么不用口香糖。
- “我的6天日记”内部可区分 Doublemint functional moments 和 Extra emotional moments，但受访者题面不应暴露内部品牌分支标签。
- 购物任务用于验证真实购买路径和卡点：第 4-5 天布置，尽量用视频 + 语音记录自然购买过程；高频用户自然购买可视作完成，低频/流失用户不强制渠道。
- 购物任务后第 5-6 天应包含 eating experience：实际吃 1 次益达、1 次绿箭，记录为什么此时吃、吃的过程真正起作用的元素、和其他食品/饮品相比有什么不同、嚼完之后做了什么。
- 习惯养成模块不是只问口香糖，而是从正餐外吃喝中选择至少 2 种产品：近 1-2 年新养成习惯的食品/饮品，以及一直以来个人最喜欢的食品/饮品，追问初尝、习惯养成、中断、变化和角色。
- 品牌与产品模块放最后，包含品牌偏好、“嚼出自在好状态”的画面/关键词、益达/绿箭印象、品牌人格化、理想口香糖和 stimulus 维度选择。

## 7. Reusable Rules

- 品类增长机会研究应先把商业问题拆成研究问题，再映射成模块。
- 如果客户已有明确战略或假设，不要重复广撒网，应在已知基础上继续往下探索。
- 场景机会研究要先建立生活方式和场景图谱，再进入目标品类。
- 日记记录应遵循：trigger -> context -> action -> alternatives -> choice logic -> target category role -> experience element -> before/during/after -> evaluation。
- 不要过早暴露品牌；前期应从真实生活和需求出发。
- 任务型题目适合验证购买/使用阻碍，但应由研究员结合项目判断是否加入。
- 输出详细题目时必须给完整题目，不要只给“建议题目示例”。
- 受访者题目要自然开放，不要用过多具体例子和选项限制回答。

## 8. Do Not Overgeneralize

- 不要把 Case_001 的 6-7 个模块当成所有项目的固定结构。
- 不要认为只要是品类增长机会，就一定需要购物任务。
- 不要把双品牌分支逻辑套到单品牌项目。
- 不要把“关于我”和“典型一天”简单压缩；是否压缩必须回到 Proposal 的研究问题判断。

## 9. Best Reference For

- 食品饮料品类增长机会。
- 衰退/流失品类破局。
- 场景需求研究。
- 双品牌不同战略场景拆解。
- 功能需求与情绪需求并行的 Digital Diary。

请只学习以上案例的设计逻辑，不要复制案例题目。
```
