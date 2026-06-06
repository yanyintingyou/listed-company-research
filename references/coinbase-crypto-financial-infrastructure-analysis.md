# Coinbase / 加密金融基础设施公司调研补充

适用对象：Coinbase (COIN)、合规加密交易所、交易所+托管+稳定币+链上基础设施复合型公司。

## 一手资料抓取路径

优先使用 SEC HTML 原文而非新闻二手稿：

- SEC submissions：`https://data.sec.gov/submissions/CIK0001679788.json`
- SEC companyfacts：`https://data.sec.gov/api/xbrl/companyfacts/CIK0001679788.json`
- FY2025 10-K：`https://www.sec.gov/Archives/edgar/data/1679788/000167978826000015/coin-20251231.htm`
- Q1 2026 10-Q：`https://www.sec.gov/Archives/edgar/data/1679788/000167978826000054/coin-20260331.htm`
- Q1 2026 earnings deck：`https://www.sec.gov/Archives/edgar/data/1679788/000167978826000053/q126earningsdeck-finalse.htm`
- Q4 2025 shareholder letter：`https://www.sec.gov/Archives/edgar/data/1679788/000167978826000011/q425shareholderletter.htm`

行情 fallback：Stooq `https://stooq.com/q/l/?s=coin.us&f=sd2t2ohlcv&h&e=csv`。

## 必须区分的收入层

不要把 COIN 机械当作“交易所手续费股”。至少拆成四层：

1. **交易收入**：consumer / institutional / other transaction revenue。受 crypto market cap、波动率、交易量、费率 mix 强影响。
2. **订阅与服务收入**：stablecoin revenue、blockchain rewards、interest and finance fee income、other S&S。
3. **稳定币经济**：USDC balances in Coinbase products、off-platform USDC balances、利率、Circle/合作方分成。
4. **链上/新资产期权**：Base、DEX integration、derivatives、prediction markets、Everything Exchange、agent payments。

输出时把“当前现金流主体”和“长期期权”分开，避免把 Base/agentic economy 早期指标直接资本化为成熟现金流。

## 关键一手指标

### FY2025（10-K / shareholder letter）

- Total revenue：$7.181B；2024：$6.564B。
- Transaction revenue：$4.055B，占 net revenue 59%。
- Subscription and services revenue：$2.828B，占 net revenue 41%。
- Stablecoin revenue：$1.349B，同比增长 48%。
- MTUs：9.2M；Assets on Platform：$376B；Trading Volume：$1.221T。
- Net income：$1.260B；Adjusted EBITDA：$2.808B。
- Trading volume 拆分：Consumer $239B；Institutional $982B。
- Transaction revenue from spot by asset：BTC 27%、XRP 14%、ETH 12%、Other 47%。

### Q1 2026（10-Q / earnings deck）

- Total revenue：$1.413B，同比 -31%。
- Transaction revenue：$755.8M，同比 -40%。
- Subscription and services revenue：$583.5M，同比 -14%，占 net revenue 44%。
- Stablecoin revenue：$305.4M；Blockchain rewards：$100.8M；Interest and finance fee income：$67.8M。
- MTUs：8.2M；Assets on Platform：$294B；Trading Volume：$202B。
- Net loss：$(394.1)M；Adjusted EBITDA：$303.3M。
- Losses on crypto assets held for investment：$482.4M，是 GAAP 净亏损的重要来源。
- Q1 deck：crypto market volumes Q/Q -28%，spot volumes Q/Q -37%，transaction revenue Q/Q -23%。
- Derivatives trading volume TTM +169% Y/Y；retail derivatives annualized revenue $200M+；prediction markets March annualized revenue $100M+；DEX cumulative volume $450M+。

## 会计与比较口径坑

1. **GAAP 净利润不等于核心经营利润**：crypto assets held for investment 的公允价值损益会大幅扰动净利润。必须同时看 operating income、Adjusted EBITDA、crypto investment gains/losses。
2. **Adjusted EBITDA 也不能当自由现金流**：它剔除 SBC、折旧摊销、投资损益等，适合作为周期中性盈利能力参考，但不能直接等同股东可分配现金。
3. **stablecoin revenue 口径变化**：Q1 2026 起，公司将 corporate payment stablecoin balances 所赚收入从 Stablecoin revenue 调整至 Corporate interest and other income，并重分类 Q1 2025 对应 $23.5M。做同比时需说明口径。
4. **Trading Volume 定义变化**：2025 Q4 公司将 routing off platform 的 spot trades 半数价值加入 Trading Volume，历史口径已 recast。引用交易量需说明定义。
5. **现金安全垫需扣债**：不要只引用 cash & equivalents。Q1 2026 cash & equivalents $10.205B，但还要扣 current debt、long-term debt、short-term borrowings；净资源估算更稳妥。
6. **客户资产与公司资产分开**：customer custodial funds 与对应 liabilities、safeguarding obligations 不应当作公司可用现金。

## 商业模式判断框架

- **Bear 视角**：交易费率下行 + crypto 低波动 + 交易量收缩，COIN 仍是高 beta 周期股。
- **Base 视角**：合规交易所 + 托管 + USDC + Prime + derivatives，周期性下降但仍明显。
- **Bull 视角**：Everything Exchange + Base + stablecoin payments + onchain finance，重估为合规链上金融基础设施。

## 估值建议

标准 DCF 对 COIN 可靠性较低，因为收入/利润高度周期性。优先使用：

1. 周期中性 Adjusted EBITDA × 倍数 + 净资源；
2. SOTP：交易所/经纪业务、S&S/稳定币、Base/链上期权、投资资产；
3. 情景概率加权。

示例框架（需按最新价格和财务更新）：

- Bear：Adjusted EBITDA $1.5B × 12x + 净资源。
- Base：Adjusted EBITDA $2.5B × 18x + 净资源。
- Bull：Adjusted EBITDA $4.0B × 22x + 净资源。
- Super Bull：Adjusted EBITDA $5.5B × 25x + 净资源。

## 输出规范

- 明确区分：文件直接披露 vs 分析性判断。
- 对 X 平台讨论只作为市场情绪/叙事补充，不替代 SEC 文件。
- 对 Base、agent payments、prediction markets 等新业务，必须标注“当前收入贡献仍早期/期权性质”，除非公司已披露成熟收入规模。
- 监管既是风险也是护城河：短期可能压制产品边界，长期可能强化合规头部平台。