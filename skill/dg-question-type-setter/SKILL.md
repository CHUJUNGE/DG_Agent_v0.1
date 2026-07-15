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
