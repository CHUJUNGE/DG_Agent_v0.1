# DG Questionnaire Agent Workflow

This is the complete workflow the skill should follow. Demo v0.1 may not fully implement every stage, but the stage contract should already exist.

## Stage Map

| Stage | Name | Demo v0.1 | Production |
|---|---|---:|---:|
| S1 | Intake | implemented | implemented |
| S2 | Document Parsing | partial | full parser / OCR / structure |
| S3 | Project Understanding | LLM prompt | structured extractor + validation |
| S4 | Case & Rule Retrieval | keyword case card selection | database / vector / reranker |
| S5 | Research Planning | LLM prompt | planner agent + rules + retrieved cases |
| S6 | Question Writing | LLM prompt | writer agent + templates + style constraints |
| S7 | Agent Self-Evaluation | brief checklist | evaluator agent + rubric |
| S8 | Gold Answer Evaluation | not shown / offline placeholder | batch comparison vs final DG |
| S9 | Revision | chat prompt | stateful revision service |
| S10 | Export | not shown | platform adapter |
| S11 | Training Iteration | documentation only | data-driven training / regression |

## S1. Intake

Goal: receive user-uploaded project materials and user notes.

Inputs:

- files
- project info
- user notes
- requested output mode

Outputs:

- `ProjectFile[]`
- `ProjectInfo`

Demo:

- local file upload / script input.

Production:

- platform upload, database project id, permission control.

## S2. Document Parsing

Goal: convert raw files into usable text.

Inputs:

- PDF / PPT / Word / TXT / MD

Outputs:

- extracted text
- file type
- source type
- page / slide references if available

Demo:

- local lightweight extraction.

Production:

- stable parser, OCR, image/table extraction, layout handling.

## S3. Project Understanding

Goal: understand the project before writing questions.

Extract:

- project name
- category / brand
- target audience
- commercial objective
- research objective
- method
- existing knowledge
- key assumptions
- unclear points

Output:

- concise project understanding.

## S4. Case & Rule Retrieval

Goal: retrieve relevant design logic.

Demo:

- keyword selection from 4 case cards.

Production:

- search historical cases by project type, category, objective, method, target audience.
- retrieve final DG gold answers and case cards.
- retrieve rules and fixed templates.

Important:

- learn design logic, not copy questions blindly.

## S5. Research Planning

Goal: decide module structure before writing questions.

Outputs:

- core research questions
- module list
- module purpose
- corresponding research question
- Diary vs IDI split
- task module need
- confirmation questions

Rules:

- no direct jump to questions.
- modules must map to commercial and research questions.
- confirmation questions max 3.

## S6. Question Writing

Goal: write respondent-facing DG questions.

Outputs:

- intro
- questions
- ending
- optional media request

Rules:

- write natural Diary tasks.
- avoid checklist language.
- keep early modules brand-light.
- use fixed About Me opening questions.
- do not add internal research explanation after every question.

## S7. Agent Self-Evaluation

Goal: check output before showing it.

Checks:

- research question coverage
- module fit
- respondent burden
- brand exposure
- language naturalness
- fixed template compliance

Demo:

- concise `Agent 检核摘要`.

Production:

- evaluator result object with scores and gap types.

## S8. Gold Answer Evaluation

Goal: compare generated output with final DG gold answer.

Inputs:

- generated DG
- final DG gold answer
- rubric

Outputs:

- score
- gap report
- rule candidates
- training candidates

This stage is not a user-facing demo screen, but it must exist in the system design.

## S9. Revision

Goal: revise output through free chat.

Rules:

- preserve unaffected content.
- revise local modules when possible.
- if feedback is reusable, classify it as rule / case card / template / eval candidate.

## S10. Export

Goal: convert DG Markdown into platform fields.

Demo:

- not implemented.

Production:

- platform question items, types, jumps, media fields, logic notes.

## S11. Training Iteration

Goal: continuously improve from database gold answers.

Loop:

```text
sample historical cases
-> generate with current model + skill
-> compare to gold DG
-> cluster gaps
-> update rules / retrieval / training data
-> run regression gate
-> release new model / skill version
```

This is the long-term quality engine.
