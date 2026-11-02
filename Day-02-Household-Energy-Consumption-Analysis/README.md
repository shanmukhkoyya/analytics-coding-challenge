# Household Energy Consumption Analysis | Excel

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:14243B,100:00C9D8&height=180&section=header&text=HOUSEHOLD%20ENERGY%20ANALYSIS&fontSize=30&fontColor=ffffff&fontAlignY=40&desc=EXCEL%20%7C%20PIVOT%20TABLES%20%7C%20DATA%20ANALYSIS&descAlignY=65" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" />
  <img src="https://img.shields.io/badge/PivotTables-0A7A48?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data_Analytics-00A6A6?style=for-the-badge" />
</p>

## 1. Project Overview

This project analyses household electricity consumption using Microsoft Excel. It explores how energy usage varies according to household characteristics such as family size, appliance count and income level.

The project demonstrates a basic data analysis workflow: reviewing raw data, checking data quality, summarising data with PivotTables, comparing groups, creating charts and communicating findings.

## 2. Business Problem

Understanding household electricity usage can help identify consumption patterns and support better energy-management decisions.

This analysis explores which household groups have higher average electricity consumption and what practical actions may help reduce unnecessary energy use.

## 3. Project Objectives

- Explore household electricity consumption.
- Compare average usage by family size.
- Analyse consumption by appliance count.
- Compare electricity usage across income groups.
- Present findings through Excel charts and dashboard reporting.
- Develop practical energy-saving recommendations.

## 4. Analysis Performed

| Analysis | Purpose |
|---|---|
| Consumption by Family Size | Compare average electricity use across household sizes |
| Consumption by Appliance Count | Understand usage across different appliance counts |
| Consumption by Income Level | Compare average usage among income groups |
| Monthly Consumption Pattern | Identify months with higher and lower average electricity usage |

## 5. Key Findings

The workbook's saved PivotTable summaries were checked on 2 November 2026. The following group averages and top-group labels match the workbook's `types of households consume the` worksheet.

| Analysis Category | Highest Reported Group | Average Consumption |
|---|---|---:|
| Appliance Count | 7 appliances | 339.05 kWh |
| Family Size | 3 family members | 330.63 kWh |
| Income Level | Middle-income households | 308.05 kWh |

*These figures match the saved PivotTable summaries. They have not been independently recalculated from the 250 raw records.*

### Monthly consumption

The workbook's saved monthly PivotTable reports:

| Month | Average Electricity Usage |
|---|---:|
| February | 349.17 kWh — highest |
| August | 254.30 kWh — lowest |
| Overall | 301.34 kWh |

## 6. Business Insights

- The group with 7 appliances has the highest reported average electricity usage among appliance-count groups.
- Households with 3 family members have the highest reported average usage among family-size groups.
- Middle-income households have the highest reported average usage among the income groups.
- February has the highest saved monthly average, while August has the lowest.
- These are descriptive sample-level comparisons. They do not establish that appliance count, family size, or income causes higher electricity consumption.

## 7. Recommendations

- Prefer energy-efficient appliances when replacing older equipment.
- Switch off lights and appliances when they are not required.
- Use LED lighting.
- Maintain appliances regularly.
- Monitor monthly electricity consumption.
- Avoid unnecessary standby power usage.
- Review high-consumption periods and use energy-intensive appliances efficiently.

## 8. Excel Skills Practised

- Data summarisation
- Data quality checks
- PivotTables
- PivotCharts
- Group-wise comparison
- Average calculations
- Monthly trend analysis
- Dashboard-style reporting
- Business insight communication

## 9. Tools Used

| Tool | Purpose |
|---|---|
| Microsoft Excel | Data analysis and reporting |
| PivotTables | Data summarisation |
| PivotCharts | Visual analysis |
| Python validation helper | Inspect workbook sheets and calculate grouped averages |
| GitHub | Project version control and documentation |

## 10. Validation and Data Quality

The workbook inspection found 250 source records in the `Raw_Data` sheet. The `Data_Check` worksheet reports 0 duplicate records and marks the data types as Correct.

The [Results Verification](./RESULTS_VERIFICATION.md) note documents the PivotTable cross-check and an important formula-recalculation limitation: some formula-driven cells had blank cached results when inspected by the workflow. Open the workbook in Excel, recalculate it, confirm the Quality Status shows PASS, refresh the PivotTables, and save the workbook before treating dashboard KPI cards as final.

The [Workbook Validation Guide](./WORKBOOK_VALIDATION_GUIDE.md) explains the complete review process. The [Python verification helper](./verify_workbook.py) can be run locally to inspect the workbook and calculate group averages from detected source columns.

## 11. Project Files

| File | Description |
|---|---|
| [Excel Analysis Workbook](./Day-02-Household_Energy_Analysis.xlsx) | Household energy data, PivotTables, charts and dashboard |
| [Results Verification](./RESULTS_VERIFICATION.md) | Workbook PivotTable cross-check, findings and limitations |
| [Workbook Validation Guide](./WORKBOOK_VALIDATION_GUIDE.md) | Steps to recalculate and validate the workbook |
| [Python Verification Helper](./verify_workbook.py) | Optional script to inspect sheets and calculate grouped averages |
| [Project PDF](./day02.pdf) | Challenge/project reference document |
| [README](./README.md) | Project documentation |

## 12. How to Explore the Project

1. Download or clone the repository.
2. Open `Day-02-Household_Energy_Analysis.xlsx` in Microsoft Excel.
3. Review the `Raw_Data`, `Data_Check`, and `Analysis` sheets.
4. Explore the PivotTables and PivotCharts.
5. Recalculate the workbook and refresh the PivotTables.
6. Compare consumption across family size, appliance count, income level and month.

To run the optional Python verification helper, install its dependencies and execute:

```bash
python -m pip install pandas openpyxl
python verify_workbook.py "Day-02-Household_Energy_Analysis.xlsx"
```

The helper does not modify the workbook. Check its detected columns and source sheet before using its output as final evidence.

## 13. Limitations

- Findings are based on the dataset included in the workbook.
- Group averages describe the available sample and may not represent all households.
- The three headline values have been matched to saved PivotTable summaries but have not been independently recalculated from every raw record in this review.
- Formula-driven KPI cells require recalculation in Excel; see the Results Verification note.
- The analysis identifies patterns but does not prove causal relationships.
- Additional information such as location, season, appliance efficiency and occupancy hours could improve the analysis.

## 14. Project Structure

```text
Day-02-Household-Energy-Consumption-Analysis/
│
├── Day-02-Household_Energy_Analysis.xlsx
├── day02.pdf
├── README.md
├── RESULTS_VERIFICATION.md
├── WORKBOOK_VALIDATION_GUIDE.md
└── verify_workbook.py
```

## 15. Author

**Shanmukh Koyya**

- **GitHub:** [github.com/shanmukhkoyya](https://github.com/shanmukhkoyya)
- **LinkedIn:** [linkedin.com/in/shanmukh-koyya](https://www.linkedin.com/in/shanmukh-koyya/)
- **Email:** [shanmukhkoyya1234@gmail.com](mailto:shanmukhkoyya1234@gmail.com)

**Project:** Day 02 — Household Energy Consumption Analysis  
**Focus:** Excel | PivotTables | PivotCharts | Data Analysis
