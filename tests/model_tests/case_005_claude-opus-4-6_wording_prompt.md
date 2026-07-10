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

- Module order and module names unless the user explicitly asks to change them.
- Research intent, observation points, Diary vs IDI split, task timing, and brand-exposure timing.
- Required fixed templates, especially About Me opening questions.
- Any client-required item, screener, stimulus, or platform constraint.

Edit:

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

When possible, turn research-heavy module titles into titles that feel related to the respondent.

Prefer titles like:

- "About Me" / "关于我";
- "My daily writing";
- "My stationery family photo";
- "My writing diary";
- "How I choose pens";
- "My next pen".

Avoid leaving respondent-facing titles as pure research labels such as "category consumption and usage map" or "writing scene topology" unless the output is only for internal review.

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

- **项目名称**：协助 KACO 打造国民级笔类大单品
- **品类/品牌**：书写工具 / 笔类；KACO
- **商业问题**：在笔类市场存量竞争、基础书写被电子化与 AI 分流的背景下，寻找未来三年具备国民级大单品潜力的新品类/新产品方向
- **目标人群**：05/10后新生代学生、年轻白领等核心人群（代际变化、圈层细分、兴趣多元）
- **核心挑战**：代际变化导致人群需求细分；书写场景被压缩和筛选；笔类新品爆炸但易陷入短期消耗逻辑
- **关键设计依据**：需要理解生活方式、兴趣场景、书写需求与文具消费逻辑；理解书写场景、书写行为及书写价值的变化；理解笔的品类认知、选择逻辑与价值期待；识别国民级大单品机会方向

## 2. 核心研究问题

1. 目标人群的生活重心、日常节奏、兴趣圈层和理想生活是什么？这些如何影响他们对书写工具的需求？
2. 书写在他们生活中扮演什么角色？哪些书写场景仍然存在、哪些正在消失、哪些正在变强？书写的价值和意义发生了什么变化？
3. 他们现在拥有和使用什么样的笔？如何分类、携带、存放、购买和替换？什么样的笔算"好"？
4. 笔在生活中像什么样的物品/关系/角色？是工具、是自我表达对象、是情绪陪伴、还是社交货币？
5. 未来他们希望笔具备什么样的形态、功能、质感和角色？什么样的笔具备国民级大单品潜力？

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 |
|------|----------|--------------|
| 板块1：关于我 | 理解受访者的生活重心、日常节奏、兴趣圈层和理想生活，为后续笔类需求提供人群背景 | 研究问题1 |
| 板块2：我的书写生活 | 理解书写在生活中的真实场景、频率、内容、工具和变化，识别书写价值和书写场景的变化 | 研究问题2 |
| 板块3：我的笔 | 理解受访者当前拥有和使用的笔类物品系统、分类逻辑、携带/存放/购买习惯，收集笔作为物品的真实状态 | 研究问题3 |
| 板块4：书写场景与笔的匹配 | 理解不同书写场景下的笔选择逻辑、场景-笔匹配关系、替代性和未满足需求 | 研究问题2、3 |
| 板块5：笔的购买与替换 | 理解购买、试用、替换、闲置和放弃的行为逻辑，识别购买决策关键因素 | 研究问题3 |
| 板块6：什么样的笔算"好" | 理解受访者评价笔的具体标准和参考物，分解"好看""好用""值得买"等抽象标准 | 研究问题3、4 |
| 板块7：笔的角色与认知 | 理解笔在生活中的角色、意义、情感投射和认知变化 | 研究问题4 |
| 板块8：未来的笔 | 基于具体场景、需求和角色边界，收集受访者对未来笔的想象和期待 | 研究问题5 |

**保留/合并/定制说明**：
- 本项目属于产品创新类型，依赖生活方式、书写场景变化、笔类物品系统和认知变化来解释产品机会，因此保留较完整的生活背景模块。
- 书写场景模块和笔物品系统模块分开设计，前者聚焦书写本身的变化，后者聚焦笔作为物品的分类、存放、购买和替换逻辑。
- 评价标准模块单独设计,要求受访者提供具体参考和示例,避免泛泛而谈"好看""好用"。
- 未来笔的想象需要基于场景、需求和角色边界进行约束,避免无边界的开放想象。

## 4. 详细题目设计

### 板块1：关于我

引导语：

我们想先认识一下你。请用你自己的方式，告诉我们关于你的一些事。

