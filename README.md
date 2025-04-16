# 🔄 SQL Transformer - AS-IS → TO-BE SQL 자동 변환 도구

> 기존 시스템의 MyBatis SQL(XML)을 새로운 시스템 구조에 맞게 자동 변환하는 실용 도구  
> **목표:** 개발자의 반복 작업 시간을 줄이는 것

---

## 🧩 주요 기능

| 기능 | 설명 |
|------|------|
| 📂 XML 일괄 분석 | 폴더 내 `.xml` 파일에서 SQL ID, 주석, 쿼리 추출 |
| 📑 매핑 정보 기반 변환 | 엑셀(.xlsx)에 정의된 테이블/컬럼 매핑 정보를 기반으로 자동 치환 |
| 🔃 역순 매핑 처리 | 컬럼명이 중첩될 경우를 고려한 안전한 역순 처리 |
| 🧪 CASE / DECODE / NVL 처리 | 복잡한 표현식 내 컬럼도 정확히 변환 가능 |
| 🕵️‍♀️ 변환 전후 SQL 비교 | `diff` 방식으로 AS-IS / TO-BE 쿼리 비교 출력 (콘솔) |
| 📤 결과 저장 | 변환 결과를 `.json`, `.xlsx` 파일로 저장 |

---

## 📁 폴더 구조

sql_transformer/ 

│ 

├── config.py # 경로, 매핑 엑셀 파일 위치 정의 

├── main.py # 전체 실행 파이프라인 구성 

│ 

├── parser/ 

│ └── sql_extractor.py # XML에서 SQL + 주석 추출 

│

├── mapping/ 

│ └── mapping_loader.py # 매핑 엑셀 로딩 (테이블/컬럼) 

│ 

├── transformer/ 

│ └── sql_converter.py # SQL 자동 변환기 (매핑 기반) 

│ 

├── generator/ 

│ └── sql_writer.py # 결과 저장 (json / excel) 

│ 

├── sample/ 

│ └── sampleSQL.xml # 테스트용 SQL 

│ └── sql_mapping.xlsx # 테이블/컬럼 매핑 엑셀

│

├── output/ 

│ └── sql_result.json # 변환 결과 JSON 저장 

│ └── sql_result.xlsx # 변환 결과 EXCEL 저장 


---

## 📁 실행

```bash

        python main.py

```

>결과는 output/sql_result.json, output/sql_result.xlsx 로 저장됩니다
>변환 전/후 SQL은 콘솔에 비교(diff) 형식으로 출력됩니다.

---

## 📌 목적
100% 완벽한 SQL 변환이 아니라,
개발자가 반복되는 수작업을 덜고 빠르게 수정 방향을 파악하도록 돕는 도구입니다.


---

