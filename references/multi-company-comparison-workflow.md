# Multi-Company Comparison Analysis Workflow

## When to Use This

Use this reference when comparing 2+ listed companies side-by-side, for example: comparing banks, internet platforms, consumer brands, or cross-market peers.

## Core Principle

Comparison is only meaningful after standardizing:

- reporting currency;
- trading currency;
- fiscal year end;
- accounting standard;
- share count;
- GAAP vs non-GAAP earnings;
- industry-specific metrics.

Do not rank companies using mixed, stale, or unverified data.

## Step-by-Step Execution Pattern

### Phase 1: Setup

Create a comparison universe:

```text
Company | Ticker | Market | Reporting currency | Trading currency | Fiscal year end | Source priority
```

Decide whether the comparison is:

- same industry / same market;
- same industry / cross-market;
- different industries but same investment theme;
- holding company vs operating company.

### Phase 2: Price and FX Baseline

Get current price and FX rate from available tools or web sources. Acceptable sources include:

1. market-data MCP tools if available;
2. exchange/company quote pages;
3. TradingView / Stooq / Nasdaq / HKEX / Eastmoney;
4. Yahoo Finance only as fallback.

Always record:

- data date;
- source;
- currency;
- close vs intraday;
- formula used.

### Phase 3: Data Extraction

For each company, extract:

- revenue;
- net income and adjusted/core earnings;
- operating cash flow;
- CapEx;
- FCF;
- cash and debt;
- book value;
- share count;
- dividends;
- industry-specific indicators.

For 3+ companies, delegate extraction in parallel where possible. Each subtask must return source links and page/section references.

### Phase 4: Consolidation and Valuation

Recalculate metrics in a single script or table to avoid inconsistent formulas:

```python
# Example formulas
pe = price / eps
pb = price / book_value_per_share
ps = market_cap / revenue
fcf_yield = fcf / market_cap
dividend_yield = dividend_per_share / price
roe = net_income / average_equity
```

Cross-market conversion must use current FX. Do not reuse historical example rates.

### Phase 5: Scoring

Create an industry-specific scorecard. Generic dimensions:

- valuation attractiveness;
- profitability;
- growth;
- balance sheet / capital adequacy;
- cash-flow quality;
- governance and risk;
- catalyst visibility.

For banks, use `references/multi-bank-comparative-analysis.md`.

### Phase 6: Report

Output should include:

1. comparison summary;
2. standardized data table;
3. company-by-company notes;
4. valuation and quality scores;
5. investor-type fit;
6. final ranking;
7. caveats and data limitations.

## Pitfalls

### Per-share metrics not always comparable

A 股、港股、美股可能使用不同股本口径。ADR/ADS 还涉及换算比例。必须确认每股指标和交易单位匹配。

### Fiscal year mismatch

例如 Alibaba 财年结束日为 3 月 31 日，“FY2025” 与自然年 2025 不同。比较时需对齐报告期。

### Currency conversion

先统一报告货币，再换算交易货币和每股价值。跨市场比较必须标注汇率来源和日期。

### Non-GAAP vs GAAP divergence

科技公司 SBC、重组、投资收益可能导致 GAAP 与 Non-GAAP 差异很大。必须同时展示。

### Banks and insurers need special metrics

银行不要用 FCF；保险不要用报告净利润 PE。使用行业专属 reference。

## Output Format Preferences

Prefer row-group bullets over Markdown pipe tables on Telegram, but use tables in files when appropriate.
