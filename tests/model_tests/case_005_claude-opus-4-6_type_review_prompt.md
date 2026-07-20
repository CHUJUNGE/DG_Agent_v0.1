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
description: Set platform question type labels and module type labels for existing Digital Diary / DG drafts. Use when the user asks to label, assign, review, or revise question types for each DG question, including 简答, 单选, 多选, 打分, 排序, AI-bot, 开场白, 结束画面, 中场休息, required image/video markers, and module types such as 访谈题 or 打卡题.
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

It also labels each module as either `访谈题` or `打卡题` for final output. A `打卡题` module is normally a repeated diary task that asks respondents to record the same event or behavior across multiple days, times, or occurrences.

## Required Reference

Before setting question types, read:

- `references/question_type_rules.md`

## Core Workflow

For each pass, work in this order:

```text
Read the current DG draft
-> identify modules, intros, questions, breaks, endings
-> assign one module type to each module
-> assign one platform type to each item
-> choose the correct user-facing type label
-> add required image/video markers when the question requires media upload
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

Keep the original Markdown structure. Add the module type immediately under each module heading. Add the user-facing type label immediately before each question, opening, break, or ending.

For module type labels:

```markdown
### 模块x：...
模块类型：访谈题
```

For repeated diary / check-in modules:

```markdown
### 模块x：...
模块类型：打卡题
事件名称：每日护肤记录
重复频次：7
单位：天
```

For the final user-facing version after wording, do not show backend field names or reasons. Use this compact format:

```markdown
【单选】1. 请选择你喜欢的...
```

For open questions:

```markdown
【简答】1. 请回想最近一次...
```

For required media uploads, append the requirement to the type label:

```markdown
【简答｜必填图片】1. 请上传今天的护肤照片，并简单描述今天使用了哪些产品。
【简答｜必填视频】2. 请上传一段购物过程视频，并说明你当时如何做选择。
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

Use `single` / `单选` only when the question asks for one mutually exclusive answer and the choice has a real routing, branching, screening, segmentation, or follow-up purpose. Do not use single choice merely to make a DG question look structured. If there is no follow-up logic, prefer `text` / `简答`.

Use `multi` / `多选` when the question identifies multiple applicable items and those selections drive later follow-up questions, display logic, or analysis by selected need/scene/channel/product. Do not use multi choice as a surface checklist without corresponding follow-up. If the selected items will not be used, prefer `text` / `简答`.

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
- image or video upload is required by the question;
- AI follow-up is explicitly needed.

Avoid long explanations. One sentence is enough.

## Risk Flags

At the end, add a short "题型检核摘要" for the researcher only when there are meaningful issues:

- too many `score` or `sort` questions;
- too many required image/video tasks;
- a `single` / `multi` question lacks clear options;
- a `single` / `multi` question has no clear branching, jump logic, display logic, or selected-option follow-up;
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

Also annotate each module with one module type:

- `访谈题`: a normal module answered once, including open questions, choice questions, stimulus reactions, intros, breaks, and endings.
- `打卡题`: a repeated diary/check-in module where respondents record the same event, behavior, or experience across multiple days, times, or occurrences.

## Annotation Placement

Add the module type immediately under each module heading. Add the question type annotation immediately before the relevant item.

For normal modules:

```markdown
### 模块1：我的基础信息
模块类型：访谈题
```

For repeated diary / check-in modules, preserve the event name, frequency, and unit when known:

```markdown
### 模块3：每日打卡
模块类型：打卡题
事件名称：每日护肤记录
重复频次：7
单位：天
```

If the draft says "每天", "连续7天", "每次使用后", "每晚记录", "发生一次记录一次", or equivalent repeated recording, label the module as `打卡题`. If repetition is unclear, use `访谈题` and flag the uncertainty in the researcher check summary.

Final user-facing output after wording must show only the type label:

```markdown
【简答】1. ...
【单选】2. ...
【多选】3. ...
【打分】4. ...
【排序】5. ...
【AI-bot】6. ...
```

If a question requires an image or video upload, append the required media marker to the type label. Keep the base question type unchanged, usually `简答`:

```markdown
【简答｜必填图片】1. 请上传今天的护肤照片，并简单描述今天使用了哪些产品。
【简答｜必填视频】2. 请上传一段购物过程视频，并说明你当时如何做选择。
```

