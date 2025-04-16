"""
    전체 모듈의 파이프라이닝 실행
"""

import os
from parser.sql_extractor import extract_sql_from_xml
from mapping.mapping_loader import load_mapping_excel
from transformer.sql_converter import convert_sql
from generator.sql_writer import save_as_json, save_as_excel
from difflib import unified_diff


def main():

    # 1.  입력 경로 정의
    #sql_xml_path = os.path.join("sample", "sampleSQL.xml") -> 하나의 파일만 변환 할 경우(파싱 할 경우)
    mapping_excel_path = os.path.join("sample", "sql_mapping.xlsx")

    # 2. SQL 파싱
    sql_list = []
    for fname in os.listdir("sample"):
        if fname.endswith(".xml"):
            sql_list += extract_sql_from_xml(os.path.join("sample", fname))

    # 3. 매핑 정보 로등
    table_map, column_map = load_mapping_excel(mapping_excel_path)

    # 4. 변환 결과 생성
    converted_result = []
    for sql in sql_list:
        if table_map and column_map:
            converted_sql = convert_sql(sql["query"], table_map, column_map)

            ## 변환 비교 출력
            print_sql_diff(sql["query"], converted_sql, sql["sql_id"], sql["source_file"])

            converted_result.append({
                "source_file" : sql["source_file"],
                "sql_id": sql["sql_id"],
                "sql_type": sql["sql_type"],
                "comment": sql["comment"],
                "original": sql["query"],
                "converted": converted_sql
            })
        else:
            converted_result.append({
                "warnings" : "컬럼에 대한 매핑 정보가 없습니다."
            })
            break
    
    save_as_json(converted_result, os.path.join("output", "sql_result.json"))
    save_as_excel(converted_result, os.path.join("output", "sql_result.xlsx"))

    print("\n### 전체 SQL 자동 반환 및 저장 완료")


def print_sql_diff(asis_sql : str , tobe_sql : str, sql_id :str = "", source_file : str = ""):
    print(f"\n ### [SQL 변환 비교] - SQL ID: {sql_id} / Source: {source_file} ")
    print("-" * 60)
    diff = unified_diff(
        asis_sql.strip().splitlines(),
        tobe_sql.strip().splitlines(),
        fromfile="AS-IS-SQL",
        tofile="TO-BE-SQL",
        lineterm="\n"
    )

    for line in diff:
        print(line)
        
    print("-" * 60)
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[예외 발생] {e}")
    finally:
        input("\n\n[프로그램 종료] 엔터를 눌러 창을 닫습니다...")