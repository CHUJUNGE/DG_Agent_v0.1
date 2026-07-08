# Skill Iteration Method

本文档说明 demo 阶段如何把研究员反馈逐步沉淀成 skill。

## 1. 为什么不直接“训练”

当前只有少量 case，直接微调或期待模型从 prompt 中完全学会研究员逻辑，效果不会稳定。

demo 阶段更适合做：

- 规则抽取。
- case card 抽象。
- 评测集建设。
- 人审反馈闭环。
- skill 化沉淀。

## 2. 每次新增 case 的处理方式

不要直接把所有原始材料塞进 skill。

推荐步骤：

1. 收集原始输入：Brief / Proposal / 客户资料 / Final DG。
2. 提炼 case card：
   - 项目类型
   - 商业问题
   - 研究目标
   - 模块结构
   - 关键题目逻辑
   - 可复用规则
   - 不可泛化的特殊点
3. 跑 demo 输出。
4. 对比正式 DG 或研究员修改版。
5. 记录 gap。
6. 把稳定规律写进：
   - `references/research_rules.md`
   - `references/generation_logic.md`
   - 对应 case card
   - eval rubric

## 3. 研究员反馈如何记录

建议每条反馈尽量写成：

```text
原输出：
研究员意见：
正式版/修改后：
问题类型：
可沉淀规则：
适用范围：
```

问题类型可以包括：

- 模块错了。
- 模块顺序错了。
- 问题太死板。
- 问题太泛。
- 过早暴露品牌。
- 题量太重。
- 需要 Diary，不适合 IDI。
- 需要 IDI，不适合 Diary。
- 素材要求不合理。
- 缺少任务模块。
- 不该套用某个 case。

## 4. 哪些内容进入 skill

进入 skill：

- 稳定的工作流。
- 高频错误规避。
- 固定题面模板。
- case card。
- 评估 checklist。
- 可复用脚本。

不进入 skill：

- 大段原始客户材料。
- 只对单个项目有效的细节。
- 未验证的个人偏好。
- 过长的完整输出样例。

## 5. Skill 文件更新规则

`SKILL.md` 只放核心流程和触发规则。

详细内容放到：

- `references/generation_logic.md`
- `references/research_rules.md`
- `references/case_xxx.md`

如果 `SKILL.md` 太长，后续模型每次加载都会变慢、变贵，也更容易跑偏。

## 6. Eval Set 建设

每个 case 至少保留：

- 输入材料摘要。
- 模型输出。
- 正式 DG 或研究员修订版。
- gap review。
- 关键评分项。

建议评分维度：

1. 项目理解是否正确。
2. 核心研究问题是否贴合商业问题。
3. 模块结构是否合理。
4. 题目是否自然、开放、可回答。
5. 是否有无用题。
6. 是否过早暴露品牌。
7. 是否控制受访者负担。
8. 是否正确处理 Diary vs IDI。
9. 是否符合固定模板要求。
10. 是否只提出少量必要确认问题。

## 7. Demo 到完整系统的升级路径

### v0.1

- prompt builder
- case cards
- Markdown 输出
- 人工 review

### v0.2

- 前端上传解析
- Vercel API proxy
- 自由对话修改
- review annotation 格式

### v0.3

- evaluator
- case 检索
- 规则自动建议
- prompt / skill 自动回归测试

### v1.0

- 正式平台集成
- 人审工作台
- 评测集 dashboard
- 导出适配
- 运行监控
