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

每个板块使用固定格式：

```text
板块x：我/我的/我是/我怎么...xxx
引导语：
题目：
1.
2.
...
结束语：
```

详细题目设计里的受访者可见板块名必须默认使用第一人称“我 / 我的 / 我是 / 我怎么...”结构。研究型模块名只用于内部结构、模块目的或 handoff，不作为最终板块标题，除非客户明确要求固定标题。

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

Prefer normal wake/sleep window, main work/study blocks, lunch/evening rest or social time, rest-day places and activities, and category-relevant touchpoints that may appear on workdays vs rest days. Ask about the respondent's normal pattern, not only the most recent day, because the most recent day may be abnormal.

### 23.4 Theme-relevant spaces beat generic space tours

Space questions should narrow to the spaces where the studied behavior, category, or object actually lives. Do not ask for a generic home tour unless the study needs the full home context.

For example, a writing project should prioritize writing/reading/work/study spaces, desks, workstations, stationery storage, and favorite corners where writing or recording happens.

### 23.5 Collect object systems before abstract usage logic

For object-led categories, first collect the respondent's object ecosystem and classification logic, then ask usage scenes and choice logic.

The early "family photo" or inventory module should capture all relevant adjacent objects, not only the target item if the adjacent category gives context; where objects are stored; how the respondent classifies them and why; daily-use vs collection vs backup vs gift objects; count, source, subcategory/type, brand, and price/price band when relevant.

Small count questions are valuable when they produce reportable baselines, such as average number owned, replacement frequency, or refill vs replacement behavior.

### 23.6 Use prompts to complete commercial dimensions

Parenthetical probes in design are useful when they help respondents cover dimensions they would not naturally separate, such as subcategory, source, price band, channel, or use occasion.

Use prompts to complete the data structure, but avoid turning prompts into assumed answer options. For example, ask "how did these come to you (bought yourself, family bought, gifts, exchange, etc.)" instead of assuming every respondent has both self-purchased and gifted items.

### 23.7 Ask concrete "most" examples before abstract criteria

Do not start with "what do you value when choosing X" if respondents are likely to answer with generic criteria such as "good" or "easy to use."

First ask for concrete examples: most used, favorite, most repurchased, most expensive, most reluctant to throw away, most idle/unused, best for gifting, etc. Then ask the respondent to explain what makes each one fit that role. Use the examples to derive evaluation standards.

### 23.8 Diary recording frequency rule

Choose diary recording structure based on behavior frequency.

If a behavior may happen more than about 5 times per day or is highly fragmented, do not ask respondents to record every occurrence. Use an end-of-day recap that lets them group occurrences by type, scene, or object used.

Use every-occurrence recording only when the event is lower-frequency, has clear boundaries, or is routine but limited in count, such as skincare steps, coffee/drink moments, shopping touchpoints, or specific mood/discomfort moments. When every-occurrence recording is used, consider setting a maximum number of entries.

### 23.9 Diary can include browsing and shopping touchpoints

When a category is tied to discovery, browsing, store visits, trial, or purchase, the diary should capture those touchpoints if they naturally occur. Respondents only record the steps that happened: browsed, visited, tried, compared, bought, gave up, or got stuck.

### 23.10 Distinguish habits from one-off journeys

Do not force a detailed "most recent purchase journey" for light, low-cost, high-frequency categories if one purchase cannot represent normal behavior. In those cases, ask everyday buying habits: where they go, how long they browse, how they choose, how many they buy, what triggers purchase, and what has changed over time.

Use a detailed one-off journey only when the category has high decision value, clear shopping friction, service experience, trial-to-buy questions, or when the research goal needs step-by-step journey evidence.

### 23.11 Product innovation needs bounded imagination and metaphor

For product innovation, do not ask only broad questions such as "what should the future product be like." Bound the imagination using the proposal's hypotheses and opportunity directions.

