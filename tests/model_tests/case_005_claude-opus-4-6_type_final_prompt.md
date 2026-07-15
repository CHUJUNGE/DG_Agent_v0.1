---

## Message 1: system

```text
You are `dg-question-type-setter`, responsible for assigning platform question type labels to DG drafts.

Follow the four-step test pipeline:
1. designer draft
2. question type review with reasons
3. wording pass
4. final question type pass with labels only

Current mode: final_labels_only

You are running the final post-wording question type pass.

Output the final user-facing DG wording:
- Add only the user-facing question type labels, for example: 【单选】1. 请选择你喜欢的...
- Do not show reasons.
- Do not show backend field names such as text/single/multi.
- Do not rewrite the wording except for inserting labels.
- Preserve module order, question order, line breaks, and respondent-facing wording.
- If there are researcher-only concerns, put them in a very short 题型检核摘要 after the final draft; do not insert uncertainty into respondent-facing labels.

# Question type setter references

## skill\dg-question-type-setter\SKILL.md

---
name: dg-question-type-setter
description: Set platform question type labels for existing Digital Diary / DG drafts. Use when the user asks to label, assign, review, or revise question types for each DG question, including 简答, 单选, 多选, 打分, 排序, AI-bot, 开场白, 结束画面, and 中场休息.
---

# DG Question Type Setter

Use this skill twice in the full pipeline:

```text
dg-questionnaire-designer
-> dg-question-type-setter review_with_reasons
-> dg-question-wording-editor
-> dg-question-type-setter final_labels_only
```

The first pass gives researchers a type rationale after the designer draft. The second pass produces the final user-facing labels after wording.

This skill does not generate a new questionnaire, rewrite respondent wording, or produce backend import JSON. It labels each question or task with a user-facing question type name. Use backend `type` values only as internal mapping, not as user-visible output.

## Required Reference

Before setting question types, read:

- `references/question_type_rules.md`

## Core Workflow

For each pass, work in this order:

```text
Read the current DG draft
-> identify modules, intros, questions, breaks, endings
-> assign one platform type to each item
-> choose the correct user-facing type label
-> decide whether reasons should be shown
-> flag uncertain or high-burden type choices
-> preserve original wording and order
```

Do not change module order, question order, or wording unless the user explicitly asks for rewriting.

## Platform Types

Use only these platform types:

| backend type | user-facing label | Meaning |
| --- | --- | --- |
| `text` | 简答 | Respondent answers freely with text, voice, image/video explanation, or narrative detail. |
| `single` | 单选 | Respondent chooses exactly one option from a fixed list. |
| `multi` | 多选 | Respondent chooses multiple options from a fixed list. |
| `score` | 打分 | Respondent gives a 1-10 numeric score or rating. |
| `sort` | 排序 | Respondent ranks options or selects a top-N order. |
| `bot` | AI-bot | AI follows up interactively based on the respondent answer. |
| `start` | 开场白 | Opening instruction, module intro, or task setup without a respondent answer. |
| `end` | 结束画面 | Closing statement without a respondent answer. |
| `halftime` | 中场休息 | Break, pause, encouragement, or transition checkpoint without a respondent answer. |

## Output Format

### `review_with_reasons`

Use after `dg-questionnaire-designer`.

Show labels and concise reasons for researcher review:

```markdown
【单选；理由：题目要求从互斥选项中选择一个答案。】
1. ...
```

### `final_labels_only`

Use after `dg-question-wording-editor`.

Show only final user-facing labels:

```markdown
【单选】1. 请选择你喜欢的...
```

Do not show reasons in this mode.

Keep the original Markdown structure. Add the user-facing type label immediately before each question, opening, break, or ending.

For the final user-facing version after wording, do not show backend field names or reasons. Use this compact format:

```markdown
【单选】1. 请选择你喜欢的...
```

For open questions:

```markdown
【简答】1. 请回想最近一次...
```

For opening copy:

```markdown
【开场白】接下来...
```

For ending screens:

```markdown
【结束画面】这一部分就到这里...
```

For breaks:

```markdown
【中场休息】已经完成一半啦，可以先休息一下，准备好后再继续。
```

After the designer stage, reasons should be shown for researcher review. Use this review format:

```markdown
【单选；理由：题目要求从互斥选项中选择一个答案。】
1. ...
```

After the wording skill has produced the final user-facing version, do not show reasons. Show only `【题型名】`.

When uncertain, still choose the best type. In a designer/review draft, add "待确认" in the reason. In the final user-facing version, do not show uncertainty inline; put uncertainty in a separate "题型检核摘要" for the researcher.

## Decision Rules

Default to `text` / `简答` for DG research questions, because Digital Diary usually needs concrete stories, contexts, reasons, photos, videos, or explanations.

Use `single` / `单选` only when the question asks for one mutually exclusive answer, such as yes/no, one current status, one most recent behavior, one primary channel, or one best-fitting option.

Use `multi` / `多选` when the question asks for all applicable items, multiple coexisting people/products/channels/behaviors, or uses wording such as "哪些", "都有哪些", "可以多选", "包括哪些".

Use `score` / `打分` only when the respondent must give a 1-10 numeric evaluation, such as satisfaction, liking, agreement, sensitivity, importance, likelihood, or recommendation likelihood. Do not create or label 1-5 ratings as platform 打分题. If the question asks "为什么打这个分", that follow-up is `text` / `简答`, not `score` / `打分`.

Use `sort` / `排序` when the respondent must rank options, order priorities, choose top-N in sequence, or compare a fixed option list by preference or importance.

Use `bot` / `AI-bot` only when the intended behavior is AI-driven follow-up, dynamic probing, or "ask the AI to continue追问". Do not label a normal open question as `bot` just because it contains follow-up prompts.

Use `start` / `开场白` for module introductions, task instructions, stimulus setup, and non-answering prefaces.

Use `end` / `结束画面` for module completion messages, final thanks, and closing transitions that do not request an answer.

Use `halftime` / `中场休息` for rest breaks, progress checkpoints, or "先休息一下再继续" messages. This should usually be one sentence inserted around the middle of a long questionnaire so the respondent can pause before continuing.

## Reasoning Standard

Each reason must explain why the selected type fits the research task, not just repeat the type name.

Good reasons mention one of:

- the answer needs open narrative detail;
- the answer is mutually exclusive;
- the answer can contain multiple items;
- the question asks for numeric rating;
- the task requires ranking;
- the item is an intro, break, or ending;
- media request is part of an open diary task;
- AI follow-up is explicitly needed.

Avoid long explanations. One sentence is enough.

## Risk Flags

At the end, add a short "题型检核摘要" for the researcher only when there are meaningful issues:

- too many `score` or `sort` questions;
- too many required image/video tasks;
- a `single` / `multi` question lacks clear options;
- a question looks like `single` but research value would be higher as `text`;
- a question combines a rating and an explanation and should be split into `score` + `text`;
- a media upload request is embedded in `text` but may need platform-level `require_image` or `require_video` later.

Do not create a backend schema, JSON, CSV, or import mapping unless the user explicitly asks for it.
## skill\dg-question-type-setter\references\question_type_rules.md

# Question Type Rules

## Source Of Truth

The current platform stores DG projects as:

```text
project -> modules -> questions
```

The platform `type` field supports these backend values and user-facing labels:

- `text`: 简答
- `single`: 单选
- `multi`: 多选
- `score`: 打分
- `sort`: 排序
- `bot`: AI-bot
- `start`: 开场白
- `end`: 结束画面
- `halftime`: 中场休息

The task of this skill is to annotate an existing DG draft with these user-facing type labels. Backend values are internal mapping only and should not be displayed to respondents or normal users.

## Annotation Placement

Add the annotation immediately before the relevant item.

Final user-facing output after wording must show only the type label:

```markdown
【简答】1. ...
【单选】2. ...
【多选】3. ...
【打分】4. ...
【排序】5. ...
【AI-bot】6. ...
```

For opening, ending, and break text:

```markdown
【开场白】...

