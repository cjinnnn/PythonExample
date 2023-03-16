import sqlite3

# SQLite3 데이터베이스 연결 생성
conn = sqlite3.connect('example.db')

# 데이터베이스에 테이블 생성
conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')

# 데이터 삽입
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1, 'Paul', 32, 'California', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00)")

# 커밋
conn.commit()

# 데이터 조회
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

# 연결 종료
conn.close()
