---
name: dg-questionnaire-designer
description: Design Digital Diary / questionnaire research plans from Briefs, Proposals, client materials, and researcher feedback. Use when the user asks to generate, review, revise, or systematize DG / Digital Diary project understanding, commercial and research questions, module structure, observation points, Diary vs IDI split, task logic, case cards, research rules, or evaluation rubrics. For respondent-facing wording polish, hand off to dg-question-wording-editor.
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
-> Research-complete question draft
-> Wording handoff
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

## Wording Handoff

This skill owns research logic, not detailed respondent-facing style rules.

After generating or revising a research-complete DG draft, hand off the detailed wording pass to `dg-question-wording-editor` when:

- the user asks for more natural,口语化, less rigid, or less checklist-like wording;
- the draft contains many parenthetical examples, hard counts, ranking/scoring language, or forced media uploads;
- the next production step is a separate wording agent.

Preserve in the handoff:

- module order and module purpose;
- corresponding research questions;
- required observation points;
- Diary vs IDI split and task timing;
- brand/product exposure constraints;
- any fixed template or client-required wording.

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

If the user says the output is “太死板 / 太像 checklist / 括号太多 / 太命令式”, preserve the research logic and route the affected sections through `dg-question-wording-editor`.

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
- Are Diary tasks logically answerable before wording polish?
- Are tasks too heavy from a research-design perspective?
- Are confirmation questions limited to at most 3?
- Did the output avoid exposing internal research labels to respondents?

## Gold Answer Evaluation

When comparing against a final DG gold answer, evaluate at three levels:

1. Structure: module presence, module order, task modules, diary days.
2. Research logic: mapping to commercial questions, Proposal coverage, Diary vs IDI split.
3. Question wording: naturalness, openness, fixed templates, respondent burden, brand exposure.

Do not rely only on text similarity. Different wording can be acceptable if the research logic and respondent task are equivalent.
