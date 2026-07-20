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