【结束画面】...

【中场休息】已经完成一半啦，可以先休息一下，准备好后再继续。
```

Designer/review output may include reasons:

```markdown
【简答；理由：需要受访者自由描述具体经历、选择过程和原因。】
1. ...
```

## Type Selection Rules

### `text` / 简答

Use for most DG questions.

Choose `text` when the answer requires:

- real-life scenes, stories, motivations, or reasons;
- process reconstruction, such as before / during / after;
- product, brand, channel, or object descriptions;
- photos, videos, screenshots, or voice explanations as part of a diary task;
- "为什么", "怎么想", "具体说说", "请分享", "请描述", "请介绍";
- follow-up explanation after a choice, score, or ranking.

If a question asks the respondent to upload media and explain it, keep the type as `text` / `简答`; mention in the reason that the media request is part of an open diary task when reasons are shown.

### `single` / 单选

Use when only one answer should be selected.

Common signals:

- yes/no;
- current status;
- one primary option;
- most recent / most common / most important single answer;
- mutually exclusive categories such as age band, city tier, household type, frequency band.

If the options are not listed in the draft, mark "待确认：选项需补齐".

### `multi` / 多选

Use when multiple answers can be true at the same time.

Common signals:

- "哪些", "都有哪些", "包括哪些";
- coexisting people, places, channels, products, brands, activities, information sources, needs, pain points;
- "可以多选" or "请选出所有符合的".

If the question asks "还有哪些" after a fixed list, it can still be `multi` if the expected answer is selecting multiple options; otherwise use `text` for open additions.

### `score` / 打分

Use when the respondent must provide a 1-10 numeric rating.

Common signals:

- "打几分";
- "1-10 分" or "满分十分";
- satisfaction, liking, agreement, sensitivity, importance, purchase interest, recommendation likelihood;
- platform 打分题 only supports 1-10; do not introduce 1-5 ratings.

If the question also asks why the respondent gave the score, split conceptually:

```markdown
【打分；理由：前半句要求给出明确分值。】
...
【简答；理由：后半句需要解释打分原因。】
...
```

If the user asked not to split wording, annotate it as `score` and flag in the check summary that it contains an open explanation follow-up.

### `sort` / 排序

Use when the respondent must rank options.

Common signals:

- "排序";
- "按喜欢程度/重要性排序";
- "选出前三并排序";
- "从最...到最...";
- fixed options are compared by priority, preference, or relevance.

Do not use `sort` for ordinary comparison questions without a fixed option list. Use `text` instead.

### `bot` / AI-bot

Use only when the item is explicitly intended for AI-driven follow-up.

Common signals:

- the question asks the AI to continue probing;
- the task requires dynamic follow-up based on the answer;
- the draft explicitly says "AI bot", "智能追问", "自动追问", or equivalent.

Do not use `bot` for a normal open question that merely contains several manual follow-up prompts.

### `start` / 开场白

Use for:

- module intro;
- task setup;
- stimulus or material viewing instruction before questions;
- opening text that does not collect an answer.

If the text asks the respondent to answer or upload something, it is not `start`; choose the appropriate question type.

### `end` / 结束画面

Use for:

- module ending;
- final closing;
- completion message;
- transition that does not collect an answer.

If the item asks for final feedback, comments, or anything else requiring an answer, use `text`.

### `halftime` / 中场休息

Use for:

- rest break;
- progress checkpoint;
- "先休息一下";
- transition between long task sections.

It should be one short sentence inserted near the middle of a long questionnaire so the respondent can pause. It should not collect a substantive answer.

## Burden And Quality Checks

After annotation, check:

- Are most DG research questions still `text`?
- Are `single` / `multi` questions supported by clear options?
- Are `score` questions limited and justified?
- Are `sort` questions used only with fixed options?
- Are upload-heavy `text` tasks concentrated in a way that may tire respondents?
- Are intro, ending, and break messages separated from actual questions?

If problems exist, add a concise "题型检核摘要".
```

