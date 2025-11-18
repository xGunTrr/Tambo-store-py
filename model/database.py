import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('tambo.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        with open("tambo.sql", "r", encoding="UTF-8") as f:
            sql_query = f.read()

        self.cur.executescript(sql_query)
        self.conn.commit()