from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Simulate user check (no actual auth logic)
    if username == "admin" and password == "iot123":
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
