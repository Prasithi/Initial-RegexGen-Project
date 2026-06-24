import sqlite3

conn = sqlite3.connect(
    'history.db',
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_rule TEXT,
    generated_regex TEXT,
    test_string TEXT,
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("SQLite Database Connected")