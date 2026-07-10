---

## Message 1: system

```text
你是 `dg-question-wording-editor`，负责把 questionnaire designer 产出的研究完整 DG 草稿改写成受访者可读、自然、开放、低负担的最终 DG wording。

你必须遵守：

1. 保留 designer 已确定的模块顺序、研究目的、观察点、任务时机、Diary vs IDI 分工、品牌/刺激物暴露顺序。
2. 不重新设计研究方案，除非发现明显研究风险；风险只放在简短的 remaining research questions。
3. 固定 About Me 开场若已出现，必须保持固定模板，不要擅自改写。
4. 删除或改写受访者题面中的研究员话术、内部逻辑、HTML 标签、占位符、过长括号、过硬命令句。
5. 媒体请求默认软化为可选支持；若 designer 标明强制或平台要求，保留要求但降低压迫感。
6. 输出完整 Markdown，不要输出 JSON。
7. 主交付是修订后的 DG wording，不要长篇解释。

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

## Technical And Placeholder Hygiene

Respondent-facing wording must not expose raw platform or draft artifacts:

- HTML tags such as `<b>`, `<strong>`, `<div>`, or `<br>`.
- "未命名模块", empty titles, test text, or placeholders.
- Internal logic labels such as "trigger -> action -> alternatives".
- Researcher-facing material value requests such as "说明该素材能帮助我们理解什么".

## Brand And Intent Exposure

Early modules should start from the respondent's life, routine, scenes, current solutions, and feelings.

Do not expose brand, product, stimulus, or client strategy too early. Brand/product questions usually belong after natural behavior and category context.

## Fixed About Me Opening

When a draft contains "关于我 / About Me / 生活底色 / 基础画像", preserve these opening three questions exactly unless the user explicitly asks to change them:

1. 首先，让我们多了解一下你吧！色彩、MBTI、星座、关键词......可以用任何你觉得能代表自己的方式来介绍自己！欢迎多多分享照片，向我们展示真实的你～
2. 和我们聊聊你的学业/工作吧！包括你所在的专业/行业、每天具体要做的事情（如果你有副业，也介绍一下吧！）
3. 可以拍一段小视频，带我们“云参观”一下你的居住空间吗？（比如宿舍/家里的整体布局、你每天待得最久的地方，你最用心打理的一个角落）

Do not shorten, split, replace, or make these three questions more research-like.

## Gold Data Wording Pattern 使用规则

当系统提供 `gold_data/reports/wording_patterns.json`、历史 final DG 题面样本或数据库 wording pattern 时，只把它们作为语气和自然度参考。

优先级如下：

1. 当前项目的 designer handoff、Brief、Proposal、客户明确要求、平台限制和固定模板。
2. 本文件、`rewrite_patterns.md`、`module_tone_guides.md` 和 `wording_eval_rubric.md` 中的现有规则。
3. 数据库 final DG 题面样本、常见开场语、媒体请求样本和历史模块语气。

使用 gold wording pattern 时应遵守：

- 可以参考历史题面如何自然开场、如何软化媒体请求、如何邀请真实经历。
- 不要复制历史题目原文，尤其不要复制项目专属品牌、品类、刺激物或内部标签。
- 不要因为历史题目中出现较长括号、强制上传、打分或排序，就放宽本文件的降负担规则。
- 如果历史样本与固定 About Me 开场、品牌延后曝光或 respondent burden 控制冲突，以本文件现有规则为主。
- 只有反复出现、且明显提升自然度和可回答性的 pattern，才可以候选进入 wording rules。

## Case_005 Promoted Wording Rules v0.1.2

These rules come from the reviewed KACO / writing-instrument case. They guide respondent-facing expression after the designer agent has fixed the research logic.

### Make module titles respondent-owned

This is a hard rule for respondent-facing DG wording: every module title should default to a first-person title using "我 / 我的 / 我是 / 我怎么..." unless the client requires a fixed title, the platform forces a title, or the output is explicitly internal-only.

Do not leave titles as neutral research labels. The title should make the respondent feel the module is about their own life, objects, habits, diary, choices, or expectations.

Prefer titles like:

- "About Me" / "关于我";
- "我的日常书写";
- "我的文具全家福";
- "我的书写日记";
- "我是怎么选笔的";
- "我的下一支笔";
- "我的一天";
- "我的日常消费";
- "我和这个品类的关系".

Avoid leaving respondent-facing titles as pure research labels such as "category consumption and usage map", "writing scene topology", "purchase journey", "future product expectation", or "category evaluation standards" unless the output is only for internal review.

If the designer draft has research-style module names, rewrite the titles while preserving the module purpose. For example:

- "书写场景与书写图谱" -> "我的日常书写"
- "笔类消费与使用图谱" -> "我的文具/笔全家福"
- "笔的选择与购买 journey" -> "我是怎么选笔的"
- "未来笔类产品期待" -> "我的下一支笔"

### Module intros and endings should carry emotional value

The question body can stay direct and simple, but module introductions and endings should create warmth and momentum. Use them to acknowledge what the respondent just shared and invite the next task.

Avoid repeated empty endings such as "your feedback is very important to us." Prefer endings that thank the respondent for the actual effort, such as completing a day of diary recording, showing objects, or sharing detailed memories.

For repeated diary days, vary the ending by day or task round instead of copying the exact same sentence.

### Transitions should connect to the previous module

Do not use the same mechanical transition in every module. The transition should show that the next task builds on the previous one.

Example pattern:

- after object inventory: "Thanks for showing us these items. Next we want to understand when and how they appear in your everyday life."
- after About Me: "Now that we know you a little, we want to look more closely at what a normal day looks like for you."

### Avoid obvious comparison prompts

Do not ask comparisons where the answer is obviously "different," such as "how is your rest day different from your workday." Ask directly for the rest-day pattern, places, activities, and category-relevant touchpoints.

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
- avoids repeated "请问/请描述/请说明" starts when invitation verbs would be more natural
- uses conversational follow-ups such as "为什么这么觉得" instead of researcher prompts like "请说明原因"

## 2. Openness

Checks:

- allows real personal answers
- does not over-prescribe examples
- avoids hidden answer options
- preserves open-ended discovery when needed

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
```

