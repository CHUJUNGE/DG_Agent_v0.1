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
- "打分 1-5"
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
- For looped / repeated daily diary recording modules, use this fixed ending exactly: "恭喜你完成今天的填答，辛苦啦！祝你度过了美好的一天～"
- For heavy media or long modules, acknowledge the concrete effort: recording a day, showing objects, uploading a process, or completing a shopping task.
- For the final module, a short thank-you and optional supplement invitation is enough.
- Preserve a designer ending if it is short, concrete, and fits the respondent tone.

Avoid repeated AI-host style endings:

- "谢谢你让我们走进你的生活/内心/故事"
- "你的分享非常重要"
- "这些内容对我们理解消费者/市场/品牌机会很有帮助"
- "接下来我们会研究/分析/识别..."
- Repeating "感谢你的认真分享，接下来..." after every module.

When an ending mentions the next module, make it respondent-facing and concrete. Say "下面从每天最常发生的喂食开始看" instead of "接下来我们想了解你的喂食行为和选择逻辑".

### Preserve Appropriate Audience Tone

Do not automatically remove:

- "～" or "啦" when used sparingly and appropriate for a younger sample;
- light expressions such as "上头", "种草", or "踩雷" when they fit the category and audience;
- concrete, vivid phrasing from the designer draft.

Adjust them only when:

- the sample includes older or formal respondents and the tone would feel off;
- every sentence uses the same playful marker;
- the expression distracts f

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

# 题目设计方案

## 1. 项目理解

- **项目名称**：Empowering 45+ Healthy Aging Pursuit
- **品类/品牌**：VMS（维生素、矿物质及补充剂）/ Reckitt 旗下 Movefree、Megared、Neuriva、Schiff；重点探索骨关节和心脏健康以外的品类机会
- **目标人群**：45 岁以上中国消费者（核心 45-60 岁，含部分 60+），以 70 后为主体代际
- **商业问题**：在 45+ 核心人群中拓展 VMS 品类增量——找到"在哪里打"（品类切入机会）和"怎么赢"（信任与沟通路径），为新品牌 Schiff 上市提供方向
- **研究目标**：系统理解 45+ 人群对"健康老龄化"的认知、生活方式、身体变化、健康实践与健康产品信任机制，识别未满足的健康需求和品类机会
- **关键设计依据**：Proposal 明确为两阶段研究，Phase 1 为 Digital Diary + 入户/IDI；Diary 收集生活事实、健康行为和即时记录，IDI/入户深挖信任机制和深层动机；目标人群年龄偏大，需控制题量和文字负担

## 2. 核心研究问题

1. 45+ 消费者如何定义"健康地老去"？他们的认知从"抗衰老"到"活力长寿"经历了怎样的变化？最大的担忧是什么？
2. 这些期待和担忧如何塑造了他们的日常生活方式？时间精力投入在哪里？哪些生活场景与健康需求高度相关？
3. 他们如何感知自己的身体变化和健康信号？在什么场景下意识到自己"没有在健康地老去"？
4. 他们目前采用哪些健康解决方案（产品、设备、服务、食补、习惯）？如何知道的？为什么信任？
5. 在骨关节和心脏健康之外，哪些健康方向（睡眠、免疫、脑健康、消化、眼部等）存在未满足需求和品类进入机会？
6. 健康产品的信任如何建立、维持和中断？什么条件下愿意尝试新品牌或新品类？

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 |
|------|----------|-------------|
| 模块1：我和我的生活 | 理解受访者作为"人"的生活状态、角色、兴趣和人生阶段，为后续健康需求提供生活底色 | Q1、Q2 |
| 模块2：我的一天 | 捕捉日常节奏、时间精力分配、与健康相关的生活场景和状态变化 | Q2、Q3 |
| 模块3：我的身体和健康 | 理解身体变化感知、健康标准、健康担忧、关键健康信号和触发场景 | Q1、Q3、Q5 |
| 模块4：我的健康解决方案 | 下载完整健康解决方案图谱（产品、设备、服务、食补、习惯），理解选择逻辑和信息来源 | Q4、Q5 |
| 模块5：我信任的健康产品 | 深挖口服健康产品/保健品的信任建立、效果判断、安全感、品牌比较和忠诚条件 | Q4、Q6 |
| 模块6：我的健康生活记录（4天日记） | 实时记录日常生活、身心状态、饮食、健康行为和健康相关触点 | Q2、Q3、Q4、Q5 |
| 模块7：我的健康期待 | 收尾模块，回顾健康老龄化的理想状态和未满足需求 | Q1、Q5 |

