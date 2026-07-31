"""
CONTOH VULNERABLE APP - JANGAN DIPAKAI DI PRODUCTION
Demo ini sengaja rentan SQL Injection untuk keperluan edukasi.
Jalankan hanya di localhost / environment sandbox.
"""
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

LOGIN_PAGE = """
<h2>Login (Vulnerable Demo)</h2>
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

        # ⚠️ VULNERABLE: query dibangun dengan string formatting langsung.
        # Input user masuk mentah-mentah ke query SQL.
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executed query:", query)  # untuk debugging/edukasi

        cur.execute(query)
        user = cur.fetchone()
        conn.close()

        if user:
            result = f"Login berhasil sebagai: {user[1]} (role: {user[3]})"
        else:
            result = "Login gagal."

    return render_template_string(LOGIN_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
