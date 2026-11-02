<div align="center"><h1>⚡ HOUSEHOLD ENERGY / SCORECARD</h1><p>DAY 02 · EXCEL ANALYSIS · 250 RECORDS</p><img src="https://img.shields.io/badge/WORKBOOK-EXCEL-217346?style=for-the-badge&logo=microsoftexcel"/></div>

## Consumption dashboard
<table><tr><td align="center"><h1>301.34</h1><sub>overall average kWh</sub></td><td align="center"><h1>349.17</h1><sub>February · highest</sub></td><td align="center"><h1>254.30</h1><sub>August · lowest</sub></td></tr></table>

## Household comparison
| SEGMENT | HIGHEST GROUP | AVERAGE USAGE |
|---|---|---:|
| Appliance count | 7 appliances | 339.05 kWh |
| Family size | 3 members | 330.63 kWh |
| Income level | Middle income | 308.05 kWh |

<sub>Values are from saved PivotTable summaries, not independently recalculated from all raw rows.</sub>

## Workbook navigation
```text
RAW_DATA → DATA_CHECK → ANALYSIS → MONTHLY PATTERNS
                                  ↘ APPLIANCE GROUPS
                                  ↘ FAMILY / INCOME GROUPS
                                  ↘ DASHBOARD
```

## Download & validation
- [Excel workbook](./Day-02-Household_Energy_Analysis.xlsx)
- [Results verification](./RESULTS_VERIFICATION.md)
- [Workbook validation guide](./WORKBOOK_VALIDATION_GUIDE.md)
- [Python inspection helper](./verify_workbook.py)
- [PDF report](./day02.pdf)

## Quality gate
250 source rows · 0 duplicates reported · data types marked Correct.

> Formula-driven cells had blank cached values during automated inspection. Recalculate and refresh the workbook in Excel before treating formula-based dashboard KPIs as final.

These sample averages do not prove that household income, appliance count or family size causes energy consumption changes.