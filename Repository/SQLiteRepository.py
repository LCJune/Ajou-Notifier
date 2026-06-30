import sqlite3

class SQLiteRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path) # sqlite3.connect() : 데이터베이스 연결 객체를 생성
        self.cursor = self.conn.cursor() # SQL을 실행하는 객체
        
        # notifications Table이 없을 시 생성
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS notifications(
            ID INTEGER PRIMARY KEY,
            Source TEXT not null,
            Title TEXT not null,
            Date TEXT not null,
            Link TEXT not null
        )
        """)
        # primary key : 기본 키, not null: 비워져 있을 수 없음(null일 수 없음) 
        
    def exsist(self, notice_id):
        
        """
        ? 사용 시 SQLite가 문자열이면 자동으로 ' '를 붙여주고, 숫자는 숫자로 처리하고,
        SQL Injection 공격을 방지함.(SQL Injection 공격 : 악의적인 사용자가 SQL 쿼리를 조작하여 데이터베이스에 접근하는 공격)
        """
        self.cursor.execute("SELECT id FROM notifications WHERE id = ?", (notice_id,)) # execute() : SQL문을 실행하는 메서드, 두 번째 인자로 튜플을 기대함.
        return self.cursor.fetchone() is not None # fetchone() : SQL문 실행 결과에서 한 행을 가져오는 메서드, 결과가 없으면 None 반환


    def insert(self, notice_id, source, title, date, link):
        self.cursor.execute("INSERT INTO notifications(ID, Source, Title, Date, Link) VALUES(?, ?, ?, ?, ?)", (notice_id, source, title, date, link))
        self.conn.commit() # commit() : 데이터베이스에 변경 사항을 저장하는 메서드
        
        
    def close(self):
        self.conn.close()
    