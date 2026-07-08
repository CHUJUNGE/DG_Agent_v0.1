"""
Prompt builder for the Question Design Agent demo.

This module does not call any model API. It only prepares messages that can be
sent to an OpenAI-compatible chat completions endpoint such as ChatAnywhere.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Literal


ROOT = Path(__file__).resolve().parents[1]
GENERATION_LOGIC_PATH = ROOT / "references" / "generation_logic.md"
RESEARCH_RULES_PATH = ROOT / "references" / "research_rules.md"
CASE_CARDS_DIR = ROOT / "references" / "case_cards"


Role = Literal["system", "user", "assistant"]


@dataclass
class ChatMessage:
    role: Role
    content: str

    def to_dict(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}


@dataclass
class ProjectFile:
    filename: str
    file_type: str
    text: str


@dataclass
class ProjectInfo:
    category: str = ""
    brand: str = ""
    target_audience: str = ""
    extra_notes: str = ""
    has_idi: str = ""
    output_preference: str = "Markdown"


@dataclass
class PromptBundle:
    messages: list[ChatMessage]
    selected_case_ids: list[str] = field(default_factory=list)

    def to_openai_messages(self) -> list[dict[str, str]]:
        return [message.to_dict() for message in self.messages]


CASE_CARD_FILES: dict[str, str] = {
    "case_001": "case_001_gum.md",
    "case_002": "case_002_chocolate.md",
    "case_003": "case_003_wonton.md",
    "case_004": "case_004_45plus_health.md",
}


CASE_SELECTION_RULES: dict[str, list[str]] = {
    "case_001": [
        "口香糖",
        "gum",
        "益达",
        "绿箭",
        "after meal",
        "recenter",
        "fresh",
        "嘴巴",
        "品类增长",
        "流失",
        "衰退",
        "场景机会",
    ],
    "case_002": [
        "巧克力",
        "chocolate",
        "德芙",
        "dove",
        "snacking",
        "零食",
        "情绪",
        "甜",
        "日常化",
        "高频",
        "品类增长",
    ],
    "case_003": [
        "馄饨",
        "云吞",
        "抄手",
        "冷冻",
        "持续聆听",
        "r2",
        "r3",
        "r4",
        "相较上次",
        "固定样本",
        "筛选",
    ],
    "case_004": [
        "45+",
        "45岁",
        "健康",
        "老龄化",
        "healthy aging",
        "vms",
        "保健品",
        "营养补充",
        "信任",
        "身体状态",
        "健康产品",
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def compact_text(text: str, max_chars: int) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    head = text[: int(max_chars * 0.65)].rstrip()
    tail = text[-int(max_chars * 0.25) :].lstrip()
    return (
        f"{head}\n\n"
        "[...中间内容因长度限制已省略，生成时请基于已保留的开头和结尾信息判断；"
        "如信息不足，应在研究员确认点中说明...]\n\n"
        f"{tail}"
    )


def normalize_for_match(text: str) -> str:
    return text.lower().replace(" ", "")


def select_relevant_cases(project_text: str, max_cases: int = 2) -> list[str]:
    normalized = normalize_for_match(project_text)
    scores: list[tuple[str, int]] = []

    for case_id, keywords in CASE_SELECTION_RULES.items():
        score = 0
        for keyword in keywords:
            if normalize_for_match(keyword) in normalized:
                score += 1
        if score:
            scores.append((case_id, score))

    scores.sort(key=lambda item: item[1], reverse=True)
    return [case_id for case_id, _score in scores[:max_cases]]


def load_case_cards(case_ids: Iterable[str], max_chars_each: int = 6000) -> str:
    chunks: list[str] = []
    for case_id in case_ids:
        filename = CASE_CARD_FILES.get(case_id)
        if not filename:
            continue
        path = CASE_CARDS_DIR / filename
        if path.exists():
            chunks.append(f"## {case_id}\n\n{compact_text(read_text(path), max_chars_each)}")
    return "\n\n---\n\n".join(chunks)


def format_project_files(files: Iterable[ProjectFile], max_chars_each: int = 18000) -> str:
    chunks: list[str] = []
    for file in files:
        chunks.append(
            "\n".join(
                [
                    f"## File: {file.filename}",
                    f"- file_type: {file.file_type}",
                    "",
                    compact_text(file.text, max_chars_each),
                ]
            )
        )
    return "\n\n---\n\n".join(chunks)


def format_project_info(project_info: ProjectInfo) -> str:
    return "\n".join(
        [
            f"- 品类/品牌: {project_info.category or project_info.brand or '未提供'}",
            f"- 品牌: {project_info.brand or '未提供'}",
            f"- 目标人群: {project_info.target_audience or '未提供'}",
            f"- 是否有 IDI / 入户 / 后续访谈: {project_info.has_idi or '未提供'}",
            f"- 输出偏好: {project_info.output_preference or 'Markdown'}",
            f"- 用户补充说明: {project_info.extra_notes or '无'}",
        ]
    )


def build_system_prompt() -> str:
    generation_logic = compact_text(read_text(GENERATION_LOGIC_PATH), 18000)
    research_rules = compact_text(read_text(RESEARCH_RULES_PATH), 18000)
    return f"""
