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

## 21. Case_005 Promoted Designer Rules v0.2.3

These rules come from the reviewed KACO / writing-instrument case. They are reusable design logic, not respondent-facing copy rules.

### 21.1 Module size and merge judgment

If a module has fewer than about 5 questions, do not keep it as a standalone module by default. Merge it with the adjacent module unless it is a genuinely independent task module, such as a shopping task, diary task, media mission, stimulus test, or screening branch.

### 21.2 Baseline life context is required in every project

Every project needs enough respondent life context before category or brand questions. Do not reduce the opening context to identity and routine only.

At minimum, judge whether the study needs to understand life center of gravity, daily rhythm, work/study/rest pattern, interests, social circle, common places, where time and energy are spent, and everyday spending pattern. Screener data may provide percentages or quotas, but the DG should still capture the "why" behind spending and lifestyle choices when it matters to the category opportunity.

For groups the research team may not know well, or where there is a clear generation/class/context gap, ask this context in more detail.

### 21.3 Routine questions should avoid low-value timelines

"Typical day" modules should not force a full morning-to-night transcript. Prefer normal wake/sleep window, main work/study blocks, lunch/evening rest or social time, rest-day places and activities, and category-relevant touchpoints. Ask about the respondent's normal pattern, not only the most recent day.

### 21.4 Theme-relevant spaces beat generic space tours

Space questions should narrow to the spaces where the studied behavior, category, or object actually lives. Do not ask for a generic home tour unless the study needs the full home context.

### 21.5 Collect object systems before abstract usage logic

For object-led categories, first collect the respondent's object ecosystem and classification logic, then ask usage scenes and choice logic. The inventory module should capture adjacent objects, storage, classification and reasons, daily-use vs collection vs backup vs gift objects, count, source, type, brand, and price/price band when relevant.

### 21.6 Use prompts to complete commercial dimensions

Parenthetical probes in design are useful when they help respondents cover dimensions they would not naturally separate, such as subcategory, source, price band, channel, or use occasion. Use prompts to complete the data structure, but avoid turning prompts into assumed answer options.

### 21.7 Ask concrete "most" examples before abstract criteria

Do not start with "what do you value when choosing X" if respondents are likely to answer with generic criteria. First ask for concrete examples: most used, favorite, most repurchased, most expensive, most reluctant to throw away, most idle/unused, best for gifting, etc. Then ask the respondent to explain what makes each one fit that role.

### 21.8 Diary recording frequency rule

If a behavior may happen more than about 5 times per day or is highly fragmented, do not ask respondents to record every occurrence. Use an end-of-day recap that lets them group occurrences by type, scene, or object used. Use every-occurrence recording only when the event is lower-frequency, has clear boundaries, or is routine but limited in count.

### 21.9 Diary can include browsing and shopping touchpoints

When a category is tied to discovery, browsing, store visits, trial, or purchase, the diary should capture those touchpoints if they naturally occur. Respondents only record the steps that happened: browsed, visited, tried, compared, bought, gave up, or got stuck.

### 21.10 Distinguish habits from one-off journeys

Do not force a detailed "most recent purchase journey" for light, low-cost, high-frequency categories if one purchase cannot represent normal behavior. Ask everyday buying habits instead. Use a detailed one-off journey only when the category has high decision value, clear shopping friction, service experience, trial-to-buy questions, or when the research goal needs step-by-step journey evidence.

### 21.11 Product innovation needs bounded imagination and metaphor

For product innovation, do not ask only broad questions such as "what should the future product be like." Bound the imagination using the proposal's hypotheses and opportunity directions. When innovation involves emotional projection, identity, or object attachment, include metaphor/role prompts.

### 21.12 Media modality choice

Images are preferred when the research needs object inventory, storage/classification, visual evaluation criteria, ideal product form, or hard-to-visualize metaphors. Videos should not be mandatory unless the task requires process, movement, walkthrough, or demonstration.
## 22. Product Innovation Design Logic v0.2.4

These rules come from the product-innovation researcher logic note. Product innovation DG design must be grounded in real consumers, real scenes, and real needs. Do not treat social-media novelty, performative trend content, or "fancy emerging things" as innovation evidence unless the study can verify that they are real in life.

### 22.1 Core principle: product innovation is change interpretation

The core job of product innovation research is to interpret change and translate it into concrete product opportunities.

Always diagnose which type of change the project is trying to understand:

- people / cohort change: a new or changing target group, generation, class, life stage, or adoption wave;
- cognition change: the category/product role in life has changed, or the evaluation standard for "good" has changed;
- lifestyle change: new routines, life centers, social patterns, interest structures, or ideal-life gaps create new scenes;
- scene and need change: old scenes expand, shrink, fragment, intensify, or generate new unmet needs;
- usage and object-system change: what people use, carry, store, replace, combine, or classify has shifted.

