# Demo to Full Agent Mapping

demo 阶段不是只做一个 prompt 页面，而是以完整 Agent 流程为骨架，先实现用户可见的关键路径，并为后续生产功能留接口。

## Mapping

| Complete Agent Stage | Demo v0.1 表现 | 后续生产实现 |
|---|---|---|
| S1 Intake | 上传文件 + 用户补充说明 | 项目 id、权限、数据库项目材料 |
| S2 Document Parsing | 前端/脚本轻量解析 | 稳定解析服务、OCR、表格、图片、页码 |
| S3 Project Understanding | prompt 内抽取项目理解 | 结构化抽取器 + 校验器 |
| S4 Case & Rule Retrieval | keyword 匹配 case card | 数据库检索、embedding、reranker |
| S5 Research Planning | prompt 生成研究问题和模块 | planner agent / planning service |
| S6 Question Writing | prompt 生成 Markdown DG | writer agent + 模板 + 风格控制 |
| S7 Agent Self-Evaluation | 简短 Agent 检核摘要 | evaluator agent + rubric score |
| S8 Gold Answer Evaluation | 离线文档与接口预留 | 数据库最终 DG 标答批量对比 |
| S9 Revision | 自由对话修改 | stateful revision service |
| S10 Export | 暂不展示 | 平台字段导出 adapter |
| S11 Training Iteration | 文档和数据契约预留 | gap 聚类、训练样本、回归门禁 |

## Demo Must Already Do

- 使用完整输出结构。
- 使用 skill 中定义的生成流程。
- 使用固定 About Me 开场题。
- 记录 selected case cards。
- 保留 prompt / rules / case card 版本。
- 输出少量确认问题。
- 支持自由对话修改。

## Demo Can Stub

- OCR。
- case 向量检索。
- evaluator score。
- gold answer comparison。
- platform export。
- model training loop。

Stub 不代表不设计。接口和数据结构必须存在，后续才能平滑接入你们已有后端、算法和数据库。
