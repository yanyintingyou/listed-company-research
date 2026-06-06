# PLTR / Palantir 调研方法补充：AI平台型软件公司的一手数据核验

适用：研究 Palantir、企业 AI 平台、政府/商业双轮驱动的软件公司，尤其是市场以“AI基础设施/企业操作系统”叙事给高 EV/Sales 的标的。

## 一手文件优先级

1. SEC 10-K / 10-Q 原文：业务描述、客户结构、分部贡献、RPO/RDV、合同可取消性、采购承诺、债务与现金。
2. SEC 8-K Exhibit 99.1 业绩稿：季度收入、指引、Non-GAAP 调整、管理层原话。
3. SEC companyfacts XBRL：批量抓收入、毛利、营业利润、净利润、经营现金流、CapEx、EPS、股数。
4. Stooq / Yahoo / StockAnalysis：只用于行情、市值、分析师目标价交叉验证；不可替代 SEC 原始披露。
5. X 平台：只作为市场情绪、争议点、叙事结构参考，不作为财务事实来源。

## PLTR 这类公司的关键原文信号

### 业务模式

- 查 10-K `Business / Overview`：平台定义、产品名称、AIP 描述。
- 查 `Revenue`：是否来自 hosted subscription、customer environment subscription、O&M、professional services。
- 查 `Sales and Marketing / Customer Acquisition`：是否披露 pilots / bootcamps，是否由公司先承担成本。

### 政府 vs 商业

- 查 `Segment and Geographic Information`：government revenue、commercial revenue、contribution、contribution margin。
- 对 Palantir 这类公司，单看收入结构不够；必须看 government/commercial contribution margin 是否同步提升。若商业分部 contribution margin 已接近政府分部，说明产品化程度可能提高。

### 美国 vs 海外

- 查 geographic revenue：United States、United Kingdom、Rest of world。
- 若美国收入占比上升，需明确标注：增长引擎可能高度集中于美国 AI 预算/国防预算周期，海外扩张尚未同速验证。

### 合同质量

必须区分：

- RPO：non-cancelable contracted revenue not yet recognized。
- RDV / total remaining deal value：口径更宽，可能包含可取消、选项、未来条件。

若文件出现 `termination for convenience`，必须在风险章节高亮：不能把全部 deal value 机械折现为确定收入。

### 云服务/采购承诺

对 AI 平台型软件公司，除传统债务外，要查 `Purchase Commitments`：

- 长期 cloud hosting minimum commitments 不是传统债务，但具有类固定成本经济实质。
- 如果收入增长放缓，长期云承诺可能压缩利润率。
- 如果收入继续高增，它也可被解释为管理层对需求的信心。

## 分析性判断表达规范

可作为文件直接披露：

- 收入、分部收入、contribution margin、RPO、RDV、客户数、前几大客户占比、现金/证券、债务、采购承诺。

必须标注为“分析性判断”：

- “从项目制向产品化平台迁移”
- “企业 AI 操作系统”
- “护城河来自 ontology + workflow + 安全治理”
- “AIP 不是普通 AI wrapper”
- “估值反映完美执行”

## 估值注意事项

PLTR 这类公司不能只用普通成熟软件 DCF，也不能只用高 EV/Sales 叙事。

建议三层并列：

1. 当前市场隐含倍数：EV / FY guidance revenue、P / guided FCF。
2. 相对估值矩阵：15x/20x/25x/30x/35x/40x/45x/50x forward EV/Sales 对应股价。
3. 10 年 DCF 情景：Bear/Base/Bull，明确收入终局规模、FCF margin、WACC、terminal growth。

输出时应强调：DCF 对高增长软件非常敏感，重点是揭示当前股价隐含假设，而不是给出“精确公允价值”。

## X 平台使用规范

X 搜索可用于总结市场共识：

- 多头叙事：AIP、美国商业收入、政府底盘、Rule of 40、AI infrastructure。
- 空头/谨慎叙事：估值、合同可取消、云承诺、客户集中、竞争。

但所有数字必须回到 SEC/IR 原文核验。不要引用 X 作为财务事实来源。
