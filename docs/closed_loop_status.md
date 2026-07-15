# Closed Loop Status

本文档说明当前仓库能完成的闭环、不能在本地 demo 内完成的部分，以及为什么后续仍需要公司工程环境、数据库标答和模型训练。

## 1. 当前能完成的 Demo 闭环

当前仓库可以完成一个轻量闭环：

```text
项目材料 / case 摘要
-> prompt builder
-> OpenAI-compatible model 生成 DG 初稿
-> 研究员 review / 人工修改记录
-> gap 分类
-> 规则、rubric、case card 或训练样本候选
-> skill references 迭代
```

对应文件：

- `src/prompt.py`：构建模型 messages。
- `scripts/run_model_test.py`：调用 ChatAnywhere / OpenAI-compatible API 生成模型输出。
- `tests/model_tests/`：保存模型输出与研究员 review。
- `scripts/build_demo_loop_report.py`：把 review 文件整理成闭环报告，输出 gap 和规则候选。
- `tests/loop_reports/`：保存闭环报告。
- `skill/dg-questionnaire-designer/VERSION.json`：记录 skill、规则、case library、rubric 版本。

运行示例：

```powershell
python .\scripts\build_demo_loop_report.py --case case_001
```

这个闭环可以证明：模型输出不是一次性产物，研究员修改意见可以沉淀成下一轮 skill / rules / eval 的候选。

## 2. 当前闭环的边界

本地 demo 只能做“人工 review 驱动的轻量闭环”，不能替代正式生产闭环。

当前可以做：

- 拼接 prompt。
- 选择少量 case card。
- 调用模型生成 Markdown DG。
- 保存模型输出。
- 根据研究员 review 提炼 gap。
- 生成规则候选和 skill 迭代建议。
- 记录版本，支持后续回归比较。

当前做不了：

- 直接连接公司数据库读取历史项目材料。
- 直接读取数据库中的最终版 DG 标答。
- 接入公司后端的项目、权限、文件、任务和审阅系统。
- 接入算法侧 embedding、reranker、auto evaluator、model registry。
- 批量跑历史 case 并自动和标答对比。
- 自动构造训练样本、偏好样本或回归评测集。
- 真正训练、微调或发布新模型版本。
- 做生产质量监控、灰度、回滚和权限审计。

这些限制不是 prompt 能解决的问题，而是工程系统、数据权限、算法服务和模型训练管线的问题。

## 3. 为什么 Skill 仍需要工程环境继续迭代

Skill 在当前阶段拆成三层：`dg-questionnaire-designer` 负责研究逻辑、生成流程和评测标准；`dg-question-wording-editor` 负责题面风格、自然度和负担控制；`dg-question-type-setter` 负责在已有 DG 题目前标注平台题型和判断理由。它们都不是数据库、后端、算法服务或训练系统的替代品。

默认执行链路采用四步：

```text
dg-questionnaire-designer
-> dg-question-type-setter review_with_reasons
-> dg-question-wording-editor
-> dg-question-type-setter final_labels_only
```

第一轮题型标注给研究员看理由，第二轮题型标注只保留最终用户可见题型名。

进入工程环境后，skill 需要继续迭代：

- 从真实项目输入中验证规则是否稳定。
- 从最终 DG 标答中发现当前规则覆盖不到的研究逻辑。
- 根据批量 gap 更新 `research_rules.md`、`generation_logic.md`、case card、`eval_rubric.md`，以及独立 wording skill 的 style / rewrite / rubric references。
- 把版本号与模型版本、prompt 版本、case library 版本绑定。
- 通过回归测试判断 skill 更新是否让旧 case 退步。

所以 skill 的正确定位是：生产 Agent 的研究逻辑规范层和评测来源，而不是最终质量的唯一来源。

## 4. 为什么模型需要数据库训练

只靠 4 个 case card 和 prompt，模型只能学到少量显性规则，无法稳定学会研究员在不同品类、不同客户、不同方法设计之间的隐性判断。

真正提升质量需要：

```text
数据库历史项目输入
+ 最终版 DG 标答
-> 批量生成
-> 自动对比
-> gap 聚类
-> 训练样本 / 偏好样本 / eval set
-> 模型训练或检索增强
-> 回归门禁
```

数据库里的最终 DG 是高价值 gold answer。模型训练应优先学习：

- 模块取舍。
- 模块顺序。
- Diary vs IDI 分工。
- 题面自然度。
- 受访者负担控制。
- 品牌暴露时机。
- 不同品类的任务设计。
- 客户已有沉淀如何继承，而不是从零泛问。

## 5. 推荐下一阶段

### v0.2 Local Demo Closure

- 补齐依赖声明。
- 固化 demo closed-loop report。
- 每次模型输出后必须有 review / gap / rule candidate。

### v0.3 Engineering Integration

- 接公司后端项目与文件接口。
- 接数据库历史项目输入和最终 DG 标答。
- 建立 batch run eval。
- 建立 auto evaluator 的第一版结构化输出。

### v0.4 Data Training Loop

- 从 gold answer 对比中构造训练样本。
- 建立固定 eval set 和回归门禁。
- 记录 model / skill / prompt / case library 联合版本。
- 支持模型、skill、prompt 的联合迭代。

### v1.0 Production Agent

- 前端审阅工作台。
- 权限、日志、监控。
- 平台导出 adapter。
- 自动评测 dashboard。
- 生产模型发布与回滚机制。