## 4. 详细题目设计

---

### 模块1：我和我的生活

**引导语：**
欢迎你加入我们的生活记录之旅！在接下来的几天里，我们想通过你的眼睛，了解你的生活、你的日常和你的故事。没有标准答案，你怎么想就怎么说。我们先从认识你开始吧～

**题目：**

1. 先和我们打个招呼吧！简单介绍一下你自己——你在哪个城市生活？家里都有谁？平时和谁住在一起？
   - 可以拍一张你觉得能代表你现在生活状态的照片，配上几句话。

2. 你现在的生活重心是什么？每天的时间和精力主要花在哪些事情上？

3. 你平时最喜欢做什么？有什么兴趣爱好或者让你特别投入的事情？

4. 你平时最常和谁在一起？和家人、朋友、同事的相处方式是怎样的？

5. 你平时主要通过什么渠道获取信息和资讯？比如看什么 App、关注什么内容、听谁的推荐比较多？

6. 回顾过去几年，你觉得自己的生活发生了哪些比较大的变化？这些变化给你带来了什么感受？

7. 如果往前看未来两三年，你最期待的事情是什么？最担心的事情又是什么？

**结束语：**
谢谢你的分享！接下来我们聊聊你平时一天是怎么度过的。

---

### 模块2：我的一天

**引导语：**
每个人的一天都不太一样。我们想了解你平时一天大概是怎么过的，不需要事无巨细，说说大致的节奏和感受就好。

**题目：**

8. 请描述一下你平时一个普通工作日的一天——从早上起来到晚上睡觉，大概的节奏是怎样的？什么时候比较忙，什么时候比较放松？

9. 你的休息日通常怎么过？和工作日最大的不同是什么？

10. 在一天当中，你觉得自己精力最好的时候是什么时候？最容易感到疲惫或者不舒服的时候呢？

11. 你平时的三餐大概是怎么安排的？自己做饭多还是在外面吃多？有没有什么饮食上特别注意的地方？

12. 你平时有运动或者锻炼的习惯吗？一般做什么运动？大概多久一次？

**结束语：**
了解了你的日常节奏，接下来我们聊聊你的身体和健康。

---

### 模块3：我的身体和健康

**引导语：**
随着年龄的变化，每个人对身体和健康的感受都不太一样。我们想听听你真实的感受和想法，没有对错之分。

**题目：**

13. 你觉得自己现在的身体状态怎么样？如果用几个词来形容，你会怎么说？

14. 和三五年前相比，你觉得自己的身体有哪些明显的变化？这些变化是什么时候开始注意到的？

15. 你有没有一些反复出现的小毛病或者身体上的不舒服？比如睡眠、消化、关节、眼睛、记忆力、精力等方面。说说具体的情况。

16. 在什么样的场景或时刻，你会特别强烈地意识到"我的身体不如以前了"或者"我需要更注意健康了"？能举一两个具体的例子吗？

17. 你心目中"健康地老去"是什么样子的？你觉得怎样才算是在"健康地变老"？

18. 你觉得自己现在离"健康地老去"这个状态有多远？哪些方面做得还不错，哪些方面还有差距？

19. 说到"变老"这件事，你最担心的是什么？最不想发生的事情是什么？

**结束语：**
谢谢你这么坦诚的分享。接下来我们聊聊你平时都用什么方式来照顾自己的健康。

---

### 模块4：我的健康解决方案

**引导语：**
每个人照顾自己健康的方式都不一样——有人靠运动，有人靠饮食，有人吃保健品，有人看中医。我们想了解你的完整"健康方案"。

**题目：**

