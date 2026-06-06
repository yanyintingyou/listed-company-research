# listed-company-research

[English](#english) | [中文](#中文)

---

## English

**Listed Company Research** is a cross-agent skill for source-backed public-equity research. It is designed to work with both **Hermes Agent** and **Codex-style agent runtimes** while keeping the core investment workflow platform-neutral.

It helps an agent conduct deep fundamental research on A-shares, Hong Kong stocks, and US-listed companies by enforcing:

- primary-source extraction before conclusions;
- explicit separation of disclosed facts, calculations, and analytical judgment;
- market-specific data-source routing;
- valuation-method routing across banks, insurers, holding companies, SaaS/platforms, AI/semiconductors, games, advertising/media, consumer brands, and cyclicals;
- source verification and model-consistency audits;
- platform-specific execution adapters for Hermes and Codex.

> Research use only. This repository does not provide personalized investment advice.

### Why this skill exists

Generic LLM prompts often fail in equity research because they:

- summarize search snippets instead of reading filings;
- mix currencies, share counts, and reporting periods;
- apply the wrong valuation method to specialized sectors;
- treat model inference as disclosed fact;
- lose the audit trail for numbers, URLs, pages, and formulas.

This skill turns listed-company research into a reproducible workflow with guardrails, references, and integrity tests.

### Repository layout

```text
listed-company-research/
├── SKILL.md                         # Main cross-agent skill
├── agents/
│   └── openai.yaml                  # Codex/OpenAI-style agent interface metadata
├── references/
│   ├── platform-adapter.md          # Hermes + Codex execution adapter
│   ├── codex-plugin-integration.md  # Codex-only plugin guidance
│   ├── data-source-map-by-market.md
│   ├── valuation-method-router.md
│   ├── source-verification-template.md
│   └── ...                          # Industry/case references
└── tests/
    └── test_skill_integrity.py      # Stdlib integrity checks
```

### Hermes configuration

#### Option A — install as a local Hermes skill

Clone the repository into your Hermes skills directory:

```bash
mkdir -p ~/.hermes/skills/research
git clone https://github.com/yanyintingyou/listed-company-research.git \
  ~/.hermes/skills/research/listed-company-research
```

Then start a fresh Hermes session or reset the current one so the skill loader can discover it.

Use it explicitly:

```text
/skill listed-company-research
```

Or start Hermes with the skill preloaded:

```bash
hermes -s listed-company-research
```

#### Option B — use from an existing clone

If you already cloned this repo somewhere else, copy or symlink it into Hermes' skill directory:

```bash
mkdir -p ~/.hermes/skills/research
ln -s /absolute/path/to/listed-company-research \
  ~/.hermes/skills/research/listed-company-research
```

#### Recommended Hermes toolsets

This skill works best when Hermes has these toolsets enabled:

- `skills` — load `SKILL.md` and references;
- `file` — read, search, patch, and write local research files;
- `web` — search and extract official filings, PDFs, and IR pages;
- `browser` — handle dynamic disclosure pages when extraction fails;
- `terminal` — run tests, download files, inspect file types, execute local scripts;
- `code_execution` — recalculate valuation metrics, TTM, FCF, FX conversions, and scorecards;
- `delegation` — split multi-company or multi-module research into subagents;
- `todo` — track deep-research workflows;
- `cronjob` — optional, for scheduled monitoring;
- `mcp_excel`/Excel tools — optional, for workbook-based valuation models.

Configure tools with:

```bash
hermes tools
# or
hermes tools list
```

After enabling/disabling tools, start a new session or use `/reset`.

#### Hermes execution notes

When running in Hermes, read `references/platform-adapter.md`. It maps the research workflow to Hermes tools such as `web_search`, `web_extract`, `browser_*`, `read_file`, `search_files`, `execute_code`, `delegate_task`, and Excel/MCP tools.

### Codex configuration

This repository preserves Codex compatibility without making Codex plugins mandatory.

#### Basic Codex usage

Use the repository as a local skill/project instruction source in your Codex-style environment. The root `SKILL.md` is the main instruction file, and `agents/openai.yaml` provides a compact OpenAI/Codex-style interface hint:

```yaml
interface:
  display_name: "Listed Company Research"
  short_description: "Primary-source listed-equity research"
  default_prompt: "Use $listed-company-research to conduct a source-backed fundamental analysis of a listed company."

policy:
  allow_implicit_invocation: true
```

If your Codex environment supports local skills or plugin instructions, point it at this repository or copy the repository into the local skills directory used by that runtime.

#### Codex plugin guidance

Read:

```text
references/codex-plugin-integration.md
```

It explains optional Codex plugin usage for:

- public-equity investing workflows;
- IR transcripts and presentations;
- market prices and FX;
- spreadsheets and valuation models;
- data analytics and dashboards;
- documents and presentations.

Plugin outputs must always be traced back to original sources, URLs, pages, tables, or calculation chains. A plugin result itself is not a citation.

### Running tests

This repository includes lightweight integrity checks with no third-party dependency:

```bash
python3 tests/test_skill_integrity.py
```

The tests check:

- frontmatter compatibility;
- required sections;
- Hermes adapter presence;
- Codex compatibility preservation;
- routed reference links;
- forbidden stale or unsafe patterns;
- package cleanliness;
- reasonable main skill size.

### Typical tasks

- “Analyze Tencent’s latest annual report using primary sources.”
- “Compare three A-share banks with a consistent valuation framework.”
- “Audit this AI-generated investment memo and identify unsupported claims.”
- “Build a source-verification appendix for this stock-research article.”
- “Recalculate DCF/SOTP assumptions and identify unit, FX, or share-count errors.”

### Limitations

- The skill does not replace paid market data terminals.
- It does not guarantee data availability from official websites when access is blocked or pages are dynamic.
- It is a research workflow, not a recommendation engine.
- Current prices, FX rates, valuation multiples, and analyst targets must always be refreshed and dated.

---

## 中文

**上市公司深度研究（listed-company-research）** 是一个跨 Agent 架构的公开股权研究 skill，兼容 **Hermes Agent** 与 **Codex 风格 Agent 运行时**。它把核心投资研究流程保持为平台无关，同时通过适配层分别说明 Hermes 和 Codex 的具体执行方式。

它适用于 A 股、港股、美股上市公司深度研究，重点强制执行：

- 先提取一手披露文件，再形成结论；
- 明确区分文件直接披露、基于原始数据的计算、分析性判断；
- 按市场选择数据源路径；
- 按行业和商业模式选择估值方法；
- 对银行、保险、综合控股集团、SaaS/平台、AI/半导体、游戏、广告媒体、消费品牌、周期品等分别路由；
- 做来源核验和模型内一致性审计；
- 为 Hermes 与 Codex 分别提供平台执行适配。

> 本项目仅用于研究讨论，不构成个性化投资建议。

### 为什么需要这个 skill

普通 LLM 提示词做上市公司研究时，常见问题包括：

- 只总结搜索摘要，不读取财报/公告原文；
- 混淆货币、股本、报告期和会计口径；
- 对银行、保险、控股集团等使用错误估值方法；
- 把模型推断写成公司披露事实；
- 缺少 URL、页码、表格、公式和计算链审计。

这个 skill 将上市公司研究拆成可复核、可追踪、可审计的流程。

### 仓库结构

```text
listed-company-research/
├── SKILL.md                         # 主 skill，兼容 Hermes / Codex
├── agents/
│   └── openai.yaml                  # Codex/OpenAI 风格 agent 接口元数据
├── references/
│   ├── platform-adapter.md          # Hermes + Codex 平台适配层
│   ├── codex-plugin-integration.md  # Codex-only 插件说明
│   ├── data-source-map-by-market.md
│   ├── valuation-method-router.md
│   ├── source-verification-template.md
│   └── ...                          # 行业/案例 reference
└── tests/
    └── test_skill_integrity.py      # 标准库完整性测试
```

### Hermes 配置方法

#### 方法 A：作为本地 Hermes skill 安装

将仓库克隆到 Hermes skills 目录：

```bash
mkdir -p ~/.hermes/skills/research
git clone https://github.com/yanyintingyou/listed-company-research.git \
  ~/.hermes/skills/research/listed-company-research
```

然后启动新的 Hermes 会话，或 `/reset` 当前会话，让 skill loader 重新发现该 skill。

显式加载：

```text
/skill listed-company-research
```

或启动 Hermes 时预加载：

```bash
hermes -s listed-company-research
```

#### 方法 B：从已有克隆目录使用

如果你已经把仓库克隆在其他位置，可以复制或软链接到 Hermes skill 目录：

```bash
mkdir -p ~/.hermes/skills/research
ln -s /absolute/path/to/listed-company-research \
  ~/.hermes/skills/research/listed-company-research
```

#### 推荐启用的 Hermes toolsets

这个 skill 在 Hermes 中最好搭配以下工具集：

- `skills`：加载 `SKILL.md` 和 references；
- `file`：读取、搜索、修改本地研究文件；
- `web`：搜索并提取官方公告、PDF、IR 页面；
- `browser`：处理动态披露网页或下载按钮；
- `terminal`：运行测试、下载文件、检查文件类型、执行脚本；
- `code_execution`：重算估值、TTM、FCF、汇率和评分模型；
- `delegation`：多公司或多模块并行研究；
- `todo`：跟踪深度研究流程；
- `cronjob`：可选，用于定期监控公告/价格/事件日历；
- `mcp_excel`/Excel 工具：可选，用于估值模型工作簿。

配置工具：

```bash
hermes tools
# 或
hermes tools list
```

启用或关闭工具后，需要新会话或 `/reset` 才会生效。

#### Hermes 执行说明

在 Hermes 中使用时，请读取：

```text
references/platform-adapter.md
```

该文件把研究动作映射到 Hermes 工具，例如 `web_search`、`web_extract`、`browser_*`、`read_file`、`search_files`、`execute_code`、`delegate_task` 和 Excel/MCP 工具。

### Codex 配置方法

本仓库保留 Codex 兼容性，但不强制依赖 Codex 插件。

#### 基础 Codex 用法

在 Codex 风格环境中，将本仓库作为本地 skill 或项目级 instruction source 使用。根目录的 `SKILL.md` 是主指令文件，`agents/openai.yaml` 提供 OpenAI/Codex 风格接口提示：

```yaml
interface:
  display_name: "Listed Company Research"
  short_description: "Primary-source listed-equity research"
  default_prompt: "Use $listed-company-research to conduct a source-backed fundamental analysis of a listed company."

policy:
  allow_implicit_invocation: true
```

如果你的 Codex 环境支持本地 skills 或插件指令，可以将其指向本仓库，或复制到该运行时使用的本地 skills 目录。

#### Codex 插件说明

请读取：

```text
references/codex-plugin-integration.md
```

它说明了 Codex 环境中可选使用的插件能力，包括：

- 上市公司投资研究流程；
- IR transcript 和 presentation；
- 市场价格与汇率；
- 表格和估值模型；
- 数据分析与 dashboard；
- 文档和演示稿。

插件输出必须回溯到原始来源、URL、页码、表格或计算链。插件结果本身不能作为引用来源。

### 运行测试

本仓库包含无需第三方依赖的轻量完整性测试：

```bash
python3 tests/test_skill_integrity.py
```

测试内容包括：

- frontmatter 兼容性；
- 必需章节；
- Hermes 适配层是否存在；
- Codex 兼容性是否保留；
- reference 链接是否完整；
- 是否存在陈旧/危险模式；
- package 是否干净；
- 主 skill 文件长度是否合理。

### 典型任务

- “用一手数据分析腾讯最新年报。”
- “用统一框架比较三家 A 股银行。”
- “审计这份 AI 生成的投资备忘录，找出没有来源支撑的判断。”
- “为这篇股票研究文章生成逐条来源核验附录。”
- “重算 DCF/SOTP 假设，并检查单位、汇率、股本口径错误。”

### 局限性

- 本 skill 不能替代付费金融终端。
- 官方网站被阻塞、动态网页复杂或 PDF 提取失败时，需要标注数据缺口和替代来源层级。
- 它是研究流程，不是自动荐股系统。
- 股价、汇率、估值倍数、分析师目标价等时间敏感数据必须重新获取并标注日期。
