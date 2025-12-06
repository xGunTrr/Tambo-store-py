import sqlite3
import os

class Database:
    def __init__(self):
        # Construct the path to the database file and SQL script
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, 'tambo.db')
        self.sql_script_path = os.path.join(base_dir, 'tambo.sql')

        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        with open(self.sql_script_path, "r", encoding="UTF-8") as f:
            sql_query = f.read()

        self.cur.executescript(sql_query)
        self.conn.commit()