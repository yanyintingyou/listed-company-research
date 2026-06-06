---
name: listed-company-research
description: Use when conducting deep fundamental research on listed companies across A-shares, Hong Kong stocks, and US stocks, including primary-source extraction, financial quality analysis, valuation routing, risk assessment, source verification, and investment thesis synthesis.
license: MIT
metadata:
  version: 1.1.0
  author: Listed Company Research Skill
  platforms:
    - hermes
    - codex
  tags:
    - research
    - equity-research
    - listed-companies
    - valuation
    - financial-analysis
    - china-stocks
    - hong-kong-stocks
    - us-stocks
    - source-verification
  hermes:
    related_skills:
      - chinese-stock-research
      - hk-conglomerate-sotp-analysis
      - hk-stock-financial-data
      - hk-stock-subsidiary-confusion-prevention
      - ai-research-model-comparison
---

# 上市公司深度研究综合 SOP

## Overview

本 skill 用于执行 A 股、港股、美股上市公司的深度基本面研究。核心目标不是生成“看起来完整”的股票报告，而是建立一套可复核、可追溯、可审计的研究流程：从一手披露文件出发，提取财务与经营事实，明确区分文件直接披露与分析性判断，再通过合适的估值方法、情景分析和风险框架形成投资论点。

适用对象包括普通工业/消费/科技公司、平台型公司、AI/半导体公司、银行、保险、综合控股集团、游戏/广告媒体等。行业专项方法应按下文 `Reference Routing` 加载对应 reference。

## Platform Compatibility

本 skill 的研究流程必须保持平台无关。需要搜索网页、提取 PDF/HTML、获取行情、运行计算、并行拆分任务或执行 Kanban 流程时，先读取 `references/platform-adapter.md`，按当前环境选择 Hermes、Codex 或通用 fallback。

不要在主流程中硬调用某个平台的专属工具。若当前平台缺少某项能力，使用可用替代方案，并在输出中说明数据来源、能力限制和未完成的核验项。

## When to Use

在用户提出以下任一需求时，优先加载本 skill：

- 研究上市公司、股票基本面、投资价值、年报/中报/季报/招股书。
- 分析 A 股、港股、美股公司，包括单家公司深度研究或多家公司横向比较。
- 做估值分析，包括 DCF、相对估值、SOTP、P/EV、P/B、DDM、EV/EBITDA、EV/Revenue。
- 审阅或重建 AI/第三方生成的公司研究报告、估值模型或投资备忘录。
- 要求写成公开文章、公众号文章、投资备忘录或研究报告。
- 要求逐条核验来源、页码、原文、数据口径或推断依据。

不要把本 skill 用于：

- 纯技术面短线交易信号；除非用户明确要求基本面+技术面结合。
- 未上市公司尽调；可借用部分框架，但需改用私募/招股书/工商资料逻辑。
- 宏观资产配置；除非宏观变量是公司估值假设的一部分。

## Non-Negotiable Research Guardrails

1. **一手披露优先**：优先使用交易所/SEC/公司 IR 的年报、中报、季报、招股书、业绩公告、电话会纪要、XBRL 或 filing HTML。二手媒体和行情平台只能用于补充、交叉验证或获取市场价格。
2. **先取原文，再下结论**：不得仅凭搜索摘要、新闻片段或二手数据库直接输出财务分析。若官方文件无法获取，必须说明阻塞原因并标注替代来源层级。
3. **事实与推断分离**：输出中必须区分：
   - **文件直接披露**：财务数字、管理层原话、业务分部描述、风险披露、会计政策。
   - **分析性判断**：商业模式定性、护城河判断、估值假设、竞争推演、风险概率。
4. **时间敏感数据必须重查**：股价、汇率、市值、估值倍数、股息率、分析师目标价均必须标注数据日期、来源、货币和价格类型。reference 中的案例数字不得直接复用为当前事实。
5. **估值方法必须匹配商业模式**：不要机械套用 PE/DCF；先识别行业、生命周期、资产结构、现金流性质，再选择估值方法。
6. **输出前做一致性审计**：检查单位、货币、股本口径、利润口径、现金流定义、资产负债表配平、DCF 假设与正文叙事是否一致。

## Standard Workflow

### 阶段 0：任务定型与输出规格

先判断用户要的是哪一类交付：

