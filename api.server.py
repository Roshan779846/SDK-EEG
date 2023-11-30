from flask import Flask, jsonify
from threading import Thread
from eeg_sdk import EEGSDK

app = Flask(__name__)
eeg_sdk = None

@app.route('/api/status', methods=['GET'])
def get_status():
    if eeg_sdk:
        return jsonify(eeg_sdk.to_json())
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

@app.route('/api/start', methods=['POST'])
def start_data_acquisition():
    if eeg_sdk:
        eeg_sdk.start_data_acquisition()
        return jsonify({"status": "success", "message": "Data acquisition started"})
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

@app.route('/api/stop', methods=['POST'])
def stop_data_acquisition():
    if eeg_sdk:
        eeg_sdk.stop_data_acquisition()
        return jsonify({"status": "success", "message": "Data acquisition stopped"})
    else:
        return jsonify({"status": "error", "message": "EEGSDK not initialized"}), 500

def run_api_server():
    app.run(port=5001)

if __name__ == "__main__":
    eeg_sdk = EEGSDK()
    eeg_sdk.load_serialized_data()

    api_thread = Thread(target=run_api_server, args=())
    api_thread.start()
