<div align="center"><h1>⚡ HOUSEHOLD ENERGY — EXCEL FIELD REPORT</h1><b>Day 02 · 250 household records</b><img src="https://img.shields.io/badge/Excel-WORKBOOK-217346?logo=microsoftexcel"/></div>

## Workbook navigation
| Sheet | Purpose |
|---|---|
| Raw_Data | 250 household records |
| Data_Check | Duplicate and type checks |
| Analysis | Summary calculations |
| Energy consumption patterns | Monthly comparison |
| Household group sheets | Appliance, family and income comparisons |
| Dashboard sheet | Summary view |

## Saved PivotTable readout
| Dimension | Highest group | Average usage |
|---|---|---:|
| Appliance count | 7 appliances | 339.05 kWh |
| Family size | 3 members | 330.63 kWh |
| Income level | Middle income | 308.05 kWh |

| Month view | Average usage |
|---|---:|
| February · Highest | 349.17 kWh |
| August · Lowest | 254.30 kWh |
| Overall | 301.34 kWh |

<sub>Values are from saved PivotTable summaries, not independently recalculated from all raw rows.</sub>

## Download desk
[Excel workbook](./Day-02-Household_Energy_Analysis.xlsx) · [Results verification](./RESULTS_VERIFICATION.md) · [Validation guide](./WORKBOOK_VALIDATION_GUIDE.md) · [Python helper](./verify_workbook.py) · [PDF](./day02.pdf)

## Quality status
250 source records · 0 duplicates reported · data types marked Correct.

> Formula-driven cells had blank cached values during automated inspection. Recalculate and refresh the workbook in Excel before treating formula-based dashboard KPIs as final.

Group averages describe this sample only; they do not prove that income, appliance count or family size causes consumption changes.