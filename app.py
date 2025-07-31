from flask import Flask, request, jsonify, render_template
import sqlite3
import os
import paho.mqtt.publish as publish

app = Flask(__name__)
DB = "iot_users.db"

# --- Simulated login page ---
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "Login successful!"
    else:
        return "Invalid credentials"

# --- Vulnerable API: MQTT message, no authentication ---
@app.route('/api/device/on', methods=['POST'])
def device_on():
    publish.single("iot/device/status", "ON", hostname="localhost")
    return jsonify({"status": "MQTT message sent: Device ON"})

# --- Insecurely exposing personal data ---
@app.route('/api/userinfo', methods=['GET'])
def user_info():
    return jsonify({
        "username": "admin",
        "email": "admin@example.com",
        "phone": "9999999999"
    })

# --- Fake firmware update endpoint (no validation) ---
@app.route('/update', methods=['POST'])
def update():
    file = request.files['firmware']
    file.save(os.path.join("uploads", file.filename))
    return "Firmware update uploaded (no validation!)"

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
