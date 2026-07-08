---
name: dg-questionnaire-designer
description: Design Digital Diary / questionnaire question plans from research Briefs, Proposals, client materials, and researcher feedback. Use when the user asks to generate, review, revise, or systematize DG / Digital Diary modules, respondent-facing questions, research logic, case cards, prompt rules, or evaluation rubrics for consumer research questionnaire design.
---

# DG Questionnaire Designer

Use this skill to help design Digital Diary / DG question plans from project materials.

In production, treat this skill as a versioned research-logic specification layer. It should work with historical project inputs, final DG gold answers, model runs, and automated evaluation results. Do not treat the skill as the only source of model quality.

## Core Workflow

Always work in this order:

```text
Project understanding
-> Commercial problem
-> Core research questions
-> Module structure
-> Module observation points
-> Respondent-facing questions
-> Agent self-check
-> Necessary confirmation questions
```

Do not jump directly from project files to questions.

## Required References

Before generating a first draft, read:

- `references/agent_workflow.md`
- `references/generation_logic.md`
- `references/research_rules.md`

When implementing backend, database, training, or evaluation integration, also read:

- `references/data_contracts.md`
- `references/eval_rubric.md`
- `VERSION.json`

Then select relevant case cards only when useful:

- `references/case_001_gum.md`: gum / mouth-related category growth, functional + emotional occasions, shopping task.
- `references/case_002_chocolate.md`: chocolate / snacking / emotional demand spaces / daily frequency growth.
- `references/case_003_wonton.md`: continuous listening / repeat wave / existing sample logic.
- `references/case_004_45plus_health.md`: 45+ / health / VMS / trust and category expansion.

Use case cards for design logic only. Do not copy case questions mechanically.

## Versioned Inputs

When the surrounding system provides versions, preserve or report:

- `skill_version`
- `generation_logic_version`
- `research_rules_version`
- `case_card_version`
- `fixed_template_version`
- `eval_rubric_version`
- `model_version`

These versions are required for later regression testing against final DG gold answers.

Demo v0.1 should already follow the complete stage contract in `references/agent_workflow.md`, even when some stages are implemented as simple prompt logic, placeholder diagnostics, or offline evaluation.

## Output Format

For a first draft, output Chinese Markdown:

```markdown
# 题目设计方案

## 1. 项目理解
## 2. 核心研究问题
## 3. 模块结构总览
## 4. 详细题目设计
## 5. Agent 检核摘要
## 6. 需要确认的问题
```

Keep sections 1-3 concise. Put most detail in section 4.

For each module in section 4, use:

```markdown
### 板块x：模块名

引导语：

题目：

1.
2.
3.

结束语：
```

Do not write “建议题目示例”, “示例题”, or “建议题量”.

Do not add research purpose, design explanation, or internal logic after every question.

## Fixed Template

When generating a “关于我 / About Me / 生活底色 / 基础画像” module, use these three opening questions exactly as questions 1-3 unless the user explicitly asks to change them:

1. 首先，让我们多了解一下你吧！色彩、MBTI、星座、关键词......可以用任何你觉得能代表自己的方式来介绍自己！欢迎多多分享照片，向我们展示真实的你～
2. 和我们聊聊你的学业/工作吧！包括你所在的专业/行业、每天具体要做的事情（如果你有副业，也介绍一下吧！）
3. 可以拍一段小视频，带我们“云参观”一下你的居住空间吗？（比如宿舍/家里的整体布局、你每天待得最久的地方，你最用心打理的一个角落）

## Question Style

Write respondent-facing questions as natural Diary tasks:

- Prefer “请和我们聊聊”, “请描画一下”, “回想一下最近一次”, “如果方便可以”.
- Avoid “每段用一行”, “至少/最多”, “按优先级”, “打分 1-5”, “必须上传” unless required by the project.
- Use fewer parenthetical examples.
- Keep brand/product intent hidden in early modules.
- Make specificity come from real moments, scenes, people, before/after changes, and reasons.

## Revision Workflow

When the user gives feedback:

1. Identify which modules or questions are affected.
2. Preserve unaffected content.
3. Revise the relevant section or provide a complete revised version if asked.
4. If the feedback reveals a reusable rule, propose where to store it:
   - `references/research_rules.md`
   - a case card
   - an eval rubric
   - a fixed template

If the user says the output is “太死板 / 太像 checklist / 括号太多 / 太命令式”, rewrite the respondent-facing wording first.

## Data-Driven Iteration Workflow

When historical gold-answer data is available, use this workflow:

```text
historical input materials
-> current model generates DG
-> compare with final DG gold answer
-> identify module, logic, wording, and burden gaps
-> produce eval result and gap report
-> propose updates to rules, case cards, templates, retrieval, or training data
-> run regression test before updating production
```

Prefer database-driven gold-answer comparison over endless manual prompt tweaking.

Gap types to classify:

- missing module
- extra module
- wrong module order
- wrong research logic
- too generic
- too rigid / checklist-like
- too many examples or parentheses
- respondent burden too high
- brand exposed too early
- Diary vs IDI split wrong
- fixed template violation

Only promote a rule into `research_rules.md` when it appears across cases or is high risk.

Use `generation_logic.md` for workflow-level constraints.

Use case cards for case-specific but reusable design logic.

Use training data when the gap requires pattern learning across many examples rather than one explicit rule.

## Demo Script

If prompt construction is needed, use `scripts/prompt.py` as the demo implementation reference.

The script is not the full system. It only builds OpenAI-compatible messages from:

- project info
- parsed project files
- research rules
- generation logic
- selected case cards

## Quality Check

Before finalizing, check:

- Does each module map to a core research question?
- Are early modules about the person and life context, not the target brand?
- Are Diary questions natural and answerable?
- Are tasks too heavy?
- Are confirmation questions limited to at most 3?
- Did the output avoid exposing internal research labels to respondents?

## Gold Answer Evaluation

When comparing against a final DG gold answer, evaluate at three levels:

1. Structure: module presence, module order, task modules, diary days.
2. Research logic: mapping to commercial questions, Proposal coverage, Diary vs IDI split.
3. Question wording: naturalness, openness, fixed templates, respondent burden, brand exposure.

Do not rely only on text similarity. Different wording can be acceptable if the research logic and respondent task are equivalent.
