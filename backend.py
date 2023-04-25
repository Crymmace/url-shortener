import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url text, key text)")
        self.conn.commit()

    def insert(self, url, key):
        self.cur.execute("INSERT INTO urls VALUES (NULL, ?, ?)", (url, key))
        self.conn.commit()

    def search(self, url="", key=""):
        self.cur.execute("SELECT * FROM urls WHERE url=? OR key=?", (url, key))
        rows = self.cur.fetchall()
        return rows

    def search_all(self):
        self.cur.execute("SELECT * FROM urls")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()
