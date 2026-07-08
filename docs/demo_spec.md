# 题目设计 Agent Demo 规格梳理

## 1. Demo 目标

本 demo 用于验证一个最小可用的“题目设计 Agent”能力：

```text
用户上传 Brief / Proposal / 客户内部资料
-> 系统读取并整理项目输入
-> 大模型结合研究员题目设计逻辑
-> 生成 Digital Diary / 问卷题目设计方案
-> 用户可继续对话修改
```

Demo 的核心不是做最终完整 web 产品，而是验证三件事：

1. 大模型能否基于项目材料正确理解商业问题和研究问题。
2. 大模型能否按研究员逻辑先设计模块，再生成题目。
3. 用户能否通过简单交互继续调整题目设计。

### 1.1 已定技术决策

```text
前端：React，部署在 GitHub Pages
后端：Vercel Functions
模型：ChatAnywhere，使用用户自有 API key，允许上传内容发送到外部模型
模型接口：优先使用 OpenAI-compatible Chat Completions
文件解析：优先前端本地解析，Vercel 后端兜底解析
首版文件类型：PPT/PPTX、PDF、Word/DOCX、TXT、MD
首版输出：Markdown
交互方式：自由对话，不设置快捷 prompt 按钮
首版不做：下载结果、Case_001 few-shot 示例
```

---

## 2. Demo 范围

### 2.1 Demo 必须实现

- 本地上传多个文件。
- 支持输入补充说明，例如项目背景、客户额外要求、输出偏好。
- 能生成一版题目设计方案。
- 能继续对话修改上一版方案。
- 输出结果以 Markdown 展示。
- 前端可部署到 GitHub Pages。
- 大模型 API key 不暴露在前端。

### 2.2 Demo 暂不实现

- 暂不做复杂登录、权限、项目管理。
- 暂不做多人协作。
- 暂不做正式平台导入格式。
- 暂不直接生成 PPT。
- 暂不强制生成 Word。
- 暂不做完整测评系统。
- 暂不做复杂 agent 多步工具调用。

### 2.3 可选增强

- 支持导出 Markdown。
- 支持复制结果。
- 支持保存本地 JSON。
- 支持生成 Word，作为后续版本。
- 支持选择“更像 Case_001 / 更简洁 / 更适合高端客群”等风格按钮。

---

## 3. 推荐架构

GitHub Pages 只能部署静态前端，不能安全保存大模型 API key。因此推荐：

```text
GitHub Pages 前端
-> API Proxy / Serverless 后端
-> 大模型 API
```

### 3.1 前端

部署位置：

```text
GitHub Pages
```

职责：

- 文件上传。
- 项目补充信息输入。
- 触发生成。
- 展示 Markdown 结果。
- 支持继续对话。
- 管理本轮会话状态。

前端不保存：

- 大模型 API key。
- 长期用户数据。
- 服务器数据库。

### 3.2 API Proxy

部署位置：

```text
Vercel Functions
```

职责：

- 接收前端传来的文本内容、必要时接收原始文件做解析兜底、以及用户指令。
- 拼接 prompt。
- 调用大模型。
- 返回生成结果。
- 保护 API key。

### 3.3 大模型

第一版接入 ChatAnywhere。ChatAnywhere 支持 OpenAI-compatible 的 Chat Completions 接口，因此后端可以按 OpenAI SDK / fetch 风格封装。

接口层只暴露：

```text
generateQuestionDesign(input)
continueConversation(messages)
```

这样后续可以从 ChatAnywhere 换成其他模型，或者接公司内部模型。

推荐配置：

```text
CHATANYWHERE_API_KEY=你的 key
CHATANYWHERE_BASE_URL=https://api.chatanywhere.tech/v1
CHATANYWHERE_MODEL=gpt-5-mini
```

说明：

- 国内使用优先 `https://api.chatanywhere.tech/v1`。
- 国外使用可考虑 `https://api.chatanywhere.org/v1`。
- 生成题目设计第一版优先使用 `/v1/chat/completions`。
- `/v1/responses` 可以后续再评估，第一版不必增加复杂度。
- 默认模型可先用 `gpt-5-mini` 做成本和效果平衡；如果输出质量不足，再切到更强模型。

---

## 4. 前端交互设计

### 4.1 页面布局

建议使用三栏或上下结构。

```text
左侧：输入区
中间：生成与对话区
右侧：结果预览区
```

如果移动端适配，可以改成上下排列。

### 4.2 输入区

字段：

- 文件上传：
  - Brief。
  - Proposal。
  - 客户内部资料。
  - Desk research。
  - 其他补充资料。
- 项目补充说明：
  - 品类/品牌。
  - 目标人群。
  - 本次更关注什么。
  - 有无 IDI。
  - 输出偏好。
- 需求补充：
  - 第一版不设置预设模式按钮。
  - 用户通过自由文本说明本次需求，系统在后台判断应该如何调整输出。

