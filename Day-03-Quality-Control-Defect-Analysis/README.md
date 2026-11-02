# Quality Control | Defect Analysis Report Blueprint

**Day 03 · Power BI · DAX · Manufacturing quality analytics**

## Reporting objective

Explore production-quality information through a report designed to help review overall defect rate, product-level defect counts, daily defect movement and production-batch records.

## Planned report components

| Report component | Intended question |
|---|---|
| Overall defect-rate KPI | What is the reported defect rate for the selected scope? |
| Top-five product chart | Which products have the highest defective-item counts? |
| Daily trend line | How does the defect rate change over time? |
| Batch detail table | Which batches, inspectors and production lines need review? |
| Date slicer | How does the view change over a selected period? |

## Layout concept

![Quality control report layout concept](screenshots/defect-analysis-layout-preview.svg)

> **Important evidence note:** This SVG is a static layout concept. Its chart shapes are placeholders and do not represent actual defect rates, product rankings or production-batch values. It is not a screenshot exported from Power BI Desktop. Open the PBIX to inspect the actual report and data.

## Deliverables

- Power BI report: Quality_Control_Defect_Analysis.pbix
- Assignment brief: Day3-Quality Control.pdf
- Layout concept: screenshots/defect-analysis-layout-preview.svg

## Review in Power BI

Open the PBIX in Power BI Desktop. Inspect the data model and DAX measures, verify how the defect rate is calculated, check the top-five ranking logic, and review the date filter context.

## Analysis questions

1. How is the defect-rate KPI defined?
2. Are defective items counted at the product, batch or transaction grain?
3. Does the top-five chart use the selected date range?
4. Are batch and inspector comparisons based on consistent denominators?
5. Do totals reconcile with the source data?

## Current reporting boundary

This README describes the intended analytical views. It does not publish numeric findings because no independently verified report results are documented here. The SVG preview must not be interpreted as a completed Power BI screenshot.

---

**Day 03 of the Data Analytics Coding Challenge**  
Shanmukh Koyya · [GitHub](https://github.com/shanmukhkoyya) · [LinkedIn](https://www.linkedin.com/in/shanmukh-koyya/)