20. 请拍一张你家里目前在用的健康相关产品的"全家福"——包括保健品、营养补充剂、中药/中成药、健康食品、健康设备等，凡是你觉得和健康有关的都算。拍完后简单介绍一下都有什么。

21. 在这些产品里，哪些是你每天都在用的？哪些是偶尔用的？哪些买了但其实没怎么用？

22. 除了这些产品，你还有没有其他照顾健康的方式？比如食补、养生习惯、定期体检、理疗、中医调理、健康类 App 等。

23. 你现在的这些健康方式，主要是为了解决什么问题或者满足什么需求？

24. 你是怎么知道这些产品或方法的？谁推荐的？还是自己查的？什么信息让你决定试一试？

25. 有没有什么健康方面的需求，你觉得现在的方法还不太能满足，或者还没找到合适的解决方案？

**结束语：**
了解了你的健康方案全貌，接下来我们想更深入地聊聊你对健康产品的信任。

---

### 模块5：我信任的健康产品

**引导语：**
选择健康产品，尤其是吃进嘴里的保健品和营养补充剂，信任特别重要。我们想听听你在这方面的真实经历和想法。

**题目：**

26. 你还记得自己第一次开始吃保健品或营养补充剂是什么时候吗？当时是什么情况让你决定开始吃的？

27. 刚开始吃的时候，你有没有什么犹豫或者担心？比如怕没效果、怕有副作用、不知道该选什么。

28. 你是怎么判断一个保健品有没有效果的？有没有什么具体的感受或者指标让你觉得"这个东西确实有用"？

29. 在你心里，什么样的保健品或品牌会让你觉得比较安心、比较靠谱？是什么让你产生这种信任感？

30. 你有没有吃过一段时间后停掉的保健品？为什么停了？

31. 如果有一个你没听过的新品牌推出了保健品，什么条件下你会愿意试一试？什么情况下你完全不会考虑？

32. 你身边的家人或朋友在吃保健品这件事上，会互相影响吗？你们之间会怎么交流这方面的信息？

**结束语：**
非常感谢你的分享！从明天开始，我们进入生活记录环节，请你记录几天的真实生活。

---

### 模块6：我的健康生活记录（4天日记）

**引导语：**
接下来的 4 天，我们想请你每天花一点时间，记录你当天的生活和健康相关的事情。不需要写很多字，拍照片、录语音、拍短视频都可以，怎么方便怎么来。

**题目：**

33. 今天过得怎么样？用一两句话或者一张照片描述一下你今天的状态和心情。

34. 今天你的身体感觉如何？有没有什么不舒服的地方，或者觉得状态特别好的时候？

35. 今天三餐吃了什么？有没有特别注意什么，或者吃了什么你觉得对健康有好处的东西？可以拍照记录。

36. 今天有没有吃保健品、营养补充剂或者其他健康产品？吃了什么？什么时候吃的？

37. 今天有没有做什么和健康有关的事情？比如运动、泡脚、按摩、体检、看医生、食补等。

38. 今天有没有看到、听到或者和别人聊到什么和健康有关的信息？比如朋友推荐、短视频、文章、广告等。如果有，是什么内容？你怎么看？

39. 今天有没有什么时刻让你特别想到"健康"这件事？是什么触发了这个想法？

**结束语（每日）：**
恭喜你完成今天的填答，辛苦啦！祝你度过了美好的一天～

---

### 模块7：我的健康期待

**引导语：**
经过这几天的记录和分享，最后我们想听听你对未来健康生活的期待。

**题目：**

40. 经过这几天的记录，你对自己的健康状况有没有什么新的感受或者发现？

41. 如果可以许一个和健康有关的愿望，你最希望解决的健康问题是什么？为什么这个问题对你来说最重要？

42. 你觉得理想的健康产品应该是什么样的？可以从效果、形式、使用方式、价格、品牌等任何角度来说。

43. 有没有什么你听说过但还没尝试的健康方式或产品，你挺想试试的？是什么让你感兴趣？又是什么让你还没行动？

**结束语：**
所有的记录到这里就结束了！非常感谢你这几天的用心分享，你的每一个回答对我们都很有价值。祝你健康快乐！

---

## 5. Wording Handoff

