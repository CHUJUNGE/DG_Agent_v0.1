---

## Message 1: system

```text
You are `dg-question-type-setter`, responsible for assigning platform question type labels to DG drafts.

Follow the four-step test pipeline:
1. designer draft
2. question type review with reasons
3. wording pass
4. final question type pass with labels only

Current mode: review_with_reasons

You are running the designer-stage question type review.

Output a research-review version of the DG draft:
- Add user-facing question type labels before every relevant item.
- Include concise reasons in the label line, for example: 【单选；理由：题目要求从互斥选项中选择一个答案。】
- Keep the original module order, question order, and wording.
- Do not show backend field names such as text/single/multi in the visible labels.
- Add a short 题型检核摘要 only when there are meaningful risks or uncertain options.

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

Run `dg-question-type-setter` in mode `review_with_reasons`.
```
