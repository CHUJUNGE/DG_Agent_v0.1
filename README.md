# DG Agent v0.1

Digital Diary / DG 题目设计 Agent 的本地 demo、skill 规则包和工程化雏形。

这个仓库当前不是一个完整生产系统，也不是一个已经训练好的专用模型。它的作用是：

- 跑通从项目材料到 DG 初稿的本地 Agent 链路。
- 把研究员的 DG 设计逻辑沉淀成可版本化的 skill / rules / case cards。
- 为后续 Web 产品、后端服务、算法检索、自动评估、数据库标答对比和训练闭环预留接口。

## 1. 项目定位

DG Agent 的目标是帮助研究员基于 Brief、Proposal、客户内部资料、desk research 等材料生成 Digital Diary 题目设计稿。

当前版本的重点是 **demo-stage full agent skeleton**：

```text
项目材料
-> prompt builder
-> questionnaire designer
-> question type review
-> wording editor
-> final question type labels
-> Markdown DG wording
```

正式产品化后，它应该升级为：

```text
Proposal-first Web 产品
-> 文件解析服务
-> 项目理解与信息完整度校验
-> case / rule retrieval
-> planner / writer / evaluator
-> 对话式修改
-> 平台导出
-> gold answer eval
-> 训练与回归闭环
```

当前仓库可以证明主链路可跑通，但不能替代公司生产环境中的数据库、权限、后端、算法服务、模型训练和质量监控。

## 2. 算法与 Agent 逻辑

当前算法逻辑本质上是 **prompt orchestration + skill rules + lightweight case retrieval + LLM generation + offline review loop**。

### 2.1 当前已实现的链路

```text
case_data / project files
-> scripts/test_prompt_with_cases.py 读取 case 输入
-> src/prompt.py 构建 designer messages
-> ChatAnywhere / OpenAI-compatible API
-> designer draft
-> dg-question-type-setter review_with_reasons
-> dg-question-wording-editor wording pass
-> dg-question-type-setter final_labels_only
-> tests/model_tests 保存输出
```

### 2.2 三层 Agent / Skill 分工

| 层 | 目录 | 职责 |
|---|---|---|
| Questionnaire Designer | `skill/dg-questionnaire-designer/` | 理解项目、拆研究问题、设计模块结构、生成研究逻辑完整的 DG 草稿、输出 Wording Handoff |
| Wording Editor | `skill/dg-question-wording-editor/` | 把 designer 草稿改成受访者可读、自然、低负担的最终 wording |
| Question Type Setter | `skill/dg-question-type-setter/` | 给已有 DG 题目标注平台题型，如简答、单选、多选、打分、排序、AI-bot、开场白、结束画面 |

默认完整执行顺序：

```text
dg-questionnaire-designer
-> dg-question-type-setter review_with_reasons
-> dg-question-wording-editor
-> dg-question-type-setter final_labels_only
```

### 2.3 当前检索逻辑

当前 case retrieval 是轻量关键词匹配，不是正式 RAG。

入口在 `src/prompt.py`：

- `CASE_SELECTION_RULES`：按品类、品牌、研究类型等关键词匹配 case。
- `select_relevant_cases()`：从项目文本中选择最多 2 个相关 case。
- `load_case_cards()`：把相关 case card 注入 prompt。

当前不会调用 embedding、向量数据库或 reranker。

### 2.4 当前评估和闭环逻辑

当前闭环是本地 demo 级：

```text
模型输出
-> 研究员 review / 人工修改
-> scripts/build_demo_loop_report.py
-> gap 分类
-> rule / skill / eval candidate
```

它可以帮助沉淀规则，但还不是生产级自动 evaluator。

### 2.5 后续应补的算法能力

正式算法系统需要补齐：

- 稳定文档解析：PDF / PPT / Word、表格、图片 OCR、页码引用。
- 结构化项目理解：商业问题、研究目标、人群、方法、刺激物、限制条件。
- RAG 检索：case metadata、embedding、reranker、rule tags、researcher notes。
- 独立 evaluator：模块结构、研究覆盖、题面自然度、品牌暴露、受访者负担等评分。
- Gold answer comparison：模型输出与数据库最终版 DG 标答批量对比。
- Gap mining：自动聚类高频错误并生成规则候选。
- Training loop：SFT / preference / eval set / regression gate。
- Model registry：记录 model、skill、prompt、case library 联合版本。

