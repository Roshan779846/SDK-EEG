from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread
from Eeg_sdk import EEGSDK


eeg_sdk = EEGSDK(serial_port='COM5', baud_rate=9600)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
eeg_sdk = None

@app.route('/status', methods=['GET'])
def get_status():
    if eeg_sdk:
        return jsonify(eeg_sdk.to_json())
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

@app.route('/start', methods=['POST'])
def start_data_acquisition():
    if eeg_sdk:
        eeg_sdk.start_data_acquisition()
        return jsonify({"status": "success", "message": "Data acquisition started"})
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

@app.route('/stop', methods=['POST'])
def stop_data_acquisition():
    if eeg_sdk:
        eeg_sdk.stop_data_acquisition()
        return jsonify({"status": "success", "message": "Data acquisition stopped"})
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

@app.route('/data', methods=['GET'])
def get_data():
    if eeg_sdk:
        # Modify this part to return the actual data you want to display
        data = {"data": "your_data_here"}
        return jsonify(data)
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

def run_api_server():
    app.run(port=5001)

if __name__ == "__main__":
    eeg_sdk = EEGSDK()
    eeg_sdk.load_serialized_data()

    api_thread = Thread(target=run_api_server, args=())
    api_thread.start()