Use `必填图片` only when the question explicitly requires a photo/image/screenshot upload or when the platform/client requirement makes image upload mandatory. Use `必填视频` only when the question explicitly requires a video upload or when the platform/client requirement makes video upload mandatory. Do not add these markers for optional wording such as "如果方便可以上传", "可以用照片/视频补充", or "欢迎补充".

If both image and video are required, use:

```markdown
【简答｜必填图片｜必填视频】1. ...
```

If the respondent may choose either image or video, do not mark both as required unless the source clearly says both are mandatory. In review mode, note "待确认：图片/视频是否必填".

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

If a question asks the respondent to upload media and explain it, keep the type as `text` / `简答`; mention in the reason that the media request is part of an open diary task when reasons are shown. If the media upload is mandatory, append `必填图片` or `必填视频` to the label.

### `single` / 单选

Use sparingly. Do not use single choice unless it has a clear research or platform purpose.

Use when only one answer should be selected and the answer drives one of:

- jump logic;
- display logic;
- screening or segmentation;
- different follow-up questions;
- analysis by mutually exclusive respondent group.

Common signals:

- yes/no;
- current status;
- one primary option;
- most recent / most common / most important single answer;
- mutually exclusive categories such as age band, city tier, household type, frequency band.

If the options are not listed in the draft, mark "待确认：选项需补齐".

Single choice should usually not stand alone. In designer/review mode, its reason should mention the downstream logic.

Example:

```markdown
【单选；理由：身份选项互斥，且不同身份会跳转到不同的学习/工作/生活节奏简答追问。】
1. 请选择你现在主要的身份：学生 / 白领 / 自由职业 / 其他
```

If there is no branching, selected-option follow-up, or analysis need, prefer `text` / `简答`:

```markdown
【简答】你现在主要在做什么？平时的学习/工作节奏是什么样的？
```

### `multi` / 多选

Use sparingly. Multi choice should usually identify multiple applicable areas that drive later follow-up logic.

Use when multiple answers can be true at the same time and the selected options drive one of:

- jump logic;
- display logic;
- selected-option follow-up;
- need/scene/channel/product-specific probing;
- analysis by selected concern or behavior.

Common signals:

- "哪些", "都有哪些", "包括哪些";
- coexisting people, places, channels, products, brands, activities, information sources, needs, pain points;
- "可以多选" or "请选出所有符合的".

If the question asks "还有哪些" after a fixed list, it can still be `multi` if the expected answer is selecting multiple options; otherwise use `text` for open additions.

Example:

```markdown
【多选；理由：该题用于识别多个并存的健康关注领域，并按所选领域跳转到对应的需求简答追问。】
1. 哪些方面的健康问题会引起您的重视？免疫力 / 睡眠 / 眼睛 / 肠胃 / 心血管 / 关节 / 情绪状态 / 其他
```

Each selected area should lead to a corresponding `简答` follow-up, such as:

```markdown
【简答】你最近在哪些情况下会特别关注睡眠？具体困扰是什么？你现在会怎么应对？
【简答】你通常在什么场景下会意识到肠胃问题？它怎么影响你的饮食、作息或产品选择？
```

If no selected-option follow-up is planned, prefer `text` / `简答`:

```markdown
【简答】最近你最关注哪些健康问题？为什么这些问题会让你在意？
```

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

- Is each module labeled as `访谈题` or `打卡题`?
- Are repeated daily/event recording modules labeled as `打卡题` with event name, frequency, and unit when available?
- Are most DG research questions still `text`?
- Are `single` / `multi` questions supported by clear options?
- Does every `single` / `multi` question have clear branching, jump logic, display logic, selected-option follow-up, or analysis value?
- Are `score` questions limited and justified?
- Are `sort` questions used only with fixed options?
- Are upload-heavy `text` tasks concentrated in a way that may tire respondents?
- Are `必填图片` / `必填视频` markers used only for mandatory upload tasks, not optional media suggestions?
- Are intro, ending, and break messages separated from actual questions?

If problems exist, add a concise "题型检核摘要".
```

---

## Message 2: user

```text
# Source DG Markdown

# 题目设计方案

## 1. 项目理解

