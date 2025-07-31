from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

STORAGE_FILE = "user_data.json"  # Stored in plaintext!

@app.route('/api/store', methods=['POST'])
def store_data():
    data = request.get_json()
    with open(STORAGE_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    return jsonify({"message": "Data stored insecurely."})

@app.route('/api/retrieve', methods=['GET'])
def retrieve_data():
    if not os.path.exists(STORAGE_FILE):
        return jsonify({"message": "No data found."})
    
    with open(STORAGE_FILE, "r") as f:
        lines = f.readlines()
        records = [json.loads(line) for line in lines]

    return jsonify(records)

if __name__ == '__main__':
    app.run(port=5009)
