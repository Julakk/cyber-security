"""
VERSI YANG SUDAH DIPERBAIKI - CSRF Protection dengan token
"""
import secrets
from flask import Flask, request, session, render_template_string, redirect, abort

app = Flask(__name__)
app.secret_key = "demo-secret-key-jangan-dipakai-production"

USER_EMAIL = {"email": "ahmad@example.com"}

HOME_PAGE = """
<h2>Dashboard (Fixed - CSRF Protected)</h2>
<p>Email saat ini: <strong>{{ email }}</strong></p>
<form method="post" action="/change-email">
    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
    Email baru: <input name="new_email">
    <input type="submit" value="Ganti Email">
</form>
"""

@app.route("/")
def home():
    session["logged_in"] = True
    # ✅ FIXED: generate CSRF token unik per session, simpan di server
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return render_template_string(HOME_PAGE, email=USER_EMAIL["email"], csrf_token=session["csrf_token"])

@app.route("/change-email", methods=["POST"])
def change_email():
    # ✅ FIXED: validasi token sebelum memproses request
    submitted_token = request.form.get("csrf_token")
    if not submitted_token or submitted_token != session.get("csrf_token"):
        abort(403, description="CSRF token tidak valid atau tidak ada. Request ditolak.")

    if session.get("logged_in"):
        USER_EMAIL["email"] = request.form["new_email"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5003)
