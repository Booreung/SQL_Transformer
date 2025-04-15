"""
    SQL 변환기 : as-is -> to-be 매핑 정보가 담긴 엑셀을 바탕으로 as-is 쿼리문을 to-be에 맞게 변환해주는 것이 목표
"""

import re
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def convert_sql(query : str, table_map : dict, column_map : dict) -> str:
    converted_query = query

    # 테이블 이름 변환
    for asis_table, tobe_table in reversed(list(table_map.items())):
        # 공백, 줄바꿈, 탭 기준으로 테이블명이 등장하는 위치 고려
        converted_query = re.sub(rf"\b{re.escape(asis_table)}\b", tobe_table, converted_query)

    # 컬럼 이름 변환
    for asis_table, colunms in reversed(list(column_map.items())):
        # "." 붙은 경우만 (ex: A.user_id → A.id)
        for asis_col, tobe_col in colunms.items():
            converted_query = re.sub(rf"\b{re.escape(asis_col)}\b(?!\s*\()", tobe_col, converted_query)

            converted_query = re.sub(rf"\b(\w+)\.{re.escape(asis_col)}\b", rf"\1.{tobe_col}",converted_query)

    # 중복 AS 제거
    converted_query = re.sub(r'\bAS\s+\w+\s+AS\s+(\w+)', r'AS \1', converted_query, flags=re.IGNORECASE)

    converted_query = re.sub(r'\bAS\s+(\w+)\s*,\s*AS\s+(\w+)', r'AS \2', converted_query, flags=re.IGNORECASE)

    return converted_query


## 테스트
# if __name__ == "__main__":
#     from mapping.mapping_loader import load_mapping_excel
#     from parser.sql_extractor import extract_sql_from_xml

#     table_map, column_map = load_mapping_excel(r"sample\sql_mapping.xlsx")
#     sql_items = extract_sql_from_xml(r"sample\sampleSQL.xml")

#     for sql in sql_items:
#         print("\n ### 원본 SQL : ")
#         print(sql["query"])

#         converted = convert_sql(sql["query"], table_map, column_map)

#         print("\n ### 변환 결과 : ")
#         print(converted)
#         print("\n")
