# Day 02 — Household Energy Workbook Validation

## Purpose

Use this checklist to independently verify the three average-consumption figures currently quoted in the project README. The workbook is the source of truth. Do not publish the figures as verified until they match a fresh calculation from the workbook.

## Figures to check

| Grouping | Group currently reported | Average currently reported |
|---|---|---:|
| Appliance count | 7 appliances | 339.05 kWh |
| Family size | 3 family members | 330.63 kWh |
| Income level | Middle-income households | 308.05 kWh |

These are comparison targets from the existing project documentation, not independently confirmed results.

## Validation procedure in Excel

1. Open the workbook: Day-02-Household_Energy_Analysis.xlsx.
2. Identify the source-data sheet and the exact electricity-consumption field. Confirm that its unit is kWh.
3. Check the source table for blank consumption values, text values, duplicate records, and invalid or negative consumption values. Record how each issue is handled; do not silently delete rows.
4. For each grouping below, create a PivotTable from the source table:
   - Put Appliance Count in Rows and the consumption field in Values.
   - Set the Values calculation to Average, not Sum or Count.
   - Repeat with Family Size in Rows.
   - Repeat with Income Level in Rows.
5. Confirm that each PivotTable uses the same eligible source records and the same consumption field.
6. Read the average for the target group and compare it with the table above. Use two decimal places for comparison.
7. Independently verify at least one group by filtering the source rows to that group and calculating the arithmetic mean of the consumption values.
8. Refresh the PivotTables and repeat the comparison after the source-data checks.
9. If any value differs, update the README and project PDF only after identifying the reason (different filters, missing values, duplicate handling, grouping labels, or calculation method).

## Formula cross-check

For a selected group, filter the source table to the group's records and calculate:

Average consumption = sum of valid consumption values / count of valid consumption values

In Excel, use AVERAGE on the filtered numeric consumption values, or use a PivotTable with the Values field summarised by Average. Do not average pre-calculated group averages unless the groups have equal record counts.

## Evidence to retain

Save screenshots or a separate audit note showing:

- The source-data column names and row count.
- Any duplicate, blank, or invalid-value handling.
- Each of the three PivotTables with the Average aggregation visible.
- The independent formula cross-check.
- The final verified figures and date of verification.

## Reporting rules

- State the number of records used for each average.
- State the unit (kWh).
- Explain exclusions or missing-value treatment.
- Describe the results as sample-level comparisons; do not imply that household size, appliance count, or income causes consumption differences.
- If the workbook does not support a quoted figure, correct the README instead of forcing the data to match it.

## Current verification status

**Pending:** the workbook has not yet been opened and recalculated in Excel as part of this review. The values in the README remain labelled as figures from existing project documentation until this validation is completed.