- **快速判断版**：适合“这家公司能买吗”“季报怎么看”。输出结论、关键数据变化、一次性项目、核心风险、下一步需核验文件。
- **深度研究版**：适合“全面研究 XX 公司”。输出数据源审计、公司概况、行业坐标、商业模式、财务质量、竞争格局、风险、估值、投资论点、来源附录。
- **横向比较版**：适合 2 家以上公司比较。使用 `references/multi-company-comparison-workflow.md`。
- **公开文章版**：适合公众号/长文。使用 `references/public-article-writing-guide.md`。
- **来源核验版**：适合用户要求逐条核验原文。使用 `references/source-verification-template.md`。

深度研究、报告审阅或投资备忘录任务，还应读取 `references/analysis-process-extensions.md`，补齐主体映射、市场预期、资本配置、催化剂、反证审计和可复现性要求。

### 阶段 1：一手数据获取

按市场选择数据源。完整市场路由见 `references/data-source-map-by-market.md`。

**美股优先级：**

1. SEC EDGAR 10-K/10-Q/8-K/S-1 filing HTML。
2. SEC companyfacts XBRL。
3. 公司 IR earnings release、shareholder letter、presentation、transcript。
4. Stooq / Nasdaq / TradingView / Yahoo 等只用于行情和估值基准日交叉验证。

**港股优先级：**

1. HKEXnews 公告原文。
2. 公司 IR 英文版年报/中报/公告；英文版通常为法定版本。
3. 公司业绩发布材料、电话会纪要。
4. 东方财富港股 F10、富途、雪球、新浪、Yahoo 等仅作行情和摘要交叉验证。

**A 股优先级：**

1. 巨潮、上交所、深交所、北交所公告原文。
2. 公司 IR 与投资者关系活动记录。
3. 东方财富公告 PDF、新浪公告 PDF 作为原文兜底。
4. Wind/iFinD/Choice 若用户有权限可用，但必须标注数据库口径。
5. 行情平台仅作价格/市值核验。

### 阶段 2：数据源审计表

深度研究必须在报告中列出数据源审计表：

```text
文件/URL：
来源类型：交易所 / SEC / 公司IR / 媒体 / 数据库 / 行情平台
报告期：
获取时间：
使用目的：
是否原始披露：是/否
是否存在截断/翻译/摘要风险：
关键页码/章节：
可信度等级：高/中/低
```

### 阶段 3：财务深度分析

用三层递进框架组织财务事实：

1. **What：数字是什么？**
   - 收入、毛利、营业利润、净利润、EPS、经营现金流、CapEx、FCF、现金、债务、股本。
   - 至少覆盖 3 年；若是季报，必须比较 YoY、QoQ、全年趋势和前期基数。
2. **Why：为什么这样？**
   - 管理层 MD&A 解释、价格/销量/汇率/并购/会计政策/一次性项目。
   - 明确 GAAP vs Non-GAAP、报告利润 vs 经常性利润。
3. **So What：意味着什么？**
   - 趋势是否可持续，对现金流、估值、风险溢价和投资论点的含义。

财务质量最低检查项：

- 经营现金流/净利润。
- FCF = CFO - CapEx，定义是否与公司口径一致。
- ROE、ROIC、增量 ROIC。
- 应收、存货、合同负债、商誉、长期股权投资、少数股东权益。
- 一次性收益/损失、减值、投资收益、公允价值变动、递延税。
- 股本口径：总股本、流通股、稀释股、加权平均股本。

### 阶段 4：商业模式与护城河

先从披露文件寻找原文信号，再做分析性判断。

**产品制 vs 项目制信号：**

- 收入确认：订阅按期摊销、API 按调用量确认、授权按使用确认 → 产品制信号。
- 收入确认：客户验收、里程碑、定制开发、本地部署 → 项目制信号。
- 分部描述：`standardised`、`cloud-based`、`ratably`、`usage-based` 等 → 产品化信号。
- 分部描述：`customised`、`accepted by customers`、`delivery resources` 等 → 项目制信号。

**护城河评分维度：**

- 品牌/心智。
- 规模/网络效应。
- 成本/运营优势。
- 资源/技术垄断。
- 渠道/关系壁垒。

输出：护城河总分、护城河宽度、护城河趋势、未来 3 年被侵蚀或强化的机制。

### 阶段 5：估值方法选择与计算

先使用 `references/valuation-method-router.md` 判断估值方法，再建模。所有估值必须给出假设、敏感性和概率权重。

基本公式：

$$E[V] = \sum_i p_i V_i$$

