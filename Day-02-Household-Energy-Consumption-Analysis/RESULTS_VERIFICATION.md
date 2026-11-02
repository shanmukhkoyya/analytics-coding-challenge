# Day 02 — Household Energy Results Verification

## Verification status

**Not independently verified yet.** The README currently reports three group averages from the existing project documentation. Those values must be checked against the Excel workbook before being presented as validated findings.

Reported values to verify:

| Grouping | Reported highest group | Reported average |
|---|---|---:|
| Appliance count | 7 appliances | 339.05 kWh |
| Family size | 3 family members | 330.63 kWh |
| Income level | Middle-income households | 308.05 kWh |

Do not change these values or describe them as confirmed until the workbook calculations have been checked.

## Workbook review procedure

Open `Day-02-Household_Energy_Analysis.xlsx` in Microsoft Excel.

### 1. Inspect workbook structure

- List all worksheet names.
- Identify the raw-data sheet and the analysis/dashboard sheets.
- Identify the exact columns for electricity consumption, appliance count, family size, and income level.
- Confirm the electricity-consumption column is numeric and consistently measured in kWh.
- Check whether blank, text, error, or duplicate records affect the averages.

### 2. Validate the three reported averages

For each grouping:

1. Filter the source data to the group named in the table above.
2. Calculate the average consumption using the numeric source values.
3. Compare the result with the corresponding PivotTable or PivotChart.
4. Confirm the group has the highest average among all groups in that dimension.
5. Record the number of records contributing to the average.

Use Excel's PivotTable Average aggregation or an equivalent formula such as AVERAGEIFS, referencing the actual workbook column names and ranges. Do not average already-aggregated group averages unless group sizes are equal.

### 3. Check data quality

Record:

- Total source rows.
- Duplicate rows and how they were handled.
- Missing values in each analysis field.
- Non-numeric or invalid consumption values.
- Minimum and maximum valid consumption.
- Number of records included and excluded from each group average.

Do not silently remove records. Document the reason for every exclusion.

### 4. Validate dashboard consistency

- Refresh all PivotTables and PivotCharts.
- Confirm dashboard values match the underlying PivotTables.
- Check slicers and filters for unintended restrictions.
- Confirm displayed units are kWh.
- Check that the highest group is selected by the average, not by total consumption or record count.

## Results log

Complete this table after checking the workbook:

| Check | Verified result |
|---|---|
| Workbook sheet names | Pending |
| Source row count | Pending |
| Duplicate handling | Pending |
| Missing-value handling | Pending |
| Average for 7 appliances | Pending |
| Average for 3 family members | Pending |
| Average for middle-income households | Pending |
| Highest group in each dimension | Pending |
| PivotTable/dashboard reconciliation | Pending |

## Completion rule

Only replace the README's unverified-results note after all three averages, group rankings, record counts, and dashboard values have been independently checked. If any result differs, update the README and dashboard documentation to match the workbook's verified calculations.
