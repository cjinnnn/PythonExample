"""
위 코드에서는 mytable이라는 이름의 테이블에 컬럼이 있는지 확인하는 SQL 쿼리를 실행하고, fetchall() 메소드를 사용하여 결과를 가져옵니다. 만약 결과가 있으면 mytable에는 컬럼이 있습니다.를 출력하고, 결과가 없으면 mytable에는 컬럼이 없습니다.를 출력합니다.
"""
import sqlite3

# SQLite 데이터베이스 파일 경로와 파일 이름을 정의합니다.
db_path = "mydatabase.db"

# 데이터베이스 연결을 만듭니다.
conn = sqlite3.connect(db_path)

# 커서를 만듭니다.
cursor = conn.cursor()

# 컬럼이 있는지 확인하는 SQL 쿼리를 만듭니다.
column_check_query = "PRAGMA table_info(mytable)"

# 커서를 사용하여 쿼리를 실행합니다.
cursor.execute(column_check_query)

# 결과를 가져옵니다.
columns = cursor.fetchall()

# 결과를 출력합니다.
if columns:
    print("mytable에는 컬럼이 있습니다.")
else:
    print("mytable에는 컬럼이 없습니다.")

# 커넥션을 닫습니다.
conn.close()
