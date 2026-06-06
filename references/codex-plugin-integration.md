# Codex 本地插件集成（Codex-only）

## 重要边界

本文件只给 Codex 环境使用。Hermes 看到本文件时，不应尝试调用 Codex 插件、Codex MCP 或 Codex 工具名；Hermes 可使用自身等价能力，或忽略本文件。

Codex 使用插件时遵循两条规则：

1. 只有当插件能力已经在当前工具列表中可用，或能通过 Codex 的工具发现机制暴露时，才调用该插件。
2. 最终研究报告引用的是原始数据源、文件、页码、URL 和计算过程，不把“某插件说了什么”当作来源。

## Codex 如何引用插件

在 Codex 中，插件不是主流程的强制依赖。需要时按能力选择：

- 若插件已有明确 skill，例如 Public Equity Investing、Data Analytics、Spreadsheets、Presentations 等，按该插件 skill 的说明触发或读取。
- 若插件工具是延迟加载的，使用 Codex 的工具发现能力查找具体工具；工具不可用时，改用 `references/platform-adapter.md` 的通用 fallback。
- 在 `SKILL.md` 和行业 reference 中不要写“必须用某插件”；只写“Codex 可选使用某插件增强某环节”。

## 插件路由

| 研究环节 | Codex 可选插件 | 用法 | 注意事项 |
|---|---|---|---|
| 上市公司投资框架、备忘录、 thesis review | Public Equity Investing | 用于投资论点、风险收益框架、上市股研究工作流 | 仍需回到一手文件和本 skill 的来源核验 |
| 财报电话会、IR transcript、presentation、filing | Quartr | 用于获取第一方 IR 材料、transcript、会议资料 | 使用前遵循 Quartr 插件自身 guide；不要编造 event/document id |
| 实时行情、历史价格、期权链 | Alpaca | 用于美股/ETF/期权/部分加密行情核验 | 只作市场数据来源，不替代公司披露 |
| 加密资产或交易所市场数据 | Binance | 分析 Coinbase、矿企、稳定币或 crypto beta 时用于市场背景 | 只读公开市场数据，不作为投资建议 |
| 模型、CSV、财务表、数据清洗 | Data Analytics | 用于重建指标、做诊断、生成 dashboard/report | 查询和图表必须保留数据源与口径说明 |
| 估值模型、财务 workbook | Spreadsheets | 用于创建/审阅 DCF、SOTP、敏感性表 | 检查公式、单位、货币、股本口径和链接断点 |
| 报告可视化、图表、仪表盘 | Build Web Data Visualization / Data Analytics | 用于展示趋势、同业比较、风险矩阵 | 图表标题和数据源必须一致，避免视觉误导 |
| 投资备忘录、研究报告 Word 文档 | Documents | 用于生成或编辑长文档 | 不改变事实核验要求 |
| 投资委员会或 pitch deck | Presentations | 用于生成 PPTX/slide deck | 每页关键数据需可追溯 |
| 本地网页预览或报告 artifact 检查 | Browser | 用于打开/验证本地报告、dashboard、HTML artifact | 主要用于渲染 QA，不替代外部来源核验 |
| 代码仓库、模型版本、发布流程 | GitHub | 用于管理研究项目仓库、PR、CI | 不用于财务事实来源 |
| 法律/诉讼/监管案例背景 | Midpage | 涉及重大诉讼、监管裁决、判例时辅助研究 | 高风险法律结论需标注来源和非法律意见 |
| 学术文献或已有参考管理 | Zotero / Hugging Face / arxiv | 只在需要学术或技术文献背景时使用 | 与公司财务事实分开标注 |

## 推荐组合

### 单家公司深度研究

1. 本 skill 建立数据源审计和研究流程。
2. Quartr 或官方 IR 获取 transcript/presentation。
3. Alpaca 或行情源核验价格、市值和估值基准日。
4. Spreadsheets/Data Analytics 重建估值和敏感性。
5. Documents 或 Presentations 输出最终交付物。

### 多公司横向比较

1. 本 skill + `multi-company-comparison-workflow.md` 统一口径。
2. Alpaca/行情源统一价格和 FX 基准日。
3. Data Analytics 或 Spreadsheets 统一计算 PE/PB/PS/FCF yield/ROE。
4. Data Visualization 生成比较图表。

### 报告/模型审阅

1. 本 skill 先做来源核验和事实/推断分类。
2. Spreadsheets 检查模型公式和假设。
3. Data Analytics 复算关键指标。
4. Documents 生成审阅意见或修订版报告。

## 报告中的引用方式

正确：

- “来源：公司 FY2025 10-K，Item 7，Management Discussion and Analysis。”
- “来源：HKEX 公告，2026-03-28，年报第 112 页。”
- “当前股价：Alpaca/Yahoo/交易所页面，2026-06-06 收盘价，USD。”

错误：

- “来源：Quartr。”
- “来源：Data Analytics。”
- “来源：插件结果。”

插件可以帮助取得或处理材料，但证据必须落到可审计的原始来源、URL、页码、表格或计算链。
