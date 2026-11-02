# Household Energy Consumption — Excel Workbook Guide

**Day 02 / Excel analysis / PivotTables / PivotCharts**

## What this workbook investigates

The project compares household electricity consumption by family size, appliance count and income level, then reviews the month-by-month pattern.

## Workbook map

| Worksheet | Purpose |
|---|---|
| Raw_Data | 250 household records |
| Data_Check | Data quality checks |
| Analysis | Summary calculations |
| energy consumption patterns | Monthly consumption summary |
| types of households consume the… | Group comparisons |
| energy-saving measures | Suggested actions |
| Household Energy Consumption Da… | Dashboard-style summary |

## Saved PivotTable observations

The workbook's saved summaries report the following group averages:

| Comparison | Highest group | Average usage |
|---|---|---:|
| Appliance count | 7 appliances | 339.05 kWh |
| Family size | 3 members | 330.63 kWh |
| Income level | Middle income | 308.05 kWh |

The monthly PivotTable reports February at 349.17 kWh (highest), August at 254.30 kWh (lowest), and an overall average of 301.34 kWh.

<sub>These figures have been matched to the saved PivotTable summaries. They have not been independently recalculated from every raw record.</sub>

## Open the deliverables

- [Excel workbook](./Day-02-Household_Energy_Analysis.xlsx)
- [Results verification](./RESULTS_VERIFICATION.md)
- [Workbook validation guide](./WORKBOOK_VALIDATION_GUIDE.md)
- [Python verification helper](./verify_workbook.py)
- [Project PDF](./day02.pdf)

## How to explore the workbook

Start with Raw_Data and Data_Check. Then inspect the Analysis sheet, PivotTables and PivotCharts. Compare family-size, appliance-count, income-level and monthly results.

The optional Python helper can inspect the workbook and calculate grouped averages. It does not modify the workbook; check its detected source sheet and columns before relying on its output.

## Data-quality and calculation note

The inspection found 250 source records. The Data_Check sheet reports zero duplicate records and data types marked Correct. However, some formula-driven cells had blank cached values during automated inspection. The workbook therefore still requires a full recalculation and refresh in Excel before formula-based dashboard KPIs can be treated as final.

## Interpretation

The reported averages describe this sample only. They do not prove that appliance count, income or family size causes electricity usage to change. Other factors—such as location, season, appliance efficiency and occupancy—could affect consumption.

## Suggested energy actions

- Choose efficient appliances when replacing older equipment.
- Use LED lighting and switch off unused devices.
- Reduce unnecessary standby usage.
- Maintain appliances and monitor monthly consumption.

---

**Project author:** Shanmukh Koyya · [GitHub](https://github.com/shanmukhkoyya) · [LinkedIn](https://www.linkedin.com/in/shanmukh-koyya/)