Useful bounded prompts include a product that best represents the respondent; a product they would want to carry with them every day; the only product they could use for the next few years; or a product suitable as a gift or social sharing object.

When innovation involves emotional projection, identity, or object attachment, include metaphor/role prompts such as what role the object plays in life or what person/object it feels like.

### 23.12 Media modality choice

Images are preferred when the research needs object inventory, storage/classification, visual evaluation criteria, ideal product form, or hard-to-visualize metaphors. Images are faster to analyze and easier to use in reports.

Videos should not be mandatory unless the task requires process, movement, walkthrough, or demonstration. If video is optional, also allow photos, text, or voice.
## 24. Product Innovation Design Logic v0.2.4

These rules come from the product-innovation researcher logic note. Product innovation DG design must be grounded in real consumers, real scenes, and real needs. Do not treat social-media novelty, performative trend content, or "fancy emerging things" as innovation evidence unless the study can verify that they are real in life.

### 24.1 Core principle: product innovation is change interpretation

The core job of product innovation research is to interpret change and translate it into concrete product opportunities.

Always diagnose which type of change the project is trying to understand:

- people / cohort change: a new or changing target group, generation, class, life stage, or adoption wave;
- cognition change: the category/product role in life has changed, or the evaluation standard for "good" has changed;
- lifestyle change: new routines, life centers, social patterns, interest structures, or ideal-life gaps create new scenes;
- scene and need change: old scenes expand, shrink, fragment, intensify, or generate new unmet needs;
- usage and object-system change: what people use, carry, store, replace, combine, or classify has shifted.

Do not ask consumers directly to summarize these abstract changes. The agent must build questions that collect facts first, then let analysis infer change.

### 24.2 Product innovation must move from concrete to abstract

For every product innovation project, structure questions from concrete facts to abstract meaning:

```text
life facts
-> category scenes and needs
-> current product / solution system
-> scene-product matching logic
-> concrete evaluation standards
-> cognition, role, metaphor, and change
-> bounded future / innovation opportunities
```

Avoid starting with "How has this product changed?", "What does this category mean to you?", or "What future product do you want?" These are too abstract for most respondents and produce generic answers.

### 24.3 Decide how much lifestyle depth is needed

All product innovation projects need some lifestyle context, but the depth depends on the innovation source.

Use heavier lifestyle modules when:

- the project is driven by cohort / generation change;
- the target group is unfamiliar to the research team;
- the proposal asks how the target group's life has changed;
- the category role may be changing because the respondent's social-cultural context changed.

Use lighter lifestyle context when:

- the project is high-frequency line extension with no major target-group shift;
- the path from broad lifestyle to product requirement would be too long;
- current category scenes, usage details, evaluation criteria, or product form are more directly actionable.

Even when lifestyle is lighter, still cover life center of gravity, rhythm, interests/social circle, and ideal life vs reality gap if they can explain product opportunities.

### 24.4 Lifestyle is a collection of scenes

Treat lifestyle as the respondent's scene system. To understand lifestyle efficiently, collect:

- life center of gravity: where their time, energy, and emotional concentration are;
- life rhythm: fast/slow, stable/fluid, many/few scene switches;
- interests and social circle: where leisure time and new scenes are most likely to emerge;
- ideal life image and reality gap: what life they want, what pain or tension blocks it.

For product innovation, the ideal-life section should usually be shallow and opportunity-oriented. It matters because product ideas, naming, claims, and emotional benefits may connect to life pain points and aspirations, but it should not become a brand-positioning deep dive unless the project asks for that.

### 24.5 Scene and need are inseparable

In product innovation, a "valuable new scene" is not merely a new place or activity. It must generate or reveal a new, stronger, more frequent, or more actionable need.

When asking scene change, probe:

- which scenes are new;
- which scenes happen more or less often;
- which scenes used to involve the category but no longer do;
- which scenes did not involve the category before but now do;
- which scenes create stronger, different, or unsolved needs;
- which scenes are only variants of old needs and therefore have low innovation value.

