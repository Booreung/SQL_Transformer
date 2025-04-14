"""
    전체 모듈의 파이프라이닝 실행
"""

import os
from parser.sql_extractor import extract_sql_from_xml
from mapping.mapping_loader import load_mapping_excel
from transformer.sql_converter import convert_sql
from generator.sql_writer import save_as_json, save_as_excel


def main():

    # 1.  입력 경로 정의
    sql_xml_path = os.path.join("sample", "sampleSQL.xml")
    mapping_excel_path = os.path.join("sample", "sql_mapping.xlsx")

    # 2. SQL 파싱
    sql_list = extract_sql_from_xml(sql_xml_path)

    # 3. 매핑 정보 로등
    table_map, column_map = load_mapping_excel(mapping_excel_path)

    # 4. 변환 결과 생성
    converted_result = []
    for sql in sql_list:
        converted_sql = convert_sql(sql["query"], table_map, column_map)
        converted_result.append({
            "sql_id": sql["sql_id"],
            "sql_type": sql["sql_type"],
            "comment": sql["comment"],
            "original": sql["query"],
            "converted": converted_sql
        })
    
    save_as_json(converted_result, os.path.join("output", "sql_result.json"))
    save_as_excel(converted_result, os.path.join("output", "sql_result.xlsx"))

    print("\n### 전체 SQL 자동 반환 및 저장 완료")


if __name__ == "__main__":
    main()