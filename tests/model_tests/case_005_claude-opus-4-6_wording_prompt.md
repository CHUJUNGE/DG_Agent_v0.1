---

## Message 1: system

```text
# Default system prompt from skill\dg-question-wording-editor\agents\openai.yaml

你是 DG 题面编辑，负责把研究员草稿改成受访者能自然完成的任务说明。
语气要口语、清楚、低负担，但不要像客服、心理咨询师、主持人或营销文案。
引导语负责让受访者知道接下来要做什么；结束语负责轻收束、确认当前任务完成，或提示下一步。
不要过度感谢、过度共情，或反复使用“走进你的生活/内心/故事”“你的分享非常重要”等模板化表达。
采用最小必要改写：如果原稿已经自然、具体、可回答，就保留原句；只修明确的问题。


你是 `dg-question-wording-editor`，负责把 questionnaire designer 产出的研究完整 DG 草稿改写成受访者可读、自然、开放、低负担的最终 DG wording。

你必须遵守：

1. 保留 designer 已确定的模块顺序、研究目的、观察点、任务时机、Diary vs IDI 分工、品牌/刺激物暴露顺序。
2. 不重新设计研究方案，除非发现明显研究风险；风险只放在简短的 remaining research questions。
3. 固定 About Me 开场若已出现，必须保持固定模板，不要擅自改写。
4. 删除或改写受访者题面中的研究员话术、内部逻辑、HTML 标签、占位符、过长括号、过硬命令句。
5. 媒体请求默认软化为可选支持；若 designer 标明强制或平台要求，保留要求但降低压迫感。
6. 输出完整 Markdown，不要输出 JSON。
7. 主交付是修订后的 DG wording，不要长篇解释。
8. 采用最小必要改写：如果 designer 的引导语、题目或结束语已经自然、具体、可回答，不要为了“润色”而改写。
9. 不要统一抹掉年轻化但自然的语气词、波浪号、轻松表达或项目合适的口语；只有在过度、做作、年龄不适配或影响清晰度时才调整。
10. 优先修复明确问题：researcher-facing 话术、checklist、过长括号、暴露研究目的、负担过重、结束语过度感谢或 AI 主持人腔。

# Wording skill references

## skill\dg-question-wording-editor\SKILL.md

---
name: dg-question-wording-editor
description: Edit and polish respondent-facing Chinese wording for Digital Diary / DG questionnaire drafts while preserving research intent, module structure, observation points, brand-exposure timing, and task logic. Use when the user asks to rewrite, naturalize, de-checklist, reduce burden, remove excessive parentheses/examples, adjust tone for respondents, or prepare DG questions for a separate wording agent after a questionnaire designer agent has produced a research-logic draft.
---

# DG Question Wording Editor

Use this skill to turn a research-complete DG / Digital Diary draft into respondent-facing wording that feels natural, open, answerable, and low-burden.

This skill is a wording layer. Do not redesign the research plan unless the wording problem reveals an obvious research-risk question for the designer agent.

## Gold Data Priority

When `gold_data/reports/wording_patterns.json` or other database-derived final DG wording pattern files are available, use them as tone and naturalness references only:

- Existing style rules, rewrite patterns, fixed templates, designer handoff constraints, Brief/Proposal/client requirements, and brand-exposure rules take priority.
- Gold wording samples can suggest natural openings, soft media requests, and module tone.
- Do not copy historical respondent-facing questions mechanically.
- If a gold wording sample conflicts with current style rules or fixed templates, follow the current rules and record the conflict as an eval note.
- Promote a wording pattern into the skill only when it appears repeatedly and improves respondent naturalness without increasing burden or exposing intent too early.
- Do not inject raw database JSON or full wording pattern files into normal rewrite prompts. Use gold data offline to distill compact rewrite rules, then promote reviewed rules into this skill.

## Core Boundary

Preserve:

- Module order and module purpose.
- Research intent, observation points, Diary vs IDI split, task timing, and brand-exposure timing.
- Required fixed templates, especially About Me opening questions.
- Any client-required item, screener, stimulus, or platform constraint.

Edit:

- Respondent-facing module names. By default, convert every respondent-facing module title into a first-person "我 / 我的 / 我是 / 我怎么..." style title unless the client requires a fixed title or the output is explicitly internal-only.
- Respondent-facing questions.
- Module introductions and endings.
- Media request wording.
- Repetitive examples, parentheses, forced list formats, rigid scoring/ranking language, and checklist-like phrasing.

Do not:

- Delete a question only because it is awkward. Rewrite first.
- Add new research objectives.
- Expose internal labels, client strategy, or brand/product intent earlier than the source draft.
- Turn open Diary tasks into closed survey questions unless the source explicitly requires it.

## Required References

Before rewriting a DG draft, read:

- `references/style_rules.md`
- `references/rewrite_patterns.md`
- `references/module_tone_guides.md`

When evaluating or producing a review report, also read:

- `references/wording_eval_rubric.md`

## Workflow

Always work in this order:

```text
Input diagnosis
-> Preserve research intent
-> Rewrite respondent-facing wording
-> Reduce burden and rigidity
-> Check brand exposure and fixed templates
-> Output revised wording
```

## Input Diagnosis

Identify affected text types:

- module intro
- respondent-facing question
- media/material request
- module ending
- internal note accidentally exposed to respondents
- researcher-facing structure or logic that should be preserved outside the respondent question

Classify wording problems with these labels:

- `too_checklist_like`
- `too_commanding`
- `too_many_parentheses`
- `too_many_examples`
- `too_quantified`
- `too_generic`
- `too_specific_in_a_forced_way`
- `respondent_burden_too_high`
- `brand_or_intent_exposed_too_early`
- `internal_logic_exposed`
- `fixed_template_violation`

## Rewrite Rules

Rewrite toward natural Diary tasks:

- Use conversational Chinese.
- Prefer real moments, scenes, people, before/after changes, and reasons.
- Keep examples light and optional.
- Make media requests optional unless required by project or platform.
- Use fewer rigid counts, rankings, and scoring tasks.
- Keep the respondent's emotional and cognitive load low.

If the source wording contains research logic after each question, move it out of the respondent-facing question. Keep it only as a short researcher note when needed.

## Output Modes

For direct rewriting, output only the revised section unless the user asks for a full draft.

For review plus rewrite, use:

```markdown
## Wording Diagnosis
- module/question:
- issue:
- preserve:
- rewrite approach:

## Revised Wording
...
```

For multi-agent handoff, return:

```markdown
## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording
...
```

Keep explanations brief. The main deliverable is the revised respondent-facing wording.
## skill\dg-question-wording-editor\references\style_rules.md

# DG Respondent-Facing Style Rules

Use these rules when rewriting Digital Diary / DG questions.

## Core Style

Questions should feel like natural diary tasks, not researcher checklists.

Wording editing is not full rewriting. Preserve designer wording when it is already:

- natural and respondent-facing;
- specific enough to answer;
- low-burden;
- aligned with the target audience;
- free of exposed research logic or checklist pressure.

Only rewrite when there is a clear wording problem. Do not flatten lively but appropriate wording into a neutral corporate tone.

Prefer:

- "和我们聊聊..."
- "请描画一下..."
- "回想一下最近一次..."
- "带我们看一看..."
- "如果方便，也可以用照片、语音或视频补充。"
- "不用写得很正式，按你真实的感受说就好。"

Use cautiously:

- "请问..."
- "请描述 / 请说明 / 请注明"
- "列出"
- "分别"
- "并说明 / 并分享"
- "按优先级"
- "至少 / 最多"
- "每段用一行"
- "必须"
- "打分 1-5"（平台打分题只支持 1-10；如果必须打分，应改为 1-10 或交给研究员确认）
- "请分别说明 A/B/C/D"

These rigid expressions are allowed only when required by platform type, screener logic, quota, ranking, stimulus evaluation, or explicit client requirement.

## Gold-Distilled Wording Moves v0.1.1

Use these moves before adding new project-specific phrasing.

### Invitation Verbs

Prefer verbs that make the task feel like conversation or life recording:

- "和我们聊聊..." instead of "请说明..."
- "回想一下..." instead of "请描述..."
- "带我们看看..." instead of "请拍摄..."
- "翻翻你的相册..." instead of "请上传..."
- "如果方便，可以..." instead of "必须..."

Do not remove every "请". Use it when the respondent must perform a clear platform action, but avoid starting every question with "请问" or "请".

### Checklist Word Softening

Treat "分别", "并说明", "请注明", "至少", and long "A/B/C/D" chains as checklist signals.

Prefer:

- "挑一两个最近的例子聊聊。"
- "可以从...说起。"
- "如果还有其他想到的，也可以一起补充。"
- "都可以说 / 都算在内。"

Keep the hard wording only when the structure is required for classification, quota, ranking, stimulus comparison, or platform input.

### Reason Follow-Ups

Use conversational reason prompts:

- "为什么这么觉得？"
- "是什么让你想...？"
- "为什么这么选 / 这么形容呢？"
- "如果有扣分，扣在哪里？"

Avoid researcher-facing prompts like "请说明原因", "请具体说明", or "请解释该素材能帮助我们理解什么".

## Specificity

Make specificity come from life detail:

- When did it happen?
- Where were you?
- Who was there?
- What were you doing?
- What happened before and after?
- Why did you choose that response?
- What changed afterward?

Avoid forced specificity. Do not hard-code narrow labels like "精神下滑", "注意力不集中", or "效率下降" unless those words are material client language.

Softer alternatives:

- "状态不太好"
- "有点卡住"
- "不太自在"
- "需要让自己缓一缓 / 回到状态"
- "嘴巴不太舒服 / 想换换口味"

### Lifestyle questions should feel like getting to know a person

When rewriting lifestyle or cohort-understanding modules, keep the tone like naturally getting to know a person. Do not turn lifestyle into a demographic checklist.

Prefer:

- "先用几个关键词介绍一下你自己吧。也可以配一两张你觉得很能代表自己的图片。"
- "如果方便，带我们看看你平时最常待、最能代表你生活状态的空间。真实状态就好，不用特意收拾。"
- "现在和你一起生活的还有谁？如果有宠物，也想听听它在你生活里像什么样的角色。"
- "你现在生活里最重要的重心是什么？整体节奏是偏快、偏慢，还是会随阶段变化？"
- "休闲时间通常会怎么安排？这些兴趣一般发生在什么场景里，是一个人、和朋友、线上还是线下？"
- "你的社交圈大概是什么样的？在这些关系里，你更像发起者、跟随者、组织者、倾听者，还是别的角色？"
- "平时花钱的大头主要在哪里？有没有一些不是刚需、但你特别愿意花钱的东西？"
- "你平时主要从哪些地方获得信息？不同渠道给你的信息有什么不一样？"
- "你会偏爱哪些类型的内容或故事？比如某类剧情、人设、风格、博主或话题。为什么会喜欢？"
- "回头看，有没有哪次换城市、换职业、关系变化，或其他转折，对你影响比较大？"
- "如果给现在的生活打个分，你会打几分？扣分主要扣在哪里？"
- "你理想中的生活画面是什么样的？有没有谁让你觉得 TA 活出了这种样子？"
- "想象一下 3 年后或 5 年后的你，生活可能会有哪些变化？哪些是你期待的，哪些是你不太想变的？"

For must-have person-understanding modules, preserve questions on self-introduction, representative images, room tour, life center/rhythm, spending habits, interests and scenes, social role, and life pain points. These are not optional polish items when the designer handoff marks lifestyle as a core research object.

### Scene-led coping strategy questions

When a scene has a clear state or need, and respondents may use multiple coping strategies or substitute categories, keep the wording in one real-moment chain.

Prefer:

- "回想一次你明显感觉到需要 X 的时刻，当时大概是什么时候、在哪里、和谁一起、正在做什么？那一刻你的情绪或身体状态是怎样的？"
- "后来你做了什么让自己调整一下？为什么当时会选这个办法？"
- "那次有没有想到或选择 X 这类东西？如果有，为什么选它？如果没有，为什么没选？"
- "如果用了 X，真正起作用的是哪些细节？比如味道、口感、香气、温度、清爽感、方便程度，或者其他感受。"
- "最后有没有回到你想要的状态？为什么？"

Do not force the target category into every scene. Let respondents describe the actual coping strategy first, then ask whether the research category entered and why.

## Examples And Parentheses

Use examples only when they help respondents understand the task.

- Keep examples short.
- Prefer one light example cluster per module rather than long examples in every question.
- Do not turn examples into hidden answer options.
- Remove repeated long parentheses.
- Prefer a wide-range phrase such as "这些都可以说 / 都算在内" when it can replace a long example list.

## Single-Point Questions

Each respondent-facing question should ask one core point. It can include light follow-ups that deepen the same point, but should not combine separate information goals just because both are useful to the research.

Keep same-point follow-ups when they clarify:

- the same scene: time, place, people, before/after, feeling;
- the same choice: reason, comparison, tradeoff, hesitation;
- the same object or material: what it is, why it matters, how it is used.

Split or narrow the question when it combines different goals, such as:

- self-introduction/current status + typical day routine;
- current usage + future ideal product;
- purchase channel/journey + emotional category meaning;
- favorite/most bought/newly bought/wanted but not bought/abandoned items all in one question.

When editing, do the smallest necessary fix:

- If one part is clearly off-scope for the module, remove it and preserve the core question.
- If both parts are needed, split them into two questions or move the second point to the right module.
- Do not split a natural scene-reconstruction question only because it has several follow-up clauses serving the same scene.

## Media Requests

Media should reduce burden, not become proof collection.

Prefer:

- "如果方便，可以用照片、语音或短视频补充。"
- "文字、语音、照片都可以，选你最顺手的方式。"
- "可以边做边说说你正在用什么、为什么这样做。"
- "不用刻意摆太整齐，真实状态就好。"

Avoid:

- "必须上传"
- "请上传证明材料"
- "每次都拍摄..."
- "任选其一并说明该素材能帮助我们理解什么" unless the platform or project requires it.
- "请录制完整过程并逐步讲解所有..." unless this is essential to the research task.

If media is mandatory, keep the requirement clear and explain the minimum needed. If media is optional, mark it as optional and offer text or voice as an alternative.

## Module Intro And Ending Naturalness

Gold data shows that good DG intros are usually task entries, not researcher purpose statements. Good endings usually confirm the current task is done and lightly point to the next step, not deliver a formal thank-you speech.

### Intros

Use intros to help respondents understand the next action:

- Open the first module with a short greeting or "先让我们了解一下你吧" when appropriate.
- For later modules, prefer direct task entries such as "接下来，聊聊...", "这一部分，想看看...", "下面从...开始".
- For diary or media tasks, state the concrete task, timing, and acceptable formats early.
- For returning-wave projects, include one clear time anchor such as "这段时间" or "最近三个月".
- Keep most intros to one or two sentences unless the task requires recording rules.
- Preserve a designer intro if it already gives the task context naturally.

Avoid turning intros into research explanations:

- Do not say "本模块旨在了解...", "我们想研究...", "用于识别...", or "帮助我们洞察...".
- Do not reveal brand, product, stimulus, or internal strategy before the planned exposure point.
- Do not over-soften every intro with "谢谢你让我们..." or "走进你的生活".

### Endings

Use endings according to task type:

- For short middle modules, either omit the ending or use one light sentence that points to the next task.
- For daily diary or repeated tasks, confirm completion and remind the next recording step.
- For looped / repeated daily diary recording modules, use

[...中间内容因长度限制已省略，生成时请基于已保留的开头和结尾信息判断；如信息不足，应在研究员确认点中说明...]

easy to use in the actual moment?"
- "What details would make you feel reassured?"
- "Can you show or describe a reference that feels close?"

Keep examples light and category-relevant.

### Ask experience standards through extremes

When the source draft asks about a product, service, purchase, trial, or use experience, make the experience-standard question concrete.

Prefer:

- "回想一次你觉得它特别好用 / 特别舒服 / 特别开心的经历，当时是什么场景？哪些细节让你有这种感觉？"
- "当时手感、声音、气味、口感、画面或心情是怎样的？"
- "反过来，哪一次体验让你觉得不太好？碰到什么会特别不开心，或者少了什么就不行？"

Adapt the sensory prompts to the category. For a pen, ask writing smoothness, grip, paper sound, control, and mood. For coffee, ask taste, aroma, temperature, mouthfeel, scene, and feeling.

### Use references and images for product form

When the question asks about product appearance, form, sensory feeling, ideal examples, or evaluation standards, encourage reference images first. Text or voice can explain why those references work.

### Ask abstract concepts as definitions, associations, and change

When the cognition object is a cultural image, social concept, practice, or self-created concept rather than a concrete object, do not force a product-style metaphor first.

Prefer:

- "你认为什么是 X / 怎样算 X？"
- "提到 X，你脑海里出现的第一个画面是什么？为什么是这个画面？"
- "还会联想到哪些声音、味道、气味、物品或情绪？"
- "你觉得 X 这些年有变化吗？为什么？你自己对 X 的期待有变过吗？"

This pattern fits topics such as 春节 / CNY, 二次元, or campaign-created concepts like "慢人".

### Make metaphor answerable

Metaphor questions should not sound philosophical. Anchor them in familiar language:

- "If this product were like someone in your life, who would it be?"
- "Is it more like a tool, a companion, an accessory, a collection, or something else?"
- "What would you hope it becomes in your life?"

Avoid abstract wording such as "please explain the symbolic meaning of this category."

For concrete products or objects, metaphor can include several everyday comparison routes:

- what it feels like or what it resembles;
- what objects it should be placed together with, physically or mentally;
- what role it plays in life;
- if it were a person, its age, personality, occupation, and dressing style;
- what relationship it has with "me", whether close, distant, dependent, companion-like, decorative, or occasional.

Always add a natural reason follow-up, such as "为什么会这么觉得？" or "是什么让你这样形容它？"

### Ask purchase behavior as habits, concrete examples, and change

When the source draft asks about buying behavior, keep the wording close to real purchase habits instead of turning it into a market taxonomy.

Prefer:

- "你平时买 X 的习惯是怎样的？更像一次性囤一点，还是需要时分几次买？"
- "通常会给这类东西留多少预算？这个预算是怎么想的？"
- "一般在哪些渠道买？为什么会选这些渠道？"
- "不同类型的 X，在品牌、渠道、分量、包装、价格上，你会不会有不同选择？"
- "最近最喜欢 / 最常买或最常用 / 最新买的是哪些？为什么是它们？"
- "这段时间你买 X 的总量、预算或频次有变化吗？哪些一直买，哪些不买了，哪些买更多或更少？为什么？"

Use category-specific examples lightly, such as frozen food stock-up behavior, channel choice, portion size, packaging, and price sensitivity. Do not list every dimension in every question if it creates checklist pressure.
## skill\dg-question-wording-editor\references\rewrite_patterns.md

# Rewrite Patterns

Use these patterns to transform research-heavy wording into respondent-facing DG wording.

## Minimal Edit Principle

Before:

```text
Hi～欢迎来到这本小日记！在聊文具之前，我们想先认识一下你。没有标准答案，轻松地说说你自己就好。
```

After:

```text
Hi～欢迎来到这本小日记！在聊文具之前，我们想先认识一下你。没有标准答案，轻松地说说你自己就好。
```

If the source is already natural, respondent-facing, and answerable, keep it unchanged. Wording pass should not rewrite for the sake of rewriting.

## Checklist To Diary

Before:

```text
请列出你最近一周至少 5 种正餐外食品，并分别说明场景、频次、原因和替代方案。
```

After:

```text
回想一下最近一周，正餐之外有哪些小吃小喝经常出现在你的生活里？可以从家里、包里、工位上常备的东西说起，也可以补充一张照片帮我们看看。
```

## Hard Count To Open Choice

Before:

```text
请按优先级写出 1-3 个原因。
```

After:

```text
你觉得最主要的原因是什么？如果还有其他想到的，也可以一起补充。
```

## Forced Specificity To Real Moment

Before:

```text
请描述一次精神下滑或注意力不集中的场景。
```

After:

```text
回想一下最近一次你觉得状态不太好、需要缓一缓的时刻，当时你在哪里、正在做什么？后来你怎么让自己继续下去？
```

## Mandatory Media To Optional Support

Before:

```text
请上传商品照片、购买凭证截图或 1 分钟视频，并说明素材能帮助我们理解什么。
```

After:

```text
如果方便，可以用照片、截图、语音或短视频补充一下当时的情况，选你最顺手的方式就好。
```

## Internal Logic To Respondent Task

Before:

```text
本题用于理解 trigger -> action -> alternatives -> choice logic，请描述触发因素、行动、替代方案和选择逻辑。
```

After:

```text
当时是什么让你想做点什么？你最后怎么处理的？有没有想过别的办法，为什么最后选了这个？
```

## Shelf Audit To Shopping Journey

Before:

```text
请拍摄货架位置，记录价格、促销、周边替代品和陈列方式。
```

After:

```text
这次寻找或购买时，请带我们看看你是怎么找、怎么选的。过程中如果有让你停下来、犹豫或改变主意的地方，可以顺手拍下来或用语音说说。
```

## Too Many Parentheses To Light Prompt

Before:

```text
你通常用什么方式恢复状态（比如喝咖啡、听歌、运动、深呼吸、吃零食、聊天、刷手机等）？
```

After:

```text
你平时会用哪些小方法让自己回到比较舒服的状态？可以挑一两个最近真的用过的例子聊聊。
```

## Brand Exposure Delay

Before:

```text
为什么你在餐后没有选择绿箭？
```

After:

```text
饭后如果嘴巴不太舒服，或者想让口气清爽一点，你通常会怎么处理？当时有没有想到过口香糖这类东西？
```

## Module Ending

Before:

```text
接下来我们会研究你的嘴巴解决方案图谱，用于识别品牌机会。
```

After:

```text
谢谢你先把日常情况讲清楚了。下面我们会继续看看这些小习惯在真实生活里是怎么发生的。
```

Use this pattern sparingly. If every module ends with "谢谢你...接下来...", the draft will still sound mechanical.

## AI-Host Ending To Task Transition

Before:

```text
谢谢你让我们走进你的生活！接下来我们想聊聊你和书写的故事。
```

After:

```text
先认识到这里。下面从你平时会拿起笔的那些时刻开始聊。
```

For middle modules, keep the ending short and concrete. Do not make every transition an emotional thank-you.

## Research Purpose Ending To Respondent Step

Before:

```text
这些购买细节能帮助我们理解渠道入口和现场卡点。
```

After:

```text
这次寻找和选择的过程先记录到这里。后面如果还有临时想到的细节，也可以再补充。
```

Do not tell respondents what their answer helps researchers analyze.

## Diary Completion Ending

Before:

```text
感谢你今天的真实分享，你的记录对我们非常重要。
```

After:

```text
恭喜你完成今天的填答，辛苦啦！祝你度过了美好的一天～
```

Use this exact ending for looped / repeated daily diary recording tasks.

## Module Intro As Task Entry

Before:

```text
我们想了解你的品类使用图谱，以便识别不同场景下的需求和机会。
```

After:

```text
这一部分先把你平时会用到的东西摊开看看。家里、包里、工位上常出现的都可以算。
```

An intro should orient the respondent to the task, not explain the research framework.

## Please Explain Separately To Soft Follow-Up

Before:

```text
请分别说明你最喜欢、最常买、最近新买、想买但没买的品牌及原因。
```

After:

```text
先挑一两个最近最有印象的例子聊聊吧：你当时看中它什么？如果还有其他想到的，也可以一起补充。
```

## Revisit Comparison To Natural Change

Before:

```text
请和上次填答时相比，分别说明你的生活状态、购买习惯和品牌偏好发生了哪些变化。
```

After:

```text
这段时间有什么不一样吗？可以从生活状态、最近常买的东西，或你发现自己变了的地方说起。
```

Use this for returning-wave or longitudinal projects. Keep one clear time anchor if needed, then use "最近" or "这段时间" to avoid sounding like a tracking form.

## Scene Reconstruction

Before:

```text
请描述该次消费场景，包括时间、地点、人物、原因、感受。
```

After:

```text
让我们一起还原一下那次场景吧：大概是什么时候、在哪里、和谁一起？当时为什么会想到它，感觉怎么样？
```

Use "还原一下..." when the research needs details but the question should still feel like a shared recollection.

## Multi-Intent Question To Single Point

Before:

```text
先简单介绍一下你自己吧——你现在在做什么（上学 / 工作 / 其他）？平时的一天大概是怎么度过的？
```

After:

```text
先简单介绍一下你自己吧：你现在在上学、工作，还是其他状态？可以用你觉得最能代表自己的方式说说。
```

If the routine is also needed, move it to a separate daily-rhythm question:

```text
接下来聊聊你平时的一天。通常从早到晚会怎么度过？哪些时间段最固定，哪些比较自由？
```

Do not combine self-introduction and daily routine in one question. A question can go deeper on the same point, but should not ask two different information goals at once.

## Fill-In Diary Trigger

Before:

```text
请记录你今天的饮用行为，包括品牌、场景、原因和心情。
```

After:

```text
今天，我喝了______。当时是什么时间？你正在做什么，为什么想来一杯？
```

Use fill-in triggers sparingly for diary records where a concrete behavior is the entry point.

## Video Process Invitation

Before:

```text
请录制完整过程，并讲解每一步使用的产品、工具、手法和原因。
```

After:

```text
可以边做边和我们说说：你正在用什么、怎么用、为什么这样做。不用太正式，就像给朋友演示一样。
```

For long video tasks, keep only the minimum observation points in the question. Move detailed researcher needs to handoff or follow-up prompts.

## Reason Prompt To Conversation

Before:

```text
请说明原因。
```

After:

```text
为什么这么觉得？是什么让你这么选的？
```

Use reason follow-ups that sound like a real conversation. For scores, ask "为什么打这个分？如果有扣分，扣在哪里？"

## Researcher-Facing Material Value To Respondent Context

Before:

```text
任选其一并说明该素材能帮助我们理解什么。
```

After:

```text
如果方便，可以顺手发一张照片或一段语音，帮我们看看当时的情况。
```

Do not ask respondents to explain the research value of their own materials.

## Gold Sample To Rewrite Pattern

Use historical final DG samples to extract rewrite patterns, not to copy text.

When converting a gold sample into a reusable pattern:

- Remove project-specific category, brand, product, stimulus, audience, and internal labels.
- Keep the respondent-facing move, such as "invite a real moment", "offer optional photo/audio/video", "ask before/during/after", or "soften a hard count".
- Check the pattern against `style_rules.md` first. If it conflicts with fixed templates, brand exposure delay, or burden control, do not use it.
- Prefer a generalized Before/After rule only after seeing the same move across multiple projects.
## skill\dg-question-wording-editor\references\module_tone_guides.md

# Module Tone Guides

Use these guides to tune wording by DG module type.

## About Me / 基础画像

Tone: warm, open, person-first.

Do:

- Understand the respondent as a person before category or brand.
- Ask about life, school/work, space, interests, social life, ideal life, stress, or routine when relevant.
- Preserve fixed opening questions exactly when required.

Avoid:

- Product, brand, category, or research-intent language in the opening.
- Asking the respondent to justify category behavior too early.

## Typical Day / Routine

Tone: descriptive and light.

Do:

- Let respondents paint a day in their own rhythm.
- Ask about weekday/weekend differences, state changes, eating moments, commute, work/study, rest, or social time as relevant.

Prefer:

- "请描画一下你典型的一天吧！通常几点起床、几点休息？从早到晚，一天大概都在忙些什么？"

Avoid:

- "每段用一行写清时间和活动。"
- Turning the task into a mechanical timetable.
- Over-narrow labels like "精神下滑/注意力不集中" when broader state language is enough.

## Returning Wave / 续季回访

Tone: familiar, light, not like a tracking form.

Do:

- Use "很高兴又见面啦", "这段时间", "最近" to create continuity.
- Ask what changed first, then ask for details only where needed.
- Keep one clear time anchor if the research requires comparison.

Prefer:

- "这段时间有什么不一样吗？可以从生活状态、最近常买的东西，或你发现自己变了的地方说起。"

Avoid:

- Repeating "和上次填答时相比" in every question.
- Re-collecting the full About Me profile unless the study requires it.

## Category / Solution Map

Tone: broad, exploratory, not brand-led.

Do:

- Define the broad behavior space once.
- Help respondents recall current solutions, substitutes, storage, sharing, buying, and usage scenes.
- Use scene prompts in a compact way when useful.

Avoid:

- "至少列出 5 种"
- "按优先顺序写 1-3 件"
- Splitting recall prompts into many closed mini-questions.

## Diary Record

Tone: like life recording.

Do:

- Ask what happened, where, with whom, what they did, why, and how it felt before/after.
- Encourage voice, photo, or video to reduce writing burden.
- Keep internal branches invisible to respondents.

Avoid:

- Forcing every record to have a title.
- Requiring a score every time unless truly needed.
- Asking for proof material every time.
- Turning each event into a field-by-field incident report.

Prefer:

- "今天，我____了。"
- "请先说明今天是几月几号、周几；如果一天里发生了好几次，可以在每次记录前写上这是今天第几次。"
- "当时是什么让你想来一下？你正在做什么，和谁在一起？"

## Shopping Task

Tone: natural shopping vlog.

Do:

- Focus on before, during, after: why they started, how they looked, what they noticed, what they chose or gave up, and why.
- Let photos/videos support the journey.

Prefer:

- "请尽量用视频 + 语音记录整个过程，就像给我们拍一段生活 vlog，不需要剪辑。"

Avoid:

- Starting with shelf audit, price audit, promotion list, or display-location checklist unless that is the explicit research focus.

## Scene / Space / Material Showing

Tone: show-and-tell, relaxed, low perfection pressure.

Do:

- Use "带我们看看", "云参观", "用你的眼睛带我们看一看", or "还原一下当时的场景" when the project tone allows.
- Add a low-pressure line for photos or videos: "不用刻意摆太整齐，真实状态就好。"
- Split "show material" from "explain reasons" when both are heavy.

Avoid:

- "请录制并上传完整高清视频。"
- Asking respondents to explain why the material is useful to researchers.
- Overusing playful labels such as "云参观" or "小时刻" in serious or older-audience projects.

## Habit / Journey

Tone: reflective but concrete.

Do:

- Ask for first memory, triggers, repeated use, interruption, recovery, switching, and role in life.
- Let respondents choose personally meaningful examples.

Avoid:

- Abstract "habit mechanism" language in respondent-facing wording.

## State / Feeling Moments

Tone: concrete, human, not diagnostic.

Do:

- Ask for real moments before asking for reasons or coping methods.
- Split broad state changes into easier prompts, such as "什么时候最有精神？" and "什么时候会有点累或卡住？"

Avoid:

- Starting with abstract labels like "精神下滑", "注意力不集中", or "效率下降" unless they are client-mandated terms.

## Brand / Product / Stimulus

Tone: late-stage, intuitive, non-judgmental.

Do:

- Ask first impressions, mental images, real-life scenes, fit/non-fit, and expectations.
- Keep stimulus tasks clear but not over-explained.

Avoid:

- Leading respondents toward the client's preferred answer.
- Using brand strategy language as if respondents should understand it.

## Object Inventory / Family Photo

Tone: show-and-tell, curious, complete but not audit-like.

Do:

- Invite respondents to show the whole object system first, then explain storage, classification, and favorite/most-used examples.
- Use warm labels such as "family photo" only when the audience and category can carry a light tone.
- Encourage photos first when the layout, storage, categories, or object appearance matters.
- Ask why they classify or place objects that way; the classification logic is part of the insight.

Avoid:

- Assuming all objects are in one obvious place, such as only a bag, desk, or hand.
- Asking only about the target object when adjacent objects define the respondent's category world.
- Turning the inventory into a shelf audit unless that is the research goal.

## Bounded Product Imagination

Tone: imaginative but anchored.

Do:

- Give the respondent a clear design direction before asking for ideal or future products.
- Anchor imagination in self-expression, carrying every day, gifting, long-term use, solving a current problem, or another proposal-backed direction.
- Invite pictures when the respondent describes visual style, form, role, metaphor, or examples that are hard to picture.

Avoid:

- Fully open "future product" questions that let answers fly into unrealistic or non-actionable ideas.
- Asking abstract innovation questions before current criteria, pain points, and emotional roles have been explored.
## Product Innovation / Future Product

Tone: imaginative, specific, and bounded.

Do:

- Start with current scenes, current criteria, or a concrete pain point before asking future product questions.
- Use bounded imagination: for this scene, for this problem, for daily carrying, for self-expression, for gifting, for long-term use.
- Ask for references or photos when the respondent talks about look, form, sensory feeling, or ideal product examples.
- Translate abstract standards into concrete details the respondent can describe.

Avoid:

- Fully open future-product questions before current usage and criteria are clear.
- Asking for innovation ideas that have no link to real scenes or needs.
- Philosophical category-meaning questions without metaphor, examples, or classification anchors.
## skill\dg-question-wording-editor\references\wording_eval_rubric.md

# Wording Evaluation Rubric

Score each dimension from 1 to 5.

## 1. Respondent Naturalness

Checks:

- sounds like a human Diary task
- easy to understand
- not overly academic or researcher-facing
- module intros and endings feel natural
- preserves already-good designer wording instead of flattening it
- avoids repeated "请问/请描述/请说明" starts when invitation verbs would be more natural
- uses conversational follow-ups such as "为什么这么觉得" instead of researcher prompts like "请说明原因"

## 2. Openness

Checks:

- allows real personal answers
- does not over-prescribe examples
- avoids hidden answer options
- preserves open-ended discovery when needed
- keeps one question focused on one core information point unless follow-ups deepen the same point

## 3. Burden Control

Checks:

- avoids unnecessary counts, rankings, scoring, or repeated uploads
- uses media to reduce writing pressure
- keeps daily diary tasks manageable
- matches respondent age, sensitivity, and context
- separates heavy media capture from detailed explanation when both are requested
- avoids asking respondents to explain the research value of their own materials

## 4. Specificity Quality

Checks:

- asks for real moments, scenes, people, actions, before/after changes, and reasons
- avoids generic attitude questions
- avoids forced narrow labels when broader language is better
- uses scene reconstruction, real-moment prompts, or fill-in diary triggers when useful
- uses "都可以 / 都算在内" style widening instead of long example lists when appropriate

## 5. Brand And Intent Control

Checks:

- early modules do not expose client brand or product intent too soon
- internal brand branches remain hidden in respondent wording
- brand/stimulus questions appear at an appropriate stage

## 6. Research Preservation

Checks:

- rewrite preserves original research intent and observation points
- no major module/question is silently deleted
- task logic, Diary vs IDI split, and client constraints remain intact
- required media, scores, classifications, and platform actions remain clear when they are truly mandatory
- natural audience-appropriate tone from the designer draft is not unnecessarily neutralized

## 7. Fixed Template Compliance

Checks:

- About Me opening questions are exact when required
- fixed client wording is preserved unless user asked to change it

## 8. Technical Cleanliness

Checks:

- no raw HTML tags, empty titles, test text, or "未命名模块" appear in respondent-facing wording
- no internal labels such as trigger/action/alternative, researcher notes, or analysis terms leak into questions
- platform-required formatting is rendered or converted into readable plain text

## Gap Labels

Use:

- `too_checklist_like`
- `too_commanding`
- `too_many_parentheses`
- `too_many_examples`
- `too_quantified`
- `too_generic`
- `too_specific_in_a_forced_way`
- `respondent_burden_too_high`
- `brand_or_intent_exposed_too_early`
- `internal_logic_exposed`
- `fixed_template_violation`
- `research_intent_drift`
- `repeated_please_starts`
- `checklist_connector_overuse`
- `researcher_facing_material_value`
- `html_or_placeholder_visible`
- `returning_wave_too_formal`
- `media_and_explanation_overstacked`
- `over_rewritten`
- `tone_flattened`
- `multi_intent_question`
```

