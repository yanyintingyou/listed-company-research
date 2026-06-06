# Lightweight integrity checks for listed-company-research.
# No third-party dependencies: this should run in Hermes, Codex, and plain Python.

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"
ADAPTER = REFERENCES / "platform-adapter.md"

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}

REQUIRED_SECTIONS = [
    "## Overview",
    "## Platform Compatibility",
    "## When to Use",
    "## Non-Negotiable Research Guardrails",
    "## Standard Workflow",
    "## Valuation Method Quick Router",
    "## Reference Routing",
    "## Output Templates",
    "## Common Pitfalls",
    "## Verification Checklist",
]

REQUIRED_ADAPTER_SECTIONS = [
    "## Hermes 运行环境适配（必须按可用工具执行）",
    "### Hermes 常用能力路由",
    "### Hermes 中的标准执行顺序",
    "### Hermes 子代理使用规则",
    "### Hermes 输出到 Telegram 的格式偏好",
    "## Codex 适配层（保留，不要删除）",
]

REQUIRED_HERMES_TOOL_NAMES = [
    "skill_view",
    "read_file",
    "search_files",
    "web_search",
    "web_extract",
    "browser_*",
    "execute_code",
    "terminal",
    "delegate_task",
    "todo",
    "mcp_excel_*",
    "cronjob",
]

REQUIRED_CODEX_TERMS = [
    "web.run",
    "web.finance",
    "Codex plan/checklist",
    "references/codex-plugin-integration.md",
]

REQUIRED_REFERENCES = [
    "references/platform-adapter.md",
    "references/analysis-process-extensions.md",
    "references/codex-plugin-integration.md",
    "references/data-source-map-by-market.md",
    "references/valuation-method-router.md",
    "references/source-verification-template.md",
    "references/multi-company-comparison-workflow.md",
    "references/insurance-company-analysis.md",
    "references/listed-company-kanban-workflow.md",
]

PLATFORM_SPECIFIC_PATTERNS = [
    r"\bskill_view\b",
    r"\bweb_extract\b",
    r"\bweb_search\b",
    r"\bdelegate_task\b",
    r"\bmcp_tradingview_yahoo_price\b",
    r"\bexecute_code\b",
]

FORBIDDEN_PATTERNS = [
    r"curl\s+.*\|\s*bash",
    r"wget\s+.*\|\s*sh",
    r"用户在20\d{2}",
    r"本session",
    r"亲身踩坑",
    r"hermes-kanban-setup",
    r"spx-technical-fundamental-analysis",
]


def load_frontmatter(text: str):
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    end = text.find("\n---\n", 4)
    assert end != -1, "frontmatter must close with ---"
    raw = text[4:end]
    body = text[end + len("\n---\n") :]
    return raw, body


def top_level_keys(frontmatter: str):
    keys = set()
    for line in frontmatter.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("\t"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.add(match.group(1))
    return keys


def scalar_value(frontmatter: str, key: str):
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""


def markdown_files_for_policy():
    return [
        path
        for path in [SKILL] + sorted(REFERENCES.glob("*.md"))
        if path.name != "platform-adapter.md"
    ]


def test_frontmatter_is_codex_compatible_and_hermes_aware():
    text = SKILL.read_text(encoding="utf-8")
    frontmatter, body = load_frontmatter(text)
    keys = top_level_keys(frontmatter)

    assert {"name", "description"}.issubset(keys), "frontmatter must include name and description"
    unexpected = keys - ALLOWED_FRONTMATTER_KEYS
    assert not unexpected, "unexpected top-level frontmatter keys: " + ", ".join(sorted(unexpected))
    assert scalar_value(frontmatter, "name") == "listed-company-research"
    assert len(scalar_value(frontmatter, "description")) <= 1024
    assert "platforms:" in frontmatter
    assert "hermes" in frontmatter.lower()
    assert "codex" in frontmatter.lower()
    assert body.strip(), "body cannot be empty"


def test_required_sections():
    text = SKILL.read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        assert section in text, f"missing required section: {section}"


def test_hermes_adapter_is_explicit_and_codex_is_preserved():
    text = ADAPTER.read_text(encoding="utf-8")
    for section in REQUIRED_ADAPTER_SECTIONS:
        assert section in text, f"missing adapter section: {section}"
    for tool_name in REQUIRED_HERMES_TOOL_NAMES:
        assert tool_name in text, f"missing Hermes tool route: {tool_name}"
    for term in REQUIRED_CODEX_TERMS:
        assert term in text, f"Codex compatibility term missing: {term}"


def test_reference_links_exist_and_are_routed():
    text = SKILL.read_text(encoding="utf-8")
    refs = set(re.findall(r"`(references/[^`]+?\.md)`", text))
    refs.update(REQUIRED_REFERENCES)

    missing = [ref for ref in sorted(refs) if not (ROOT / ref).exists()]
    assert not missing, "missing references: " + ", ".join(missing)

    unrouted = []
    for ref_file in sorted(REFERENCES.glob("*.md")):
        ref = "references/" + ref_file.name
        if ref not in refs:
            unrouted.append(ref)
    assert not unrouted, "reference files not routed from SKILL.md: " + ", ".join(unrouted)


def test_platform_specific_tool_names_are_isolated():
    assert ADAPTER.exists(), "platform-adapter.md must exist"
    hits = []
    for path in markdown_files_for_policy():
        text = path.read_text(encoding="utf-8")
        for pattern in PLATFORM_SPECIFIC_PATTERNS:
            if re.search(pattern, text):
                hits.append(f"{path.relative_to(ROOT)} matches {pattern}")
    assert not hits, "platform-specific tool names must live in platform-adapter.md only:\n" + "\n".join(hits)


def test_forbidden_patterns():
    hits = []
    for path in [SKILL] + sorted(REFERENCES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if re.search(pattern, text):
                hits.append(f"{path.relative_to(ROOT)} matches {pattern}")
    assert not hits, "forbidden patterns found:\n" + "\n".join(hits)


def test_package_has_no_embedded_backups():
    backups = [path.name for path in ROOT.iterdir() if path.is_dir() and path.name.startswith(".backup")]
    assert not backups, "move backup directories outside the skill package: " + ", ".join(backups)


def test_reasonable_size():
    text = SKILL.read_text(encoding="utf-8")
    assert len(text) <= 25_000, "SKILL.md should remain concise; move details to references"


if __name__ == "__main__":
    tests = [
        test_frontmatter_is_codex_compatible_and_hermes_aware,
        test_required_sections,
        test_hermes_adapter_is_explicit_and_codex_is_preserved,
        test_reference_links_exist_and_are_routed,
        test_platform_specific_tool_names_are_isolated,
        test_forbidden_patterns,
        test_package_has_no_embedded_backups,
        test_reasonable_size,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
