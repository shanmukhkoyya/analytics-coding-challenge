# Banking Sector Analytics
### Management insight brief | Day 04 | Power BI and DAX

## Executive view

The supplied sample contains 250 transaction records and 92 unique customers, dated from 24 September 2023 to 9 September 2025. The analysis reviews recorded balances, credit and debit activity, and loan-status information.

## Financial activity snapshot

| Indicator | Project result |
|---|---:|
| Credit transaction amount | 1,161,613.89 |
| Debit transaction amount | 1,282,489.51 |
| Net transaction movement | -120,875.62 |
| Average recorded balance | 52,646.45 |
| Records with balance below 5,000 | 10 |

## Loan-status view

| Indicator | Project result |
|---|---:|
| Loan records | 70 |
| Active | 25 |
| Default | 26 |
| Closed | 19 |
| Default rate | 37.14% |

The remaining 180 of the 250 transaction rows have blank loan-status values and are not treated as loan records in the default-rate denominator.

## Questions for a reviewer

- How are credits and debits distributed over time?
- Which customers have higher transaction activity?
- How is the net transaction movement calculated?
- What share of the recorded loan rows has a Default status?
- Which records fall below the project-defined 5,000 balance threshold?

## Dashboard content

The Power BI report is organised into three views:

**01 — Banking Overview**  
Customer and transaction KPIs, average balance, demographic breakdowns, monthly movement and low-balance highlighting.

**02 — Loan and Customer Performance**  
Loan-status distribution, default rate, a hypothetical interest-rate What-If parameter and customer rankings.

**03 — Customer Transaction Details**  
Customer-level transaction history, dates, types, amounts and net transaction impact.

## Files for review

- [Power BI report](./Banking_Sector_Analytics_Dashboard.pbix)
- [Source CSV](./Banking_Data.csv)
- [Analysis PDF](./Day4_Banking_Sector_Analysis.pdf)
- [Insight presentation](./Banking_Sector_Analytics_Insight_Summary_FINAL.pptx)

## Visual layout references

These SVG files are static layout previews, not screenshots exported from Power BI Desktop:

- [Banking overview](./screenshots/dashboard-overview.svg)
- [Loan and customer performance](./screenshots/loan-performance.svg)
- [Customer transactions](./screenshots/customer-transactions.svg)

## Interpretation cautions

Credit and debit amounts are used as deposit and withdrawal indicators in this exercise; they are not independently verified bank cash-flow statements. The 37.14% default rate applies to the 70 rows with loan statuses, not all 250 transaction rows. The sample does not explain the causes of defaults or represent an entire bank.

## Open in Power BI

Open the PBIX in Power BI Desktop, review the data model and measures, check the filters and confirm the loan-default denominator against the underlying data. Use the PDF and PowerPoint for supporting documentation.

---

**Day 04 — Banking Sector Analytics**  
Shanmukh Koyya · [GitHub](https://github.com/shanmukhkoyya) · [LinkedIn](https://www.linkedin.com/in/shanmukh-koyya/)
