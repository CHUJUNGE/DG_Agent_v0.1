# DG Agent Evaluation Rubric

Use this rubric for both offline evaluation and production regression tests.

## Score Scale

Each dimension can be scored 1-5:

- 1 = unusable
- 2 = major issues
- 3 = acceptable draft
- 4 = strong draft
- 5 = close to final DG standard

## Dimensions

### 1. Project Understanding

Checks:

- category / brand understood
- target audience understood
- commercial objective captured
- research objective captured
- important proposal signals preserved

### 2. Research Question Fit

Checks:

- research questions are consumer-level, not copied business slogans
- each research question maps to commercial problem
- no key proposal question omitted

### 3. Module Structure

Checks:

- modules are necessary
- no important module missing
- no obvious redundant module
- module purposes are clear

### 4. Module Order

Checks:

- begins with person / life context where needed
- moves from broad context to category / brand
- task and stimulus modules appear at suitable timing

### 5. Diary vs IDI Split

Checks:

- Diary handles facts, real moments, shallow why, photos/videos
- IDI handles deep perception, complex stimuli, abstract brand meaning
- long/multiple videos are not forced into Diary

### 6. Question Wording

Checks:

- respondent-facing
- natural and open
- not checklist-like
- not overly academic
- no excessive parentheses
- no forced scoring/ranking unless needed

### 7. Respondent Burden

Checks:

- daily questions are not too heavy
- media requests reduce burden rather than add proof burden
- high-end / sensitive audiences are treated with restraint

### 8. Brand Exposure Control

Checks:

- early modules do not reveal brand/product intent
- brand and stimulus questions appear after natural behavior context

### 9. Task Design

Checks:

- shopping/use/cooking tasks are only added when research logic supports them
- task instructions feel natural
- task captures before/during/after

### 10. Fixed Template Compliance

Checks:

- About Me opening questions are exact when module exists
- output format follows required Markdown structure
- confirmation questions are max 3

## Gap Types

Use these labels:

- `missing_module`
- `extra_module`
- `wrong_order`
- `wrong_question_logic`
- `too_rigid`
- `too_generic`
- `too_heavy`
- `too_many_parentheses`
- `brand_exposed_too_early`
- `bad_diary_idi_split`
- `template_violation`
- `gold_logic_mismatch`

## Regression Gate

Candidate version should not ship if:

- average score drops vs previous version
- any core case has severe regression
- fixed About Me template breaks
- confirmation questions exceed 3
- output returns to checklist style
- brand is exposed too early in early modules