## 3. 技术栈

### 3.1 当前实际使用

| 类型 | 技术 |
|---|---|
| 主要语言 | Python 3 |
| 模型接口 | OpenAI-compatible Chat Completions API |
| 当前 API provider | ChatAnywhere，默认可通过环境变量替换 |
| 输出格式 | Markdown |
| 文档解析依赖 | `pdfplumber`, `python-docx` |
| 规则载体 | Markdown skill references |
| 本地数据 | `case_data/`, `gold_data/`, `tests/` |

### 3.2 requirements

当前 `requirements.txt`：

```text
pdfplumber>=0.11,<0.12
python-docx>=1.1,<2
```

仓库里还存在 `.deps/` 本地依赖目录，主要是本地运行时缓存，不是核心业务代码。

### 3.3 尚未引入但后续需要

正式工程化时预计需要：

- Web framework / API service：FastAPI、Next.js API routes 或公司现有后端。
- 文件解析服务：统一处理 PDF / PPT / Word / OCR / 图片。
- 向量检索：embedding model、vector database、reranker。
- 作业系统：异步任务、重试、状态追踪。
- 数据库：项目材料、final DG 标答、model runs、reviews、eval results。
- 监控：日志、质量 dashboard、模型版本回滚。

## 4. 快速开始

### 4.1 安装依赖

```powershell
pip install -r requirements.txt
```

### 4.2 设置环境变量

```powershell
$env:CHATANYWHERE_API_KEY="your_api_key"
$env:CHATANYWHERE_BASE_URL="https://api.chatanywhere.tech/v1"
$env:CHATANYWHERE_MODEL="claude-opus-4-6"
$env:DG_AGENT_CASE_ROOT="D:\DG_Agent_v0.1\case_data"
```

如果 case 数据放在其他目录，把 `DG_AGENT_CASE_ROOT` 改成包含 `Case_001`、`Case_002` 等文件夹的路径。

### 4.3 连接测试

```powershell
python .\scripts\run_chatanywhere_smoke.py
```

### 4.4 只生成 prompt preview，不调用模型

```powershell
python .\scripts\test_prompt_with_cases.py --case case_006
```

输出写入：

```text
tests/prompt_tests/
```

### 4.5 跑 designer-only

```powershell
python .\scripts\run_model_test.py --case case_001
```

输出写入：

```text
tests/model_tests/
```

### 4.6 跑完整四步链路 dry-run

只生成 prompt，不调用模型：

```powershell
python .\scripts\run_full_model_test.py --case case_006 --model claude-opus-4-6 --dry-run
```

### 4.7 跑完整四步链路

```powershell
python .\scripts\run_full_model_test.py --case case_006 --model claude-opus-4-6
```

完整链路会生成：

- designer prompt
- designer output
- type review prompt / output
- wording prompt / output
- final type prompt / output

## 5. 目录结构与文件作用

```text
DG_Agent_v0.1/
├── README.md
├── requirements.txt
├── src/
├── scripts/
├── case_data/
├── gold_data/
├── references/
├── skill/
├── docs/
└── tests/
```

### 5.1 根目录

| 文件 / 目录 | 作用 |
|---|---|
| `README.md` | 项目总说明，说明算法逻辑、技术栈、运行方式和文件结构 |
| `requirements.txt` | Python 依赖 |
| `.gitignore` | Git 忽略规则 |
| `.deps/` | 本地依赖缓存目录，非核心业务代码 |
| `.agents/` | 本地 agent / Codex 相关配置目录 |
| `.codex/` | 本地 Codex 相关配置目录 |

### 5.2 `src/`

| 文件 | 作用 |
|---|---|
| `src/prompt.py` | 核心 prompt builder；定义数据类、读取规则、选择 case card、构建 designer system/user messages、构建对话修改 prompt |

