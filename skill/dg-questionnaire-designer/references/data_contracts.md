# Data Contracts

These contracts let the skill connect to product backend, algorithm services, database gold answers, and evaluation pipelines.

## ProjectFile

```json
{
  "id": "file_001",
  "filename": "proposal.pdf",
  "fileType": "pdf",
  "sourceType": "proposal",
  "extractedText": "...",
  "metadata": {
    "pageCount": 20,
    "parserVersion": "parser_v0.1"
  }
}
```

## ProjectInfo

```json
{
  "projectId": "project_001",
  "category": "口香糖",
  "brand": "益达 / 绿箭",
  "targetAudience": "18-40 Urban Striver",
  "method": "Digital Diary",
  "hasIdi": "unknown",
  "extraNotes": "..."
}
```

## GenerationRequest

```json
{
  "projectInfo": {},
  "files": [],
  "selectedCaseIds": ["case_001"],
  "versions": {
    "skillVersion": "0.1.0",
    "generationLogicVersion": "0.1.0",
    "researchRulesVersion": "0.1.0",
    "caseLibraryVersion": "0.1.0",
    "promptVersion": "0.1.0",
    "modelVersion": "gpt-5-mini"
  }
}
```

## GenerationOutput

```json
{
  "markdown": "...",
  "selectedCaseIds": ["case_001"],
  "diagnostics": {
    "missingInfo": [],
    "riskFlags": [],
    "tokenEstimate": 0
  },
  "versions": {}
}
```

## TrainingCase

```json
{
  "caseId": "case_001",
  "projectType": ["category_growth", "occasion_study"],
  "category": "gum",
  "brand": "Extra / Doublemint",
  "inputMaterials": {
    "brief": "...",
    "proposal": "...",
    "internalMaterials": []
  },
  "goldDgMarkdown": "...",
  "metadata": {
    "moduleNames": ["关于我", "我典型的一天"],
    "diaryDays": 6,
    "hasShoppingTask": true,
    "hasIdi": true
  }
}
```

## EvalResult

```json
{
  "runId": "run_001",
  "caseId": "case_001",
  "overallScore": 3.8,
  "dimensionScores": {
    "projectUnderstanding": 4,
    "researchQuestionFit": 4,
    "moduleStructure": 3,
    "moduleOrder": 4,
    "questionWording": 3,
    "respondentBurden": 3,
    "brandExposureControl": 4,
    "diaryIdiSplit": 3,
    "taskDesign": 3,
    "fixedTemplateCompliance": 5
  },
  "gaps": [
    {
      "type": "too_rigid",
      "evidence": "...",
      "goldReference": "...",
      "suggestedRule": "..."
    }
  ]
}
```

## RuleCandidate

```json
{
  "target": "research_rules",
  "rationale": "Repeated gap across category growth cases.",
  "proposedText": "...",
  "examples": ["case_001", "case_002"],
  "riskLevel": "medium"
}
```