- 客户：KACO，笔类品牌，已有礼盒升级与IP联名沉淀，现有增长路径天花板显现
- 商业目标：研判未来三年具备国民级大单品潜力的新品类/新产品方向
- 核心挑战：代际变化（05/10后新生代）× 书写被电子化/AI分流 × 新品爆炸短期消耗逻辑
- 目标人群：05/10后学生、年轻白领；兼顾圈层先锋人群（手帐、速写等）作为趋势信号；关注男性增量机会
- 研究重点：理解"人"的代际变化 → 书写场景与价值变化 → 笔的品类认知与选择逻辑 → 识别国民级大单品机会方向
- 项目类型：产品创新 × 特殊人群研究 × 场景需求研究；无持续追踪背景，需完整画像

---

## 2. 核心研究问题

1. 05/10后新生代的生活方式、兴趣圈层与消费逻辑是什么？哪些需求具备跨人群迁移的共性？
2. 书写场景发生了哪些变化？哪些场景在增加、减少或消失，哪些是新出现的？
3. 笔在这一代人生活中扮演什么角色？是工具、表达媒介、收藏品，还是其他？
4. 用户当前拥有和使用哪些笔？不同笔对应哪些场景，彼此之间是否可替代？
5. 用户评价一支"好笔"的具体标准是什么？哪些维度最关键，哪些是加分项？
6. 哪些产品方向具备从圈层先锋向大众迁移的潜力？

---

## 3. 模块结构总览

| 模块 | 模块目的 | 对应研究问题 |
|------|----------|-------------|
| 模块1：关于我这个人 | 理解受访者本人：身份、生活重心、兴趣圈层、消费习惯、社交角色、生活痛点；建立人物底色，为后续书写场景和产品认知提供解释框架 | Q1 |
| 模块2：我的一天 | 还原典型工作日/学习日的日常节奏，识别书写行为自然嵌入的时间段与场景 | Q1、Q2 |
| 模块3：我和书写 | 理解书写场景的变化：哪些场景在增加、减少、消失或新出现；书写的功能与情感价值 | Q2、Q3 |
| 模块4：我的笔和文具 | 下载受访者当前拥有的笔类产品全貌；建立笔-场景映射；理解购买习惯与消费逻辑 | Q4、Q5 |
| 模块5：我怎么选一支笔 | 深挖评价标准：好看、好写、手感、便携、社交属性、情感价值等具体维度；收集极致体验 | Q5 |
| 模块6：我心目中的下一支笔 | 在已有标准和场景基础上，探索有边界的产品创新方向；识别圈层先锋信号与大众共性需求 | Q6 |

> 工作日/休息日差异：在模块2中用对比追问收集，不单独拆分为两个重复模块。
> 品牌暴露：KACO品牌名延后至模块6或不在Diary中出现，由研究员确认。

---

## 4. 详细题目设计

---

### 模块1：关于我这个人

**引导语：**
欢迎来到这次研究！在正式开始之前，我们想先好好认识一下你。这个模块没有标准答案，请放轻松，用你最自然的方式介绍自己就好。

**题目：**

1. 先来介绍一下你自己吧！可以用关键词、颜色、MBTI、星座，或者任何你觉得能代表自己的方式——欢迎配上照片，让我们看到真实的你。

2. 你现在的生活状态是什么样的？上学、工作、还是其他？每天主要在忙什么？

3. 你的时间和精力主要花在哪些地方？哪些事情对你来说最重要，哪些是你特别享受的？

4. 你有哪些兴趣爱好？哪些是长期坚持的，哪些是最近才开始的？这些爱好通常在什么场合、和谁一起？

5. 可以带我们"云参观"一下你的居住空间吗？拍一段小视频或几张照片，展示你每天待得最久的地方，或者你最用心打理的一个角落。

6. 聊聊你的社交圈吧——你通常和哪些人来往？在不同的圈子里，你通常是什么角色？比如发起活动的人、跟随者、组织者，还是倾听者？

7. 说到花钱，你的大头消费在哪里？有没有哪些不是必需品，但你特别愿意为它花钱的东西？为什么？

8. 如果给你现在的生活打个分（1-10分），你会打几分？扣分主要扣在哪里？

**结束语：**
谢谢你的分享！认识你真的很有意思。接下来我们聊聊你的日常节奏～

---

### 模块2：我的一天

**引导语：**
接下来，请带我们走进你典型的一天。不用刻意美化，就是最真实的日常。

**题目：**

1. 描述一下你最近典型的一天吧——通常几点起床、几点休息？从早到晚，大概都在做什么？

2. 工作日和休息日，你的节奏有什么不同？哪些事情只在工作日发生，哪些只在休息日？

