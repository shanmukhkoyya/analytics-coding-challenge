# Day 02 — Household Energy Results Verification

## Verification outcome

**The three README headline results match the saved PivotTable summaries in the workbook.** This is a workbook PivotTable cross-check, not a separate raw-row recalculation.

The workbook inspection was run on 2 November 2026 using the repository's GitHub Actions workflow:
[Inspect household energy workbook — successful run](https://github.com/shanmukhkoyya/analytics-coding-challenge/actions/runs/41383932997).

## Results checked

The PivotTable results are stored in the worksheet named `types of households consume the`.

| Grouping | Highest group in PivotTable | PivotTable average | README value | Match |
|---|---|---:|---:|---|
| Appliance count | 7 appliances | 339.0476 kWh | 339.05 kWh | Yes |
| Family size | 3 family members | 330.6250 kWh | 330.63 kWh | Yes |
| Income level | Middle | 308.0476 kWh | 308.05 kWh | Yes |

The PivotTable summary also reports an overall average electricity usage of 301.34 kWh.

## Workbook structure and checks observed

The workbook contains seven worksheets:

- `Raw_Data`
- `Data_Check`
- `Analysis`
- `energy consumption patterns`
- `types of households consume the`
- `energy-saving measures`
- `Household Energy Consumption Da`

The `Raw_Data` sheet contains 250 records and eight columns. Relevant field names are:

- `Family_Size`
- `Electricity_Usage (kWh)`
- `Appliances_Count`
- `Income_Level`

The `Data_Check` sheet shows 250 total records, 0 duplicate records, and data types marked as Correct.

## Additional saved PivotTable observation

The `energy consumption patterns` worksheet reports:

- February: highest monthly average electricity usage at 349.1667 kWh.
- August: lowest monthly average electricity usage at 254.30 kWh.
- Overall monthly PivotTable average: 301.34 kWh.

## Important limitation — formula recalculation

The workbook inspection found formulas in the `Data_Check`, `Analysis`, and dashboard cells. However, when reading the workbook's saved cached values, the formula results were blank. The formula definitions are present, but their last calculated values were not available in the saved workbook cache inspected by the workflow.

Before treating the workbook dashboard KPIs as final:

1. Open the workbook in Microsoft Excel.
2. Set Calculation Options to Automatic.
3. Use Formulas → Calculate Now (or press Ctrl+Alt+F9).
4. Confirm the Quality Status formula returns PASS.
5. Confirm the Analysis KPI formulas and dashboard cards show numeric values.
6. Save the workbook and recheck the report.

The `Income_Level` field is formula-driven from `Monthly_Income`; confirm those formula cells are calculated and saved before refreshing the income-level PivotTable.

## What this verification does and does not establish

**Established:** each of the three headline averages and top-group labels matches the saved PivotTable summaries visible in the workbook.

**Not established:** an independent recalculation of all three averages directly from the 250 raw rows, a complete audit of every raw-data value, or successful recalculation of the workbook's formula-driven KPI/dashboard cells.

The README may describe the three numbers as checked against the workbook PivotTable summaries. It should not call the raw-data calculations or formula-driven dashboard KPIs independently validated until the follow-up steps above have been completed.