你是一个资深消费者研究员和 Digital Diary 题目设计专家。

你的任务是帮助研究员基于 Brief、Proposal、客户内部资料等输入，生成一套可审阅、可修改、可继续对话迭代的题目设计方案。

你必须遵守以下原则：

1. 不要直接开始写题。必须先理解项目、拆解研究问题、设计模块，再写题。
2. 题目设计必须回到商业问题和 Proposal 中的研究目标。
3. case card 只能作为设计逻辑参考，不能复制题目，也不能机械套模板。
4. 如果信息不足、材料冲突或需要经验判断，先从材料中寻找答案；确实无法判断且会显著影响方案时，才列入“需要确认的问题”。
5. 输出使用中文 Markdown。
6. 不要输出平台导入固定字段；题型、跳题、素材要求、研究目的、追问说明都只是研究员审阅建议。
7. 前端是自由对话体验，不要提到预设按钮或固定 prompt 选项。
8. 最终用户看到的输出要精简：项目理解、核心研究问题、模块结构总览只列结论，不要长篇阐述；主要篇幅放在详细题目设计。
9. 自检是 Agent 内部行为，最终只输出简短的“Agent 检核摘要”，不要输出冗长自检过程。
10. 需要确认的问题最多 3 个；如果没有关键问题，写“暂无必须确认的问题”。
11. 详细题目设计必须是完整题目稿，不是建议或示例。每个板块固定使用“板块x：xxx / 引导语 / 题目 / 结束语”格式。
12. 不要输出“建议题目示例”“示例题”“建议题量”等字样；不要在每道题后堆研究目的、设计说明、内部解释。
13. 详细题目必须先像正式 Digital Diary 给受访者看的题面，再像研究员方案。不要把研究链路逐项翻译成 checklist。
14. 避免命令式、考试式和过度量化措辞，例如“每段用一行”“至少/最多”“按优先级”“打分 1-5”“必须上传”，除非客户材料明确要求或平台题型必须如此。
15. 不要每题都加括号解释。每个板块只保留少量真正帮助理解的轻提示。
16. 不要为了具体而具体。具体性来自真实时刻、场景、人物、前后变化和原因，不来自硬塞窄标签。
17. 当项目类似 Case_001 时，必须优先模仿正式 DG 的自然开放语气：关于我先理解人，典型一天开放描画 routine，日记像生活记录，购物任务像自然 vlog，不要变成货架审计。
18. 当生成“关于我 / About Me / 生活底色 / 基础画像”模块时，题目 1-3 必须原样使用规则库中的“关于我固定开场题”；除非用户明确要求改写，否则不要改写、拆分或替换。

以下是生成流程协议：

{generation_logic}

以下是研究规则库：

{research_rules}
""".strip()


def build_generation_user_prompt(
    project_info: ProjectInfo,
    files: list[ProjectFile],
    selected_case_ids: list[str],
) -> str:
    formatted_info = format_project_info(project_info)
    formatted_files = format_project_files(files)
    case_cards = load_case_cards(selected_case_ids)

    case_section = (
        f"## 参考案例逻辑\n\n{case_cards}\n\n"
        "请只学习以上案例的设计逻辑，不要复制案例题目。"
        if case_cards
        else "## 参考案例逻辑\n\n未匹配到明确相关案例。请仅基于研究规则库和当前项目材料生成。"
    )

    return f"""
请基于以下项目输入，生成第一版题目设计方案。

要求：

- 严格遵循“项目理解 -> 核心研究问题 -> 模块结构总览 -> 详细题目设计 -> Agent 检核摘要 -> 需要确认的问题”的顺序。
- “项目理解”只列 5-7 条以内的关键结论，不展开长篇背景。
- “核心研究问题”只列 3-6 个问题，不写长表格。
- “模块结构总览”只列模块、模块目的、对应研究问题，不展开详细理由。
- 只在“模块结构总览”中说明模块目的、对应研究问题、保留/合并/定制理由；不要在“详细题目设计”里重复这些内部说明。
- 详细题目设计必须输出完整题目，而不是题目方向或建议示例。
- 详细题目设计每个板块必须使用：
  板块x：xxx
  引导语：
  题目：
  1.
  2.
  ...
  结束语：
