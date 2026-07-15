# Engineering Interfaces

本文档定义 DG Agent 从 demo 走向正式工程化时建议保留的接口。

## 1. 核心数据对象

### ProjectFile

```ts
type ProjectFile = {
  id: string;
  filename: string;
  fileType: "pdf" | "ppt" | "pptx" | "doc" | "docx" | "txt" | "md";
  sourceType?: "brief" | "proposal" | "internal" | "desk_research" | "final_reference" | "other";
  extractedText: string;
  metadata?: {
    pageCount?: number;
    slideCount?: number;
    wordCount?: number;
    parserVersion?: string;
  };
};
```

### ProjectInfo

```ts
type ProjectInfo = {
  category?: string;
  brand?: string;
  targetAudience?: string;
  method?: string;
  hasIdi?: string;
  outputPreference?: "markdown";
  extraNotes?: string;
};
```

### PromptBuildRequest

```ts
type PromptBuildRequest = {
  projectInfo: ProjectInfo;
  files: ProjectFile[];
  selectedCaseIds?: string[];
  mode?: "first_draft" | "revision";
};
```

### DesignOutput

```ts
type DesignOutput = {
  markdown: string;
  selectedCaseIds: string[];
  model: string;
  createdAt: string;
  diagnostics?: {
    tokenEstimate?: number;
    missingInfo?: string[];
    riskFlags?: string[];
  };
};
```

### QuestionTypeAnnotation

用于题型标注层。当前阶段不要求生成后端导入 JSON，只在现有 DG Markdown 中为每道题前置平台题型和判断理由。

```ts
type PlatformQuestionType =
  | "text"      // 简答
  | "single"    // 单选
  | "multi"     // 多选
  | "score"     // 打分
  | "sort"      // 排序
  | "bot"       // AI-bot
  | "start"     // 开场白
  | "end"       // 结束画面
  | "halftime"; // 中场休息

type QuestionTypeAnnotation = {
  moduleName?: string;
  itemText: string;
  type: PlatformQuestionType;
  label: "简答" | "单选" | "多选" | "打分" | "排序" | "AI-bot" | "开场白" | "结束画面" | "中场休息";
  reason?: string; // designer/review 阶段可见；wording 后最终版本不显示
  uncertainty?: string;
};
```

### ReviewAnnotation

```ts
type ReviewAnnotation = {
  caseId?: string;
  section: string;
  originalText: string;
  revisedText?: string;
  issueType:
    | "too_long"
    | "too_rigid"
    | "wrong_research_logic"
    | "too_many_examples"
    | "missing_module"
    | "bad_question_wording"
    | "respondent_burden"
    | "other";
  researcherComment: string;
  ruleCandidate?: string;
};
```

### TrainingCase

正式系统中从数据库抽取的训练/评测样本。

```ts
type TrainingCase = {
  caseId: string;
  projectType: string[];
  category?: string;
  brand?: string;
  targetAudience?: string;
  inputMaterials: {
    brief?: string;
    proposal?: string;
    internalMaterials?: string[];
    deskResearch?: string[];
  };
  goldDgMarkdown: string;
  metadata?: {
    moduleNames?: string[];
    diaryDays?: number;
    hasShoppingTask?: boolean;
    hasIdi?: boolean;
    sourceProjectId?: string;
  };
};
```

### ModelRun

```ts
type ModelRun = {
  runId: string;
  caseId: string;
  modelVersion: string;
  skillVersion: string;
  promptVersion: string;
  caseLibraryVersion?: string;
  generatedMarkdown: string;
  createdAt: string;
};
```

### AutoEvalResult

```ts
type AutoEvalResult = {
  runId: string;
  caseId: string;
  overallScore: number;
  gaps: Array<{
    type:
      | "missing_module"
      | "extra_module"
      | "wrong_order"
      | "wrong_question_logic"
      | "too_rigid"
      | "too_generic"
      | "too_heavy"
      | "brand_exposed_too_early"
      | "bad_diary_idi_split"
      | "template_violation";
    evidence: string;
    goldReference?: string;
    suggestedRule?: string;
  }>;
};
```

