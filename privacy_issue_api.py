from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "cloud storage"
personal_data = []

@app.route('/api/user/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    print(f"[!] Received Personal Data: {data}")  # Simulate insecure logging
    personal_data.append(data)
    return jsonify({"message": "User data submitted!"})

@app.route('/api/user/view', methods=['GET'])
def view_data():
    return jsonify(personal_data)

if __name__ == '__main__':
    app.run(port=5008)