$$\text{安全边际} = \frac{\text{内在价值} - \text{当前价格}}{\text{内在价值}} \times 100\%$$

必须说明：

- 估值基准日和股价来源。
- 使用货币与汇率。
- 股本口径。
- 估值方法为什么适用。
- 什么假设会让结论失效。

### 阶段 6：风险评估

至少输出 Top 5 风险，每个风险包含概率、影响、触发条件、缓解因素、估值影响。

常见风险维度：

- 经营风险：客户集中、供应链依赖、产品迭代、竞争加剧。
- 宏观/周期风险：需求弹性、价格周期、原材料、大宗商品、广告/消费周期。
- 政策/地缘风险：监管、反垄断、出口管制、制裁、VIE、跨境审计。
- 财务风险：债务、商誉、应收、汇率、少数股东权益、关联交易。
- 资本配置风险：低 ROIC 并购、过度 CapEx、回购/分红不可持续。

### 阶段 7：模型内一致性审计

输出投资结论前必须检查：

- 资产负债表是否配平：Assets = Liabilities + Equity。
- FCF 定义是否一致：CFO - CapEx，是否剔除并购/融资性项目。
- 同一指标在正文、表格、估值模型、摘要中是否一致。
- 股本是否混用总股本、流通股、稀释股本或加权平均股本。
- 财报货币、交易货币、估值货币是否统一。
- 港股 CNY/HKD 换算方向是否正确。
- DCF 终值假设与正文增长叙事是否一致。
- 先例交易是否误把控制权溢价用于少数股权上市估值。

### 阶段 8：投资论点合成

最终报告必须回答：

- 公司真正靠什么赚钱？
- 当前利润中有多少是可持续的？
- 市场当前价格隐含了什么预期？
- 最大的看多与看空论点是什么？
- 催化剂是什么？没有催化剂是否可能成为价值陷阱？
- 适合哪类投资者，不适合哪类投资者？
- 结论的置信度是多少，缺失数据是什么？

评级可使用：强烈买入 / 买入 / 持有 / 减持 / 回避。若数据不足，必须明确写“暂不评级”或“仅能形成初步判断”。

若输出面向公众或可能被理解为个人投资建议，必须标注“仅供研究讨论，不构成个性化投资建议”。

## Valuation Method Quick Router

完整路由见 `references/valuation-method-router.md`。快速规则：

- **银行**：P/B、P/TBV、ROE-COE、股息率；不要用 FCF。
- **保险**：P/EV、P/Operating EPS、NBV 倍数、DDM；不要用报告净利润 PE。
- **综合控股集团**：SOTP + 控股折价 + 催化剂；不要用单一 PE。
- **软件/SaaS/平台**：EV/Revenue、EV/FCF、Rule of 40、RPO/NRR；成熟期可 DCF。
- **高资本开支 AI/半导体**：FCF、折旧周期、CapEx/Revenue、ROIC、供需周期；警惕只用 P/S。
- **游戏公司**：老 IP 现金流 + 新游期权 + 流水/留存/版号风险。
- **广告媒体**：EV/EBITDA、FCF yield、宏观 beta、点位扩张质量。
- **消费品牌**：PE、EV/EBITDA、ROIC、定价权、渠道库存。
- **周期品**：EV/EBITDA、P/B、周期底部盈利、资产负债表压力；不要用景气顶点 PE。

## Reference Routing

按任务选择 reference，不要无差别加载全部文件。

- **市场数据源路径**：`references/data-source-map-by-market.md`
- **Hermes/Codex 平台适配**：`references/platform-adapter.md`
- **分析流程增强项**：`references/analysis-process-extensions.md`
- **Codex 插件集成（Codex-only）**：`references/codex-plugin-integration.md`
- **估值方法选择**：`references/valuation-method-router.md`
- **来源逐条核验**：`references/source-verification-template.md`
- **公开文章/公众号写作**：`references/public-article-writing-guide.md`
- **多公司横向比较**：`references/multi-company-comparison-workflow.md`
- **银行股比较**：`references/multi-bank-comparative-analysis.md`
- **A 股银行数据获取**：`references/a-share-bank-data-acquisition.md`
- **保险公司研究**：`references/insurance-company-analysis.md`
- **AI/大模型/软件平台公司**：`references/ai-company-analysis-framework.md`
- **AI 资本开支周期**：`references/ai-capex-cycle-analysis.md`
- **港股控股集团/SOTP 案例**：`references/kingsoft-holding-sotp-case.md`
- **广告/媒体公司案例**：`references/ad-media-company-analysis-focus-media.md`
- **游戏分部案例**：`references/game-segment-analysis-kingsoft-seasun.md`
- **Coinbase/加密金融基础设施**：`references/coinbase-crypto-financial-infrastructure-analysis.md`
- **Palantir/AI 平台型软件公司**：`references/pltr-aip-company-analysis-notes.md`
- **Kanban 多智能体执行**：`references/listed-company-kanban-workflow.md`