## 2. API 拆分

### POST /api/parse-files

用途：解析上传文件，返回文本。

demo 阶段：

- 可在前端本地解析。
- 后端只接收已经解析的文本。

完整系统：

- 后端统一解析。
- 支持页码、表格、图片 OCR、段落类型识别。

请求：

```ts
type ParseFilesRequest = {
  files: File[];
};
```

响应：

```ts
type ParseFilesResponse = {
  files: ProjectFile[];
  warnings?: string[];
};
```

### POST /api/build-prompt

用途：将结构化项目材料、规则库和 case cards 拼成模型 messages。

请求：

```ts
type BuildPromptRequest = PromptBuildRequest;
```

响应：

```ts
type BuildPromptResponse = {
  messages: Array<{ role: "system" | "user" | "assistant"; content: string }>;
  selectedCaseIds: string[];
};
```

### POST /api/generate-design

用途：调用模型生成第一版题目设计。

请求：

```ts
type GenerateDesignRequest = {
  messages: Array<{ role: "system" | "user" | "assistant"; content: string }>;
  model?: string;
};
```

响应：

```ts
type GenerateDesignResponse = DesignOutput;
```

### POST /api/revise-design

用途：自由对话式修改。

请求：

```ts
type ReviseDesignRequest = {
  currentDesignMarkdown: string;
  userMessage: string;
  history?: Array<{ role: "user" | "assistant"; content: string }>;
  projectContext?: {
    projectInfo?: ProjectInfo;
    files?: ProjectFile[];
    selectedCaseIds?: string[];
  };
};
```

响应：

```ts
type ReviseDesignResponse = {
  markdown: string;
  changeSummary?: string[];
  needsFullRegeneration?: boolean;
};
```

### POST /api/evaluate-design

用途：评估生成结果。

demo 阶段可以先不做，或只输出 checklist。

完整系统建议检查：

- 是否覆盖商业问题。
- 是否覆盖 Proposal 中的研究目标。
- 模块是否遗漏或过重。
- 题目是否可分析。
- 语言是否自然。
- 是否过早暴露品牌。
- 是否有过多括号、打分、排序、强制上传。
- 是否存在受访者负担风险。

请求：

```ts
type EvaluateDesignRequest = {
  projectInfo: ProjectInfo;
  files: ProjectFile[];
  designMarkdown: string;
  rubricVersion?: string;
};
```

### POST /api/set-question-types

用途：在已有 DG Markdown 上标注题型。该接口不负责平台导入字段映射；最终用户可见版本只显示中文题型名，例如 `【单选】1. ...`。designer/review 阶段可以额外返回理由。

请求：

```ts
type SetQuestionTypesRequest = {
  designMarkdown: string;
  mode?: "final_labels_only" | "review_with_reasons";
};
```

响应：

```ts
type SetQuestionTypesResponse = {
  annotatedMarkdown: string;
  annotations?: QuestionTypeAnnotation[];
  checks?: Array<{
    id: string;
    status: "pass" | "warning";
    message: string;
    evidence?: string;
  }>;
};
```

### POST /api/eval-against-gold

用途：将模型生成结果与数据库中的最终版 DG 标答对比。

请求：

```ts
type EvalAgainstGoldRequest = {
  trainingCase: TrainingCase;
  modelRun: ModelRun;
  rubricVersion?: string;
};
```

响应：

```ts
type EvalAgainstGoldResponse = AutoEvalResult & {
  dimensionScores: {
    projectUnderstanding: number;
    researchQuestionFit: number;
    moduleStructure: number;
    moduleOrder: number;
    questionWording: number;
    respondentBurden: number;
    brandExposureControl: number;
    diaryIdiSplit: number;
    taskDesign: number;
    goldSimilarity: number;
  };
};
```

### POST /api/batch-run-eval

用途：批量从数据库抽取历史 case，让当前模型生成并与标答对比。

请求：

