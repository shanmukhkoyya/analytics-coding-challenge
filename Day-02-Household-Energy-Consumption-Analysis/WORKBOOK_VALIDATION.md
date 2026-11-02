# Workbook Validation — Household Energy Consumption

## Validation status

**Pending independent recalculation in Microsoft Excel.**

The workbook is present in this repository. The three averages currently shown in the README are transcribed from the existing project documentation and have not been independently recalculated in this review. Do not describe them as verified until the checks below are completed.

## Figures awaiting verification

| Analysis | Previously reported result | Verification status |
|---|---:|---|
| Average consumption — 7 appliances | 339.05 kWh | Pending |
| Average consumption — family size 3 | 330.63 kWh | Pending |
| Average consumption — middle-income households | 308.05 kWh | Pending |

## Excel verification steps

1. Open `Day-02-Household_Energy_Analysis.xlsx` in Microsoft Excel.
2. Identify the source-data sheet and confirm the actual table name and row count.
3. Check for blank values, duplicate rows, invalid numeric values, and inconsistent category labels.
4. Confirm the electricity-consumption column is numeric and measured in kWh.
5. Inspect the PivotTable or formula used for each reported group average.
6. Confirm the filter/group condition is exact (for example, appliance count equals 7, not a text match or a range).
7. Recalculate each average directly from the underlying rows. Use the same missing-value handling as the workbook and document that choice.
8. Compare the independent result with the reported value, allowing only a clearly stated rounding difference.
9. Check that PivotTables and charts update correctly after refresh.
10. Capture genuine screenshots of the source data, PivotTables, and final dashboard.

## Independent calculation reference

For a group average:

`Average consumption = sum of valid kWh values in the group / count of valid kWh values in the group`

For each group, record:
- Exact filter condition.
- Number of included records.
- Number of blank or excluded kWh values.
- Sum of included kWh values.
- Independently calculated average.
- Difference from the README figure.

## Evidence to add after validation

Recommended files:

- `screenshots/source-data.png`
- `screenshots/appliance-pivot.png`
- `screenshots/family-size-pivot.png`
- `screenshots/income-pivot.png`
- `screenshots/excel-dashboard.png`

These must be actual screenshots from Excel. Do not create placeholder images or represent a static design as an Excel screenshot.

## Acceptance criteria

The figures can be marked verified only when the independent calculations reconcile with the workbook's PivotTables or formulas, the calculation population and missing-value treatment are documented, and the screenshots show the actual workbook outputs.
