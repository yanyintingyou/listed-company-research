# Hermes / Codex 平台适配层

## 使用原则

本 skill 的主流程只描述研究动作，不假设某个固定运行环境。执行到搜索、抓取、PDF 提取、行情、计算、并行任务或 Kanban 编排时，按当前平台选择可用工具。

如果某项工具不存在，不要伪造执行结果。改用同等能力 fallback，并在数据源审计表中写明限制。

## Hermes 运行环境适配（必须按可用工具执行）

在 Hermes 中执行本 skill 时，不要把研究流程停留在文字规划；应使用 Hermes 当前可用工具完成检索、提取、计算、文件审计和验证，并在最终报告中说明真实执行结果。

### Hermes 常用能力路由

| 研究动作 | Hermes 优先工具 | 使用边界与注意事项 |
|---|---|---|
| 加载/查看 skill 与 reference | `skill_view` | 先读取本 skill；需要行业、估值、来源核验、平台适配时再读取对应 reference，避免一次性加载全部文件。 |
| 本地文件读取 | `read_file` | 用于用户给出本地年报、CSV、Markdown、模型说明、研究报告等文件；不要用 shell `cat/head/tail` 替代。 |
| 本地文件查找/内容搜索 | `search_files` | 用于找 PDF、CSV、Excel、脚本、报告、引用链接和历史产物；不要用 shell `find/grep/rg` 替代。 |
| 文件修改 | `patch` / `write_file` | 修改 skill、报告或脚本时优先用结构化文件工具；大重写用 `write_file`，局部修订用 `patch`。 |
| 网页搜索 | `web_search` | 用于发现公司 IR、交易所公告、SEC filing、行情源、新闻背景；不能把搜索摘要当作财务事实。 |
| 网页/PDF/HTML 提取 | `web_extract` | 优先提取官方披露、SEC HTML、HKEX/巨潮 PDF、公司 IR HTML；若被截断，记录风险并改用下载+本地解析。 |
| 动态网站/反爬页面 | `browser_*` 工具 | 当 `web_extract` 不返回链接、需要点击分页/下载按钮或视觉检查时使用浏览器；完成后记录页面 URL 和操作路径。 |
| 计算与表格处理 | `execute_code` | 适合 3 个以上计算步骤、批量 URL/文件处理、指标重算、数据源审计表生成；输出应保留公式和输入来源。 |
| Shell/系统命令 | `terminal` | 仅用于下载、运行测试、检查文件类型、安装缺失依赖、执行脚本；读取文件仍优先 `read_file`。 |
| 并行研究 | `delegate_task` | 多家公司、多个市场或“数据提取/估值/行业”可并行拆分；子任务必须返回 URL、页码、数值口径和不确定项，父任务需复核关键数字。 |
| 任务管理 | `todo` | 深度研究或多步骤修改时建立任务清单，完成一步更新一步。 |
| 学术/技术论文 | `mcp_arxiv_*` | 仅当公司研究需要技术/学术背景时使用；论文结论不能替代公司披露。 |
| GitHub/代码仓库 | `mcp_github_*` 或 `terminal` git | 仅用于研究项目仓库管理、PR/issue/代码检索；不作为财务事实来源。 |
| Excel 文件 | `mcp_excel_*` | 当用户提供或要求修改 Excel 估值模型时使用；必须检查公式、单位、货币、股本口径。 |
| 计划/定时监控 | `cronjob` | 仅在用户明确要求定期跟踪公司公告、价格或事件日历时创建；prompt 必须自包含。 |

### Hermes 中的标准执行顺序

1. 若用户给本地路径，先将 Windows 路径转换为 WSL 路径，例如 `C:\Users\LTY\...` → `/mnt/c/Users/LTY/...`。
2. 用 `search_files` 枚举目录，用 `read_file` 读取文本文件；PDF/Excel/图片按对应工具处理。
3. 对上市公司研究任务，读取本 skill 后按 `Reference Routing` 选择最少必要 references。
4. 用 `web_search` 找官方来源，用 `web_extract` 或浏览器提取原文；如果已有本地文件，优先分析本地文件。
5. 用 `execute_code` 统一重算估值、汇率、TTM、FCF、核心利润、评分模型；不要手算复杂指标。
6. 输出前用数据源审计表和 Verification Checklist 逐项自检。
7. 如果工具失败，明确写失败原因和替代方案，不要补造数据。