```ts
type BatchRunEvalRequest = {
  caseQuery: {
    projectTypes?: string[];
    categories?: string[];
    dateRange?: [string, string];
    limit?: number;
  };
  modelVersion: string;
  skillVersion: string;
  promptVersion: string;
};
```

响应：

```ts
type BatchRunEvalResponse = {
  batchId: string;
  totalCases: number;
  completedCases: number;
  summary: {
    averageScore: number;
    passRate: number;
    topGapTypes: Array<{ type: string; count: number }>;
  };
};
```

### POST /api/generate-rule-candidates

用途：基于批量评测 gap 聚类，自动生成规则、case card 或训练样本候选。

请求：

```ts
type GenerateRuleCandidatesRequest = {
  batchId: string;
  minFrequency?: number;
};
```

响应：

```ts
type GenerateRuleCandidatesResponse = {
  candidates: Array<{
    target:
      | "research_rules"
      | "generation_logic"
      | "case_card"
      | "fixed_template"
      | "training_data"
      | "retrieval_strategy";
    rationale: string;
    proposedText?: string;
    examples: string[];
    riskLevel: "low" | "medium" | "high";
  }>;
};
```

### POST /api/regression-gate

用途：模型、prompt、skill 或 case library 更新前的上线门禁。

请求：

```ts
type RegressionGateRequest = {
  previousVersion: {
    modelVersion: string;
    skillVersion: string;
    promptVersion: string;
  };
  candidateVersion: {
    modelVersion: string;
    skillVersion: string;
    promptVersion: string;
  };
  evalSetId: string;
};
```

响应：

```ts
type RegressionGateResponse = {
  pass: boolean;
  summary: {
    previousAverageScore: number;
    candidateAverageScore: number;
    regressions: Array<{
      caseId: string;
      dimension: string;
      previousScore: number;
      candidateScore: number;
    }>;
  };
};
```

响应：

```ts
type EvaluateDesignResponse = {
  score?: number;
  checks: Array<{
    id: string;
    status: "pass" | "warning" | "fail";
    message: string;
    evidence?: string;
  }>;
  suggestedFixes?: string[];
};
```

### POST /api/export

用途：把 Markdown 题目方案转成平台字段草案。

注意：用户已明确“不需要固定字段”，所以 demo 阶段不做强制导出。完整系统中只作为适配层。

请求：

```ts
type ExportRequest = {
  designMarkdown: string;
  targetFormat: "platform_draft" | "csv" | "json";
};
```

响应：

```ts
type ExportResponse = {
  items: Array<{
    moduleName: string;
    intro?: string;
    questionText: string;
    questionType?: string;
    mediaRequest?: string;
    logicNote?: string;
  }>;
};
```

## 3. 前端状态建议

```ts
type DemoState = {
  uploadedFiles: ProjectFile[];
  projectInfo: ProjectInfo;
  chatHistory: Array<{ role: "user" | "assistant"; content: string }>;
  currentDesignMarkdown?: string;
  selectedCaseIds: string[];
  isGenerating: boolean;
  error?: string;
};
```

## 4. Skill 与工程接口的关系

skill 不直接负责 UI 或 API。

skill 负责：

- 定义 Agent 该如何理解项目。
- 定义如何选择 case card。
- 定义题目设计流程。
- 定义输出格式和质量标准。

工程接口负责：

- 文件解析。
- 模型调用。
- 会话状态。
- 结果保存。
- 人审标注。
- 平台字段导出。

## 5. 后续迭代接口

建议预留一个反馈接口：

### POST /api/submit-review

```ts
type SubmitReviewRequest = {
  projectId: string;
  modelOutputId: string;
  annotations: ReviewAnnotation[];
};
```

用途：

- 记录研究员为什么改。
- 抽象成新规则。
- 进入 eval set。
- 未来作为 case library 的训练/检索素材。

正式系统中，人工反馈接口不是唯一迭代来源。主路径应是：

```text
数据库历史输入 + 最终 DG 标答
-> 批量生成
-> 自动对比
-> gap 聚类
-> 规则 / 训练 / 检索候选
-> 回归测试
```
