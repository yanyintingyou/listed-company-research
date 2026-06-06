# A股上市银行财务数据获取实战指南

## 适用场景
分析A股上市银行（四大行、股份行、城商行等）的年报、半年报、季报。

## 数据源优先级（银行专项）

### 1. 巨潮资讯网直链（最稳定）
格式：`http://static.cninfo.com.cn/finalpage/[YYYY-MM-DD]/[公告ID].PDF`

已验证可用的银行公告ID示例：
- 中国银行2025年年报：`http://static.cninfo.com.cn/finalpage/2026-03-31/1225058470.PDF`
- 中国银行2026Q1季报：`http://static.cninfo.com.cn/finalpage/2026-04-30/1225261331.PDF`
- 工商银行2024年年报：`http://static.cninfo.com.cn/finalpage/2025-03-29/1222948914.PDF`
- 工商银行2025年年报：`http://static.cninfo.com.cn/finalpage/2026-03-28/1225047240.PDF`

**获取方法**：搜索"[银行名] [年份] 年报 PDF cninfo"或"[银行名] [年份] 季报 巨潮资讯"

### 2. 中国货币网 chinamoney.com.cn（央行指定信息披露）
格式：`https://www.chinamoney.com.cn/chinese/cwbg/[日期]/[contentId].html`（页面内含PDF下载）
或直接PDF：`https://www.chinamoney.com.cn/dqs/cm-s-notice-query/fileDownLoad.do?contentId=[ID]&mode=save&priority=0`

### 3. 银行官网投资者关系页面
- **中国银行**：`www.boc.cn/investor/ir3/`（年报）；`www.boc.cn/investor/ir2/`（季报）
- **农业银行**：`www.abchina.com/cn/aboutabc/investor_relations/report/am/[日期]/[文件名].pdf`
  - 2025年年报：`P020260330775691624018.pdf`
  - 2024年年报：`P020250428599899234186.pdf`
  - 季报路径：`www.abchina.com/En/investor-relations/corporate-announcements/Announcements/[日期]/[文件名].pdf`
- **工商银行**：`v.icbc.com.cn/userfiles/resources/icbcltd/download/[年份]/[文件名].pdf`
  - 2026Q1：`Announce20260429_5.pdf`

### 4. 前瞻眼 qianzhan.com（聚合下载页）
格式：`https://stock.qianzhan.com/hs/sourcefiles_[代码].SH.html`
提供所有历史报告的 PDF 下载链接列表。不同平台的网页提取能力可能无法直接返回 PDF 链接；按 `references/platform-adapter.md` 选择浏览器、网页提取或搜索 fallback。

### 5. 东方财富网（补充数据）
格式：`https://emweb.eastmoney.com/pc_hsf10/OperationsRequired/Index?code=SH[代码]`
提供已结构化的财务指标、每股数据，但不是原始PDF。

## 每股数据搜索技巧

### 每股净资产
搜索："[银行名] [年份] 每股净资产 [代码]"
- 通常在年报PDF的"主要财务指标"表格中
- 东方财富网也会披露

### 每股分红
搜索："[银行名] [年份] 分红 每股股利 [代码]"
- 年报中有"每10股派X元（含税）"的表述
- 需要除以10得到每股分红
- 注意区分中期分红和末期分红

## 行情兜底代码格式

行情平台只用于获取当前价格、市值、52周区间和估值基准日，不能替代年报/季报原文。若使用 Yahoo、TradingView、东方财富、雪球、富途等行情源，必须标注数据日期、来源、货币和是否为收盘价。

常见代码格式：
- A股上海：`601988.SS` 或 `SSE:601988`
- A股深圳：`000001.SZ` 或 `SZSE:000001`

## PDF 提取注意事项

1. **巨潮直链 PDF 通常可提取**：cninfo.com.cn 的 PDF 链接适合优先尝试当前平台的 PDF/网页提取能力。
2. **银行官网 PDF 通常可提取**：abchina.com、boc.cn 的 PDF 链接一般可用。
3. **超大年报可能被截断**：完整年报 PDF 可能超过在线提取能力；必要时下载后用本地 PDF 解析工具分段提取。
4. **中英文版本**：银行官网通常提供中英文版本，英文版有时提取质量更高（特别是IFRS准则版本）
5. **季报通常比年报短**：季报PDF更容易完整提取

## 并行获取策略

当需要同时获取多家银行数据时，优先使用当前平台的并行/多代理能力；没有并行能力时，按统一模板顺序处理：
- 每个子任务负责一家银行
- 子任务内使用当前平台的搜索和 PDF/网页提取能力获取内容
- 子任务返回结构化数据摘要
- 父任务汇总并对比分析

## 关键陷阱

1. **区分集团 vs 母公司数据**：银行有合并报表和母公司报表，分析应使用合并报表
2. **区分中国会计准则 vs 国际准则**：A股使用中国会计准则（PRC GAAP），H股使用IFRS，两者净利润通常一致但其他指标可能有差异
3. **季报未经审计**：季报数据是未经审计的，需要注明
4. **年化ROE/ROA**：季报中的ROE/ROA需要年化处理（乘以4），但要考虑季节性因素
5. **股本变动**：银行可能有优先股、永续债等影响总股本的工具，计算每股指标时需注意
6. **分红时间差异**：中期分红和末期分红可能在不同时间发放，计算股息率时应使用全年合计