### Hermes 子代理使用规则

适合 `delegate_task` 的情况：

- 3 家以上公司横向比较。
- 同一公司需要同时处理财务数据、行业竞争、估值模型。
- 多市场多语言材料提取。
- 大量来源需要并行核验。

子任务 prompt 必须包含：

- 公司/ticker/市场/报告期。
- 需要返回的字段模板。
- 必须引用原始 URL、文件名、页码或章节。
- 不得直接给最终评级，除非子任务就是独立研究。
- 对不确定数据标注“未核验”或“仅二手来源”。

父任务必须复核：

- 股价和汇率基准日。
- 股本口径。
- 货币单位。
- 关键财务数字。
- 子代理推断是否有原文支撑。

### Hermes 输出到 Telegram 的格式偏好

当前 Hermes 常通过 Telegram 交付，Telegram 不支持原生 Markdown 表格。面向用户的最终回复优先使用：

- 分级标题；
- 项目符号；
- “字段：值”的行组；
- 简短代码块展示公式或审计表模板；
- 如需交付文件，使用 `MEDIA:/absolute/path/to/file`。

若生成长表格、CSV、Excel、Markdown 报告，应写入本地文件并把文件路径/媒体附件交付给用户。

## Codex 适配层（保留，不要删除）

以下内容用于保留 Codex 兼容性。Hermes 执行时可跳过 Codex 专属列；Codex 执行时按可用插件/工具选择，不得因为 Hermes 规则而删除或弱化 Codex 路由。

| 能力 | Codex 优先方式 | 通用 fallback |
|---|---|---|
| 加载 skill | Codex 已触发 skill 时直接遵循；若手工测试，可读取 `SKILL.md` | 明确说明当前平台未自动加载 skill，并按本文件路径执行 |
| 网页搜索 | `web.run` 搜索、可用搜索插件或浏览器工具 | 交易所/公司 IR/SEC URL 直达；记录未检索到的来源 |
| 网页/PDF 提取 | `web.run open`、PDF 工具、本地 `PyMuPDF`/`pdfplumber`/浏览器下载后提取 | 下载原始文件后用本地 PDF 解析；若失败，记录截断/提取风险 |
| 官方 filing/XBRL | Codex 网页工具、shell HTTP 客户端、SEC JSON endpoints | 手动打开 SEC/交易所页面并记录 URL |
| 行情/汇率 | `web.finance`、行情网页、交易所/数据源页面、可用行情插件 | 使用多个行情源交叉验证并标注日期、货币、收盘/盘中 |
| 代码计算 | shell Python/Node、表格工具、数据分析插件 | 手工表格计算并列公式 |
| 并行公司提取 | Codex 可用 subagent/parallel 工具；没有时顺序执行 | 将每家公司设为独立小节，保留统一数据模板 |
| Kanban 编排 | Codex plan/checklist 分阶段执行 | 按 `Standard Workflow` 顺序推进 |
| 本地插件增强 | 读取 `references/codex-plugin-integration.md`，仅在 Codex 环境中按可用插件增强 | 插件不可用时不阻塞主流程 |

## 写作规则

- 在 `SKILL.md` 和行业 reference 中优先写“搜索能力”“PDF 提取能力”“行情能力”“并行任务能力”，不要裸写平台专属工具名。
- 平台专属工具名只应出现在本适配文件或明确标注为平台示例的段落中。
- Codex 插件名和插件调用边界只应出现在 `references/codex-plugin-integration.md`，并明确标注为 Codex-only。
- 输出中需要披露的是数据来源和限制，不需要向读者暴露内部工具细节，除非用户明确要求审计执行过程。

## 最低执行标准

无论使用 Hermes 还是 Codex，都必须做到：

1. 先确认公司、ticker、市场、报告期和交付规格。
2. 优先抓取官方披露或说明官方披露无法获取的原因。
3. 标注每个时间敏感数据的日期、来源、货币和口径。
4. 区分文件直接披露、基于原始数据的计算、分析性判断和二手来源信息。
5. 在最终输出前做单位、货币、股本、利润口径和估值假设一致性审计。
