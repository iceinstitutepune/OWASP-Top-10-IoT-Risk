from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data = []

@app.route('/api/data/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    sensor_data.append(data)
    return jsonify({"message": "Data uploaded to cloud!"})

@app.route('/api/data/view', methods=['GET'])
def view_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(port=5001)