题目：

1. 请简单介绍一下你自己（比如年龄、身份、现在在做什么）

2. 你现在的生活重心是什么？时间和精力主要花在哪些事情上？

3. 你平时有哪些兴趣爱好或圈层？（比如喜欢做什么、关注什么、属于哪些圈子）

4. 你的日常节奏是怎样的？工作日和休息日分别都在做什么？

5. 如果用一个词或一句话形容你现在的生活状态，会是什么？

6. 你理想中的生活是什么样的？和现在有什么不一样？

结束语：

谢谢你的分享！接下来我们想聊聊你和书写的故事。

---

### 板块2：我的书写生活

引导语：

我们想了解你平时的书写情况——不只是写字,也包括画画、涂鸦、记录等各种用笔的时刻。

题目：

1. 你平时会在哪些时候、哪些场合用笔写/画东西？请尽量详细地列出来。

2. 请挑选其中一个最近发生的书写/画画场景，详细说说：
   - 当时在哪里？
   - 在做什么？
   - 为什么要写/画？
   - 写/画了什么内容？
   - 用的是什么笔？
   - 写/画完之后呢？

3. 如果可以，请拍一张照片，展示你最近写/画的东西。

4. 和几年前相比，你现在的书写频率、书写内容、书写方式有什么变化吗？为什么会有这样的变化？

5. 有哪些原本需要用笔的场景，现在已经不怎么用笔了？是什么替代了它？

6. 有哪些新出现的、或变得更频繁的书写/画画场景吗？

7. 对你来说，书写/画画在生活中意味着什么？

结束语：

感谢你的分享！接下来我们想看看你现在用的笔。

---

### 板块3：我的笔

引导语：

我们想了解你现在拥有和使用的笔——请把它们当成你生活中的物品，告诉我们它们的样子、来源和你和它们的关系。

题目：

1. 你现在一共有多少支笔？（大概数量就好）

2. 请拍照展示你现在拥有的笔（可以分几次拍，比如笔袋里的、桌上的、抽屉里的）

3. 你会怎么给这些笔分类？为什么这样分？

4. 哪些笔是每天都会用的？哪些是偶尔用的？哪些基本不用？

5. 哪些笔是随身带着的？哪些是放在固定地方的？为什么？

6. 请挑选 3 支对你来说比较特别的笔（可能是最常用的、最喜欢的、最贵的、最舍不得扔的），分别说说：
   - 这是什么笔？
   - 什么时候、在哪里、为什么买/得到的？
   - 为什么对你来说特别？
   - 主要在什么场合用它？

7. 有没有买了但基本没用/闲置的笔？为什么会这样？

8. 你最近一次买笔/得到新笔是什么时候？买/得到了什么？

结束语：

谢谢你的展示！接下来我们想聊聊不同场景下你会选择什么样的笔。

---

### 板块4：书写场景与笔的匹配

引导语：

我们想了解在不同的书写/画画场景下，你会选择什么样的笔、为什么选它、以及有没有更合适的选择。

题目：

1. 请回想板块2中你提到的那些书写/画画场景，在这些场景下你分别会用什么笔？

2. 请挑选 2-3 个对你来说比较重要或比较频繁的书写/画画场景，分别说说：
   - 这个场景下你会用什么笔？
   - 为什么选这支笔？
   - 这支笔在这个场景下表现如何？有什么满意的地方？有什么不够理想的地方？
   - 有没有其他笔也可以用？它们之间可以互相替代吗？
   - 如果有一支"完全适合这个场景"的笔，它应该是什么样的?

3. 有没有某个场景，你一直没找到特别合适的笔？为什么觉得不够合适？

4. 有没有某个场景，你会特意换一支笔、或者特别在意用什么笔？为什么？

结束语：

感谢你的分享！接下来我们想了解你平时是怎么买笔、换笔的。

---

### 板块5：笔的购买与替换

引导语：

我们想了解你平时是怎么买笔、试笔、换笔的——从发现到购买到使用到可能的放弃。

题目：

1. 你平时会在哪里买笔？（线上/线下、具体渠道）

2. 你平时是怎么发现/注意到新的笔的？（比如逛店、社交平台、朋友推荐等）

3. 请回忆最近一次购买笔的完整过程：
   - 什么时候、在哪里？
   - 当时为什么想买笔？
   - 怎么选的？看了哪些？最后为什么选了这支？
   - 买完之后实际使用感受如何？
   - 如果可以，请拍照展示这支笔。

