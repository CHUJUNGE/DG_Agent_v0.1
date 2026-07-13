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

- **项目名称**：凡可奇低端猫粮消费者研究
- **品类/品牌**：低端猫粮（凡可奇为乐宾集团旗下低端线品牌）
- **目标人群**：低端猫粮消费者（推测包括学生党、新晋打工人、多猫家庭、流浪猫救助等预算有限但追求"平价好粮"的养宠人群）
- **商业问题**：以用户真实需求为原点，构建凡可奇的品牌与产品策略——理解低端猫粮人群画像、需求模型、心智场景、换粮旅程，找到品牌可切入的机会点
- **研究目标**：①理解人群画像与情感驱动 ②构建猫粮需求模型与优先级 ③提炼与养宠驱动勾连的心智场景 ④刻画换粮旅程与品牌切入机会
- **关键设计依据**：Proposal 明确产出四大板块（人群画像+需求模型+心智场景+换粮旅程）；已有中端猫粮（茁悦）研究沉淀，本次需关注低端人群的差异化特征；情感驱动是区分人群的关键线索

## 2. 核心研究问题

1. 低端猫粮消费者是什么样的人？他们的生活状态、经济压力、生活重心和养宠在生活中的位置是什么？
2. 他们和猫的关系是怎样的？养猫的情感驱动和深层需求是什么？不同人群之间有何差异？
3. 他们日常怎么喂猫、怎么选粮？猫粮在整个养猫花销和喂养体系中扮演什么角色？
4. 他们对猫粮的核心需求是什么？需求的维度、层次和优先级如何？"平价好粮"的标准是什么？
5. 他们的换粮旅程是怎样的？信息获取、决策、购买、使用、复购/换粮的关键节点、痛点和机会点在哪里？
6. 哪些养宠场景（幸福/烦恼/揪心/骄傲）与猫粮需求高度关联？这些心智场景如何转化为产品机会？

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 |
|------|----------|-------------|
| 板块1：关于我 | 理解受访者生活状态、经济压力、生活重心，建立人群画像基础 | Q1 |
| 板块2：我和我的猫 | 理解人猫关系、养猫契机、情感驱动、养猫在生活中的角色 | Q2 |
| 板块3：我怎么养猫 | 理解日常养猫全貌——喂养体系、花销结构、猫粮在其中的位置 | Q3 |
| 板块4：我怎么选猫粮 | 理解猫粮需求维度、评价标准、"好粮"定义、需求优先级 | Q4 |
| 板块5：我的换粮经历（含实时记录） | 刻画换粮旅程——信息获取、决策、购买、使用、复购/换粮全链路 | Q5 |
| 板块6：我和猫的那些时刻 | 提炼高浓度心智场景，连接情感驱动与猫粮需求 | Q6 |
| 板块7：我心目中的好猫粮 | 收集产品期待、品牌感知、未来方向，为品牌策略提供输入 | Q4、Q5、Q6 |

**设计说明**：
- 板块1-2先理解"人"和"人猫关系"，不急于进入猫粮产品；板块3从养猫全貌过渡到猫粮；板块4-5聚焦猫粮选择和换粮旅程；板块6回到情感场景；板块7最后收集产品和品牌期待。
- Proposal四大产出（人群画像、需求模型、心智场景、换粮旅程）均有对应模块覆盖。
- 情感驱动作为人群区分关键线索，在板块2集中采集，在板块6通过场景深化。

---

## 4. 详细题目设计

### 板块1：关于我

**引导语：**
欢迎你参加这次研究！在接下来的几天里，我们想通过你的分享，了解你的生活和你与猫咪的故事。没有标准答案，越真实越好。我们先从认识你开始吧～

**题目：**

1. 先来介绍一下你自己吧——你多大了？现在在做什么工作/上什么学？坐标哪个城市？和谁一起住？
（文字回答即可，也欢迎发一张你觉得能代表你现在状态的照片）

2. 聊聊你现在的生活状态——你觉得自己现在的生活重心在哪里？每天的时间和精力主要花在什么上面？

3. 说到花钱，你觉得自己现在的经济状况怎么样？每个月的钱主要花在哪些地方？有没有什么是你觉得"该省省、该花花"的？

4. 你对现在的生活满意吗？如果用1-10分打个分，你会打几分？最想改变的是什么？

**结束语：**
谢谢你的分享！接下来我们聊聊你和你的猫～

---

### 板块2：我和我的猫

**引导语：**
每个养猫的人都有自己的故事。我们想听听你和猫咪之间的故事～

**题目：**

5. 你现在养了几只猫？分别叫什么名字？来一张你家猫咪的合影或者单独的照片吧～

6. 说说你当初是怎么开始养猫的？是什么契机让你决定养猫的？

7. 猫咪在你的生活里是什么样的存在？如果要用一个人的身份来形容你和猫的关系（比如朋友、孩子、室友、老板……），你会怎么形容？

8. 养猫这件事，给你带来最大的快乐是什么？最大的烦恼或压力又是什么？

