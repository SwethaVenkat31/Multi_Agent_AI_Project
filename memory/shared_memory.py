# memory/shared_memory.py
import sqlite3
from datetime import datetime

class SharedMemory:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memory_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                type TEXT,
                timestamp TEXT,
                extracted_fields TEXT,
                thread_id TEXT
            )
        ''')

    def log(self, source, type_, extracted_fields, thread_id=None):
        timestamp = datetime.now().isoformat()
        self.conn.execute('''
            INSERT INTO memory_log (source, type, timestamp, extracted_fields, thread_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (source, type_, timestamp, str(extracted_fields), thread_id))
        self.conn.commit()

    def fetch_all(self):
        return self.conn.execute('SELECT * FROM memory_log').fetchall()
