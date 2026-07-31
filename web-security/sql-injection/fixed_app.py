"""
VERSI YANG SUDAH DIPERBAIKI
Perbedaan utama: parameterized query (menggunakan '?' placeholder),
sehingga input user tidak pernah jadi bagian dari struktur SQL.
"""
from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)

LOGIN_PAGE = """
<h2>Login (Fixed Demo)</h2>
<form method="post">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
</form>
{% if result %}<p>{{ result }}</p>{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        # ✅ FIXED: parameterized query, input user diperlakukan sebagai data,
        # bukan bagian dari perintah SQL.
        cur.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user = cur.fetchone()
        conn.close()

        if user:
            result = f"Login berhasil sebagai: {user[1]} (role: {user[3]})"
        else:
            result = "Login gagal."

    return render_template_string(LOGIN_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