`src/prompt.py` 关键对象和函数：

| 名称 | 作用 |
|---|---|
| `ChatMessage` | OpenAI-compatible message 数据结构 |
| `ProjectFile` | 输入文件结构 |
| `ProjectInfo` | 项目补充信息结构 |
| `PromptBundle` | prompt messages 与 selected case ids 的封装 |
| `CASE_SELECTION_RULES` | 当前关键词 case 匹配规则 |
| `select_relevant_cases()` | 根据项目文本选择相关 case |
| `build_system_prompt()` | 注入 generation logic、research rules、researcher rules |
| `build_generation_prompt()` | 构建 designer 生成 prompt |
| `build_chat_prompt()` | 构建自由对话修改 prompt |

### 5.3 `scripts/`

| 文件 | 作用 |
|---|---|
| `scripts/test_prompt_with_cases.py` | 从 `case_data` 读取 case 输入，生成 prompt preview，不调用模型 |
| `scripts/run_model_test.py` | 调用模型跑 designer-only 生成 |
| `scripts/run_full_model_test.py` | 跑完整链路：designer -> type review -> wording -> final type labels |
| `scripts/run_chatanywhere_smoke.py` | 测试 ChatAnywhere / OpenAI-compatible API 是否可用 |
| `scripts/build_demo_loop_report.py` | 从模型输出或 review 中提取 gap，生成 demo closed-loop report |
| `scripts/analyze_gold_json.py` | 分析 `gold_data/final_dg_all.json`，生成模块、题型、媒体请求、常见 wording 统计 |
| `scripts/ai_distill_gold_rules.py` | 从 gold data 小批量生成 AI-assisted rule candidates，默认可只写 prompt preview |

### 5.4 `case_data/`

本地测试 case 输入材料。每个 case 是一个项目文件夹：

```text
case_data/
├── Case_001/
├── Case_002/
├── Case_003/
├── Case_004/
├── Case_005/
└── Case_006/
```

每个 case 通常包含：

| 文件类型 | 作用 |
|---|---|
| `Brief` | 项目 brief |
| `Proposal` | 项目方案，当前推荐首选输入 |
| `客户内部资料` | 客户已有沉淀 |
| `Desk Research` | 桌面研究材料 |
| `Final Digital Diary DG` | 最终版 DG 标答；生成 prompt 时应排除，只用于评估或规则蒸馏 |
| `case_info.json` | 可选；补充品类、品牌、目标人群、IDI 信息等 |

新增 case 建议结构：

```text
case_data/
  Case_007/
    【Brief】xxx.docx
    【Proposal】xxx.pdf
    【客户内部资料】xxx.pdf
    【Desk Research】xxx.pptx
    【Final Digital Diary DG】xxx.pdf
    case_info.json
```

### 5.5 `references/`

早期全局规则和 case card 目录。当前更推荐以 `skill/dg-questionnaire-designer/references/` 为主，但这里仍保留历史和全局参考。

| 文件 / 目录 | 作用 |
|---|---|
| `references/generation_logic.md` | 题目生成流程规则 |
| `references/research_rules.md` | 研究设计规则库 |
| `references/researcher_logic_case001.md` | Case 001 研究员逻辑沉淀 |
| `references/case_cards/` | 早期 case cards |
| `references/case_cards/case_001_gum.md` | 口香糖 / gum 项目 case card |
| `references/case_cards/case_002_chocolate.md` | 巧克力项目 case card |
| `references/case_cards/case_003_wonton.md` | 馄饨 / 持续聆听项目 case card |
| `references/case_cards/case_004_45plus_health.md` | 45+ 健康项目 case card |

### 5.6 `skill/`

Agent 行为规则和可版本化 skill 包。

#### `skill/dg-questionnaire-designer/`