Do not ask consumers directly to summarize these abstract changes. The agent must build questions that collect facts first, then let analysis infer change.

### 22.2 Product innovation must move from concrete to abstract

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

Avoid starting with "How has this product changed?", "What does this category mean to you?", or "What future product do you want?"

### 22.3 Decide how much lifestyle depth is needed

All product innovation projects need some lifestyle context, but the depth depends on the innovation source.

Use heavier lifestyle modules when the project is driven by cohort/generation change, the target group is unfamiliar, the proposal asks how the target group's life has changed, or the category role may be changing because the respondent's social-cultural context changed.

Use lighter lifestyle context when the project is high-frequency line extension with no major target-group shift, the path from broad lifestyle to product requirement would be too long, or current category scenes, usage details, evaluation criteria, or product form are more directly actionable.

Even when lifestyle is lighter, still cover life center of gravity, rhythm, interests/social circle, and ideal life vs reality gap if they can explain product opportunities.

### 22.4 Lifestyle is a collection of scenes

Treat lifestyle as the respondent's scene system. To understand lifestyle efficiently, collect life center of gravity, life rhythm, interests and social circle, and ideal life image vs reality gap.

For product innovation, the ideal-life section should usually be shallow and opportunity-oriented. It matters because product ideas, naming, claims, and emotional benefits may connect to life pain points and aspirations, but it should not become a brand-positioning deep dive unless the project asks for that.

### 22.5 Scene and need are inseparable

In product innovation, a "valuable new scene" is not merely a new place or activity. It must generate or reveal a new, stronger, more frequent, or more actionable need.

When asking scene change, probe which scenes are new, more frequent, less frequent, disappeared, newly category-relevant, or stronger in need. Also distinguish scenes that are only variants of old needs and therefore have low innovation value.

Use proposal hypotheses or known behavior types to make scene probes specific. Broad "what changed" questions should be broken into more specific scene probes.

### 22.6 Cognition has two layers

Product innovation must capture cognition change in two layers:

1. category/product role: what role the product plays in life, how close/far it feels, and what kind of object/person/relationship it resembles;
2. evaluation standard: what now counts as "good", "useful", "beautiful", "safe", "convenient", "worth buying", or "worth sharing."

Both layers should be asked through concrete tasks, examples, sorting, reference images, metaphors, and comparison.

### 22.7 Role cognition requires metaphor and classification

For abstract category roles, use metaphor and classification: what person/object/relationship the product feels like, what other objects it is mentally grouped with, and whether it is closer to tool, self-expression object, emotional object, social object, collection, companion, or basic utility.

Ask how its role changed from past to now, and what role the respondent hopes it will play in the future.

### 22.8 Evaluation standards must be decomposed by category

Never accept "good-looking", "easy to use", "safe", "good quality", or "good value" as final innovation inputs. Decompose each into category-specific sensory, functional, usage, emotional, identity, form, and physical-detail dimensions.

Ask for concrete references and images when standards involve appearance, form, sensory imagination, or ideal product examples.

### 22.9 Current product system before future innovation

Before asking future product ideas, first understand current scenes and needs, current products/solutions, scene-product matching, substitutability, carry/storage/gift/collection/abandonment logic, purchase and usage habits, and concrete criteria for "good."

Only after this should the questionnaire ask about role change, cognition change, and future innovation directions.

### 22.10 Innovation output may be big or small

Do not assume product innovation must be disruptive. Some categories need safe, stable, incremental innovation.

If the target group has broadened from niche to mass, common baseline needs may become more important than niche aspirations. Innovation may focus on reliability, protection, stability, ease, affordability, or no-trouble use rather than surprising new features.

### 22.11 Example application: writing instruments

For a writing-instrument innovation project, include target lifestyle change, writing scene change, current pen/stationery system, scene-pen mapping, substitutability, carried vs desk vs collection pens, buying/usage habits, decomposed criteria, and role/metaphor change.

### 22.12 Example application: mid/low-end cat food

For a mass pet-food innovation project, diagnose whether broader pet ownership makes common baseline needs more important. Probe pet cognition differences, practical companion-style needs, and concrete product-form details such as particle size, thickness, shape, chewability, convenience, and acceptance.

### 22.13 Product innovation self-check

Before finalizing a product innovation DG, check whether the design identified the change source, collected concrete facts before abstract meaning, connected lifestyle to category scenes and product needs, asked scene change specifically, decomposed evaluation standards, included role/metaphor when needed, avoided unbounded future imagination, and distinguished disruptive innovation from safe/stable incremental innovation.
