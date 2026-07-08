# Complete Agent System Flow

## 1. Demo vs Complete System

demo 是完整系统的一条最短路径，不是完整 Agent。

```text
Demo:
上传材料 -> 解析文本 -> 拼 prompt -> 调模型 -> Markdown 输出 -> 自由对话修改

Complete Agent:
材料解析 -> 结构化理解 -> 案例/规则检索 -> 研究设计规划 -> 题目生成 -> 自检评估 -> 标答对比 -> 数据驱动迭代 -> 平台导出
```

## 2. 完整 Agent 的工作流

### Step 1. Intake

收集输入：

- Brief
- Proposal
- 客户内部资料
- Desk research
- Final reference
- 用户补充说明

输出：

- 文件清单
- 文本内容
- 文件类型和来源标签

### Step 2. Material Understanding

抽取：

- 项目名称
- 品类/品牌
- 目标人群
- 商业目标
- 研究目标
- 客户已有沉淀
- 方法设计
- 是否有 IDI / 入户 / 后续访谈
- 是否有刺激物
- 关键不确定点

### Step 3. Case / Rule Retrieval

检索：

- 相似项目类型
- 相似品类
- 相似研究目标
- 可复用模块
- 不应泛化的特殊逻辑

当前 demo 用 `case_cards/*.md` 做轻量检索。

完整系统可升级为：

- case metadata
- embedding search
- reranker
- rule tags
- researcher notes

### Step 4. Research Planning

规划：

- 核心研究问题
- 模块结构
- 模块顺序
- 哪些放 Diary
- 哪些放 IDI
- 是否需要任务模块
- 记录天数和受访者负担
- 必要确认问题

### Step 5. Question Writing

生成：

- 模块引导语
- 受访者题面
- 结束语
- 可选素材要求
- 可选追问方向

关键原则：

- 题面先像受访者能回答的问题，再像研究员的逻辑。
- 不要把研究链路逐条翻译成 checklist。
- 固定模板题应锁定，例如“关于我”前三题。

### Step 6. Agent Evaluation

检查：

- 是否覆盖商业问题。
- 是否覆盖 Proposal。
- 是否过早暴露品牌。
- 是否有无效题或重复题。
- 是否过度量化。
- 是否过度命令式。
- 是否有受访者负担风险。

demo 阶段只保留简短 `Agent 检核摘要`。

完整系统应有独立 evaluator。

### Step 7. Gold Answer Evaluation

正式系统应优先使用数据库中的最终版 DG 标答做自动评测。

对比内容：

- 模块是否一致或语义等价。
- 模块顺序是否合理。
- 是否遗漏关键任务。
- 是否覆盖 Proposal。
- 题面是否接近正式 DG 的自然语言。
- 是否存在过重、过硬、过早暴露品牌的问题。

### Step 8. Human Review

demo 阶段需要研究员修改来建立第一版规则。

正式系统中，人审更适合作为抽检、高风险项目复核和新类型项目校准，而不是主要迭代来源。

### Step 9. Feedback to Skill / Rules / Eval / Training

把自动对比 gap 和必要人审意见沉淀为：

- prompt 规则
- skill reference
- case card
- eval rubric
- golden answer
- bad case
- training sample
- retrieval strategy

## 3. 为什么 demo 不应该假装完整

只靠少量模板和 4 个 case card，模型不会真正“学会研究员”。正式系统必须利用数据库里大量最终版 DG 标答。

demo 应避免承诺：

- 自动达到最终 DG 水平。
- 自动理解所有 proposal 复杂逻辑。
- 自动判断所有模块取舍。
- 自动导出平台字段。

demo 应证明：

- 文件上传与文本进入模型链路可行。
- 规则库和 case card 能影响输出方向。
- 研究员可以通过自由对话快速修正。
- 修改意见可以被收集并沉淀为下一版规则。
- 当前 skill / prompt 能作为后续自动评测和训练闭环的基线。

## 4. 下一阶段优先级

1. 建立稳定文件解析。
2. 接入数据库历史输入和最终版 DG 标答。
3. 批量生成并自动对比。
4. 建立 gap taxonomy 和 eval rubric。
5. 抽象高频问题进入 `research_rules.md`。
6. 把 skill 的 `SKILL.md` 保持为核心工作流和版本化规范。
7. 增加回归测试和上线门禁。
8. 再考虑平台导出字段。