Use proposal hypotheses or known behavior types to make scene probes specific. A broad question like "which writing scenes changed" may get generic answers; a more specific probe such as "in high-volume study/writing moments, what has changed" can produce usable product needs.

### 24.6 Cognition has two layers

Product innovation must capture cognition change in two layers:

1. category/product role: what role the product plays in life, how close/far it feels, and what kind of object/person/relationship it resembles;
2. evaluation standard: what now counts as "good", "useful", "beautiful", "safe", "convenient", "worth buying", or "worth sharing."

Both layers should be asked through concrete tasks, examples, sorting, reference images, metaphors, and comparison, not through abstract "what does it mean" questions.

When the cognition object is not a concrete physical product/object but a cultural image, cultural practice, social concept, or self-created concept, use direct definition, association, and change probes instead of product metaphor first.

Examples include Spring Festival / CNY, 二次元, or "慢人" in a Xiaohongshu slow-person festival context.

Ask:

- what the respondent thinks counts as X / what X means to them, such as "怎样算过年" or "什么是二次元";
- the first image that appears in their mind when X is mentioned, why that image appears, and what sounds, tastes, smells, emotions, objects, or images they associate with it;
- whether X has changed in their view, why, and how their own expectations have changed, such as whether the "年味" of Spring Festival feels stronger, weaker, or about the same now.

### 24.7 Role cognition requires metaphor and classification

For abstract category roles, use metaphor and classification:

- what person, object, relationship, or life role the product feels like;
- what other objects it is mentally grouped with;
- whether it is closer to tool, self-expression object, emotional object, social object, collection, companion, or basic utility;
- how its role changed from past to now, and what role the respondent hopes it will play in the future.

Classification is not only organization; it reveals cognition. For example, if a product is placed with work tools, it may be cognitively a tool. If placed with toys, hangers, collectibles, or identity objects, it may be closer to emotion or self-expression.

When the cognition object is already a concrete physical product/object, use metaphor in several ways and always ask why:

- what the object is like, or what it can be compared to;
- what other objects it belongs with mentally or physically, including adjacent objects such as bag charms, toys, collectibles, accessories, or tools;
- what role it plays in daily life;
- if it were a person, what age, personality, occupation, and dressing style it would have;
- what relationship it has with "me", including closeness, distance, dependency, companionship, or occasional use.

### 24.8 Evaluation standards must be decomposed by category

Never accept "good-looking", "easy to use", "safe", "good quality", or "good value" as final innovation inputs. Decompose each into category-specific dimensions.

Depending on the category, dimensions may include:

- sensory experience: scent, texture, sound, appearance, touch, taste, foam, particle shape, etc.;
- functional performance: solves what, protects what, saves what effort, prevents what risk;
- actual use experience: convenience, compatibility, smoothness, control, stability, ease of replacement;
- emotional or identity value: self-expression, reassurance, companionship, pride, gifting, social display;
- form and physical detail: size, thickness, weight, shape, material, portability, storage, refill/reuse.

Ask for concrete references and images when standards involve appearance, form, sensory imagination, or ideal product examples.

When the project touches any product, usage, purchase, trial, or service experience, include experience-standard questions. The goal is to understand what consumers count as a good or bad experience, not only what functions they name.

Use category-specific extreme-experience prompts:

- ask for the best / happiest / smoothest / most satisfying experience, adapted to the category, such as the smoothest writing moment for a pen or a particularly good cup of coffee;
- encourage sensory detail and scene reconstruction: touch, sound, taste, aroma, appearance, body feeling, emotion, and what happened before/during/after;
- after the good experience, ask the reverse: the worst / most frustrating / most disappointing experience, what makes them especially unhappy, and what missing element would make the experience unacceptable.

### 24.9 Current product system before future innovation

Before asking future product ideas, first understand:

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
