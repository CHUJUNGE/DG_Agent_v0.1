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
- returning-wave projects do not repeat full profile modules without a reason
- space-based modules are not repetitive copies when research-dimension modules would work better

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
- mandatory photos/videos/audio/screenshots are limited and justified
- long videos, complete process recordings, physical sorting, shelf audits, or collage-style tasks are flagged as high burden
- repeated media requests reuse earlier materials where possible
- multi-room or multi-space video requests are counted and reduced when excessive

### 8. Brand Exposure Control

Checks:

- early modules do not reveal brand/product intent
- brand and stimulus questions appear after natural behavior context
- early brand/product/stimulus exposure has a clear research reason if present
- slogans, positioning statements, and stimulus language are treated as brand exposure signals

### 9. Task Design

Checks:

- shopping/use/cooking tasks are only added when research logic supports them
- task instructions feel natural
- task captures before/during/after
- repeated daily events are structured as separate entries or clear segments
- workday/rest-day modules are split only when the contrast serves the research question
- 3+ repeated diary modules explain why multiple days or repeated structures are needed
- product or device family-photo tasks are followed by focused dimension-by-dimension probes
- sensitive numeric questions use ranges or estimates unless exact values are required
- scoring/rating questions are counted and justified when frequent

### 10. Fixed Template Compliance

Checks:

- About Me opening questions are exact when module exists
- output format follows required Markdown structure
- confirmation questions are max 3
- any About Me template deviation is explicitly marked for researcher confirmation

### 11. Module Completion And Platform Hygiene

Checks:

- no unnamed modules
- no empty modules
- no module with zero questions unless explicitly marked as a placeholder
- no raw HTML, test strings, UI placeholders, or repeated junk text in respondent-facing draft
- all modules have a clear purpose or research-question mapping

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
- `unnamed_or_empty_module`
- `excessive_media_burden`
- `repeated_media_request`
- `complex_task_too_heavy`
- `sensitive_numeric_overreach`
- `rating_overuse`
- `about_me_template_drift`
- `raw_platform_or_test_text`
- `returning_wave_profile_repeated`
- `space_module_repetition`
- `too_many_space_videos`
- `repeated_diary_without_rationale`
- `family_photo_probe_overstacked`
- `slogan_or_positioning_exposed`

## Regression Gate

Candidate version should not ship if:

- average score drops vs previous version
- any core case has severe regression
- fixed About Me template breaks
- confirmation questions exceed 3
- output returns to checklist style
- brand is exposed too early in early modules
- unnamed or empty modules are present
- high-burden media tasks are not flagged
- repeated daily events are collapsed into an unclear long question
