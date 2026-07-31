"""
Setup script: membuat database SQLite contoh untuk demo SQL Injection.
Jangan gunakan password plaintext seperti ini di aplikasi production!
"""
import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user'
    )
""")

cur.executemany(
    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
    [
        ("admin", "S3curePass123!", "admin"),
        ("ahmad", "mypassword", "user"),
        ("guest", "guest123", "user"),
    ],
)

conn.commit()
conn.close()

print("Database 'users.db' berhasil dibuat dengan 3 user contoh.")
