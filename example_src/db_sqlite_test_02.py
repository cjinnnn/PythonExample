"""
위 코드에서는 mytable이라는 이름의 테이블이 데이터베이스에 존재하는지 확인하는 SQL 쿼리를 실행하고, fetchone() 메소드를 사용하여 결과를 가져옵니다. 만약 결과가 있으면 mytable이 존재합니다.를 출력하고, 결과가 없으면 mytable이 존재하지 않습니다.를 출력합니다.
컬럼이 있는지 확인하려면, PRAGMA table_info(table_name) 쿼리를 사용하여 확인할 수 있습니다. 이 쿼리는 지정된 테이블의 열 정보를 반환합니다. 따라서 아래와 같이 코드를 작성할 수 있습니다.
"""

import sqlite3

# SQLite 데이터베이스 파일 경로와 파일 이름을 정의합니다.
db_path = "mydatabase.db"

# 데이터베이스 연결을 만듭니다.
conn = sqlite3.connect(db_path)

# 커서를 만듭니다.
cursor = conn.cursor()

# 테이블이 있는지 확인하는 SQL 쿼리를 만듭니다.
table_check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='mytable'"

# 커서를 사용하여 쿼리를 실행합니다.
cursor.execute(table_check_query)

# 결과를 가져옵니다.
table_exists = cursor.fetchone()

# 결과를 출력합니다.
if table_exists:
    print("mytable이 존재합니다.")
else:
    print("mytable이 존재하지 않습니다.")

# 커넥션을 닫습니다.
conn.close()