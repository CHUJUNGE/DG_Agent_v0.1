# Demo Closed Loop Report - case_001

## 1. Run Metadata

- Created at: 2026-07-08T02:47:43.218306+00:00
- Review source: `tests\model_tests\case_001_gpt-5-mini_review_v2.md`
- Selected case cards: case_001, case_002
- Input files: 【Brief】Mars gum.docx (brief), 【Proposal】 Gum Occasion Study - Synocodes - 251218.pdf (proposal), 【客户内部资料】既有知识沉淀.docx (client_material)

## 2. Version Baseline

- skill_version: 0.1.0
- generation_logic_version: 0.1.0
- research_rules_version: 0.1.0
- case_library_version: 0.1.0
- fixed_template_version: 0.1.0
- eval_rubric_version: 0.1.0
- data_contracts_version: 0.1.0
- status: demo_stage_full_agent_skeleton

## 3. Detected Review Gaps

### too_many_examples_or_parentheses

- Hits: 6
- Evidence: 不需要每个都有括号去解释，为了引导而引导，仍然死板，但比上一版好一点
- Evidence: 3. 最近一个月里让你觉得“状态不好/不自在”的主要原因是什么？请举一个最近发生的具体小例子来说明那种感觉。
- Evidence: 3. 有没有你会有“准备上场/重要时刻前”的例子（例如面试、汇报、见朋友等）？请描述一次最近的例子和当时你为了准备/缓解紧张做了什么。

### respondent_burden

- Hits: 6
- Evidence: 4. 在日常里，你通常用哪几种简单方式来“调节情绪/恢复状态”（可以是喝饮料、吃东西、听歌、走动、呼吸等，按重要性列出最多 5 个，并简短说明为什么选它们）。
- Evidence: 2. 在这一天里，你什么时候最容易感到“精神下滑”或“注意力不集中”？请具体描述至少一个场景（时间、地点、当时在做什么、当时感受）。
- Evidence: 1. 请列出你最近一周里至少 5 种你在正餐之外会吃或喝的东西（例如：茶饮、咖啡、零食、薄荷糖、口香糖、坚果、小面包等），并在每种后面写上你通常在什么场合吃它（例如：通勤/午后下午茶/加班）。

### missing_or_wrong_research_logic

- Hits: 3
- Evidence: 引导语：我们把“正餐以外、不以填饱为目的”的那些吃喝统称为“随手小吃/小饮”，请帮我们画出你最近一周里这些小东西的地图。
- Evidence: 结束语：谢谢你的回答。下面进入我们的日记模块——我们会请你在接下来 6 天中记录发生的具体时刻。
- Evidence: 内部提示（仅供研究员/项目团队）：日记模块应区分“功能性场景”和“情绪性场景”；购物任务优先线下拍照+短视频，无法线下者提供 O2O 截图与操作视频替代。鼓励受访者使用语音或短视频以降低文字负担。

### too_rigid_or_checklist

- Hits: 2
- Evidence: 不需要每个都有括号去解释，为了引导而引导，仍然死板，但比上一版好一点
- Evidence: 问题1“每段用一行写清时间和活动”语气太命令

### bad_question_wording

- Hits: 2
- Evidence: 问题1“每段用一行写清时间和活动”语气太命令
- Evidence: 问题2“描述一个场景比较random”，意思是这个意思，比如“精神下滑”或“注意力不集中”又太specific了，为了具体而具体

## 4. Rule / Skill Update Candidates

- `too_many_examples_or_parentheses` (6 hit): update `references/research_rules.md`. Evidence: 不需要每个都有括号去解释，为了引导而引导，仍然死板，但比上一版好一点
- `respondent_burden` (6 hit): update `references/research_rules.md + references/eval_rubric.md`. Evidence: 4. 在日常里，你通常用哪几种简单方式来“调节情绪/恢复状态”（可以是喝饮料、吃东西、听歌、走动、呼吸等，按重要性列出最多 5 个，并简短说明为什么选它们）。
- `missing_or_wrong_research_logic` (3 hit): update `references/generation_logic.md`. Evidence: 引导语：我们把“正餐以外、不以填饱为目的”的那些吃喝统称为“随手小吃/小饮”，请帮我们画出你最近一周里这些小东西的地图。
- `too_rigid_or_checklist` (2 hit): update `references/research_rules.md`. Evidence: 不需要每个都有括号去解释，为了引导而引导，仍然死板，但比上一版好一点
- `bad_question_wording` (2 hit): update `references/research_rules.md`. Evidence: 问题1“每段用一行写清时间和活动”语气太命令

## 5. Current Demo Loop

1. Build prompt from project files, rules, generation logic, and selected case cards.
2. Generate the DG draft with an OpenAI-compatible model.
3. Record researcher review or model-review notes under `tests/model_tests/`.
4. Build this loop report to classify gaps and propose rule / rubric / training updates.
5. Promote only stable, reusable findings into skill references; keep one-off project details out of the skill.

## 6. Not Solvable Inside This Local Demo

- Company database connection: requires production credentials, project permissions, schema access, and data governance.
- Company backend integration: requires API contracts, auth, file storage, job orchestration, and deployment environment.
- Algorithm service integration: requires embedding/reranker/evaluator services and model registry access.
- Gold-answer evaluation at scale: requires historical input materials paired with final DG gold answers from the database.
- Model training or fine-tuning: requires curated training/eval datasets, approved training pipeline, model versioning, and regression gates.
- Production monitoring: requires logs, user feedback capture, quality dashboards, and rollback/version controls.

## 7. Production Loop Required Next

Database historical inputs + final DG gold answers -> batch generation -> auto evaluation -> gap clustering -> skill/rule candidates + training samples -> regression gate -> new model/skill release.
