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
- the expression distracts from the task;
- the client or project requires a more restrained tone.

## Technical And Placeholder Hygiene

Respondent-facing wording must not expose raw platform or draft artifacts:

- HTML tags such as `<b>`, `<strong>`, `<div>`, or `<br>`.
- "未命名模块", empty titles, test text, or placeholders.
- Internal logic labels such as "trigger -> action -> alternatives".
- Researcher-facing material value requests such as "说明该素材能帮助我们理解什么".

## Brand And Intent Exposure

Early modules should start from the respondent's life, routine, scenes, current solutions, and feelings.

Do not expose brand, product, stimulus, or client strategy too early. Brand/product questions usually belong after natural behavior and cat

[...中间内容因长度限制已省略，生成时请基于已保留的开头和结尾信息判断；如信息不足，应在研究员确认点中说明...]

is your rest day different from your workday." Ask directly for the rest-day pattern, places, activities, and category-relevant touchpoints.

### Avoid yes/no prompts when the recruited sample will obviously say yes

If the sample is recruited for category involvement, avoid questions such as "Do you have a favorite X?" Go directly to concrete selection and explanation, such as choosing a few representative items and explaining why.

### Keep parenthetical probes light but useful

Parentheses are acceptable when they help the respondent recall dimensions they might otherwise miss. Keep them short, avoid long commercial taxonomies, and do not make examples feel like fixed answer options.

### Media wording should prefer photos when photos are analytically better

For object family photos, storage/classification, ideal products, visual evaluation standards, or metaphors, encourage photos first. Allow video only when it is easier for the respondent or when the task needs movement/process.

Use low-pressure language: photos are helpful, real state is fine, and text or voice can supplement when needed.
## Product Innovation Wording Rules v0.1.3

Use these wording rules when the designer handoff says the project is about product innovation, product upgrade, new product opportunity, or concept direction.

### Start future questions from a concrete anchor

Do not ask only:

- "What should the future product be like?"
- "What is your ideal product?"
- "What new functions do you want?"

Rewrite future questions around a concrete anchor:

- a specific scene;
- a specific pain point;
- a product the respondent would carry or use every day;
- a product that represents the respondent;
- a product suitable for gifting or sharing;
- the only product they could keep using for the next few years.

### Turn vague criteria into sensory and use details

When respondents are asked about "good-looking", "easy to use", "safe", "useful", or "worth buying", help them describe what that means in concrete terms.

Use prompts such as:

- "What does good-looking mean to you here? Color, shape, material, size, or another detail?"
- "What makes it easy to use in the actual moment?"
- "What details would make you feel reassured?"
- "Can you show or describe a reference that feels close?"

Keep examples light and category-relevant.

### Use references and images for product form

When the question asks about product appearance, form, sensory feeling, ideal examples, or evaluation standards, encourage reference images first. Text or voice can explain why those references work.

### Make metaphor answerable

Metaphor questions should not sound philosophical. Anchor them in familiar language:

- "If this product were like someone in your life, who would it be?"
- "Is it more like a tool, a companion, an accessory, a collection, or something else?"
- "What would you hope it becomes in your life?"

