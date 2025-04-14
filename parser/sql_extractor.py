"""
    SQL 파싱
"""

import os
import re
from lxml import etree


def extract_sql_from_xml(xml_path : str):
    if not os.path.exists(xml_path):
        return FileNotFoundError(f"### XML 파일 없음: {xml_path}")
    
    with open(xml_path, "r", encoding="utf-8") as f:
        xml_content = f.read()
    
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(xml_content.encode("utf-8"), parser=parser)

    sql_elements = ["select", "insert", "update", "delete"]
    extracted = []

    for elem in root:
        if elem.tag in sql_elements:
            sql_id = elem.attrib.get("id", "")
            sql_type = elem.tag
            sql_raw = "".join(elem.itertext()).strip()
            query = re.sub(r'\s+', ' ', sql_raw)

            comment = ""
            previous = elem.getprevious()
            if previous is not None and isinstance(previous, etree._Comment):
                comment = previous.text.strip()

            extracted.append({
                "source_file" : xml_path,
                "sql_id" : sql_id,
                "sql_type" : sql_type,
                "query" : query,
                "comment" : comment
            })

    return extracted


## 테스트
# if __name__ == "__main__":
#     test_path = r"sample\sampleSQL.xml"
#     result = extract_sql_from_xml(test_path)

#     import json
#     print(json.dumps(result, indent=2, ensure_ascii=False))