9. 你身边的人（家人、朋友、同事）怎么看你养猫这件事？他们的态度对你有影响吗？

**结束语：**
感谢分享！接下来我们聊聊你平时是怎么照顾猫咪的～

---

### 板块3：我怎么养猫

**引导语：**
养猫是一件日常又琐碎的事情，我们想了解你平时是怎么照顾猫咪的，包括吃喝拉撒各个方面～

**题目：**

10. 你平时每天在养猫上大概花多少时间？一天下来，你都会为猫做哪些事情？（比如喂食、铲屎、陪玩、梳毛……）

11. 你家猫咪平时都吃些什么？除了猫粮之外，还会吃什么？（比如罐头、零食、冻干、自制猫饭……）请拍一张你家猫咪现在吃的所有食物的"全家福"～

12. 你每个月在猫身上大概花多少钱？这些钱主要花在哪些方面？你觉得哪些是必须花的，哪些是可花可不花的？

13. 在所有养猫的花销里，猫粮占多大比例？你觉得这个比例合理吗？你理想中猫粮应该花多少钱？

14. 你现在给猫吃的主粮是什么？（品牌、口味、价格大概多少？）拍一张你家现在在吃的猫粮包装吧～

**结束语：**
了解了你的养猫日常，接下来我们重点聊聊你是怎么选猫粮的～

---

### 板块4：我怎么选猫粮

**引导语：**
选猫粮是养猫人的一门"必修课"。我们想了解你在选猫粮这件事上的真实想法和做法～

**题目：**

15. 你选猫粮的时候，最看重的是什么？你会怎么判断一款猫粮好不好？

16. 你现在吃的这款猫粮，当初是怎么选中它的？是谁推荐的、在哪里看到的、还是自己一个个试出来的？

17. 你对现在这款猫粮满意吗？最满意的地方是什么？最不满意或者最担心的是什么？

18. 你有没有觉得"便宜的猫粮就是不好的"？你怎么看"低价猫粮"和"好猫粮"之间的关系？在你心里，"平价好粮"应该是什么样的？

19. 你买猫粮的时候，会看配料表/成分表吗？你会关注哪些成分或指标？这些知识是从哪里学到的？

20. 你一般在哪里买猫粮？（比如电商平台、线下宠物店、社区团购……）为什么选择这个渠道？

21. 你平时会从哪里获取猫粮相关的信息？（比如小红书、抖音、朋友推荐、宠物医生……）你最信任哪种信息来源？

**结束语：**
谢谢你的分享！接下来我们想了解你换猫粮的经历～

---

### 板块5：我的换粮经历

**引导语：**
很多养猫的人都有过换粮的经历。我们想听听你的换粮故事，从发现问题到最终决定，整个过程是怎样的～

**题目：**

22. 你从开始养猫到现在，换过几次猫粮？能大概回忆一下每次换粮的经历吗？（从什么粮换到什么粮，为什么换？）

23. 说说你最近一次换粮的经历——
- 是什么原因让你想换粮的？
- 你是怎么开始找新猫粮的？看了哪些信息、问了谁？
- 你对比了哪些品牌或产品？最后怎么做的决定？
- 换粮的过程顺利吗？有没有遇到什么问题？（比如猫不吃、拉肚子、不确定好不好……）

24. 在换粮的过程中，有没有什么让你特别纠结、犹豫或者不确定的时刻？最后是怎么解决的？

25. 你有没有想过给猫换更贵的粮？是什么让你最终没有换/换了？如果价格不是问题，你会选什么粮？

26. 你有没有试过某款猫粮之后觉得"踩雷"了？是什么情况？后来怎么处理的？

**结束语：**
感谢你分享换粮的经历！接下来我们想请你记录一些和猫咪相关的日常时刻～

---

### 板块6：我和猫的那些时刻

**引导语：**
在接下来的几天里，请你留意和猫咪在一起的那些时刻，把它们记录下来。可以是开心的、烦恼的、感动的、揪心的——什么样的时刻都可以，越真实越好～

**题目：**

27. 【每日记录】今天和猫咪在一起，有没有什么让你印象深刻的时刻？请描述一下当时的情景——发生了什么？你当时在做什么？心情怎么样？
（欢迎拍照或录一段小视频～）

28. 【每日记录】今天给猫咪喂食的时候，有没有什么特别的？（比如猫咪的反应、你的感受、遇到什么问题……）

29. 回想一下养猫以来，你觉得最幸福的一个场景是什么？当时发生了什么？为什么那个时刻让你觉得特别幸福？

30. 养猫以来，最让你烦恼或头疼的一个场景是什么？当时发生了什么？后来怎么解决的？

31. 有没有哪个时刻让你特别揪心或担心猫咪？当时发生了什么？你做了什么？

32. 有没有哪个时刻让你觉得特别骄傲——觉得"我把猫养得真好"或者"我的猫真棒"？当时是什么情况？

