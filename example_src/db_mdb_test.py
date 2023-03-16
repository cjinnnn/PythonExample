
"""
Python에서 Access 데이터베이스를 사용하려면 pyodbc 모듈을 사용해야 합니다. 이 모듈은 ODBC 드라이버를 통해 Access 데이터베이스에 연결하는 기능을 제공합니다. 다음은 간단한 예제 코드입니다.
위 코드에서 conn 변수에 연결 정보를 저장하고, cursor 변수를 사용하여 쿼리를 실행하고 결과를 가져옵니다. 연결을 종료하기 전에는 항상 conn.close()를 호출하여 리소스를 해제해야 합니다.
참고로, Access 데이터베이스를 사용하기 위해서는 해당 데이터베이스에 대한 ODBC 드라이버가 필요합니다. Windows 운영체제에서는 기본적으로 Microsoft Access ODBC 드라이버가 설치되어 있지만, 다른 운영체제에서는 해당 드라이버를 따로 설치해야 할 수도 있습니다.
"""

import pyodbc

# Access 데이터베이스에 연결
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\path\to\access\database.accdb;')

# 커서 생성
cursor = conn.cursor()

# 쿼리 실행
cursor.execute('SELECT * FROM table_name')

# 결과 가져오기
rows = cursor.fetchall()

# 연결 종료
conn.close()
