import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("""
CREATE TABLE leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT
)
""")
conn.commit()
conn.close()