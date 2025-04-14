"""
    변환된 SQL을 엑셀과 JSON으로 저장해줌
"""

import openpyxl
import json
import os
from openpyxl.styles import Font, Alignment


def save_as_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"### 저장 완료 -> {path}")


def save_as_excel(data,path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "SQL 변환 결과"

    headers = ["SQL_ID", "SQL_TYPE", "주석", "AS-IS 쿼리", "TO-BE 쿼리"]

    ws.append(headers)

    for col in ws.columns:
        for cell in col:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

    for item in data:
        ws.append([
            item.get("sql_id", "-"),
            item.get("sql_type", "-"),
            item.get("comment", "-"),
            item.get("original", "-"),
            item.get("converted", "-"),
        ])

    os.makedirs(os.path.dirname(path), exist_ok=True)
    wb.save(path)
    print(f"### Excle 저장 완료 -> {path}")