| 文件 | 作用 |
|---|---|
| `SKILL.md` | designer skill 入口说明，定义何时触发、读哪些 reference、输出什么 |
| `VERSION.json` | skill、rules、case library、rubric 版本记录 |
| `references/agent_workflow.md` | 完整 Agent 工作流说明 |
| `references/data_contracts.md` | 数据对象和工程接口契约 |
| `references/eval_rubric.md` | designer 输出评估标准 |
| `references/generation_logic.md` | designer 生成流程规则 |
| `references/research_rules.md` | 研究设计规则库 |
| `references/research_design_ai_agent_rules.md` | 从研究员 Word 指导中沉淀的高优先级规则 |
| `references/case_001_gum.md` | designer case card |
| `references/case_002_chocolate.md` | designer case card |
| `references/case_003_wonton.md` | designer case card |
| `references/case_004_45plus_health.md` | designer case card |
| `scripts/prompt.py` | skill 内部 prompt helper 副本或实验脚本 |

#### `skill/dg-question-wording-editor/`

| 文件 | 作用 |
|---|---|
| `SKILL.md` | wording skill 入口说明 |
| `VERSION.json` | wording skill 版本记录 |
| `agents/openai.yaml` | wording agent 默认 system prompt 配置 |
| `references/style_rules.md` | 受访者题面风格规则 |
| `references/rewrite_patterns.md` | 坏例到好例的改写模式 |
| `references/module_tone_guides.md` | 不同模块类型的语气指南 |
| `references/wording_eval_rubric.md` | wording 输出评估标准 |

#### `skill/dg-question-type-setter/`

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 题型标注 skill 入口说明 |
| `VERSION.json` | 题型标注 skill 版本记录 |
| `references/question_type_rules.md` | 平台题型判断规则，包括简答、单选、多选、打分、排序、AI-bot、开场白、结束画面、中场休息等 |

### 5.7 `gold_data/`

离线 gold data 和规则蒸馏材料。

| 文件 / 目录 | 作用 |
|---|---|
| `gold_data/final_dg_all.json` | 数据库导出的历史最终版 DG 标答集合 |
| `gold_data/reports/gold_data_inventory.md` | `analyze_gold_json.py` 生成的统计报告 |
| `gold_data/reports/designer_patterns.json` | 面向 designer skill 的结构和任务模式摘要 |
| `gold_data/reports/wording_patterns.json` | 面向 wording skill 的题面风格模式摘要 |
| `gold_data/ai_distillation/` | AI-assisted rule mining 的 prompt、response 和候选规则输出 |

注意：gold data 不应直接塞进生成 prompt。正确方式是离线蒸馏、人工 review，再把稳定规则写入 skill references。

### 5.8 `docs/`

工程化和产品化设计文档。

| 文件 | 作用 |
|---|---|
| `docs/system_flow.md` | 完整 Agent 系统流程 |
| `docs/demo_full_agent_mapping.md` | demo 阶段与完整 Agent 阶段的映射 |
| `docs/ux.md` | Proposal-first 产品 UX 设计 |
| `docs/engineering_interfaces.md` | 后续后端 API 和数据对象设计 |
| `docs/data_training_iteration.md` | 数据驱动训练和自动迭代方法 |
| `docs/eval_plan.md` | Agent 输出评估计划和评分维度 |
| `docs/skill_iteration_method.md` | 如何把研究员反馈沉淀成 skill |
| `docs/gold_data_skill_distillation.md` | 如何从 gold data 离线蒸馏规则 |
| `docs/closed_loop_status.md` | 当前本地 demo 闭环能力与边界 |

### 5.9 `tests/`

本地测试输出、模型输出和闭环报告。

| 目录 | 作用 |
|---|---|
| `tests/prompt_tests/` | prompt preview 输出 |
| `tests/model_tests/` | 模型输入 prompt、designer output、wording output、type setter output、研究员 review |
| `tests/loop_reports/` | `build_demo_loop_report.py` 生成的闭环报告 |

这些不是传统单元测试，而是 demo / prompt / model run 的记录材料。

## 6. 关键数据流

### 6.1 Prompt 构建数据流

```text
case_data/Case_xxx
-> scripts/test_prompt_with_cases.py
-> load_case_inputs()
-> project_info_for_case()
-> src/prompt.py::build_generation_prompt()
-> tests/prompt_tests/case_xxx_prompt_preview.md
```