### 4.3 生成区

按钮：

- 生成题目设计。
- 重新生成。
- 继续优化。
- 清空会话。

状态：

- 文件读取中。
- 正在分析项目。
- 正在生成模块。
- 正在生成题目。
- 生成完成。
- 生成失败。

### 4.4 对话区

对话区应是自由输入的自然语言聊天，不做预设按钮或固定指令。

目标体验应接近用户和研究助理对话：

```text
用户可以用自己的话描述需求、追问、质疑、要求重写或补充信息。
系统根据上下文理解用户意图，并基于当前题目设计方案继续调整。
```

对话区不应显示：

- 高端客群少而精。
- 更像 Case_001。
- 场景机会导向。
- 产品创新导向。
- 任何固定 prompt 按钮。

这些判断可以作为系统背后的研究逻辑存在，但不应作为前端显性选项暴露给用户。

### 4.5 结果预览区

第一版用 Markdown 渲染。

展示结构：

```text
1. 项目理解
2. 核心研究问题
3. 模块结构总览
4. 每个模块的题目设计
5. 研究员自检
6. 需要研究员确认的问题
```

---

## 5. 文件处理策略

### 5.1 第一版建议

为了 demo 速度和交互体验，第一版优先采用“前端本地解析文件，后端只接收解析后的文本”的方式。

但为了稳定性，保留后端解析兜底：

```text
优先：浏览器本地解析文件 -> 发送文本给 Vercel Function -> 调模型
兜底：本地解析失败 -> 上传原始文件给 Vercel Function -> 后端解析 -> 调模型
```

推荐优先支持：

- `.txt`
- `.md`
- `.docx`
- `.pdf`
- `.pptx`

### 5.2 解析方式

前端优先解析：

- TXT / MD：浏览器直接读取文本。
- DOCX：使用浏览器端 docx 文本提取库，例如 `mammoth`。
- PDF：使用浏览器端 PDF 文本提取库，例如 `pdfjs-dist`。
- PPTX：可先使用 JSZip 解压 pptx 并提取 slide XML 中的文本。

后端兜底解析：

- TXT / MD：直接读取文本。
- DOCX：提取段落和表格文字。
- PDF：提取文本，必要时按页截断。
- PPTX：提取每页文本。

说明：

```text
前端解析会让 demo 体感更快，也减少后端上传和解析压力。
但 PPTX / PDF 在浏览器端解析可能遇到兼容性问题，所以 Vercel Function 仍应保留兜底能力。
```

### 5.3 大文件处理

第一版应设置限制：

```text
单文件大小：建议 20MB 以内
单次上传文件数：建议 8 个以内
总文本长度：超出后先摘要再进入生成
```

### 5.4 文本组织

传给模型前，应把文件整理成结构化文本：

```text
## File: Brief - xxx.docx
文件类型：Brief
主要内容：
...

## File: Proposal - xxx.pptx
文件类型：Proposal
主要内容：
...

## File: 客户内部资料 - xxx.pdf
文件类型：客户内部资料
主要内容：
...
```

---

## 6. Prompt 资产结构

后续建议创建：

```text
prompt.py
```

或前端/后端如果用 TypeScript：

```text
prompt.ts
```

### 6.1 Prompt 分层

建议拆成：

```text
SYSTEM_ROLE_PROMPT
RESEARCH_LOGIC_PROMPT
INPUT_EXTRACTION_PROMPT
MODULE_PLANNING_PROMPT
QUESTION_GENERATION_PROMPT
QUALITY_CHECK_PROMPT
OUTPUT_FORMAT_PROMPT
```

### 6.2 Prompt 来源

主要来自：

```text
研究员题目设计逻辑梳理_Case001.md
```

其中应重点抽取：

- 商业问题 -> 研究问题 -> 模块 -> 题目 的推导链。
- 模块设计通用规律。
- Case_001 的反例和判断逻辑。
- 日记记录标准链路。
- Diary 与 IDI 分工。
- 题量和高端客群规则。
- 题目自检规则。

---

## 7. 输出格式

第一版建议输出 Markdown，而不是固定平台字段。

### 7.1 标准输出

```markdown
# 题目设计方案

## 1. 项目理解
- 商业问题：
- 研究目标：
- 目标人群：
- 客户已有认知：
- 本次设计重点：

## 2. 核心研究问题
1.
2.
3.

## 3. 模块结构总览
| 模块 | 模块目的 | 对应研究问题 | 保留/合并理由 |

## 4. 详细题目设计
### 板块1：...
引导语：
题目：
1.
2.
...
结束语：

## 5. Agent 检核摘要
- 已对照商业问题与 Proposal 检核：
- 主要风险：
- 已做的控制：

## 6. 需要确认的问题
1.
2.
3.
```

### 7.2 输出字段是否固定

不固定。

Agent 可以建议：

