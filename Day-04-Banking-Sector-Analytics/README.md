<div align="center">
<h1>🏦 BANKING ANALYTICS — MANAGEMENT BRIEF</h1>
<img src="https://img.shields.io/badge/POWER%20BI-PBIX-F2C811?style=for-the-badge&logo=powerbi"/>
<p>Day 04 · Customer, transaction and loan exploration</p>
</div>

## Executive dashboard
| 250 source rows | 92 customers | Average balance 52,646.45 |
|:---:|:---:|:---:|

## Transaction position
| Credit total | Debit total | Net (credit − debit) |
|---:|---:|---:|
| 1,161,613.89 | 1,282,489.51 | **−120,875.62** |

10 records have balances below 5,000.

## Loan status register
| Status | Records |
|---|---:|
| Active | 25 |
| Default | 26 |
| Closed | 19 |
| Blank | 180 |
| **Known-status total** | **70** |

Default rate among nonblank loan statuses: **37.14%** (26 of 70). Blank statuses are not classified into a known status.

## Report concept gallery
| Overview | Loan performance | Transactions |
|---|---|---|
| ![Overview](screenshots/dashboard-overview.svg) | ![Loans](screenshots/loan-performance.svg) | ![Transactions](screenshots/customer-transactions.svg) |
<sub>Conceptual SVG previews, not Power BI screenshot exports.</sub>

## Deliverables
[Power BI dashboard](Banking_Sector_Analytics_Dashboard.pbix) · [Source CSV](Banking_Data.csv) · [Insight presentation](Banking_Sector_Analytics_Insight_Summary_FINAL.pptx) · [Project PDF](Day4_Banking_Sector_Analysis.pdf)

## Management interpretation
The dataset spans 2023-09-24 to 2025-09-09. Credit/debit totals are dataset indicators, not independently verified cash-flow statements. Review missing loan statuses before decisions.