4. 你会因为什么原因买新笔？

5. 你会因为什么原因不再用某支笔/扔掉某支笔？

6. 你会试用或尝试新的笔吗？什么样的笔会让你想试试？

7. 买笔的时候，你最看重什么？什么因素会让你放弃购买？

结束语：

谢谢你的分享！接下来我们想聊聊你对"好笔"的标准。

---

### 板块6：什么样的笔算"好"

引导语：

不同人对"好笔"的定义可能很不一样。我们想通过一些具体的例子,了解你心中"好"的标准。

题目：

1. 请挑选 1-2 支你觉得"很好看"的笔（可以是你拥有的,也可以是你见过/想要的），分别说说：
   - 这是什么笔？
   - 为什么觉得它好看？具体好看在哪里？
   - 它让你想到什么？
   - 如果可以，请提供图片或照片。

2. 请挑选 1-2 支你觉得"很好用"的笔,分别说说：
   - 这是什么笔？
   - 为什么觉得它好用？具体好用在哪里？
   - 什么场景下它特别好用？
   - 如果可以，请提供图片或照片。

3. 有没有某支笔,你觉得它"值得买"或"值得推荐"？为什么？

4. 有没有某支笔,虽然好看/好用,但你不会买或不会推荐？为什么？

5. 如果让你给笔打分,你会看哪些方面？每个方面你会怎么判断？

6. 你会参考别人对笔的评价吗？你会看重哪些评价内容？

结束语：

谢谢你的详细分享！接下来我们想聊聊笔在你生活中的意义和角色。

---

### 板块7：笔的角色与认知

引导语：

我们想了解笔在你生活中扮演什么样的角色、对你来说意味着什么。

题目：

1. 如果用一个物品、一种关系或一个角色来比喻,你觉得笔更像什么？为什么？

2. 你会把哪些物品和笔归为同一类？为什么？

3. 笔在你的生活中是：
   - 工具（帮我完成某件事）
   - 自我表达的对象（代表我、展示我）
   - 情绪陪伴（让我感到舒服、安心、快乐）
   - 社交货币（可以分享、送人、讨论）
   - 收藏品（拥有本身就有价值）
   - 其他：______
   
   请选择最接近的 1-2 个，并说说为什么。

4. 和几年前相比,笔在你生活中的角色和意义有什么变化吗？

5. 你会把笔送人吗？什么样的笔适合送人？会送给谁？

6. 你希望笔在未来的生活中扮演什么样的角色？

结束语：

感谢你的分享！最后，我们想听听你对未来笔的想象和期待。

---

### 板块8：未来的笔

引导语：

基于你的真实需求和期待,我们想了解你希望未来出现什么样的笔。

题目：

1. 如果有一支笔,专门为你最重要/最频繁的那个书写/画画场景设计,它应该是什么样的？
   - 在什么场景下用？
   - 应该具备什么功能/特性？
   - 应该是什么样的外观/形态/材质？
   - 应该给你什么样的使用感受？

2. 如果有一支笔,能代表你、展示你,它应该是什么样的？

3. 如果有一支笔,你愿意每天带着、用很久,它应该是什么样的？

4. 如果有一支笔,你会想买来送人或分享给朋友,它应该是什么样的？

5. 你觉得未来什么样的笔,可能会成为"很多人都会买、都会用"的国民级产品？为什么？

6. 对 KACO 这个品牌,你有什么印象或期待吗？

结束语：

非常感谢你的耐心分享！你的真实经历和想法对我们非常重要。

---

## 5. Wording Handoff

**目标人群语气注意：**
- 目标人群为 05/10 后新生代学生、年轻白领,成长于短视频、兴趣圈层和内容种草环境,表达方式更口语化、更视觉化、更圈层化。
- 题面应避免说教感和调研感,多用"我们想了解""请告诉我们""你平时会"等自然表达。
- 鼓励照片、图片等视觉化记录,降低纯文字表达压力。

**不能改动/删除：**
- 板块3"我的笔"中的拍照展示笔、笔的分类逻辑、3 支特别的笔及其来源故事,这些是笔类物品系统的核心观察点。
- 板块4"书写场景与笔的匹配"中的场景-笔选择逻辑、替代性和未满足需求追问,这是产品创新的关键链路。
- 板块6"什么样的笔算好"中要求提供具体笔的示例和参考,不能简化为抽象标准列举。
- 板块8"未来的笔"中基于具体场景、角色和需求的约束性想象,不能改为无边界开放题。