3. 在你的日常里，有没有一些固定的"仪式感"时刻——比如早上的某个习惯、下午的某个放松方式，或者睡前的某个动作？具体说说。

4. 你一天中最有状态的时间段是什么时候？最容易分心或疲惫的时间段呢？

**结束语：**
很好，我们对你的日常有了初步的感觉。接下来聊聊书写这件事～

---

### 模块3：我和书写

**引导语：**
"书写"这件事，对不同的人来说意义完全不同。我们想听听你的真实感受——不只是用笔写字，而是更广义的"动笔"这件事。

**题目：**

1. 你现在还会动笔写东西吗？在哪些情况下会写？请尽量具体描述最近一次动笔的场景——当时在哪里、在做什么、写了什么。

2. 和两三年前相比，你动笔的频率和场合有没有变化？哪些场景写得更多了，哪些写得更少了，有没有完全消失的，或者新出现的？

3. 有没有哪些事情，你觉得"一定要用笔写，不能用手机或电脑替代"？为什么？

4. 除了记录信息，动笔对你还有什么其他意义？比如放松、整理思路、表达自己，或者别的什么？

5. 你有没有特别享受的书写时刻？描述一下那个场景——当时的状态、在写什么、用的什么笔、感觉怎么样。

6. 反过来，有没有让你觉得"写字好麻烦"或者"不想动笔"的时候？是什么情况？

**结束语：**
谢谢你聊了这么多关于书写的感受！接下来我们来看看你现在都有哪些笔～

---

### 模块4：我的笔和文具

**引导语：**
现在，请带我们认识一下你的"笔的世界"。不管多还是少，都欢迎分享。

**题目：**

1. 拍一张你现在拥有的笔的"全家福"吧——笔袋里的、桌上的、抽屉里的，都可以。如果方便，也可以把你的文具收纳区域一起拍进来。

2. 看看这张全家福，哪支笔是你最常用的？哪支是你最喜欢的？这两个答案一样吗？为什么？

3. 有没有最近新买的笔？是什么，为什么买它？

4. 有没有买了但现在不怎么用的笔？是什么情况让它"退休"了？

5. 有没有一直想买但还没买的笔？是什么，是什么让你还没下手？

6. 你通常在哪里买笔？线上还是线下，哪个平台或店铺？买笔的时候，你一般怎么做决定——冲动购买、货比三家，还是有固定偏好？

7. 你一般一次买几支笔？大概多久买一次？每次大概花多少钱？

8. 你有没有特别喜欢或特别不喜欢的笔的品牌？为什么？

**结束语：**
你的笔的世界很有意思！接下来我们聊聊你选笔的标准～

---

### 模块5：我怎么选一支笔

**引导语：**
每个人选笔的逻辑都不一样。我们想深入了解你的标准——不是泛泛的"好用"，而是具体到你真正在意的那些细节。

**题目：**

1. 你觉得一支"好笔"应该是什么样的？请尽量具体——不只是"顺滑""好看"，而是你真正在意的那些细节。

2. 回想一下你用过的笔里，体验最好的一次是什么情况？当时用的是什么笔，好在哪里？尽量描述那种感觉。

3. 反过来，有没有让你特别失望或不舒服的用笔体验？是什么情况，哪里出了问题？

4. 颜值对你选笔有多重要？你理想中的笔在外观上应该是什么样的？

5. 你会在意笔的品牌吗？品牌对你来说意味着什么——品质保证、身份表达，还是其他？

6. 如果一支笔颜值很高但写起来一般，你会买吗？如果写感很好但外观普通呢？

7. 你有没有把笔当作礼物送人，或者收到过笔作为礼物？是什么场合，你怎么看待"笔作为礼物"这件事？

**结束语：**
你对笔的理解很有深度！最后，我们来聊聊你对未来的笔有什么期待～

---

### 模块6：我心目中的下一支笔

**引导语：**
这是最后一个模块，也是最有想象空间的一个。基于你之前分享的一切，我们想听听你对"理想中的笔"的期待。

**题目：**

1. 如果现在市面上有一支笔，能完美解决你某个具体的书写场景或痛点，你最希望它解决的是什么？

2. 你觉得现在的笔类产品，有没有哪些地方让你觉得"一直没有做好"或者"一直没有人做"？

3. 想象一支"最能代表你"的笔——它是什么样的？外观、手感、功能、使用场景，随便说。

