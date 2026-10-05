# Day 04 — Banking Sector Analytics

## Project Overview

A Power BI analysis of customer behavior, banking transactions, account balances, and loan performance.

The project transforms the supplied banking dataset into an interactive management dashboard using Power Query, DAX, data modeling, drill-through analysis, conditional formatting, a What-If parameter, and customer ranking.

## Business Questions

- What is the overall customer and transaction position?
- Are deposits keeping pace with withdrawals?
- What is the current loan default exposure?
- Which customers show the highest transaction activity?
- Which records require low-balance attention?
- What limitations exist in the supplied transaction data?

## Dataset

**File:** `Banking_Data.csv`

The source contains customer details, account type, balances, transaction dates, transaction types, transaction amounts, and loan status. The assignment specifies Power BI cleaning, modeling and visualization for these fields. 

## Data Preparation

The Power Query workflow includes:

- Duplicate removal and missing-value handling
- Net Transaction Impact: Credit = positive, Debit = negative
- Age Groups: 18–30, 31–50, 51+
- Standardized account codes: SAV, CUR, FD, LN

## Data Model

The model includes:

- `Banking_Data` — transaction fact table
- `Customer` — distinct customer table
- `Calendar` — dedicated transaction-date table

A Year → Quarter → Month hierarchy is used for transaction analysis.

## Key Measures

- Total Deposits
- Total Withdrawals
- Net Balance Growth
- Average Account Balance
- Loan Default Rate %
- Monthly Transaction Volume
- Customer Profitability Score
- Total Transactions
- Customer Transaction Rank
- Interest Rate Revenue Scenario

## Dashboard Pages

### 1. Banking Overview

- Total Customers KPI
- Total Deposits
- Total Withdrawals
- Net Balance Growth
- Average Account Balance
- Customers by Age Group & Gender
- Monthly Transaction Trend
- Day-of-Week transaction analysis
- Low-balance highlighting

### 2. Loan & Customer Performance

- Loan Status Distribution
- Loan Default Rate KPI
- Interest Rate What-If scenario
- Top customer transaction activity
- Customer ranking with Top 3 highlighting

### 3. Customer Transaction Details

A drill-through page for customer-level transaction history, including transaction date, type, amount, net impact, and account type.

## Key Findings

| Metric | Result |
|---|---:|
| Total Customers | 92 |
| Total Deposits | 1,161,614 |
| Total Withdrawals | 1,282,490 |
| Net Balance Growth | -120,876 |
| Average Account Balance | 52,646 |
| Loan Records | 70 |
| Default Loans | 26 |
| Loan Default Rate | 37.14% |
| Low-balance Records | 10 |

### Business Interpretation

**Negative transaction movement:** Withdrawals exceed deposits by 120,876, resulting in negative net balance growth.

**Loan risk:** The 37.14% default rate is above the dashboard's red threshold of 15%, making loan risk a major management concern.

**Low-balance monitoring:** 10 records fall below the 5,000 balance threshold used in the dashboard.

**Customer concentration:** The Top 10 customer view helps identify customers contributing the highest transaction activity.

## Data Limitation

The supplied `Transaction_Date` contains dates only and does not include transaction time. Therefore, an Hour-of-Day heat map cannot be calculated reliably without inventing timestamps.

## Power BI Features Demonstrated

- Power Query transformation
- DAX measures
- Data modeling
- Conditional formatting
- KPI traffic-light logic
- Drill-through
- What-If parameter
- Customer ranking
- Date hierarchy
- Interactive dashboard reporting

## Deliverables

- `Banking_Sector_Analytics_Dashboard.pbix`
- `Banking_Data.csv`
- `Day4_Banking_Sector_Analysis.pdf`
- `Banking_Sector_Analytics_Insight_Summary_FINAL.pptx`

## Project Files

| File | Purpose |
|---|---|
| [Power BI Dashboard](./Banking_Sector_Analytics_Dashboard.pbix) | Interactive dashboard |
| [Banking Dataset](./Banking_Data.csv) | Source data |
| [Assignment Brief](./Day4_Banking_Sector_Analysis.pdf) | Challenge requirements |
| [Insight Summary](./Banking_Sector_Analytics_Insight_Summary_FINAL.pptx) | 3-slide management summary |

---
**Day 04 of the Analytics Coding Challenge — Power BI / DAX**