**需要延后暴露的品牌/产品/刺激物：**
- KACO 品牌在板块8最后一题才出现,前面板块不应提及品牌名。
- 秀丽笔、爆闪马克笔等具体品类爆品不在题面中出现,这些是客户内部视角,不应引导受访者。

**需要保留的观察点：**
- 生活重心、日常节奏、兴趣圈层和理想生活(服务研究问题1)
- 书写场景、书写频率、书写内容和书写价值的变化(服务研究问题2)
- 笔的物品系统:分类、携带、存放、购买、替换、闲置(服务研究问题3)
- 场景-笔匹配逻辑、替代性和未满足需求(服务研究问题3)
- 购买 journey:发现、选择、购买、使用、评价(服务研究问题3)
- 评价标准的具体化和参考物(服务研究问题3)
- 笔的角色、认知、意义和情感投射(服务研究问题4)
- 基于场景、需求和角色边界的未来笔想象(服务研究问题5)

**可能过重或过硬的题面：**
- 板块3"我的笔"要求拍照展示所有笔、挑选3支特别的笔详细说明,填写负担较高,需要 wording agent 优化引导语,降低任务感。
- 板块4"书写场景与笔的匹配"要求挑选2-3个场景分别详细说明,可能过于繁重,需要适当简化或调整为"至少选1个,最多3个"。
- 板块6"什么样的笔算好"要求分别挑选"好看的笔""好用的笔"并提供图片,需要降低正式感,可改为"可以是你自己的笔,也可以是你在网上见过的、想要的"。

**建议交给 dg-question-wording-editor 处理：**
- 所有题面的口语化、自然化处理,去除 checklist 感和调研感。
- 引导语和结束语的衔接自然度,避免过于正式或机械。
- 括号中的示例和追问,确保是启发而非限定,不要让受访者觉得必须按示例回答。
- 拍照、提供图片等任务的表达,降低任务感和压力感,改为鼓励性而非强制性。
- 部分题目可能需要拆分或合并,以降低单题负担和提高填写流畅度。

---

## 6. Agent 检核摘要

- 已对照商业问题(寻找国民级大单品方向)与 Proposal 研究目标检核,模块设计从生活方式、书写场景变化、笔类物品系统、场景-笔匹配、评价标准、角色认知到未来想象,覆盖完整产品创新研究链路。
- 主要风险1:题量较大(约70题),填写负担偏高,需要 wording agent 优化题面表达和任务引导,降低填写压力。
- 主要风险2:部分题目要求拍照、提供图片、详细列举,可能对部分受访者构成障碍,已在 handoff 中标记,建议改为鼓励性而非强制性。
- 已做的控制1:基础画像模块(板块1)先理解受访者本人,不急于关联产品/品牌;品牌(KACO)在板块8最后才出现,避免前期暴露。
- 已做的控制2:评价标准模块(板块6)要求提供具体笔的示例和参考,避免"好看""好用"等抽象标准;未来笔模块(板块8)基于场景、需求和角色边界约束想象,避免无边界开放。

---

## 7. 需要确认的问题

1. 是否有 IDI 或后续访谈承接深层认知和情感问题？板块7"笔的角色与认知"涉及较抽象的 perception,如果有 IDI,该板块可以适当简化,留给访谈深挖;如果没有 IDI,该板块需要保留并可能需要更具体的追问设计。

2. 记录天数和日记任务设计：当前方案未包含"实时记录书写时刻"的日记任务,主要依赖回忆性问题。如果希望收集更真实的书写场景和笔使用行为,是否需要增加3-5天的实时日记记录模块(每天记录当天发生的书写时刻、用了什么笔、场景和感受)？这会增加填写负担,但可以获得更真实的行为数据。

3. 是否需要增加购物任务或试用任务？如果希望观察受访者在真实购买场景下的选择逻辑和决策过程,可以考虑增加"请在接下来一周内,如果有机会买笔/逛文具店/逛线上笔类商品,记录下来"的任务模块。这需要受访者配合度较高,且可能延长项目周期。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构，但把所有受访者可见的引导语、题目和结束语改成自然可回答的 DG wording。
```
