"""
VERSI YANG SUDAH DIPERBAIKI - Secure JWT Authentication
"""
import jwt
import secrets
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ FIXED #1: secret kuat, digenerate random, panjang, dan disimpan di environment variable
# (di production: os.environ["JWT_SECRET"], jangan hardcode!)
SECRET = secrets.token_hex(32)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # (Di real app: cek password pakai bcrypt.checkpw, bukan plaintext compare)
    if username == "admin" and password == "admin123":
        now = datetime.datetime.now(datetime.timezone.utc)
        payload = {
            "username": username,
            "role": "admin",
            # ✅ FIXED #2: token expiry (15 menit), tidak berlaku selamanya
            "exp": now + datetime.timedelta(minutes=15),
            "iat": now,
        }
        # ✅ FIXED #3: tidak ada data sensitif (password) di payload
        token = jwt.encode(payload, SECRET, algorithm="HS256")
        return jsonify({"token": token})

    return jsonify({"error": "Login gagal"}), 401

@app.route("/profile")
def profile():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        # ✅ FIXED #4: algorithms dibatasi ketat, hanya HS256 yang diterima
        # (mencegah "alg:none" attack dan algorithm confusion)
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return jsonify(payload)
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token sudah expired, silakan login ulang"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token tidak valid"}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5005)