---

## Message 2: user

```text
# Source DG Markdown

## Wording Pass Complete

**Preserved research intent:**
- 六模块结构与顺序不变：人 → 日常 → 书写场景 → 笔的持有 → 选择逻辑 → 未来期待
- 品牌保护：全篇不出现 KACO，品牌/产品概念留后续 IDI
- 模块 4 拍照"全家福"任务保留为核心行为证据
- 模块 2 第 3 题"本来可能用笔但用了电子设备"的反向追问保留
- 模块 6 第 3 题对非日常笔类品类的开放探索保留
- 所有 designer 标注的观察点（自然书写时刻 vs 替代时刻、买了但不用的笔、周边配件、自发提及的品牌信号）均保留
- 品类举例列表在模块 6 第 3 题保留但微调，不做引导

**Major wording changes:**
1. **模块 1 第 1 题**：拆分自我介绍与日常节奏为两题，原题合并了身份、城市、节奏三个不同信息目标（multi_intent_question）
2. **模块 1 第 5 题**："3 个关键词形容审美偏好"对低龄受访者偏抽象，改为更具体、可回答的开放描述，降低任务难度
3. **模块 2 引导语**：原稿已自然，微调使"流水账"表述更轻松
4. **模块 3 第 1 题**："请尽量多列一些，越具体越好"有 checklist 压力（too_checklist_like），软化为开放回忆
5. **模块 3 第 4 题**：designer 标注对低龄受访者偏抽象，加入轻场景提示锚定
6. **模块 4 第 1 题**："并数一数大概有多少支，分别是什么类型的笔"偏审计感（too_checklist_like），软化
7. **模块 5 第 2 题**："最在意/最不在意"保持纯开放，但加轻提示降低空白感
8. **模块 6 引导语**："放飞想象力，怎么天马行空都可以"过度开放，加入轻锚定
9. **模块 6 第 5 题**：designer 标注"爆款"措辞略带引导，调整措辞去掉"火了""都想要"的正面预设
10. **全篇结束语**：原稿"你的每一个回答对我们都很有价值"偏模板化，简化收束
11. **各模块结束语**：部分过度感谢或研究员视角的过渡句，改为轻任务过渡
12. **媒体请求**：模块 4 拍照为核心任务保留要求，但降低压迫感；其余模块媒体请求统一软化为可选

**Remaining research questions for designer agent:**
1. **日记天数与填写节奏未确认**：当前 6 模块 30+ 题若单日填写偏重，建议 designer 确认是一次性填写还是分 3–5 天推送，以便决定是否拆分模块
2. **受访者配额与筛选**：05 后/10 后学生与年轻白领是否使用同一套题目？不同教育路径（公立/职高/国际高中）是否需要筛选题？
3. **是否有后续 IDI**：影响模块 6 的深度——若无后续环节，可能需要在日记中增加品牌与概念模块
4. **模块 2 是否需要多日记录**：当前设计为记录"一天"，若需要多日重复记录，模块 2 应改为 looped diary 格式，结束语也需相应调整

---

## Revised DG Wording

---

### 模块 1：我和我的世界

**引导语：**
Hi～欢迎来到这次对话！在正式开始之前，我们想先认识一下真实的你。没有标准答案，怎么想就怎么说～

**题目：**

1. 先来个自我介绍吧！你现在是学生还是已经工作了？在哪个城市？可以用你觉得最能代表自己的方式说说。

2. 聊聊你平时的日常节奏吧——一天大概是怎么度过的？哪些时间段比较固定，哪些比较自由？

3. 除了上课/上班，你最近花时间最多的事情是什么？

4. 你最近最沉迷或最投入的兴趣爱好/圈子是什么？它吸引你的点是什么？如果方便，可以分享一些相关的图片。

5. 你平时喜欢逛什么平台或 App 来消磨时间、找乐子或找灵感？最近有被种草什么东西吗？

6. 你觉得自己在审美或个人风格上，比较偏向什么样的感觉？可以用几个词、一张图、或者举个你喜欢的东西来说明都行。

**结束语：**
先认识到这里。接下来想请你记录一下真实的一天。

---

### 模块 2：我的一天

**引导语：**
请选一个上学日/工作日，从早到晚记录一下你这一天是怎么度过的。不用写得很正式，像流水账一样记就好～

**题目：**

1. 大致记录一下你今天从起床到睡觉的主要活动和时间安排。

2. 今天有没有哪个时刻你拿起了笔？是在什么情况下拿起来的？写了/画了什么？

3. 今天有没有哪个时刻，你本来可能会用笔，但最后用了手机、平板或电脑来完成？是什么情况？

4. 拍一张你今天随身带的文具（笔袋、铅笔盒，或者散落在包里桌上的笔）给我们看看吧，简单说说都有些什么。

**结束语：**
辛苦啦！接下来聊聊你跟"写写画画"这件事的关系。

---

### 模块 3：我什么时候会拿起笔

**引导语：**
不管是认真做笔记、写作业，还是随手涂鸦、列清单，甚至只是拿着笔转一转——所有你会拿起笔的时刻，我们都想听听。

**题目：**

1. 想一想，你平时在哪些场景下会用到笔？不用刻意分类，想到什么说什么就好。

2. 这些场景里，哪个是你最频繁的？哪个是你做起来最享受的？可能不是同一个，都说说看。

3. 跟你一两年前比，你用笔的场景有没有什么变化？变多了还是变少了？你觉得是因为什么？

4. 你觉得用笔写/画跟用电子设备比，体验上最不一样的地方在哪里？比如做笔记、列计划、涂鸦这些事情，你会更倾向用笔还是用电子设备？为什么？

5. 你有没有什么跟笔有关的小习惯或"仪式感"？比如考试换新笔芯、写手帐必须用某支笔、无聊的时候就喜欢转笔之类的。

**结束语：**
接下来看看你手边都有些什么笔～

---

### 模块 4：我的文具全家福

**引导语：**
来一个有趣的任务——把你目前手边所有的笔都找出来，给它们拍一张"全家福"吧！

**题目：**

1. 把你手边的笔都集合起来，拍一张合照吧。大概有多少支？都是些什么笔？

2. 从里面挑出你最喜欢的一两支，拍个特写，告诉我们它为什么是你的最爱。

3. 有没有哪支笔你买了但很少用、甚至根本没用过？当时为什么买了，后来为什么不用了？

4. 你大概多久会买一次新笔？一般在什么情况下会想买新的？

5. 除了笔本身，你有没有跟笔相关的配件或周边？比如笔袋、替换芯、挂件、笔架之类的，有的话也拍来看看吧。

**结束语：**
看到你的笔家族了！接下来聊聊你平时是怎么挑笔的。

---

### 模块 5：我是怎么选笔的

**引导语：**
每个人选笔都有自己的偏好和门道，有人看颜值，有人看手感，有人随缘。来聊聊你的选笔方式吧～

**题目：**

1. 回想一下你最近一次买笔的经历：买的是什么笔？在哪里买的？为什么选了这一支（或这几支）？

2. 你在挑一支笔的时候，一般最看重的是什么？有没有什么是你完全不在意的？可以从外观、手感、出墨、价格、品牌，或者其他你觉得重要的角度聊聊。

3. 你一般是怎么知道/发现一支新笔的？会在哪些渠道看到相关信息或推荐？

4. 你有没有特别喜欢或会主动关注的笔的品牌？为什么喜欢它？

5. 你觉得一支日常用的笔大概多少钱是你比较舒服的价格？超过多少钱你就会犹豫或者觉得不值？

6. 你最近有没有看到过什么让你觉得"这支笔好酷"或者特别想要的笔或文具？是在哪里看到的？它哪里吸引了你？

**结束语：**
了解了你的选笔方式，最后来聊聊你对"下一支笔"的想象～

---

### 模块 6：我的下一支笔

**引导语：**
最后一个部分，聊一些关于"下一支笔"的想象和期待。不用考虑现实限制，说说你真正想要的就好。

**题目：**

1. 如果可以完全按你的想法定制一支笔，你希望它是什么样的？外观、颜色、手感、功能……随便从哪个角度说都行。如果脑海里有画面，也欢迎画出来或者找一张参考图。

2. 你觉得现在市面上的笔，最让你觉得遗憾或"要是能……就好了"的地方是什么？

3. 除了你日常在用的那类笔，你有没有对其他类型的笔产生过兴趣或好奇？比如马克笔、彩墨笔、秀丽笔、自动铅、速写笔、手工笔之类的。感兴趣或不感兴趣的原因是什么？

4. 你觉得一支笔在什么样的情况下，会变得对你特别有意义、不只是一个写字工具？

5. 想象一下，如果明天有一款笔突然在你身边引起了很多讨论，同学/同事都在聊它，你觉得它可能是什么样的？大家会因为什么在讨论它？

**结束语：**
所有问题都回答完啦，辛苦你认真填写！如果后续有进一步交流的机会，我们再联系你～

# Task

Run `dg-question-type-setter` in mode `final_labels_only`.
```