### 6.2 模型生成数据流

```text
build_generation_prompt()
-> ChatAnywhere / OpenAI-compatible chat completions
-> tests/model_tests/case_xxx_model_designer_output.md
-> build_wording_prompt()
-> wording output
-> build_type_setter_prompt()
-> final type-labeled output
```

### 6.3 规则迭代数据流

```text
model output / researcher review
-> scripts/build_demo_loop_report.py
-> tests/loop_reports/
-> stable rule candidates
-> skill references / eval rubric / case cards
```

### 6.4 Gold data 离线蒸馏数据流

```text
gold_data/final_dg_all.json
-> scripts/analyze_gold_json.py
-> gold_data/reports/
-> scripts/ai_distill_gold_rules.py
-> gold_data/ai_distillation/
-> human review
-> skill references
```

## 7. 当前边界

当前可以做：

- 从本地 case 材料构建 prompt。
- 调用模型生成 designer draft。
- 执行 designer -> type review -> wording -> final type labels 链路。
- 保存 prompt 和模型输出。
- 分析本地 gold data JSON。
- 根据 review 生成 demo closed-loop report。
- 维护 skill / rule / case card 版本。

当前不能做：

- 生产级 Web 上传和项目管理。
- 稳定 OCR、复杂版面解析、图片理解和页码引用。
- 公司数据库实时连接。
- 公司后端权限、任务、审阅和日志系统。
- embedding / reranker / auto evaluator / model registry。
- 数据库最终版 DG 标答批量对比。
- 自动训练、微调或模型发布。
- 生产监控、灰度、回滚和质量 dashboard。

## 8. 产品工程化路线

### v0.1 Local Demo

- 本地脚本链路。
- prompt builder。
- skill rules。
- case cards。
- 模型输出记录。
- 人工 review 闭环。

### v0.2 Web Demo

- Proposal 上传。
- 项目前置信息表。
- 必填信息完整度校验。
- 信息收集摘要。
- 一键生成 DG 初稿。
- 对话式局部修改。
- 版本保存。

### v0.3 Engineering Integration

- 后端 API 服务化。
- 文件解析服务。
- 项目、权限、任务状态和日志。
- review annotation。
- 初版 evaluator。
- case 检索。

### v0.4 Data Eval

- 接入数据库历史项目输入。
- 接入 final DG gold answers。
- batch generation。
- auto eval。
- gap taxonomy。
- eval set。

### v1.0 Production

- 平台导出 adapter。
- 人审工作台。
- 质量 dashboard。
- 回归门禁。
- model / skill / prompt / case library 联合版本管理。
- 生产监控和回滚。

## 9. 新接手者建议阅读顺序

1. `README.md`：先理解整体定位。
2. `docs/demo_full_agent_mapping.md`：理解 demo 和完整 Agent 的边界。
3. `docs/ux.md`：理解产品形态。
4. `docs/engineering_interfaces.md`：理解未来 API 和数据对象。
5. `src/prompt.py`：理解当前核心生成逻辑。
6. `scripts/run_full_model_test.py`：理解完整本地链路如何执行。
7. `skill/dg-questionnaire-designer/SKILL.md`：理解 designer agent。
8. `skill/dg-question-wording-editor/SKILL.md`：理解 wording agent。
9. `skill/dg-question-type-setter/SKILL.md`：理解题型标注 agent。
10. `docs/data_training_iteration.md`：理解后续数据闭环和训练路线。

## 10. 维护规则

- 不要把大段原始客户材料直接写进 skill。
- 新 case 先提炼 case card，再决定是否进入规则库。
- Gold data 只用于离线蒸馏，不直接注入常规生成 prompt。
- 每次改 skill / rules / prompt，应记录版本和影响。
- 每次模型输出后，最好保留 prompt、output、review 和 gap report。
- 稳定、高频、可泛化的研究逻辑进入 `research_rules.md`。
- 流程级约束进入 `generation_logic.md`。
- 题面自然化规则进入 `dg-question-wording-editor/references/`。
- 题型判断规则进入 `dg-question-type-setter/references/question_type_rules.md`。