## Output Templates

### 快速判断版

```md
## 一句话结论

## 数据源与基准日
- 股价：
- 财报/公告：
- 其他来源：

## 关键变化
- 收入：
- 利润：
- 现金流：
- 一次性项目：

## 投资含义
- 看多：
- 看空：
- 当前估值隐含预期：

## 下一步需核验
```

### 深度研究版

```md
## 结论摘要
## 数据源审计表
## 公司与行业坐标
## 商业模式与护城河
## 财务质量分析
## 管理层与治理
## 风险评估
## 估值分析
## 情景分析与概率加权
## 投资论点与评级
## 一致性审计
## 来源附录
```

### 多公司比较版

使用 `references/multi-company-comparison-workflow.md`，最低输出：

- 同口径数据表。
- 各公司估值和财务质量评分。
- 可比性限制。
- 投资者类型适配。
- 最终排序与置信度。

## Common Pitfalls

### 数据源错误

- 用新闻摘要替代官方披露。
- 没有标注股价、汇率、估值倍数的日期和来源。
- 把 reference 中的历史案例数字当作当前事实。
- 官方 PDF 提取失败时不说明阻塞原因，直接使用二手来源。

### 单位与货币错误

- 港股公司用人民币报告、港币交易，CNY/HKD 换算方向错误。
- million、billion、亿元、百万元混用。
- 每股指标使用错误股本口径。
- A+H/ADR 多地上市时混淆上市主体和子公司层级。

### 会计口径错误

- 用报告净利润替代经常性利润。
- 忽略减值、投资收益、公允价值变动、递延税、资本公积转回。
- 混淆 GAAP 与 Non-GAAP。
- 经营现金流与净利润严重背离却未解释。

### 估值方法错误

- 银行使用 FCF。
- 保险使用报告净利润 PE。
- 综合控股集团使用单一 PE。
- 周期品使用景气顶点利润估值。
- 高 CapEx 科技公司只看 P/S，不看 FCF、折旧和 ROIC。
- 把“折价大”直接等同于“安全边际高”，忽略催化剂。

### 商业模式判断错误

- 仅凭收入结构断言产品制/项目制，没有核对收入确认和分部原文。
- 把未来叙事当成当前收入来源。
- 忽略客户集中、合同取消权、RPO/RDV 质量、续费率和销售效率。

## Verification Checklist

完成深度研究前逐项检查：

- [ ] 已获取并标注官方披露文件或解释无法获取的原因。
- [ ] 已列出数据源审计表。
- [ ] 已确认上市主体、运营主体、ticker、证券类别、股本口径、ADR/ADS/A-H/VIE/控股结构映射。
- [ ] 已区分文件直接披露与分析性判断。
- [ ] 已标注股价、汇率、市值、估值倍数的日期、来源、货币。
- [ ] 已覆盖 3 年以上财务趋势或解释数据缺口。
- [ ] 已提取能解释收入和利润的关键经营 KPI，或说明公司未披露导致的置信度影响。
- [ ] 已审查资本配置、回购/分红/SBC、并购、债务和增量 ROIC。
- [ ] 已识别一次性项目和经常性利润。
- [ ] 已检查现金流质量、ROIC、增量 ROIC。
- [ ] 已选择与行业/商业模式匹配的估值方法。
- [ ] 已说明市场当前价格隐含预期、主要看多/看空版本和结论失效条件。
- [ ] 已列出关键催化剂、事件日历和需要继续跟踪的数据。
- [ ] 已做情景分析、敏感性分析或概率加权。
- [ ] 已输出 Top 5 风险及估值影响。
- [ ] 已完成模型内一致性审计。
- [ ] 若在 Codex 中使用插件，插件输出已回溯到原始来源、URL、页码、表格或计算链。
- [ ] 若在 Hermes 中执行，已按 `references/platform-adapter.md` 使用可用工具完成真实检索、提取、计算或文件审计；失败项已说明原因和替代方案。
- [ ] 已说明结论置信度和仍需补充的数据。
