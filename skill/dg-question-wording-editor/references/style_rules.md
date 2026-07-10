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
