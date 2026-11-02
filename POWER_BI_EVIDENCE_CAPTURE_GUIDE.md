# Power BI Evidence Capture Guide

This guide covers the Power BI repositories in the portfolio that still need genuine report screenshots. A PBIX file must be opened in Power BI Desktop before its real report pages, measures, and visuals can be captured.

## Before capturing

1. Download or clone the relevant repository.
2. Open its PBIX file in Power BI Desktop.
3. Confirm the report opens without errors.
4. Check data-source paths. Refresh only when the required source data is available and the refresh is expected to succeed.
5. Review each report page and confirm displayed figures before taking screenshots.
6. Use Windows Snipping Tool (Win + Shift + S) or Power BI export options to save genuine captures as PNG files.

Keep the complete report canvas visible. Do not redraw visuals, fabricate values, or label a conceptual SVG as a screenshot.

## 1. Data Transformation & Data Modeling

Repository: [Data-Transformation-Data-Modeling-using-Power-BI](https://github.com/shanmukhkoyya/Data-Transformation-Data-Modeling-using-Power-BI)

PBIX: `Data Transformation & Data Modeling using Power BI.pbix`

Save genuine captures in the existing `images/` folder:

| Suggested filename | Capture |
|---|---|
| dashboard-overview.png | Main Power BI report page and headline metrics |
| data-model.png | Actual Model view with tables and relationships |
| analysis-detail.png | A report page with its real visuals and filters |

The existing `Business_Dashboard.svg` is a static layout preview, not a screenshot. The `data-model-architecture.svg` is a documentation diagram; it should not be described as a captured Power BI Model view.

## 2. Day 03 — Quality Control Defect Analysis

Repository: [analytics-coding-challenge / Day 03](https://github.com/shanmukhkoyya/analytics-coding-challenge/tree/main/Day-03-Quality-Control-Defect-Analysis)

PBIX: `Quality_Control_Defect_Analysis.pbix`

Save genuine captures in `Day-03-Quality-Control-Defect-Analysis/screenshots/`:

| Suggested filename | Capture |
|---|---|
| report-overview.png | Main report page with the visible KPI cards and overall defect analysis |
| defect-analysis.png | Actual breakdown by product/category, if present |
| batch-trend-analysis.png | Actual production-batch or time-based analysis, if present |

The current `defect-analysis-layout-preview.svg` is a conceptual design companion with placeholder shapes, not real report data.

## 3. Day 04 — Banking Sector Analytics

Repository: [analytics-coding-challenge / Day 04](https://github.com/shanmukhkoyya/analytics-coding-challenge/tree/main/Day-04-Banking-Sector-Analytics)

PBIX: `Banking_Sector_Analytics_Dashboard.pbix`

Save genuine captures in `Day-04-Banking-Sector-Analytics/screenshots/`:

| Suggested filename | Capture |
|---|---|
| banking-overview.png | Banking Overview report page |
| loan-customer-performance.png | Loan & Customer Performance report page |
| customer-transactions.png | Customer Transaction Details report page |

The existing SVG files are static dashboard layout previews. Keep them labelled as previews until actual Power BI Desktop captures are added.

## 4. Standalone DAX & Data Visualization Assignment

Repository: [PowerBI---DAX-Data-Visualization](https://github.com/shanmukhkoyya/PowerBI---DAX-Data-Visualization)

PBIX: `Power BI Assignment – DAX & Data Visualization.pbix`

Create a `screenshots/` folder and save verified captures:

| Suggested filename | Capture |
|---|---|
| report-overview.png | Main report page |
| data-model.png | Actual model view |
| dax-measures.png | Measure definitions or a genuine DAX measure view |
| analysis-page.png | A report page showing actual analysis |

The current `images/project-overview.svg` is a static overview graphic, not a screenshot of the report.

## Projects with existing screenshot evidence

The Employee Productivity & Work Pattern Analysis repository already contains four dashboard PNG screenshots. Check that those existing captures remain readable and correspond to the current PBIX before adding more.

## Quality checks for every screenshot

- The image is captured from the actual open PBIX report or Model view.
- Page title, chart titles, labels, and units are readable.
- Slicers and filters show the intended selection.
- KPI values match the report after refresh and validation.
- No error messages, blank visuals, or unintended editing selections obscure the report.
- The README labels the file as a Power BI screenshot only after it has been captured from Power BI Desktop.

## Current status

The repositories contain their PBIX files and some conceptual SVG previews. Actual exports for the projects in sections 1–4 are still pending. The guide does not claim those exports have been completed.
