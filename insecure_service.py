# insecure_service.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to IoT Firmware Update Server - Version 1.0"

@app.route('/update', methods=['POST'])
def update_firmware():
    firmware = request.files.get('firmware')
    if firmware:
        firmware.save("firmware_uploaded.bin")
        return "Firmware uploaded successfully (no checks!)"
    else:
        return "No firmware file provided."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
