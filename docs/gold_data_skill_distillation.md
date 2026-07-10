# Gold Data Skill Distillation

The final DG database export should not be loaded into normal generation context. It is too large, noisy, and project-specific.

Use it as an offline learning source:

```text
final_dg_all.json
-> compact project/module/question digests
-> AI-assisted rule mining on small batches
-> AI rule candidate report
-> human review
-> promote compact rules into skills
-> regression test against gold DG cases
```

## What Enters Runtime Context

Only compact, reviewed rules should enter the two skills:

- questionnaire structure rules
- module order rules
- Diary vs IDI split rules
- task design rules
- wording rewrite rules
- burden-control rules
- brand-exposure rules

Raw project JSON, full final DG questions, and large pattern files should not be injected into prompts.

## Local Commands

Generate inventory and broad pattern summaries:

```powershell
python scripts\analyze_gold_json.py
```

Generate AI-assisted rule candidates. By default this only writes prompt previews and does not call the model:

```powershell
python scripts\ai_distill_gold_rules.py --max-projects 12 --batch-size 4 --focus both
```

Actually call the configured OpenAI-compatible API:

```powershell
python scripts\ai_distill_gold_rules.py --max-projects 12 --batch-size 4 --focus both --run
```

Use smaller batches first, review output quality, then scale up.

AI distillation outputs are written under `gold_data/ai_distillation/`, which is intentionally ignored by git because it is derived from real project data.

## Designer Skill Learns

`dg-questionnaire-designer` should learn from gold data at the rule level:

- which module patterns appear repeatedly across similar research types
- when historical DGs keep or compress About Me / life-context modules
- when diary, shopping, usage, trial, or stimulus tasks are added
- where brand/product exposure usually appears
- which high-frequency structures still conflict with current research rules

The output should be compact candidate text for `research_rules.md`, `generation_logic.md`, case cards, or eval rubric updates.

## Wording Skill Learns

`dg-question-wording-editor` should learn from gold data at the rewrite-pattern level:

- how final DGs invite real moments and scenes
- how media requests are softened
- how module intros and endings sound natural
- which historical samples are too heavy and should become negative examples
- which repeated phrasing patterns improve answerability without increasing burden

The output should be compact candidate text for `style_rules.md`, `rewrite_patterns.md`, `module_tone_guides.md`, or wording eval rubric updates.

## Conflict Rule

If mined gold-data patterns conflict with existing rules, current rules win.

Treat the conflict as evidence for review, not as automatic skill modification.