33. 在这些时刻里，有没有哪些和猫粮/喂食直接相关的？猫粮在这些时刻里扮演了什么角色？

**结束语：**
谢谢你记录这些珍贵的时刻！最后，我们想听听你对理想猫粮的想法～

---

### 板块7：我心目中的好猫粮

**引导语：**
最后一个板块，我们想听听你对猫粮的期待和想象～

**题目：**

34. 如果让你用三个词来形容你心目中"最理想的猫粮"，你会用哪三个词？为什么？

35. 你觉得一款猫粮，做到哪些事情你就会觉得"这个牌子靠谱"？

36. 你有没有特别信任或者喜欢的猫粮品牌？是什么让你信任它？如果没有，你觉得是为什么？

37. 如果有一款猫粮，价格和你现在买的差不多，但它特别打动你、让你愿意试试——你觉得它应该是什么样的？它会怎么让你知道它的存在？

38. 你会把自己用的猫粮推荐给别人吗？在什么情况下你会推荐？你一般会怎么说？

39. 你觉得养猫这件事，未来会有什么变化吗？你对猫粮的需求会不会跟着变？

**结束语：**
所有问题都回答完啦！非常感谢你的耐心和真诚分享，你的每一个回答都很有价值。祝你和猫咪每天都开开心心的！🐱

---

## 5. Wording Handoff

- **目标人群语气注意**：低端猫粮消费者可能包括学生党、新晋打工人、多猫家庭、流浪猫救助者，年龄偏年轻，经济压力较大。语气应轻松、平等、不居高临下，避免让受访者感觉被"审视"消费能力。"低端""便宜"等词需要谨慎处理，可用"平价""性价比"替代。
- **不能改动/删除**：
  - 板块2的情感驱动题（Q6-Q8）——这是Proposal中人群区分的关键线索
  - 板块4的"平价好粮"定义题（Q18）——直接服务需求模型产出
  - 板块5的换粮旅程完整链路（Q22-Q26）——直接服务换粮旅程产出
  - 板块6的四类心智场景题（Q29-Q33）——直接服务心智场景产出
- **需要延后暴露的品牌/产品/刺激物**：凡可奇品牌全程不暴露；板块1-6均不提及任何具体品牌引导；板块7的品牌感知题（Q36）由受访者自发提及，不做品牌提示
- **需要保留的观察点**：情感驱动类型、人猫关系定义、猫粮在养猫花销中的位置、"平价好粮"标准、换粮触发点与卡点、四类心智场景与猫粮需求的连接
- **可能过重或过硬的题面**：
  - Q12-Q13连续问花销比例，可能让预算敏感人群不适，建议wording agent柔化表达
  - Q23换粮旅程拆解较细，可考虑拆成多个小题或用引导式追问降低一次性回答压力
  - Q19问配料表/成分表，部分低端消费者可能完全不看，需要加"如果不看也没关系"的安全出口
  - 板块6每日记录题（Q27-Q28）连续记录可能负担较重，建议wording agent控制记录天数和每日题量
- **建议交给 dg-question-wording-editor 处理**：
  - 全部题面的口语化、自然化处理
  - 花销相关题的敏感度降低
  - 换粮旅程题的拆分和引导优化
  - 每日记录题的负担控制
  - 括号内提示的精简（避免变成checklist）
  - Q18"低价猫粮"措辞的敏感度处理

---

## 6. Agent 检核摘要

- **已对照商业问题与Proposal检核**：Proposal四大产出（人群画像、需求模型、心智场景、换粮旅程）均有对应模块和题目覆盖
- **主要风险**：
  1. Proposal仅提取了前12页，后续可能有刺激物测试、竞品对比、具体人群分层等要求未被纳入，可能导致模块遗漏
  2. 花销和价格相关题目对预算敏感人群可能造成不适，需wording agent柔化
  3. 板块6每日记录如果天数过多，受访者疲劳风险较高
- **已做的控制**：
  - 凡可奇品牌全程未暴露，品牌感知放在最后板块由受访者自发提及
  - 先理解人和人猫关系（板块1-2），再进入猫粮选择和换粮（板块4-5），最后才问品牌和产品期待（板块7）
  - 题量控制在39题（不含每日重复记录），整体负担适中

---

## 7. 需要确认的问题

1. **Proposal后半部分是否有刺激物/概念测试或竞品对比环节？** 当前仅提取了Proposal前12页，如果后续有具体的产品概念、包装设计或竞品对比需要测试，需要增加相应模块。

2. **是否有IDI/入户等后续深访环节？** 如果有IDI承接，部分深层动机题（如品牌信任、深层情感驱动）可以从Diary中减轻，留给IDI深挖；如果没有IDI，当前Diary需要承担全部深度。

3. **每日记录（板块6）的天数和频次如何安排？** 建议至少覆盖3天（含工作日和休息日），但具体天数需要结合项目预算和受访者礼金确认。

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构，但把所有受访者可见的引导语、题目和结束语改成自然可回答的 DG wording。
```
