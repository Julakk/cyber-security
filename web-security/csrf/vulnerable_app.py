"""
CONTOH VULNERABLE APP - CSRF Demo
Endpoint ganti email TIDAK memvalidasi asal request, sehingga
bisa dipicu dari web lain selama korban punya session aktif.
"""
from flask import Flask, request, session, render_template_string, redirect

app = Flask(__name__)
app.secret_key = "demo-secret-key-jangan-dipakai-production"

# Simulasi "database" user in-memory
USER_EMAIL = {"email": "ahmad@example.com"}

HOME_PAGE = """
<h2>Dashboard (Vulnerable)</h2>
<p>Email saat ini: <strong>{{ email }}</strong></p>
<form method="post" action="/change-email">
    Email baru: <input name="new_email">
    <input type="submit" value="Ganti Email">
</form>
<p>Coba buka <code>attacker_page.html</code> di tab baru untuk simulasi serangan CSRF.</p>
"""

@app.route("/")
def home():
    session["logged_in"] = True  # auto-login demo
    return render_template_string(HOME_PAGE, email=USER_EMAIL["email"])

@app.route("/change-email", methods=["POST"])
def change_email():
    # ⚠️ VULNERABLE: tidak ada validasi CSRF token, hanya cek session login.
    # Request dari domain manapun akan diterima selama cookie session ikut terkirim.
    if session.get("logged_in"):
        USER_EMAIL["email"] = request.form["new_email"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
