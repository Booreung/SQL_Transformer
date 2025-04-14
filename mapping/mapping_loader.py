"""
    매핑 조건(엑셀파일) 읽어오기 (테이블+컬럼)
"""

import openpyxl
from collections import defaultdict


def load_mapping_excel(excel_path : str):
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb.active

    table_map = {}
    column_map = defaultdict(dict)

    for row in sheet.iter_rows(min_row=2, values_only=True):
        asis_table, tobe_table, asis_col, tobe_col = row

        if asis_table and tobe_table:
            table_map[asis_table.strip()] = tobe_table.strip()

        if asis_col and tobe_col:
            column_map[asis_table.strip()][asis_col.strip()] = tobe_col.strip()

    return table_map, column_map


## 테스트
if __name__ == "__main__" :
    table_map, column_map = load_mapping_excel(r"mapping\sql_mapping.xlsx")

    print("### [테이블 매핑]")
    print(table_map)

    print("\n### [컬럼 매핑]")
    from pprint import pprint
    pprint(column_map)
