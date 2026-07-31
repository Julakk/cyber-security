"""
MINI CTF CHALLENGE: "Login Bypass"
Kategori: Web
Difficulty: Easy

Tujuan: Login sebagai admin TANPA tahu passwordnya, untuk dapetin flag.

Cara main:
    pip install flask --break-system-packages
    python3 challenge.py
    Buka http://localhost:6000

Coba selesein sendiri dulu sebelum baca WRITEUP.md!
Hint: lihat folder web-security/sql-injection/ di repo ini kalau butuh clue. 😉
"""
from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "challenge.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE users (username TEXT, password TEXT, role TEXT)")
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ("admin", os.urandom(8).hex(), "admin"),  # password random, gak mungkin ditebak
    )
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", ("guest", "guest", "user"))
    conn.commit()
    conn.close()

PAGE = """
<h2>🚩 Mini CTF: Login Bypass</h2>
<form method="post">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
</form>
{% if result %}<p>{{ result }}</p>{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cur.execute(query)
        user = cur.fetchone()
        conn.close()

        if user and user[2] == "admin":
            result = "🎉 Berhasil! Flag: flag{sql_1nj3ct10n_l0g1n_byp4ss_c0ngr4ts}"
        elif user:
            result = f"Login berhasil sebagai {user[0]}, tapi kamu bukan admin. Coba lagi!"
        else:
            result = "Login gagal."

    return render_template_string(PAGE, result=result)

if __name__ == "__main__":
    init_db()
    print("[*] Challenge running at http://localhost:6000")
    print("[*] Goal: login sebagai admin tanpa tahu password (password-nya random!)")
    app.run(port=6000)