---

## Message 2: user

```text
# Designer draft to rewrite

# 题目设计方案

## 1. 项目理解

- 项目名称：凡可奇低端猫粮消费者研究
- 品类/品牌：低端猫粮市场（凡可奇品牌）
- 目标人群：学生党、新晋打工人、多猫家庭、流浪猫救助等预算有限但追求"平价好粮"的养猫人群
- 商业问题：低端猫粮市场增速可观，需理解目标人群的真实需求，为品牌升级和产品策略提供依据
- 研究目标：理解低端猫粮消费者的情感驱动、人宠关系、养宠核心需求、猫粮需求模型、喂食场景、换粮旅程及痛点机会
- 关键设计依据：客户已有中端猫粮研究沉淀，本次聚焦低端人群差异化；情感驱动是养宠核心起点；需构建猫粮需求模型、心智场景和换粮旅程

## 2. 核心研究问题

1. 低端猫粮消费者的生活状态、经济压力和养猫情感驱动是什么？
2. 他们在哪些真实场景下喂猫？喂食中有哪些情绪、担心、幸福或烦恼时刻？
3. 他们如何理解"平价好粮"？评价猫粮的标准和决策逻辑是什么？
4. 当前使用的猫粮品牌/产品/渠道是什么？为什么选择？有哪些痛点和未满足需求？
5. 换粮旅程中的信息获取、决策卡点和品牌切入机会在哪里？

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 |
|------|----------|--------------|
| 板块1：我和我的猫 | 理解受访者生活状态、经济压力、养猫契机、人宠关系和情感驱动 | 研究问题1 |
| 板块2：我的一天 | 收集受访者日常节奏、生活场景、时间分配和养猫日常 | 研究问题1、2 |
| 板块3：我怎么喂猫 | 理解日常喂食场景、情绪、猫的反应、喂食频次和习惯 | 研究问题2、3 |
| 板块4：我给猫买的粮 | 收集当前使用的猫粮品牌/产品/渠道、选择原因、评价标准和痛点 | 研究问题3、4 |
| 板块5：我的喂食记录 | 实时记录3-5天内的喂食时刻、猫的反应、自己的感受和产品表现 | 研究问题2、4 |
| 板块6：我是怎么换粮的 | 理解换粮旅程、信息获取、决策过程、卡点和品牌机会 | 研究问题5 |
| 板块7：我理想中的猫粮 | 收集未满足需求、理想产品期待和愿意为之付费的改善点 | 研究问题3、4、5 |

**设计说明**：本项目为首次研究，非持续追踪，因此保留完整生活画像模块；情感驱动是核心线索，需在基础画像中充分理解人宠关系；喂食场景模块设计为静态图谱+动态日记结合，以捕捉真实喂食时刻和情绪；换粮旅程单独成模块，因Proposal明确要求梳理信息获取方式和品牌切入点。

## 4. 详细题目设计

### 板块1：我和我的猫

引导语：

我们想先认识你和你的猫。请用你自己的方式，告诉我们你的生活、你和猫的故事。

题目：

1. 请简单介绍一下你自己：你现在做什么？住在哪里？平时生活节奏大概是怎样的？

2. 你现在养了几只猫？每只猫分别叫什么名字、多大了、什么品种或花色？

3. 请上传一张你和猫的合照，或者你最喜欢的猫的照片。

4. 你是什么时候、因为什么开始养猫的？当时发生了什么？

5. 对你来说，猫在你生活里扮演什么角色？像家人、朋友、陪伴、责任，还是别的什么？

6. 你觉得你和猫的关系是怎样的？你们平时怎么相处？

7. 养猫给你带来最大的快乐是什么？有没有让你特别幸福或感动的时刻？

8. 养猫有没有让你觉得压力大、焦虑或担心的时候?通常是什么情况？

9. 你现在的收入/预算情况大概怎样？养猫的花费在你整体开销中占比大概多少？

10. 在猫的吃喝上，你每个月大概花多少钱？这个预算对你来说是宽松、刚好还是有点紧？

结束语：

谢谢你分享你和猫的故事！

---

### 板块2：我的一天

引导语：

接下来，我们想了解你平时一天的生活是怎么过的，包括你和猫在一起的时间。

题目：

1. 你通常几点起床、几点睡觉？

2. 请描述一下你典型的一天：从早上起床到晚上睡觉，你通常会做哪些事？在哪里？和谁在一起？

3. 你一天中哪些时间段是和猫在一起的？你们会做什么？

4. 你一天中哪些时间段最忙、最累或压力最大？

5. 你一天中哪些时间段最放松、最开心？

6. 工作日和休息日的生活节奏有什么不同？和猫相处的时间会有变化吗？

7. 请上传一张能代表你日常生活的照片，可以是你的房间、你常待的地方、或者你和猫日常的样子。

结束语：

感谢你让我们看到你的日常！

---

### 板块3：我怎么喂猫

引导语：

现在我们想了解你平时是怎么给猫喂食的，包括你的习惯、感受和猫的反应。

题目：

1. 你平时一天喂猫几次？大概什么时间喂？

2. 你通常在什么情况下给猫喂食？比如固定时间、猫主动要、你有空的时候，还是别的？

3. 喂猫的时候，你通常在做什么？是专门喂猫,还是顺手喂一下？

4. 喂猫的时候,你的心情通常是怎样的？

5. 有没有哪些喂食的时刻让你觉得特别幸福、温暖或治愈？请具体描述。

6. 有没有哪些喂食的时刻让你觉得烦恼、焦虑或揪心？请具体描述。

7. 你的猫吃东西的时候是什么样子？它吃得快还是慢？挑食吗？

8. 你怎么判断猫喜不喜欢这个粮？

9. 你会担心猫吃的粮有什么问题吗？通常担心什么？

10. 除了主粮,你还会给猫吃/喝别的东西吗？什么时候给？为什么给？

结束语：

谢谢你分享喂猫的日常！

---

### 板块4：我给猫买的粮

引导语：

接下来，我们想了解你现在给猫吃的是什么粮，以及你是怎么选的。

题目：

1. 你现在主要给猫吃什么牌子、什么系列的猫粮？请具体说说。

2. 请上传一张你现在用的猫粮包装照片。

3. 你是在哪里买的这款猫粮？线上还是线下？具体什么平台或店？

4. 这款猫粮一袋/一包多少钱？你觉得这个价格怎么样？

5. 你为什么选择这款猫粮？当时是怎么决定的？

6. 你觉得这款猫粮哪些方面还不错？

7. 你觉得这款猫粮哪些方面不太满意或有顾虑？

8. 你对"平价好粮"是怎么理解的？什么样的猫粮算是"平价好粮"？

9. 对你来说，选猫粮的时候最看重什么？比如价格、成分、品牌、猫爱吃、朋友推荐，还是别的？

10. 你会看猫粮的配料表、成分表或营养标签吗？你主要看什么？

11. 你觉得什么样的猫粮是"好粮"？你怎么判断一款猫粮好不好？

12. 你有没有用过或听说过其他低价位的猫粮品牌？你对它们的印象是什么？

结束语：

谢谢你的分享！

---

### 板块5：我的喂食记录

引导语：

接下来的3-5天里，我们希望你在每次给猫喂主粮的时候，简单记录一下当时的情况和感受。不需要每次都写很多，几句话就够了。

题目：

**每次喂食时记录：**

1. 现在是几月几日、星期几、几点？

2. 你现在在哪里？在做什么？

3. 为什么这个时候喂猫？

4. 你现在的心情怎么样？

5. 猫看到粮是什么反应？吃得怎么样？

6. 你喂完之后是什么感觉？

7. 这次喂食有没有什么特别的地方？比如猫特别爱吃、不太爱吃、你特别开心或担心什么？

8. 如果方便的话，请拍一张猫吃粮的照片或视频。

结束语：

感谢你这几天的记录！这些真实时刻对我们非常重要。

---

### 板块6：我是怎么换粮的

引导语：

我们想了解你平时是怎么给猫换粮、选新粮的，包括你会去哪里找信息、怎么做决定。

题目：

1. 你大概多久会考虑给猫换一次粮？

2. 什么情况下你会想给猫换粮？

3. 你上一次换粮是什么时候？从什么粮换到什么粮？

4. 你当时为什么想换粮？

5. 你是怎么找到新粮的？在哪里看到的信息？

6. 你会去哪些地方了解猫粮信息？比如电商平台、社交媒体、朋友推荐、宠物店、兽医，还是别的？

7. 你在选新粮的时候，会重点关注哪些信息？比如价格、评价、成分、品牌背书、测评、销量，还是别的？

8. 你在决定买之前，通常会纠结什么？有什么顾虑或担心？

9. 你最终是怎么下决心买的？

10. 换粮之后，你怎么判断这次换得对不对？

11. 你有没有换粮失败的经历？发生了什么？

12. 如果有一个新的低价猫粮品牌想让你试试,你会考虑哪些因素？什么会让你愿意试试？什么会让你不敢试？

结束语：

谢谢你分享换粮的经历！

---

### 板块7：我理想中的猫粮

引导语：

最后，我们想听听你对理想猫粮的期待,以及你希望改善的地方。

题目：

1. 如果不考虑价格，你理想中的猫粮是什么样的？

2. 在你现在的预算范围内，你最希望猫粮在哪些方面做得更好？

3. 有没有哪些需求是你现在用的猫粮满足不了的？

4. 如果有一款猫粮，在你的预算内，同时能解决你最担心的问题，你觉得它应该是什么样的？

5. 你愿意为哪些改善多花一点钱？为什么？

6. 你觉得低价猫粮品牌可以在哪些方面做得更好，让你更信任、更愿意选择？

7. 对于凡可奇这个品牌，你有听说过吗？你对它的印象是什么？

8. 如果让你给低价猫粮品牌提一个最想要的改进建议，你会提什么？

结束语：

非常感谢你的参与和分享！你的真实经历和想法对我们非常重要。

---

## 5. Wording Handoff

**目标人群语气注意：**
- 目标人群包括学生党、新晋打工人、多猫家庭、流浪猫救助等，年龄和经济状况差异较大，语气需要平实、不预设、不condescending。
- 避免"铲屎官""主子"等过度萌化或亚文化用语,除非受访者自己使用。
- 经济压力和预算话题需要自然带过,不要让受访者感到被评判。

**不能改动/删除：**
- 板块1中关于养猫契机、人宠关系、情感驱动的题目必须保留,这是Proposal核心要求。
- 板块3和板块5关于喂食场景、情绪、幸福/烦恼/揪心时刻的题目必须保留,这是心智场景提炼的基础。
- 板块6换粮旅程的信息获取、决策卡点题目必须保留,这是品牌切入机会识别的依据。
- 板块4和板块7关于"平价好粮"理解、评价标准、未满足需求的题目必须保留,这是需求模型构建的核心。

**需要延后暴露的品牌/产品/刺激物：**
- 凡可奇品牌只在板块7最后出现,前面所有模块不要主动提及,避免影响受访者真实表达。

**需要保留的观察点：**
- 生活状态和经济压力(板块1)
- 养猫情感驱动和人宠关系(板块1)
- 日常节奏和养猫时间分配(板块2)
- 喂食场景、情绪和猫的反应(板块3、板块5)
- 当前猫粮选择逻辑和评价标准(板块4)
- "平价好粮"的理解(板块4、板块7)
- 换粮信息获取和决策卡点(板块6)
- 未满足需求和理想产品期待(板块7)

**可能过重或过硬的题面：**
- 板块5日记记录要求3-5天、每次喂食都记录,对部分受访者可能负担较重,wording agent可优化为"尽量记录"或"选几次印象深的记录"。
- 板块4和板块6中关于配料表、成分、信息渠道的题目可能显得过于研究型,需要口语化、场景化。
- 板块1中关于收入和预算的题目需要更自然的表达,避免侵入感。

**建议交给 dg-question-wording-editor 处理：**
- 所有题面的口语化和去checklist化。
- 括号提示的优化:减少括号堆砌,改为自然引导。
- 板块引导语和结束语的温度和自然度。
- 题目顺序的微调,确保对话流畅。
- 照片/视频要求的表达方式,避免任务感过重。

---

## 6. Agent 检核摘要

- 已对照Proposal核心产出要求检核:情感驱动、人宠关系、猫粮需求模型、心智场景、换粮旅程均有对应模块和观察点设计。
- 主要风险:板块5日记记录可能对部分受访者负担较重;板块1经济话题可能引起不适;题面整体偏研究型,需wording agent大幅口语化。
- 已做的控制:基础画像模块(板块1-2)先理解人和生活,不急于进入猫粮;喂食场景采用静态图谱(板块3)+动态日记(板块5)结合,平衡深度和负担;凡可奇品牌延后到板块7出现;换粮旅程单独成模块,覆盖信息获取和决策全链路。
- 模块逻辑完整:从人群画像->日常生活->喂食场景->当前猫粮->实时记录->换粮旅程->未来期待,符合从concrete facts到abstract meaning的产品创新逻辑。
- 题量约70题(含日记记录),处于合理区间,但需wording agent评估实际填写负担。

---

## 7. 需要确认的问题

1. 板块5日记记录要求3-5天、每次喂食都记录,对目标人群(学生党、打工人等)可能负担较重,是否可以调整为"选择2-3天记录"或"每天选1-2次印象深的喂食记录"?
2. 是否有IDI或入户环节承接深层情感驱动、品牌认知和刺激物测试?如果有,Diary可以更聚焦事实和场景,深层perception交给IDI。
3. 是否需要在板块7之后增加凡可奇品牌/产品概念的刺激物测试模块?如果需要,建议在Diary中只做初步反应收集,详细测试交给IDI,避免Diary题量过重。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构，但把所有受访者可见的引导语、题目和结束语改成自然可回答的 DG wording。
```