4. 如果有一支笔，你愿意每天随身携带、用很多年，它需要具备哪些条件？

5. 你有没有在社交媒体上看到过让你心动的笔或文具内容？是什么，为什么心动？如果有截图或链接，欢迎分享。

6. 最后，用一句话或一个词，说说"笔"对你现在的生活意味着什么。

**结束语：**
非常感谢你完成了所有的填答，你的分享对我们非常有价值！希望你今天过得愉快～

---

## 5. Wording Handoff

- 目标人群语气注意：受访者以05/10后学生和年轻白领为主，语气应轻松、平等、有点好奇感，避免问卷腔和说教感；圈层先锋受访者可能对文具有较强自我表达欲，给足空间；男性受访者可能对"颜值""仪式感"等词有距离感，wording agent注意替换或软化。

- 不能改动/删除：
 - 模块3第2题（书写场景变化，含增加/减少/消失/新出现四个维度，是核心变化链路，不能合并或删除）
 - 模块4第1题（笔的全家福，必填照片，是后续所有追问的素材基础）
 - 模块5第2、3题（极致正负体验，是评价标准的核心采集路径）
 - 模块6第4题（愿意长期随身携带的条件，是国民级大单品潜力的关键判断题）

- 需要延后暴露的品牌/产品/刺激物：KACO品牌名、具体产品线、任何刺激物概念均不在Diary中出现；如有概念测试，建议放IDI承接。

- 需要保留的观察点：
 - 书写场景变化链路（增加/减少/消失/新出现）
 - 笔-场景映射与可替代性
 - 评价标准的具体维度（不能只停留在"好用/好看"）
 - 圈层先锋信号（社媒内容、新兴爱好、新书写场景）
 - 男性增量机会相关线索（把玩感、机械结构、功能性等）

- 必填图片/必填视频要求：
 - 模块1第5题：必填视频或必填照片（居住空间/最常待的角落）
 - 模块4第1题：必填照片（笔的全家福）
 - 以上两处为必填，其余素材请求均为可选补充

- 可能过重或过硬的题面：
 - 模块4第6、7题（购买渠道+频率+金额连续追问，可能显得像调查问卷，建议wording agent合并语气或拆成对话式追问）
 - 模块5第6题（颜值vs写感的二选一设定，可能显得过于假设性，建议软化为"你会怎么权衡"）

- 建议交给dg-question-wording-editor处理：
 - 全部题面的口语化和去checklist化处理
 - 模块3的书写价值相关题面（避免过于文艺或抽象）
 - 模块6的产品想象题面（避免过于开放导致答案泛化，需要保持有边界的引导感）
 - 男性受访者版本的语气适配建议

---

## 6. Agent 检核摘要

- 已对照商业问题与Proposal检核：六个模块完整覆盖"人 × 书写 × 笔"三重研究维度，模块顺序遵循"具体行为/场景 → 变化 → 品类认知 → 产品标准 → 创新方向"链路。
- 品牌暴露风险已控制：KACO及任何刺激物均未在Diary题目中出现，建议概念测试放IDI。
- 媒体任务已控制：全卷仅2处必填素材（空间视频/照片 + 笔的全家福照片），其余均为可选，负担可控。
- 单题单点已执行：模块4的全家福后续追问已按维度拆分（最常用/最喜欢/新买/闲置/想买未买），未堆叠在一题。
- 主要风险：Proposal仅提供前8页，产品创新的具体方向假设（如秀丽笔、爆闪马克笔之后的下一个品类方向）未在材料中明确，模块6的创新方向题目目前保持开放探索，如客户有预设方向假设，需补充材料后调整模块6题目设计。

---

## 7. 需要确认的问题

1. Proposal仅提供前8页，是否有后续页面涉及具体目标人群配额（如学生/白领比例、男女比例、圈层先锋定义）？这会影响模块1的画像深度和模块6的创新方向边界。

2. 是否有IDI或入户访谈承接Diary后的深层追问？如有，模块5（评价标准）和模块6（产品创新方向）中的深层感知题可适当减轻Diary负担，转移至IDI。

3. 客户是否有预设的产品创新假设方向（如特定笔类品类、特定功能方向或特定人群切口）？如有，模块6需要围绕客户假设设计有边界的测试题，而非完全开放探索。

# Task

Run `dg-question-type-setter` in mode `review_with_reasons`.
```