- **目标人群语气注意**：受访者以 45-60 岁为主，含部分 60+。文字表达应温和、尊重、不居高临下；避免过于年轻化的网络用语；鼓励使用照片、语音、短视频降低文字负担。
- **不能改动/删除**：
  - 模块3 中关于身体变化感知、健康信号触发场景的题目（Q14、Q16）——这是连接生活方式与品类机会的关键链路。
  - 模块5 中信任机制的完整链路（Q26-Q31：first entry → 犹豫 → 效果判断 → 安全感 → 中断 → 新品牌接受条件）。
  - 模块4 中"全家福"素材采集题（Q20）——后续模块引用此素材。
  - 日记模块每日结束语固定为"恭喜你完成今天的填答，辛苦啦！祝你度过了美好的一天～"。
- **需要延后暴露的品牌/产品/刺激物**：Reckitt、Movefree、Megared、Neuriva、Schiff 等品牌名不得在 Diary 中出现；如有刺激物测试，应放在 IDI/入户环节。
- **需要保留的观察点**：
  - 生活角色与人生阶段变化（模块1）
  - 身体信号与触发场景（模块3）
  - 完整健康解决方案图谱，不限于保健品（模块4）
  - 信任建立全链路（模块5）
  - 日记中健康信息触点和社交影响（模块6 Q38）
- **可能过重或过硬的题面**：
  - Q20 全家福拍摄任务——对部分 60+ 受访者可能有操作负担，wording agent 可补充"拍不全没关系，拍你手边能看到的就行"。
  - Q26-Q31 信任链路连续 6 题——题面可适当口语化、降低"访谈感"，但链路不能压缩。
  - 日记模块每天 7 题——对 45+ 人群属中等负担，wording agent 可在引导语中强调"简单记录即可，不需要写很多"。
- **建议交给 dg-question-wording-editor 处理**：
  - 全卷题面的口语化和自然化处理。
  - 模块1 开场题的语气温度调整。
  - 日记模块引导语的轻量化表达。
  - 各模块过渡语的自然衔接。
  - 检查是否有题面仍偏"问卷感"或"checklist 感"的地方。

## 6. Agent 检核摘要

- **已对照商业问题与 Proposal 检核**：全部 6 个核心研究问题均有对应模块和题目覆盖；Proposal 中"健康老龄化认知 → 生活方式 → 健康标准与痛点 → 解决方案 → 信任机制"的链路完整。
- **品牌暴露控制**：全卷未出现 Reckitt 及旗下任何品牌名、slogan 或定位语；品牌/刺激物测试建议放入 IDI/入户。
- **素材复用**：模块4 Q20 集中采集健康产品全家福，后续 Q21、Q23 引用该素材追问，未重复要求拍摄。
- **负担控制**：全卷约 43 题（含 4 天日记 ×7 题 = 28 题 + 基础模块 15 题 + 收尾 4 题），日记每日 7 题，对 45+ 人群属可接受范围；已在 handoff 中标记高负担风险点。
- **Diary vs IDI 分工**：Diary 聚焦生活事实、行为记录、浅层 why 和即时感受；深层信任机制追问（如品牌人格化、跨品类信任迁移、复杂概念测试）留给 IDI/入户。

## 7. 需要确认的问题

1. **日记记录天数与工作日/休息日分配**：当前方案设计为 4 天日记，未强制区分工作日和休息日。是否需要明确要求至少包含 1 个工作日和 1 个休息日？还是由受访者自然记录即可？
2. **健康方向聚焦程度**：Proposal 提到需识别骨关节和心脏健康以外的品类机会（睡眠、免疫、脑健康、消化、眼部等）。当前方案采用开放式探索，未预设具体健康方向。是否需要在模块3 或模块7 中加入对特定健康方向的定向追问？
3. **IDI/入户的具体承接范围**：当前方案将深层信任机制、品牌人格化和刺激物测试留给 IDI/入户。是否已确认 IDI/入户的执行安排？如果 IDI 不确定能覆盖所有受访者，是否需要在 Diary 中适当加深信任模块？

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构和已经自然的受访者表达。只改写确实存在问题的引导语、题目、结束语和素材请求；不要全量重写。
```
