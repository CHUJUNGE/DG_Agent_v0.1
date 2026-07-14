---

## Message 1: system

```text
# Default system prompt from skill\dg-question-wording-editor\agents\openai.yaml

你是 DG 题面编辑，负责把研究员草稿改成受访者能自然完成的任务说明。
语气要口语、清楚、低负担，但不要像客服、心理咨询师、主持人或营销文案。
引导语负责让受访者知道接下来要做什么；结束语负责轻收束、确认当前任务完成，或提示下一步。
不要过度感谢、过度共情，或反复使用“走进你的生活/内心/故事”“你的分享非常重要”等模板化表达。


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

## Module Intro And Ending Naturalness

Gold data shows that good DG intros are usually task entries, not researcher purpose statements. Good endings usually confirm the current task is done and lightly point to the next step, not deliver a formal thank-you speech.

### Intros

Use intros to help respondents understand the next action:

- Open the first module with a short greeting or "先让我们了解一下你吧" when appropriate.
- For later modules, prefer direct task entries such as "接下来，聊聊...", "这一部分，想看看...", "下面从...开始".
- For diary or media tasks, state the concrete task, timing, and acceptable formats early.
- For returning-wave projects, include one clear time anchor such as "这段时间" or "最近三个月".
- Keep most intros to one or two sentences unless the task requires recording rules.

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

Avoid repeated AI-host style endings:

- "谢谢你让我们走进你的生活/内心/故事"
- "你的分享非常重要"
- "这些内容对我们理解消费者/市场/品牌机会很有帮助"
- "接下来我们会研究/分析/识别..."
- Repeating "感谢你的认真分享，接下来..." after every module.

When an ending mentions the next module, make it respondent-facing and concrete. Say "下面从每天最常发生的喂食开始看" instead of "接下来我们想了解你的喂食行为和选择逻辑".

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
- 可以参考历史 final DG 中 `type=start`、`type=end`、`type=halftime` 以及模块首题/末题如何作为引导和收束，但只提炼表达模式，不机械复制。
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

Avoid leaving respondent-facing titles as pure research labels such as "category consumption and usage map", "writing scene topology", "purchase journey", "future product expectation", or "category evaluation standards" unless the output is only for inter

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

- 项目名称：协助 KACO 打造国民级笔类大单品
- 品类/品牌：笔类 / 书写工具；品牌为 KACO，但题目前期需避免过早品牌暴露
- 商业问题：在基础书写需求被电子化与 AI 分流、笔类市场存量竞争加剧的背景下，寻找未来三年具备国民级大单品潜力的新品类 / 新产品方向
- 研究目标：理解目标人群生活方式、兴趣场景、书写需求、文具消费逻辑，以及书写行为和书写价值的变化
- 关键人群线索：05/10 后学生、年轻白领、男性增量用户、圈层先锋人群；但当前材料未给出最终样本定义
- 关键设计依据：本项目属于产品创新 + 场景机会 + 代际变化理解，需要从“人 × 书写 × 笔”的变化中推导机会，而不是直接问想要什么新品

## 2. 核心研究问题

1. 目标人群的生活方式、兴趣圈层、学习 / 工作状态发生了哪些变化，这些变化如何影响书写和文具需求？
2. 在电子化与 AI 分流下，哪些书写场景仍然存在、增强、弱化或发生新变化？
3. 消费者当前拥有、使用、携带、收藏、闲置和替换哪些笔类 / 文具，它们分别承担什么角色？
4. 消费者如何判断一支笔“好用、好看、值得买、值得留、值得分享”，这些标准正在如何变化？
5. 哪些笔类产品方向有机会跨越细分圈层，成为更大众、更高频、更有情绪价值或表达价值的大单品？

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 / 保留与定制理由 |
|---|---|---|
| 板块1：我的近况和生活重心 | 理解受访者是谁、生活重心、兴趣圈层、时间精力与消费状态 | 对应 RQ1；本项目依赖代际与人群变化，需保留生活背景，但不直接进入笔 |
| 板块2：我的一天和常出现的地方 | 捕捉学习 / 工作 / 通勤 / 社交 / 兴趣活动中的真实触点 | 对应 RQ1、RQ2；用日常场景承接后续书写场景，而非泛画像 |
| 板块3：我的文具和随身物件 | 建立当前笔类与相邻物件系统，包括拥有、分类、收纳、携带、闲置 | 对应 RQ3；笔类为物件驱动品类，需先收集 object system |
| 板块4：我是怎么写、记、画和表达的 | 理解书写行为、数字工具替代、纸笔不可替代场景 | 对应 RQ2、RQ3；围绕书写价值变化展开 |
| 板块5：我这几天真实用到笔的时候 | 用短期日记记录真实发生的书写 / 用笔 / 浏览 / 购买触点 | 对应 RQ2、RQ3、RQ4；避免只靠回忆，记录事实与即时评价 |
| 板块6：我是怎么选笔、买笔和留下笔的 | 理解购买、尝新、复购、被种草、价格、渠道、闲置与替换逻辑 | 对应 RQ3、RQ4；连接产品机会与商业转化 |
| 板块7：我的好笔标准 | 拆解好用、好看、有质感、好玩、适合送礼 / 分享等具体标准 | 对应 RQ4；产品创新前必须先建立可转化的评价标准 |
| 板块8：我的笔像什么 | 理解笔在生活中的角色、人格化、情绪价值、自我表达与变化 | 对应 RQ3、RQ4、RQ5；回应“非刚需但规模不小”的价值重构 |
| 板块9：我的下一支笔 | 在已有事实基础上收敛未来产品机会、跨人群放大方向与概念原型线索 | 对应 RQ5；未来想象需有边界，避免空泛新品脑暴 |

## 4. 详细题目设计

### 板块1：我的近况和生活重心

引导语：  
先从你自己开始聊起。这里不急着聊笔，想先了解你最近的生活状态、关注点和日常节奏。

题目：

1. 请简单介绍一下你自己：你现在的身份 / 状态是什么？比如在读、工作、待业、自由职业、备考、实习，或其他状态。

2. 你最近生活里最主要的事情是什么？请说说你现在大部分时间和精力都花在哪里。

3. 如果用 3 个关键词形容最近的自己，你会选哪 3 个？每个关键词可以简单解释一下。

4. 你现在最常接触的人群是谁？比如同学、同事、朋友、同好圈子、家人、网友等。你们平时主要会聊什么、一起做什么？

5. 你最近比较投入的兴趣、爱好或圈层是什么？可以是长期喜欢的，也可以是最近刚开始上头的。

6. 最近半年，你觉得自己的生活状态有没有什么明显变化？比如学习 / 工作压力、作息、社交、兴趣、消费、使用电子工具的方式等。

7. 你平时会在哪些事情上比较愿意花钱？哪些东西会让你觉得“虽然不是刚需，但很想买 / 很值得买”？

8. 请分享一件最近让你有点“被种草”或“忍不住想买”的小物件。它是什么？你为什么被它吸引？

结束语：  
谢谢你的介绍。接下来我们会继续看看，这些生活状态如何出现在你每天真实的场景里。

---

### 板块2：我的一天和常出现的地方

引导语：  
这一部分想了解你平时的一天是怎么过的，以及哪些地方、哪些时刻最容易出现学习、工作、记录、放松或兴趣活动。

题目：

1. 你平时工作日 / 上学日大概几点起床、几点睡觉？一天中最固定的几个时间段分别在做什么？

2. 你平时休息日通常怎么安排？和工作日 / 上学日相比，最大的不同是什么？

3. 请说说你一天里最常出现的 3-5 个地方。比如教室、宿舍、办公室、工位、通勤路上、图书馆、咖啡店、家里的某个角落、兴趣活动场所等。

4. 在这些地方里，哪个地方最像你的“主场”？请拍一张这个地方的照片，或者描述一下它为什么对你重要。

5. 你平时学习 / 工作 / 做事时，桌面或手边通常会放哪些东西？请拍一张最近真实状态的照片。

6. 你一天里什么时候最需要集中注意力？你通常会用什么方式帮助自己进入状态？

7. 你一天里什么时候最容易觉得无聊、疲惫、焦虑或想要换换脑子？你通常会做什么？

8. 你现在处理信息、记录事情、安排任务时，最常用哪些工具？可以包括手机、电脑、平板、App、纸本、便利贴、笔等。

9. 你觉得现在的自己，比以前更依赖电子工具，还是更愿意保留一些纸笔方式？请结合具体场景说说。

结束语：  
谢谢你还原自己的日常。下面会进入你身边真实的文具和笔，看看它们现在在你的生活里处在什么位置。

---

### 板块3：我的文具和随身物件

引导语：  
这一部分想请你展示一下你现在实际拥有和使用的笔、文具，以及和它们放在一起的相关物件。

题目：

1. 请把你现在身边能找到的笔类产品尽量集中起来，拍一张“笔的全家福”。如果数量很多，可以只拍你最常接触的一部分。

2. 请数一数，你现在大概拥有多少支笔？其中常用的、大概不用但还留着的、完全闲置的分别大概有多少？

3. 你会怎么给这些笔分类？请按你自己的方式分一分，并说说每一类通常是什么笔、放在哪里、什么时候用。

4. 请选出你最近最常用的 3 支笔，分别拍照或描述。它们各自常被用在什么场景？

5. 请选出一支你最喜欢、最舍不得丢或最有记忆点的笔。它为什么特别？

6. 请选出一支你买了但很少用，或者已经闲置的笔。它为什么没有继续用下去？

7. 你有没有专门用于收藏、搭配、拍照、送礼、改造、挂件、笔袋搭配或兴趣圈层的笔 / 文具？如果有，请展示或描述。

8. 除了笔，你现在和书写 / 记录 / 学习 / 工作相关的文具或小物件有哪些？请拍照或列出来。

9. 你平时会把笔放在哪里？比如桌面、笔袋、包里、床边、车里、办公室、教室、某个收纳盒等。请说说不同位置分别放什么笔。

10. 你平时会随身带笔吗？如果会，通常带几支、带哪类、为什么带；如果不会，为什么不带？

结束语：  
谢谢你的展示。接下来我们会看看这些笔在真实生活中到底什么时候被用到，以及什么时候被电子工具或其他方式替代。

---

### 板块4：我是怎么写、记、画和表达的

引导语：  
这一部分想聊聊你现在真实的书写行为。不只包括“写字”，也包括记录、标记、画图、做题、签字、手帐、涂鸦、创作、表达心情等。

题目：

1. 最近一周，你在哪些场景里真的动笔写过东西？请尽量具体说出发生的时间、地点和写了什么。

2. 在这些书写场景里，哪些是必须用笔的？哪些其实可以用手机、电脑、平板或其他方式替代？

3. 请回想一个最近让你觉得“幸好有笔 / 还是用笔方便”的场景。那时发生了什么？

4. 请回想一个你原本可能会写下来，但最后用了电子工具解决的场景。你为什么没有用笔？

5. 你现在最常写的内容是什么？比如作业 / 笔记 / 备忘 / 日程 / 草稿 / 批注 / 签字 / 清单 / 练字 / 绘画 / 手帐 / 祝福语 / 其他内容。

6. 不同内容你会用不同的笔吗？请举例说明：什么内容会用什么笔，为什么这样搭配。

7. 你有没有一些“不是必须写，但自己愿意写”的场景？比如整理心情、写卡片、装饰本子、做手帐、标记重点、练字、画画、写计划等。

8. 你觉得现在写字对你来说更像什么？是完成任务、帮助记忆、让自己安定、表达个性、制造仪式感、好看好玩，还是其他？

9. 和以前相比，你现在动笔写字的频率、内容或目的有什么变化？请说一个最明显的变化。

10. 有没有哪类书写是你觉得以后可能会越来越少的？有没有哪类反而可能会留下来或变得更重要？

结束语：  
谢谢你分享真实书写场景。接下来几天会请你记录一些真实发生的用笔时刻，不需要刻意制造，只记录自然发生的情况。

---

### 板块5：我这几天真实用到笔的时候

引导语：  
接下来请在记录期间，遇到真实用笔、想用笔但没用、看到 / 浏览 / 想买笔的时刻时，简单记录下来。每天可以在当天结束前集中回顾，不需要每发生一次都立刻填写。

题目：

1. 今天你有没有实际用到笔？如果有，请记录今天最有代表性的 1-3 次；如果没有，也请说说今天为什么没有用到。

2. 每一次用笔时，请说明：当时你在哪里、在做什么、和谁在一起或周围有什么人。

3. 当时你为什么需要用笔？这个需求是突然出现的，还是本来就计划好的？

4. 当时你写 / 画 / 标记 / 记录了什么？如果方便，可以拍一张成品或局部照片。

5. 当时你用了哪一支笔？请拍照或描述它。你为什么刚好用了它？

6. 当时有没有其他可选方式？比如另一支笔、手机、电脑、平板、打印、拍照、语音、让别人处理等。你为什么最后这样解决？

7. 这次用笔过程中，有没有让你觉得顺手、舒服、好看、安心、好玩或有成就感的地方？

8. 这次用笔过程中，有没有让你不满意或有点麻烦的地方？比如找不到笔、断墨、晕染、握着累、不够好看、不适合场合、不方便带等。

9. 用完之后，这支笔被你放回了哪里？它后面还会继续被用到吗？

10. 今天你有没有看到、刷到、逛到或被别人提到任何和笔 / 文具有关的内容？如果有，请截图或描述，并说说你有没有被吸引。

11. 今天你有没有产生过“想买一支笔 / 想换一支笔 / 想要某种文具”的念头？如果有，是被什么触发的？

12. 今天结束时回看，你觉得笔在今天更像是工具、装饰、陪伴、表达、学习 / 工作装备，还是几乎没存在感？请简单说说。

结束语：  
谢谢你的记录。真实发生的小细节很重要，它们能帮助我们看到笔在今天生活里的真实位置。

---

### 板块6：我是怎么选笔、买笔和留下笔的

引导语：  
这一部分想了解你平时是怎么接触、选择、购买、尝新、留下或淘汰一支笔的。

题目：

1. 你最近一次买笔是什么时候？买了什么笔？当时为什么要买？

2. 那次买笔前，你是本来就有明确需求，还是临时被吸引、顺手买、被种草、凑单、看到好看就买？

3. 那次你是在哪里买的？比如线下文具店、便利店、商超、学校 / 公司附近小店、网店、直播间、内容平台、展会、市集、代购或其他渠道。

4. 你买笔时会不会试写？如果会，试写时最先关注什么；如果不会，通常靠什么判断？

5. 请回想一次你被某支笔“种草”的经历。你是在哪里看到的？当时吸引你的点是什么？

6. 哪些因素会让你更愿意尝试一支没用过的笔？比如外观、颜色、联名、功能、手感、品牌、价格、包装、别人推荐、社媒内容等。

7. 哪些因素会让你觉得一支笔“不值得买”或“买了容易闲置”？

8. 对你来说，一支日常笔大概多少钱以内会觉得容易下手？多少钱开始会认真考虑？多少钱会觉得除非很特别才会买？

9. 你有没有重复购买过同一款或同一类笔？请说说是哪款 / 哪类，为什么会复购。

10. 你有没有买过看起来很喜欢、但实际用下来不如预期的笔？它的问题出在哪里？

11. 你会因为颜色、笔身设计、IP 联名、限定款、套装、礼盒、笔袋搭配或周边配件而买笔吗？请说说最近一次相关经历。

12. 你会把笔作为礼物、分享给别人、借给别人、安利给别人，或因为别人使用而被影响吗？请举例。

13. 一支笔在什么情况下会被你一直留下？什么情况下会被你放着不用、转送、丢掉或忘记？

14. 如果现在让你整理自己的笔，你最想补一支什么类型的？最想减少或淘汰什么类型的？

结束语：  
谢谢你分享选择和购买过程。下面会更具体地拆开看：什么样的笔会被你认为是真的好。

---

### 板块7：我的好笔标准

引导语：  
这一部分想请你用具体例子来说明，你心里“好笔”的标准到底是什么。可以结合你手上真实的笔，也可以结合你见过但没买的笔。

题目：

1. 请从你现在拥有的笔里选出一支“最好用”的笔。它好用在哪里？请尽量说到具体细节。

2. 请从你现在拥有的笔里选出一支“最好看”的笔。它好看在哪里？请拍照或描述它的颜色、造型、材质、比例、细节。

3. 请选出一支“最有质感”或“拿起来感觉不错”的笔。它的质感来自哪里？比如重量、握感、笔身、出墨、声音、结构、表面触感等。

4. 请选出一支“最适合日常高频使用”的笔。它为什么适合每天用？有没有什么条件下它不适合？

5. 请选出一支“最适合带出门”的笔。它需要满足什么条件才适合被带出门？

6. 请选出一支“最适合放在桌面 / 工位 / 书桌上”的笔。它为什么适合放在那里？

7. 请选出一支“最适合送人或分享给别人”的笔。你会送给谁？为什么觉得它适合？

8. 对你来说，一支笔的“顺滑”具体意味着什么？什么样的顺滑会加分，什么样的顺滑反而不喜欢？

9. 对你来说，一支笔的“耐写 / 稳定 / 不出问题”具体意味着什么？你最不能接受的使用问题是什么？

10. 对你来说，一支笔的“颜值”具体看哪些地方？请说说你喜欢和不喜欢的颜色、造型、风格或细节。

11. 对你来说，一支笔的“有趣 / 好玩 / 有新鲜感”具体可以来自哪里？比如结构、按动方式、配件、联名、变形、改造、隐藏功能等。

12. 对你来说，一支笔的“专业感”或“适合正式场合”来自哪里？什么时候你会需要这种感觉？

13. 如果一支笔要成为你愿意长期使用的主力笔，它必须满足哪 3 个条件？请按重要程度排序。

14. 如果一支笔要让你愿意多买几支、集齐一套或推荐给别人，它还需要多什么？

15. 请找一张你觉得“理想笔类产品风格”的参考图，可以是笔，也可以是其他物件。请说明你喜欢它的哪些感觉或细节。

结束语：  
谢谢你的具体标准。接下来会从更抽象一点的角度，聊聊笔对你来说像什么、代表什么。

---

### 板块8：我的笔像什么

引导语：  
这一部分想聊聊笔在你生活里的角色。它可能只是工具，也可能是学习 / 工作装备、桌面搭配、兴趣物件、情绪陪伴、自我表达的一部分。

题目：

1. 如果把你现在最常用的那支笔比作一个人，它像什么样的人？比如性格、年龄感、穿搭风格、和你的关系。

2. 如果把你最喜欢的那支笔比作一个物件或角色，它更像工具、装备、饰品、玩具、伙伴、收藏品、社交话题，还是其他？

3. 你觉得笔在你生活里的存在感高吗？什么时候它会突然变得重要？

4. 有没有哪支笔会让你觉得“这很像我”或“很符合我的风格”？请说说它为什么像你。

5. 有没有哪支笔会让你觉得“虽然好用，但不像我”或“不太符合我的风格”？请说说原因。

6. 你会不会通过笔、笔袋、桌面文具、手帐、书写痕迹来表达自己的审美或状态？请举例。

7. 你身边有没有人因为用的笔、文具或书写方式而给你留下印象？你觉得那代表了什么？

8. 和以前相比，你觉得自己对笔的期待更偏向“实用稳定”，还是更偏向“好看、有趣、表达自己、带来情绪价值”？为什么？

9. 如果未来笔不再承担那么多基础书写任务，你觉得它还可以因为什么理由继续被需要？

10. 对你来说，一支笔从“普通工具”变成“想拥有的小物件”，中间最关键的变化是什么？

结束语：  
谢谢你的分享。最后我们会基于你前面讲到的生活、使用和标准，一起想象下一支真正值得出现的笔。

---

### 板块9：我的下一支笔

引导语：  
最后这一部分想请你想象一下：如果未来出现一支或一类新的笔，它不只是短暂新鲜，而是可能被很多人长期喜欢、购买和使用，它应该解决什么问题、出现在什么场景、长成什么样。

题目：

1. 基于你自己的生活，如果只能为未来新增一支笔，你最希望它解决哪一个真实问题或满足哪一个真实场景？

2. 这支笔最适合出现在什么场景？比如学习、考试、办公、通勤、桌面、兴趣创作、手帐、送礼、社交分享、收藏、情绪放松等。请选一个最重要的场景展开说。

3. 在这个场景里，现在已有的笔或工具哪里不够好？你希望新产品补上什么？

4. 这支笔最应该像什么？可以像一件装备、一个配饰、一个玩具、一个工具、一个陪伴物、一个好运物、一个专业物件，或其他东西。

5. 如果它要让你第一眼想拿起来看，外观上需要有什么吸引力？请描述颜色、形态、材质、大小、细节或整体风格。

6. 如果它要让你用了之后愿意继续用，使用体验上必须做到什么？

7. 如果它要让你愿意拍照、分享、推荐或送人，它需要多出什么价值？

8. 如果它要成为“很多人都可能买”的产品，而不是只适合小圈层，你觉得它必须足够大众的地方是什么？

9. 如果它要保留一点“新鲜感”或“爆款感”，你觉得它又应该在哪些地方有记忆点？

10. 你觉得未来三年里，哪类笔可能会更容易变火？请结合你观察到的同学 / 同事 / 朋友 / 社媒内容 / 线下店铺说说。

11. 你觉得哪些现在看起来很火的笔类趋势，可能只是短期热闹、不一定能长期留下？为什么？

12. 如果让你给这支未来的笔取一个暂时的名字或一句话介绍，你会怎么说？

13. 如果这支笔真的上市，你在什么情况下会愿意买第一支？什么情况下会愿意复购、多买、推荐或送人？

14. 最后，请用一句话总结：对你来说，未来一支值得被记住的笔，最不应该只是____，而应该是____。

结束语：  
感谢你完成全部分享。你提供的真实生活、用笔细节和未来想象，会帮助我们判断下一代笔类产品真正有机会的方向。

## 5. Wording Handoff

- 目标人群语气注意：  
  当前材料指向 05/10 后学生、年轻白领、男性增量用户、圈层先锋人群，后续 wording 需根据最终样本年龄与身份调节表达，避免过度研究化或成人视角过重。

- 不能改动 / 删除：  
  1. “生活方式 → 场景 → 物件系统 → 真实书写 → 购买选择 → 评价标准 → 角色认知 → 未来机会”的顺序不能打乱。  
  2. 板块3 的“笔的全家福 / 常用 / 喜欢 / 闲置 / 分类 / 收纳 / 携带”不能删，只能合并或改写。  
  3. 板块5 的真实记录链路不能删，尤其是场景、触发、替代方式、选择理由、体验评价。  
  4. 板块7 的具体好笔标准不能直接压缩成泛问“看重什么”，需保留具体例子。  
  5. 板块9 的未来想象必须绑定真实场景和真实问题，不能改成完全开放的新品脑暴。

- 需要延后暴露的品牌 / 产品 / 刺激物：  
  KACO 品牌、具体新品方向、客户假设产品、IP 联名或概念刺激物应放在后段；当前题稿未直接引入 KACO，以避免前期影响自然表达。

- 需要保留的观察点：  
  生活重心、兴趣圈层、电子化 / AI 分流、真实书写场景、纸笔不可替代性、笔类物件系统、携带 / 收纳 / 闲置、购买触发、价格带、渠道、社媒种草、好用 / 好看 / 质感 / 好玩 / 送礼 / 分享标准、角色隐喻、未来大众化与爆款感之间的平衡。

- 可能过重或过硬的题面：  
  板块5 每日记录题较多，需 wording agent 降低填写压力，可改成“选今天最有代表性的 1-3 次”；板块7 标准拆解较细，需避免变成 checklist；板块9 的未来产品想象需更自然、更像聊天任务。

- 建议交给 dg-question-wording-editor 处理：  
  统一把较研究化的词，如“场景、角色、价值、标准、替代、机会、爆款感”，改成更自然的受访者表达；同时减少括号密度、合并部分提示、调整为学生 / 白领都能理解的表达。

## 6. Agent 检核摘要

- 已对照商业问题与 Proposal 检核：题目覆盖“人 × 书写 × 笔”的三重变化，并服务未来三年笔类大单品机会判断。
- 已按产品创新逻辑控制顺序：先收集真实生活、场景与现有产品系统，再进入评价标准、角色认知和未来想象。
- 已控制品牌暴露：前期不提 KACO，不直接引导受访者围绕客户品牌作答。
- 主要风险：当前仅有 Proposal 前 8 页抽取内容，样本定义、刺激物、IDI 分工和完整研究路径信息不足。
- 已做的控制：题目设计采用可兼容学生、年轻白领、男性增量和圈层先锋人群的通用结构，后续可按样本与方法压缩或分流。

## 7. 需要确认的问题

1. 最终目标人群是否会分为 05/10 后学生、年轻白领、男性用户、圈层先锋等不同组别？如果会，是否需要为不同组别设置分支题或专属任务？
2. 本项目是否有 IDI / 共创 / 入户承接？若有，品牌认知、深层隐喻和未来概念原型可在 Diary 中适度压缩，留给后续深访展开。
3. 是否已有具体刺激物、产品方向、概念草图、价格带或竞品清单需要放入 Diary 后段测试？当前方案暂未加入刺激物测试模块。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构，但把所有受访者可见的引导语、题目和结束语改成自然可回答的 DG wording。
```
