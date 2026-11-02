"""
Independent audit helper for the Day 02 Household Energy workbook.

Usage:
    python verify_workbook.py "Day-02-Household_Energy_Analysis.xlsx"

Requires:
    pip install pandas openpyxl

The script does not modify the source workbook. It scans worksheets, looks for
likely energy-consumption and household-group columns, and prints the values
needed to verify the averages documented in the project README.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd


ALIASES = {
    "consumption": [
        "energy consumption", "electricity consumption", "consumption",
        "energy used", "electricity used", "kwh", "units consumed",
    ],
    "appliance_count": [
        "appliance count", "number of appliances", "no of appliances",
        "total appliances", "appliances",
    ],
    "family_size": [
        "family size", "family members", "number of family members",
        "no of family members", "household size", "members",
    ],
    "income_level": [
        "income level", "income group", "monthly income", "income category",
    ],
}


def normalise(value: object) -> str:
    text = str(value).strip().lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def find_column(columns, aliases):
    normalised = {column: normalise(column) for column in columns}
    for alias in aliases:
        target = normalise(alias)
        for column, candidate in normalised.items():
            if candidate == target:
                return column
    for alias in aliases:
        target = normalise(alias)
        for column, candidate in normalised.items():
            if target and (target in candidate or candidate in target):
                return column
    return None


def load_sheet(path: Path, sheet_name: str):
    preview = pd.read_excel(path, sheet_name=sheet_name, header=None, nrows=20)
    best = None
    for header_row in range(min(15, len(preview))):
        headers = preview.iloc[header_row].tolist()
        cleaned = [
            str(value).strip() if pd.notna(value) else f"Unnamed_{i}"
            for i, value in enumerate(headers)
        ]
        if not any(find_column(cleaned, aliases) for aliases in ALIASES.values()):
            continue
        frame = pd.read_excel(path, sheet_name=sheet_name, header=header_row)
        frame = frame.dropna(how="all")
        score = sum(
            find_column(frame.columns, aliases) is not None
            for aliases in ALIASES.values()
        )
        if best is None or score > best[0]:
            best = (score, header_row, frame)
    return best


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path, help="Path to the Excel workbook")
    parser.add_argument(
        "--output", type=Path, default=Path("day02_workbook_audit.json"),
        help="JSON report output path (default: day02_workbook_audit.json)",
    )
    args = parser.parse_args()

    if not args.workbook.is_file():
        raise SystemExit(f"Workbook not found: {args.workbook}")

    excel = pd.ExcelFile(args.workbook)
    report = {
        "workbook": args.workbook.name,
        "sheets": [],
        "verification_note": (
            "Compare these independently calculated group means with the "
            "README figures. Confirm the correct source sheet, units, filters, "
            "and treatment of blanks before accepting a match."
        ),
    }

    for sheet_name in excel.sheet_names:
        selected = load_sheet(args.workbook, sheet_name)
        if selected is None:
            report["sheets"].append({
                "sheet": sheet_name,
                "status": "No likely analysis header detected in first 15 rows",
            })
            continue

        _, header_row, frame = selected
        columns = {
            key: find_column(frame.columns, aliases)
            for key, aliases in ALIASES.items()
        }
        sheet_result = {
            "sheet": sheet_name,
            "header_row_excel_number": header_row + 1,
            "rows": int(len(frame)),
            "columns_detected": {
                key: str(value) if value is not None else None
                for key, value in columns.items()
            },
            "null_counts": {},
            "duplicate_rows": int(frame.duplicated().sum()),
            "group_averages": {},
        }

        for key, column in columns.items():
            if column is not None:
                sheet_result["null_counts"][str(column)] = int(frame[column].isna().sum())

        consumption = columns["consumption"]
        if consumption is not None:
            numeric = pd.to_numeric(
                frame[consumption].astype(str).str.replace(",", "", regex=False),
                errors="coerce",
            )
            sheet_result["consumption_summary"] = {
                "non_null_numeric_values": int(numeric.notna().sum()),
                "missing_or_non_numeric_values": int(numeric.isna().sum()),
                "overall_average": (
                    round(float(numeric.mean()), 4) if numeric.notna().any() else None
                ),
                "minimum": (
                    round(float(numeric.min()), 4) if numeric.notna().any() else None
                ),
                "maximum": (
                    round(float(numeric.max()), 4) if numeric.notna().any() else None
                ),
            }

            for group_key in ("appliance_count", "family_size", "income_level"):
                group_column = columns[group_key]
                if group_column is None:
                    continue
                temp = pd.DataFrame({
                    "group": frame[group_column],
                    "consumption": numeric,
                }).dropna(subset=["group", "consumption"])
                grouped = (
                    temp.groupby("group", dropna=False)["consumption"]
                    .agg(["mean", "count"])
                    .reset_index()
                )
                sheet_result["group_averages"][group_key] = [
                    {
                        "group": str(row["group"]),
                        "average_consumption": round(float(row["mean"]), 4),
                        "records": int(row["count"]),
                    }
                    for _, row in grouped.iterrows()
                ]

        report["sheets"].append(sheet_result)

    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nAudit report saved to: {args.output}")


if __name__ == "__main__":
    main()
