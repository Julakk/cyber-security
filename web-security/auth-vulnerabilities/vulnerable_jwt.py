"""
CONTOH VULNERABLE APP - Broken JWT Authentication
Berisi beberapa kesalahan umum yang sering ditemukan di aplikasi nyata.
"""
import jwt
import base64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# ⚠️ VULNERABLE #1: secret lemah, gampang di-brute-force
SECRET = "123456"

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "admin" and password == "admin123":
        # ⚠️ VULNERABLE #2: tidak ada 'exp' (expiry) -> token berlaku selamanya
        # ⚠️ VULNERABLE #3: data sensitif (password) ikut masuk payload
        # (JWT payload cuma base64-encoded, BUKAN dienkripsi -> gampang dibaca siapa saja)
        payload = {
            "username": username,
            "password": password,
            "role": "admin",
        }
        token = jwt.encode(payload, SECRET, algorithm="HS256")
        return jsonify({"token": token})

    return jsonify({"error": "Login gagal"}), 401

@app.route("/profile")
def profile():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        # ⚠️ VULNERABLE #4: algorithms tidak dibatasi ketat, rentan "alg:none" attack
        # kalau library/versi tertentu tidak strict, token dengan alg:none bisa diterima
        payload = jwt.decode(token, SECRET, algorithms=["HS256", "none"])
        return jsonify(payload)
    except Exception as e:
        return jsonify({"error": str(e)}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5004)

# --- Demonstrasi decode tanpa signature verification (untuk edukasi) ---
def demo_decode_without_verification(token):
    """Nunjukin kalau payload JWT bisa dibaca siapa saja tanpa tau secret-nya."""
    header_b64, payload_b64, _ = token.split(".")
    payload_b64 += "=" * (-len(payload_b64) % 4)  # padding
    decoded = base64.urlsafe_b64decode(payload_b64)
    return json.loads(decoded)