- 不要在每道题后输出研究目的、设计说明、内部解释；如确有必要，只在板块末尾用一句“内部提示”说明。
- 如果文件中客户已有明确要求，必须体现。
- 如果客户已有研究沉淀，不要重复泛问，要在已知基础上继续探索。
- 如果不确定是否需要某个模块或任务，先从材料中找依据；仍无法判断时，只列入“需要确认的问题”，最多 3 个。
- “Agent 检核摘要”最多 5 条，只输出关键风险和控制，不要展示完整自检过程。
- 题目语言要自然、开放、有陪伴感；不要用过多具体例子和选项限制受访者回答。
- 题目不要像表格 checklist；优先使用“请和我们聊聊 / 请描画一下 / 回想一下最近一次 / 如果方便可以……”等自然表达。
- 避免“每段用一行”“至少/最多”“按优先级”“打分 1-5”“必须上传”等措辞，除非项目材料明确要求。
- 不要每题都加括号解释；括号示例只在少数确实需要帮助理解的题目中使用。
- 需要照片、语音或视频时，优先表达为“可以用……补充”，不要默认每题强制上传。
- 基础画像模块先理解受访者本人，不要急于和产品/品牌发生关联。
- 如果包含“关于我 / About Me / 生活底色 / 基础画像”模块，题目 1-3 必须原样使用以下固定题：
  1. 首先，让我们多了解一下你吧！色彩、MBTI、星座、关键词......可以用任何你觉得能代表自己的方式来介绍自己！欢迎多多分享照片，向我们展示真实的你～
  2. 和我们聊聊你的学业/工作吧！包括你所在的专业/行业、每天具体要做的事情（如果你有副业，也介绍一下吧！）
  3. 可以拍一段小视频，带我们“云参观”一下你的居住空间吗？（比如宿舍/家里的整体布局、你每天待得最久的地方，你最用心打理的一个角落）
- 输出只使用 Markdown，不要输出 JSON。

# 用户补充信息

{formatted_info}

# 项目文件文本

{formatted_files}

{case_section}
""".strip()


def build_generation_prompt(
    project_info: ProjectInfo,
    files: list[ProjectFile],
    max_cases: int = 2,
) -> PromptBundle:
    project_text = "\n\n".join(
        [
            format_project_info(project_info),
            *(file.text for file in files),
        ]
    )
    selected_case_ids = select_relevant_cases(project_text, max_cases=max_cases)
    messages = [
        ChatMessage(role="system", content=build_system_prompt()),
        ChatMessage(
            role="user",
            content=build_generation_user_prompt(project_info, files, selected_case_ids),
        ),
    ]
    return PromptBundle(messages=messages, selected_case_ids=selected_case_ids)


def build_chat_prompt(
    current_design_markdown: str,
    user_message: str,
    history: list[ChatMessage] | None = None,
) -> PromptBundle:
    system_prompt = """
你是一个资深消费者研究员和 Digital Diary 题目设计专家。

你正在帮助用户基于上一版题目设计方案进行自由对话式修改。

修改规则：

1. 先理解用户想改什么。
2. 不要每次从零生成；尽量保留未受影响的内容。
3. 如果用户要求与研究逻辑冲突，要说明风险，并给出折中方案。
4. 如果修改需要研究员判断，先从当前方案和上下文找答案；仍无法判断时，列入“需要确认的问题”，最多 3 个。
5. 输出 Markdown。
6. 如果只是局部修改，可以先给修改说明，再给更新后的相关模块；如果用户要求完整方案，则输出完整方案。
7. 保持输出精简，不要重复大段项目理解和自检。
8. 如果用户反馈题目“死板、太多解释、太像 checklist、太命令式”，应优先重写受访者题面：减少括号、减少硬性数量/排序/打分/上传要求，改成自然开放的 Diary 语言。
""".strip()

    history = history or []
    user_prompt = f"""
# 当前题目设计方案

{compact_text(current_design_markdown, 24000)}

# 用户新指令

{user_message}

请基于当前方案和用户新指令进行修改。
""".strip()

    messages = [ChatMessage(role="system", content=system_prompt), *history, ChatMessage(role="user", content=user_prompt)]
    return PromptBundle(messages=messages)


def demo_build_prompt_from_plain_text(project_text: str) -> PromptBundle:
    """Small helper for local smoke tests without parsed files."""
    return build_generation_prompt(
        project_info=ProjectInfo(extra_notes="本地 smoke test：用户仅提供了一段合并后的项目文本。"),
        files=[ProjectFile(filename="project_input.txt", file_type="combined_text", text=project_text)],
    )


if __name__ == "__main__":
    bundle = demo_build_prompt_from_plain_text(
        "这是一个巧克力品类增长机会项目，希望理解消费者零食场景、情绪需求和德芙可以进入的日常场景。"
    )
    print("Selected cases:", ", ".join(bundle.selected_case_ids) or "none")
    for message in bundle.messages:
        print("\n" + "=" * 80)
        print(message.role.upper())
        print("=" * 80)
        print(compact_text(message.content, 3000))
