# Demo Closed Loop Report - case_001

## 1. Run Metadata

- Created at: 2026-07-08T08:17:16.465483+00:00
- Review source: `tests\model_tests\case_001_gpt-5-mini_output_v3 _review.md`
- Selected case cards: case_001, case_002
- Input files: 【Brief】Mars gum.docx (brief), 【Proposal】 Gum Occasion Study - Synocodes - 251218.pdf (proposal), 【客户内部资料】既有知识沉淀.docx (client_material)

## 2. Version Baseline

- skill_version: 0.1.1
- generation_logic_version: 0.1.1
- research_rules_version: 0.1.1
- case_library_version: 0.1.0
- fixed_template_version: 0.1.0
- eval_rubric_version: 0.1.0
- data_contracts_version: 0.1.0
- status: demo_stage_full_agent_skeleton

## 3. Detected Review Gaps

### missing_or_wrong_research_logic

- Hits: 5
- Evidence: （注：模块目的与对应问题仅用于设计逻辑说明；详细题面见下文）
- Evidence: 1. 模块一的引导语以及结束语是可以的，但是其他模块的结束语不行，首先不能直接出现品类以及该板块的目的给受访者，应该是更加口水词的内容，请自行对照final dg去改善
- Evidence: 引导语：这里的“正餐以外的吃吃喝喝”指的是不以填饱肚子为主目的的那些东西——小零食、薄荷糖、含片、能量软糖、能量饮、口喷、口腔清新剂等。请按你真实生活来写，不用担心种类多。

### too_many_examples_or_parentheses

- Hits: 4
- Evidence: - 方法与节奏建议：Digital Diary（6天，包含工作日与休息日），搭配后续深访（如有）用于深入解释行为背后动机
- Evidence: 2. 在这一天里，你会在哪些时刻觉得状态不太在、需要“缓一缓”或需要“提振一下”？举一个最近发生的具体例子，描述当时你在做什么、在哪里、和谁在一起。
- Evidence: 4. 如果你曾经看到过口香糖在收银台或某个位置促销，你会因此而增加购买可能性吗？请描述一次你因此购买或没购买的例子。

### respondent_burden

- Hits: 3
- Evidence: 1. 回想一下你家/包里/工作位经常囤或随手拿的那些“正餐以外”的物品都有哪些？请写出你这周内至少用过或看到过的若干种（可以用逐条短句列出，文字+可选照片）。
- Evidence: - 已做的控制：把情绪场景与功能场景并列、购物任务与实操吃用体验安排在后段以避免前期信息偏差，并鼓励多媒体材料降低文字负担。
- Evidence: - 受访者负担可控性：日记模板尽量精简且可用语音/视频替代，购物与食用任务为指定日并提供替代回溯路径以容纳低频用户。

### bad_question_wording

- Hits: 1
- Evidence: （注：模块目的与对应问题仅用于设计逻辑说明；详细题面见下文）

## 4. Rule / Skill Update Candidates

- `missing_or_wrong_research_logic` (5 hit): update `references/generation_logic.md`. Evidence: （注：模块目的与对应问题仅用于设计逻辑说明；详细题面见下文）
- `too_many_examples_or_parentheses` (4 hit): update `references/research_rules.md`. Evidence: - 方法与节奏建议：Digital Diary（6天，包含工作日与休息日），搭配后续深访（如有）用于深入解释行为背后动机
- `respondent_burden` (3 hit): update `references/research_rules.md + references/eval_rubric.md`. Evidence: 1. 回想一下你家/包里/工作位经常囤或随手拿的那些“正餐以外”的物品都有哪些？请写出你这周内至少用过或看到过的若干种（可以用逐条短句列出，文字+可选照片）。
- `bad_question_wording` (1 hit): update `references/research_rules.md`. Evidence: （注：模块目的与对应问题仅用于设计逻辑说明；详细题面见下文）

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