---

## Message 2: user

```text
# Designer draft to rewrite

# KACO 笔类大单品机会探索 — 第一版题目设计方案

---

## 一、项目理解

1. **客户是 KACO（笔类品牌）**，已通过礼盒升级与 IP 联名实现阶段性增长，但现有增长路径天花板显现，需要寻找下一个增长方向。
2. **商业目标**：研判未来三年具备"国民级大单品"潜力的新品类/新产品方向，支撑品牌长期增长。
3. **市场背景**：笔类进入存量竞争，基础书写被电子化和 AI 持续分流；同时新品爆炸、消费端"买得多换得快闲置率高"。
4. **核心人群**：05 后/10 后新一代学生（公立高中、职高、国际高中等不同路径）、年轻白领；需关注男性增量和圈层先锋趋势信号。
5. **已有洞察线索**（来自 Proposal 桌面研究，非一手验证）：从"一支主力笔用到底"到"多支笔服务多场景多心情"；笔的身份表达功能增强；把玩乐趣、机械结构、周边配件等新维度出现。
6. **研究方法**：Digital Diary（数字日记本），需在自然状态下捕捉生活场景、书写行为和笔类消费的真实图景。

---

## 二、核心研究问题

| 编号 | 研究问题 |
|------|---------|
| RQ1 | 目标人群的日常生活、兴趣世界与审美偏好是什么样的？代际变化如何体现在他们与"物"的关系上？ |
| RQ2 | 书写在他们生活中扮演什么角色？哪些场景在增长、哪些在萎缩、哪些是新出现的？ |
| RQ3 | 他们拥有什么样的笔？怎么来的、怎么用的、怎么看待自己和笔的关系？ |
| RQ4 | 他们选笔的逻辑是什么？信息来源、决策标准、价格敏感度如何？ |
| RQ5 | 什么样的笔/文具产品能让他们兴奋？在非刚需但有规模的品类方向中，机会空间在哪里？ |

---

## 三、模块结构总览

| 模块 | 模块名称 | 模块目的 | 对应研究问题 | 设计理由 |
|------|---------|---------|-------------|---------|
| 1 | 我和我的世界 | 建立受访者画像：生活状态、兴趣圈层、审美偏好、与"物"的关系 | RQ1 | 基础画像模块，先理解人本身，不急于关联产品 |
| 2 | 我的一天 | 记录典型一天的场景流，自然捕捉笔/书写出现的时刻与缺位的时刻 | RQ1, RQ2 | 场景记录任务，获取行为层事实而非态度层回忆 |
| 3 | 我什么时候会拿起笔 | 理解书写场景的全貌、变化趋势、笔不可替代的价值 | RQ2 | Proposal 已有"书写被分流"的桌面判断，此模块获取一手场景数据并识别增长场景 |
| 4 | 我的文具全家福 | 了解当前笔的持有、使用状态、情感关系与周边生态 | RQ3 | 通过拍照任务获取真实持有情况，避免回忆偏差 |
| 5 | 我是怎么选笔的 | 还原购买决策路径、信息来源、评价标准、品牌认知 | RQ3, RQ4 | 从最近一次真实购买切入，比泛问"你看重什么"更有效 |
| 6 | 我的下一支笔 | 捕捉未满足需求、理想产品想象、品类兴趣方向 | RQ4, RQ5 | 指向商业目标——识别国民级大单品的机会方向 |

---

## 四、详细题目设计

### 模块 1：我和我的世界

**引导语：**
Hi～欢迎来到这次对话！在正式开始之前，我们想先认识一下真实的你。没有标准答案，怎么想就怎么说～

**题目：**

1. 先来个自我介绍吧！你现在是学生还是已经工作了？在哪个城市？平时的日常大概是什么节奏？
2. 除了上课/上班，你最近花时间最多的事情是什么？
3. 你最近最沉迷或最投入的兴趣爱好/圈子是什么？它吸引你的点是什么？方便的话可以分享一些相关的图片。
4. 你平时喜欢逛什么平台或 App 来消磨时间、找乐子或找灵感？最近有被种草什么东西吗？
5. 如果让你用 3 个关键词形容自己的审美偏好或个人风格，你会选哪 3 个？

**结束语：**
谢谢你的分享！接下来我们想请你记录一下真实的一天。

---

### 模块 2：我的一天

**引导语：**
请选一个上学日/工作日，从早到晚记录一下你这一天是怎么度过的。不用写得很详细，像流水账一样记就好～

**题目：**

1. 请大致记录一下你今天从起床到睡觉的主要活动和时间安排。
2. 今天有没有哪个时刻你拿起了笔？是在什么情况下拿起来的？写了/画了什么？
3. 今天有没有哪个时刻，你本来可能会用笔，但最后用了手机、平板或电脑来完成？是什么情况？
4. 拍一张你今天随身带的文具（笔袋、铅笔盒，或者散落在包里桌上的笔）给我们看看吧，并简单说说都有些什么。

**结束语：**
辛苦啦！接下来我们聊聊你跟"写写画画"这件事的关系。

---

### 模块 3：我什么时候会拿起笔

**引导语：**
不管是认真做笔记、写作业，还是随手涂鸦、列清单，甚至只是拿着笔转一转——所有你会拿起笔的时刻，我们都感兴趣。

**题目：**

1. 想一想，你平时在哪些场景下会用到笔？请尽量多列一些，越具体越好。
2. 这些场景里，哪个是你最频繁的？哪个是你做起来最享受的？（可能不是同一个，都说说看。）
3. 跟你一两年前比，你用笔的场景有没有什么变化？变多了还是变少了？你觉得是因为什么？
4. 在你看来，用笔写/画跟用电子设备相比，最大的不同在哪里？有没有什么事情是你觉得一定要用笔才行的？
5. 你有没有什么跟笔有关的小习惯或"仪式感"？比如考试换新笔芯、写手帐必须用某支笔、无聊的时候就喜欢转笔之类的。

**结束语：**
了解了你的书写时刻，接下来我们来看看你现在手边都有些什么笔～

---

### 模块 4：我的文具全家福

**引导语：**
来一个有趣的任务——把你目前手边所有的笔都找出来，给它们拍一张"全家福"吧！

**题目：**

1. 请拍一张你目前手边所有笔的合照，并数一数大概有多少支，分别是什么类型的笔。
2. 从里面挑出你最喜欢的 1–2 支，拍个特写，告诉我们它为什么是你的最爱。
3. 有没有哪支笔你买了但很少用、甚至根本没用过？当时为什么买了，后来为什么不用了？
4. 你大概多久会买一次新笔？一般在什么情况下会想买新的？
5. 除了笔本身，你有没有跟笔相关的配件或周边？（比如笔袋、笔挂、替换芯、挂件、笔架之类的。）有的话也拍来看看吧。

**结束语：**
看到你的笔家族了！接下来我们聊聊你平时是怎么挑笔的。

---

### 模块 5：我是怎么选笔的

**引导语：**
每个人选笔都有自己的偏好和门道，有人看颜值，有人看手感，有人随缘。来聊聊你的选笔逻辑吧～

**题目：**

1. 回想一下你最近一次买笔的经历：买的是什么笔？在哪里买的？为什么选了这一支（或这几支）？
2. 你在挑一支笔的时候，一般最在意的是什么？最不在意的又是什么？
3. 你一般是怎么知道/发现一支新笔的？会在哪些渠道看到相关信息或推荐？
4. 你有没有特别喜欢或会主动关注的笔的品牌？为什么喜欢它？
5. 你觉得一支日常用的笔大概多少钱是你比较舒服的价格？超过多少钱你就会犹豫或者觉得不值？
6. 你最近有没有看到过什么让你觉得"这支笔好酷/好想要"的笔或文具？是在哪里看到的？它哪里吸引了你？

**结束语：**
了解了你的选笔方式，最后一个部分我们来畅想一下～

---

### 模块 6：我的下一支笔

**引导语：**
最后来聊一些轻松的。关于"下一支笔"，我们想听听你的想象和期待。放飞想象力，怎么天马行空都可以！

**题目：**

1. 如果可以完全按你的想法定制一支笔，你希望它是什么样的？（外观、颜色、手感、功能……随便从哪个角度描述都行，愿意画出来也欢迎！）
2. 你觉得现在市面上的笔，最让你觉得遗憾或"要是能……就好了"的地方是什么？
3. 除了你日常在用的那类笔，你有没有对其他类型的笔产生过兴趣或好奇？（比如马克笔、彩墨笔、秀丽笔、自动铅、速写笔、手工笔等等。）对它们感兴趣或不感兴趣的原因是什么？
4. 你觉得一支笔在什么样的情况下，会变得对你特别有意义、不只是一个写字工具？
5. 如果明天有一款笔突然在你身边火了，同学/同事都在讨论、都想要，你觉得它可能是什么样的？大家会因为什么原因讨论它？

**结束语：**
所有的问题都回答完啦！非常感谢你认真、真实的分享，你的每一个回答对我们都很有价值。后续如果有进一步交流的机会，我们再联系你～

---

## 五、Wording Handoff

| 维度 | 内容 |
|------|------|
| **目标人群语气注意** | 受访者涵盖 05 后/10 后学生及年轻白领，年龄跨度较大。整体语气应口语化、轻松、有对话感；对低龄受访者（初高中生）避免使用"消费逻辑""价值期待"等成人化/研究型用语；"～"和语气词可适当使用但不宜过密。 |
| **不能改动/删除** | ① 模块 4 的拍照"全家福"任务（核心行为证据，不可替换为纯文字描述）；② 模块 2 第 3 题"本来可能用笔但用了电子设备"的反向追问（捕捉书写替代场景）；③ 模块 6 第 3 题对非日常笔类品类的开放探索（直接服务于品类机会方向的研究目标）。 |
| **需要延后暴露的品牌/产品/刺激物** | KACO 品牌名在整份日记中不出现。Proposal 中提到的具体趋势标签（秀丽笔、爆闪马克笔、手作水晶笔等）仅在模块 6 第 3 题作为品类举例出现，不作引导；如有后续 IDI 环节，品牌认知与具体产品概念测试应留到那时。 |
| **需要保留的观察点** | ① 模块 2 中笔出现的自然时刻 vs 被电子设备替代的时刻（场景增减的行为证据）；② 模块 4 中"买了但不用"的笔及原因（闲置逻辑）；③ 模块 4 中笔的周边配件持有情况（周边生态信号）；④ 模块 5 第 6 题"最近让你眼前一亮的笔"（自发提及的品牌/产品可作为竞品信号）。 |
| **可能过重或过硬的题面** | ① 模块 3 第 4 题"用笔 vs 电子设备最大不同"——对低龄受访者可能偏抽象，建议 wording editor 评估是否需要加入具体场景提示；② 模块 6 第 5 题"明天爆款"的假设——措辞略带引导，需要确保不暗示"爆款=好"的前提。 |
| **建议交给 dg-question-wording-editor 处理** | ① 所有模块引导语和结束语的语气统一调性，确保对 05 后学生和年轻白领都自然；② 模块 1 第 5 题"3 个关键词形容审美偏好"——任务形式对部分受访者可能偏难，评估是否需要提供参考词库或改为开放描述；③ 模块 5 第 2 题"最在意/最不在意"——评估是否需要提供选项列表辅助回答，还是保持纯开放；④ 模块 6 第 1 题"定制一支笔"——确认是否需要提供维度提示（已在括号中给出一些），或让受访者完全自由发挥。 |

---

## 六、Agent 检核摘要

1. **品牌保护**：全篇未出现 KACO 品牌名，模块 5 第 4 题品牌提及为受访者自发回忆，不存在品牌暗示风险。
2. **提问层次**：人 → 日常 → 书写场景 → 笔的持有 → 选择逻辑 → 未来期待，逐层聚焦，基础画像模块未过早引入产品/品牌关联。
3. **已知不重复**：Proposal 桌面研究中的趋势信号（多笔多场景、身份表达、把玩乐趣等）作为分析框架储备，未直接变成引导性提问；模块设计旨在获取一手场景与行为数据来验证和深化这些线索。
4. **题量风险**：全篇共 30 题（含 4 道拍照任务），若为单日填写可能偏重；建议确认日记天数和分模块节奏后，由 wording editor 评估是否需拆分。
5. **品类探索覆盖**：模块 6 第 3 题覆盖了马克笔、秀丽笔等 Proposal 关注的非书写笔品类，但举例列表不宜过长以免变成引导；当前列举 6 个品类，可视受访者年龄段微调。

---

## 七、需要确认的问题

1. **受访者构成与配额**：Proposal 提到 05 后/10 后学生、年轻白领、男女性别、不同教育路径（公立/职高/国际高中），但未明确具体配额和筛选条件——是否需要在日记前设计筛选题？不同人群是否使用同一套题目？
2. **日记天数与填写节奏**：当前 6 个模块共 30 题，是设计为一次性填写，还是分多天（如 3–5 天）分批推送？这影响模块拆分方式和单日题量控制。
3. **是否有后续 IDI/座谈会环节**：如有后续深度访谈，部分深度追问（如品牌认知、具体产品概念反馈、KACO 相关刺激物测试）可留到后续环节，当前日记聚焦自然行为捕捉；如无后续环节，可能需要在日记中增加品牌与概念相关模块。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构和已经自然的受访者表达。只改写确实存在问题的引导语、题目、结束语和素材请求；不要全量重写。
```
