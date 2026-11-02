from pathlib import Path
from openpyxl import load_workbook
import json

workbook_path = Path("Day-02-Household-Energy-Consumption-Analysis/Day-02-Household_Energy_Analysis.xlsx")
if not workbook_path.exists():
    raise FileNotFoundError(workbook_path)

for data_only in (False, True):
    wb = load_workbook(workbook_path, read_only=True, data_only=data_only)
    print("\n=== WORKBOOK VALUES: data_only={} ===".format(data_only))
    print("Sheets:", wb.sheetnames)
    for ws in wb.worksheets:
        print("\n--- SHEET:", ws.title, "rows:", ws.max_row, "columns:", ws.max_column, "---")
        shown = 0
        for row in ws.iter_rows(values_only=True):
            values = list(row)
            if any(v is not None for v in values):
                print(json.dumps(values, default=str, ensure_ascii=False))
                shown += 1
            if shown >= 30:
                print("[preview limited to first 30 non-empty rows]")
                break
    wb.close()