Avoid abstract wording such as "please explain the symbolic meaning of this category."
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
今天的记录完成啦，辛苦。明天继续按真实发生的时刻来写就好。
```

Use for daily or repeated diary tasks. Confirm completion and remind the next action instead of giving a generic compliment.

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

1. **客户身份与目标：** KACO 是笔类品牌，近年通过礼盒升级与 IP 联名实现增长，但增长路径天花板显现；核心商业目标是找到未来 3 年具备"国民级大单品"潜力的新品类/产品方向。
2. **市场背景：** 笔类市场存量竞争，基础书写需求被电子化与 AI 持续分流，产品端新品爆炸、同质化严重，笔正在变成"低决策成本的尝鲜品"。
3. **人群焦点：** 以 05/10 后学生和年轻白领为核心样本，代际变化显著——成长于 AI、短视频、兴趣圈层环境，用笔方式从"功能工具"转向"自我表达与场景匹配"。
4. **已有观察（待验证假设）：** 学生从"一支主力笔用到底"转向"多支笔服务不同场景与心情"；秀丽笔、爆闪马克笔等非刚需品类曾成为爆品；周边生态（笔袋、挂件、改造）正在兴起。
5. **研究路径：** 需沿 **人 → 书写 → 笔 → 机会** 逐层深入，先理解人群生活方式与书写价值变化，再进入品类认知和产品机会。
6. **提案仅提取了前 8 页（共 28 页）：** 后续页面可能包含方法细节、样本设计、刺激物规划等，当前设计基于已有信息完成，可能需要根据完整提案调整。

---

## 二、核心研究问题

| # | 研究问题 |
|---|---------|
| RQ1 | 目标人群的日常生活方式、兴趣场景和消费逻辑是什么样的？ |
| RQ2 | 书写在他们生活中扮演什么角色？书写的场景、行为和主观价值正在发生哪些变化？ |
| RQ3 | 他们如何认知笔的品类？选择和购买笔的决策逻辑是什么？ |
| RQ4 | 笔在书写功能之外，承载了哪些情感、社交、审美或自我表达的价值？ |
| RQ5 | 什么样的笔类产品方向具备跨人群、跨场景的放大潜力？ |

---

## 三、模块结构总览

| 模块 | 模块名称 | 模块目的 | 对应研究问题 | 说明 |
|------|---------|---------|-------------|------|
| 1 | 我的一天 | 建立受访者生活方式画像，理解日常节奏、兴趣圈层和消费心态 | RQ1 | 基础画像模块，先理解人本身，不与产品/品牌关联 |
| 2 | 我和写字这件事 | 理解书写在生活中的角色定位、场景分布和主观价值变化 | RQ2, RQ4 | 从生活自然切入书写，不预设"书写重要"的立场 |
| 3 | 我的文具全家福 | 通过实物映射当前笔的拥有、使用和情感关系图谱 | RQ3, RQ4 | 以拍照任务驱动，观察品类结构、使用分化和周边生态 |
| 4 | 我是怎么选笔的 | 还原发现—选择—购买的完整决策链路 | RQ3 | 覆盖渠道、信息源、决策标准、价格敏感度和品牌认知 |
| 5 | 我的下一支笔 | 捕捉未被满足的需求、跨品类灵感和未来想象 | RQ5 | 从已知延伸到未知，为产品创新方向提供信号 |

---

## 四、详细题目设计

### 模块 1：我的一天

**引导语：**
Hi！欢迎来到这次对话～在接下来的几天里，我们想通过几个小模块来认识你。没有标准答案，怎么想就怎么写，说多说少都可以。我们先从你的日常生活聊起吧！

**题目：**

1. 先简单介绍一下你自己吧——你现在在做什么（上学 / 工作 / 其他）？平时的一天大概是怎么度过的？

2. 最近生活中，你最花时间和精力的事情是什么？（学习、工作、兴趣爱好、社交……什么都可以说）

3. 你最近迷上了什么，或者对什么特别感兴趣？（一个爱好、一部剧、一个博主、一种风格、一个圈子……随便聊聊）

4. 如果用 3 个词来形容你最近的状态或心情，你会选哪 3 个？为什么是它们？

5. 你平时花钱最多的几个方面是什么？最近有没有什么"忍不住下单"或者"买了觉得特别值"的东西？给我们看看？

**结束语：**
谢谢你的分享！接下来我们来聊聊跟"写字"有关的事情～

---

### 模块 2：我和写字这件事

**引导语：**
这个模块我们来聊聊"写字"。不管你觉得自己算不算爱写字的人，都欢迎随便说说～

**题目：**

1. 你觉得自己算是一个"爱写字"的人吗？为什么这么觉得？

2. 想想你最近一周——有哪些时候是"必须手写"的？有哪些时候是你"主动选择手写"而不是打字的？分别是什么情况？

3. 除了学习或工作中的记录，你平时还有什么时候会动笔？（比如写手帐、画画、涂鸦、抄句子、练字、做手工……都算）

4. 你觉得"用笔写"和"用手机或电脑打字"，感受上有什么不一样？如果两种方式都能完成，你更偏向哪种？为什么？

5. 跟你小时候相比，"写字"在你生活里的分量有变化吗？是多了还是少了？具体变了什么？

6. 如果有一天你完全不需要手写任何东西了，你觉得你会失去什么？还是觉得无所谓？

**结束语：**
聊得很好！接下来我们来看看你手边都有些什么笔～

---

### 模块 3：我的文具全家福

**引导语：**
这个模块想请你做一件有趣的事——找到你平时装笔的地方（笔袋、笔筒、桌面都行），给你所有的笔拍一张"全家福"。

**题目：**

1. 请拍一张你现在手边所有笔的合照，然后数一数：大概有多少支？都是些什么类型的笔？

2. 这些笔里面，你最常用的是哪几支？为什么它们能成为你的"主力"？

3. 有没有哪支笔是你特别喜欢或特别有感情的？喜欢它什么？可以拍个特写给我们看看吗？

4. 有没有哪支笔其实买了之后不怎么用？当时为什么想买？后来为什么搁置了？

5. 你会根据不同的场合、用途或心情换不同的笔吗？比如上课一种、做笔记一种、画画一种？说说你的搭配方式。

6. 除了笔本身，你有没有在笔的周边上花心思？比如笔袋、笔挂件、贴纸装饰、可改造的配件？拍给我们看看。

7. 最近半年，你有没有试过什么以前没用过的新类型的笔或文具？是什么让你想试试看的？体验怎么样？

**结束语：**
谢谢你的全家福！接下来我们聊聊你平时是怎么挑笔的～

---

### 模块 4：我是怎么选笔的

**引导语：**
每个人挑笔的方式都不太一样。这个模块我们想听听你的经历和想法。

**题目：**

1. 回忆一下你最近一次买笔的经历——什么时候、在哪里买的？买了什么？为什么选了它？

2. 你平时一般在哪些地方买笔？（文具店、超市、网店、直播间……）在不同地方买笔的时候，你挑选的方式有什么不一样吗？

3. 你一般是怎么知道一支新笔或新文具的？（同学/同事推荐、社交媒体、逛店偶然看到、直播、其他？）

4. 当你面前有一排笔可以挑，你最先看的是什么？最后决定买哪支，通常是因为什么？

5. 你买笔一般在什么价格范围？有没有一个你觉得"超过这个价就不考虑"的价格？有没有过"花了比平时多的钱但觉得值"的经历？

6. 有没有你比较认的笔的品牌？或者明确不想买的品牌？是因为什么？

7. 你有没有在小红书、抖音、B 站或其他平台上刷到过跟笔或文具相关的内容？什么样的内容最容易让你"种草"或下单？

**结束语：**
快到最后啦！最后一个模块，我们来聊聊你理想中的笔～

---

### 模块 5：我的下一支笔

**引导语：**
最后一个模块，我们来畅想一下。如果可以许愿，你希望下一支笔是什么样的？

**题目：**

1. 如果你可以自己设计一支"完美的笔"，你最想让它在哪些方面特别出色？（外观、手感、功能、玩法……什么方面都可以说）

2. 你觉得现在市面上的笔，最让你不满意或者觉得"差点意思"的地方是什么？

3. 最近有没有看到什么笔或文具让你觉得"好酷 / 好想要 / 好有意思"？是在哪里看到的？它打动你的是什么？

4. 你觉得笔除了写字，还可以跟什么场景或用途结合？什么样的组合你会觉得有吸引力？

5. 有没有文具以外的产品（任何品类都行），它的设计、体验或玩法让你觉得"如果笔也能这样就好了"？

6. 如果朋友过生日或者你想送人一份小礼物，你会考虑送笔吗？会送什么样的？如果不会，是因为什么？什么样的笔你才愿意拿来送人？

**结束语：**
所有模块都完成啦！非常感谢你的认真分享，你的每一个回答对我们都很有价值～

---

## 五、Wording Handoff

| 维度 | 说明 |
|------|------|
| **目标人群语气注意** | 核心人群为 05/10 后学生和年轻白领，语气应轻松、平等、有亲和力；避免"请问您""贵方"等距离感用语；可适度口语化但不油腻；引导语和结束语可以用"～"但正文题面保持自然即可 |
| **不能改动/删除** | ① 模块 3 的拍照全家福任务（核心观察点）；② 模块 2 Q2"必须手写 vs 主动选择手写"的区分结构（区分刚需场景与情感性场景）；③ 模块 4 Q4"最先看的是什么 → 最终决定的理由"的两步结构（还原真实决策链路） |
| **需要延后暴露** | KACO 品牌名称在全部模块中均不出现；模块 4 Q6 问品牌认知时为自然回忆，不提供任何品牌列表或提示；如后续有品牌相关刺激物测试，应作为独立追加模块 |
| **需要保留的观察点** | ① 模块 3 全家福照片中的笔数量、品类结构和周边生态；② 模块 3 Q5 场景/心情换笔行为（验证"一支到多支"假设）；③ 模块 5 Q4 笔与非书写场景的结合想象（探索新品类方向信号） |
| **可能过重或过硬的题面** | ① 模块 2 Q6"完全不需要手写了你会失去什么"——对低书写频率人群可能过于抽象，建议 wording editor 评估是否需要增加铺垫或调整为更具象的假设情境；② 模块 4 Q5 价格相关——直接问"超过多少不考虑"可能感受偏硬，建议调整为更自然的表述 |
| **建议交给 wording editor 处理** | ① 全部引导语和结束语的语气微调（当前为偏通用的温暖语气，可能需要针对学生 vs 白领子人群做差异化）；② 模块 1 Q5 消费题的措辞——当前"忍不住下单"较口语化，需确认是否符合全年龄段受访者理解；③ 模块 3 Q6 周边题的举例列表——需根据最终确认的人群微调（学生 vs 白领的周边行为差异大） |

---

## 六、Agent 检核摘要

| # | 检核项 | 状态 |
|---|--------|------|
| 1 | **基础画像先于产品关联：** 模块 1 仅涉及生活方式和消费心态，未提前引入品牌或品类信息 | ✅ 已控制 |
| 2 | **品牌暴露控制：** 全 5 个模块均未出现 KACO 品牌名称；模块 4 品牌题为自然回忆式 | ✅ 已控制 |
| 3 | **提案仅提取 8/28 页：** 后续页面可能包含样本设计、分组逻辑、刺激物测试等关键信息，当前设计可能需要相应增补模块 | ⚠️ 风险待确认 |
| 4 | **人群分组差异未体现：** 提案提到公立高中/职高/国际高中、男/女、圈层先锋等细分维度，当前题目未做分组差异化设计——如需针对不同子人群增减题目，需在确认人群后调整 | ⚠️ 待确认后调整 |
| 5 | **"已有观察"未被当作结论：** 模块 3 Q5（场景换笔）和模块 5 Q4（非书写场景）设计为开放探索题而非验证式封闭题，避免预设结论 | ✅ 已控制 |

---

## 七、需要确认的问题

1. **提案完整内容：** 当前仅提取了提案前 8 页（共 28 页），后续页面是否包含具体的样本设计、人群分组、研究阶段划分或刺激物测试计划？如有，可能需要增加筛选模块或刺激物测试模块。

2. **目标人群范围与分组：** 提案提到 05/10 后学生（含公立高中/职高/国际高中）、年轻白领、男性增量、圈层先锋等多个维度——最终参与 Digital Diary 的人群范围和分组方式是什么？是否需要针对不同子人群做题目差异化？

3. **是否有后续 IDI / 入户 / 工作坊：** 如果 Digital Diary 后有深度访谈或共创工作坊，部分探索性题目（如模块 5 的产品想象）可以在日记中做轻量铺垫、在后续访谈中深入；如果日记是唯一触点，则需要在模块 5 加重深度。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构和已经自然的受访者表达。只改写确实存在问题的引导语、题目、结束语和素材请求；不要全量重写。
```
