# Power BI Evidence Capture Guide

This guide explains how to replace conceptual layout previews with genuine report evidence. A PBIX file must be opened in Power BI Desktop before its real report pages, measures, and visuals can be captured.

## Before capturing

1. Download or clone the repository.
2. Open the relevant PBIX file in Power BI Desktop.
3. Check whether the report opens without errors.
4. Confirm data-source paths. Refresh only when the required source data is available and the refresh is expected to succeed.
5. Review each report page and confirm the displayed figures before taking screenshots.
6. Use Windows Snipping Tool (Win + Shift + S) or Power BI's export options to save genuine captures as PNG files.

Keep the complete report canvas visible. Do not redraw visuals, fabricate values, or label a conceptual SVG as a screenshot.

## Day 03 — Quality Control Defect Analysis

PBIX: Day-03-Quality-Control-Defect-Analysis/Quality_Control_Defect_Analysis.pbix

Save verified captures inside Day-03-Quality-Control-Defect-Analysis/screenshots/:

| Suggested filename | Capture |
|---|---|
| report-overview.png | Main report page with the visible KPI cards and overall defect analysis |
| defect-analysis.png | Page or visual that breaks down defects by product/category |
| batch-trend-analysis.png | Page or visual showing production batch or time-based analysis, if present |

Only capture a visual when it exists in the PBIX. The current defect-analysis-layout-preview.svg is a conceptual design companion with placeholder shapes, not real report data.

## Day 04 — Banking Sector Analytics

PBIX: Day-04-Banking-Sector-Analytics/Banking_Sector_Analytics_Dashboard.pbix

Save verified captures inside Day-04-Banking-Sector-Analytics/screenshots/:

| Suggested filename | Capture |
|---|---|
| banking-overview.png | Banking Overview report page |
| loan-customer-performance.png | Loan & Customer Performance report page |
| customer-transactions.png | Customer Transaction Details report page |

The existing SVG files are static dashboard layout previews. Keep them labelled as previews until replaced or supplemented with actual Power BI Desktop captures.

## Quality checks for every screenshot

- The screenshot is from the actual open PBIX report.
- Page title, chart titles, labels, and units are readable.
- Slicers and filters show the intended selection.
- KPI values match the report after refresh/validation.
- No error messages, blank visuals, or unintended editing selections obscure the report.
- The README labels the file as a Power BI screenshot only after it has been captured from Power BI Desktop.

## Current status

The repository contains the PBIX files and conceptual SVG previews. Actual Power BI screenshot exports are still pending. This guide does not claim those exports have been completed.