- 题型。
- 跳题。
- 素材要求。
- 研究目的。
- 追问说明。
- 受访者提示。

但这些只是建议字段，不是固定平台导入字段。最终由研究员决定。

---

## 8. 后端 API 草案

### 8.0 模型调用配置

Vercel 环境变量：

```text
CHATANYWHERE_API_KEY=sk-...
CHATANYWHERE_BASE_URL=https://api.chatanywhere.tech/v1
CHATANYWHERE_MODEL=gpt-5-mini
```

后端不要把 API key 返回给前端，也不要在 GitHub Pages 中写入 key。

推荐调用：

```http
POST https://api.chatanywhere.tech/v1/chat/completions
Authorization: Bearer ${CHATANYWHERE_API_KEY}
Content-Type: application/json
```

请求 body：

```json
{
  "model": "gpt-5-mini",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ]
}
```

### 8.1 生成接口

```http
POST /api/generate
```

请求：

```json
{
  "projectInfo": {
    "category": "",
    "brand": "",
    "targetAudience": "",
    "extraNotes": "",
    "conversationStyle": "free_chat"
  },
  "files": [
    {
      "filename": "proposal.pptx",
      "fileType": "proposal",
      "text": "..."
    }
  ]
}
```

响应：

```json
{
  "markdown": "...",
  "warnings": [],
  "needsResearcherConfirmation": []
}
```

### 8.2 继续对话接口

```http
POST /api/chat
```

请求：

```json
{
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "currentDesign": "..."
}
```

响应：

```json
{
  "markdown": "...",
  "changeSummary": "..."
}
```

---

## 9. 工程目录建议

如果使用 Vite + React：

```text
question-design-agent-demo/
  src/
    components/
      FileUploader.tsx
      ProjectInfoForm.tsx
      ChatPanel.tsx
      ResultPreview.tsx
    lib/
      api.ts
      markdown.ts
      fileClient.ts
    types/
      demo.ts
    App.tsx
    main.tsx
  api/
    generate.ts
    chat.ts
    parseFiles.ts
  prompts/
    prompt.ts
  docs/
    demo_spec.md
    researcher_logic.md
```

如果要保持极简，也可以先用：

```text
index.html
src/
  main.js
  style.css
api/
  generate.js
prompts/
  prompt.js
```

---

## 10. Demo 开发阶段

### Phase 1：静态交互原型

目标：

- 页面能上传文件。
- 能填写项目信息。
- 能展示 mock 生成结果。

不接大模型。

### Phase 2：接入后端与大模型

目标：

- 前端调用 `/api/generate`。
- 后端拼 prompt。
- 大模型返回 Markdown。

### Phase 3：支持继续对话

目标：

- 用户能基于当前结果继续修改。
- 支持多轮消息。

### Phase 4：工程化增强

目标：

- 更稳定的文件解析。
- token 超长处理。
- 可导出结果。
- 加入 case few-shot。
- 加入评估集。

---

## 11. 目前还需要确认的信息

已确认：

1. 允许上传内容发送到外部模型。
2. 使用用户自有模型 API key。
3. API Proxy 部署在 Vercel。
4. 前端技术栈使用 React。
5. 第一版支持上传：PPT / PDF / Word / TXT / MD。
6. 文件解析优先前端本地解析，后端 Vercel Function 做兜底解析。
7. 输出先只需要 Markdown。
8. 第一版不做下载结果。
9. 第一版不放入 Case_001 few-shot 示例。
10. 前端保持自由对话，不暴露预设 prompt，不做快捷操作按钮。

仍需确认：

1. 具体模型供应商和调用协议：OpenAI-compatible / Claude / DeepSeek / 通义 / 公司内部模型？
2. Word 文件是否只需支持 `.docx`，还是也要支持旧版 `.doc`？
3. PPT 是否只需支持 `.pptx`，还是也要支持旧版 `.ppt`？
4. GitHub Pages 是否已有目标仓库和部署路径？
5. Vercel Function 的运行区域和超时限制是否有内部要求？

---

## 12. 推荐下一步

建议下一步按这个顺序做：

1. 确认 demo 技术路线：
   - 前端：GitHub Pages + React/Vite。
   - 后端：Vercel Functions。
   - 文件解析：前端本地解析优先，Vercel 后端兜底。
   - 输出：Markdown。

2. 创建 `prompt.py`：
   - 先把研究员逻辑拆成 prompt 模块。
   - 以 `generation_logic.md` 作为生成流程协议。
   - 以 `research_rules.md` 作为规则库。
   - 以 `case_cards/` 作为案例逻辑参考。
   - 先不接前端。
   - 用 Case_001 的材料本地测试一次生成效果。

3. 创建前端静态 demo：
   - 先用 mock 返回。
   - 页面交互跑通。

4. 接入 API Proxy：
   - 用真实模型生成。
   - 再迭代 prompt。
