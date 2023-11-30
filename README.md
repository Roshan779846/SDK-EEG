EEG SDK API Readme
This repository provides a simple EEG (Electroencephalogram) Software Development Kit (SDK) implemented in Python. The SDK allows users to connect to simulated EEG hardware, start and stop data acquisition, and retrieve EEG data points.

Repository Structure
eeg_sdk.py: Contains the implementation of the EEGSDK class, which handles the connection to simulated EEG hardware, data acquisition, and data retrieval.

sdk-test.ipynb: A Jupyter notebook demonstrating how to use the EEGSDK class. It connects to the EEG hardware, starts data acquisition, retrieves and prints EEG data points, stops data acquisition, and disconnects from the hardware.

api-server.py: Implements a Flask API to interact with the EEGSDK. It provides endpoints to get the status, start data acquisition, and stop data acquisition.

Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/eeg-sdk.git
cd eeg-sdk
Install Dependencies:

bash
Copy code
pip install flask
Run the EEG SDK:

Open sdk-test.ipynb in a Jupyter notebook environment and execute the cells to test the EEG SDK functionality.
Run the API Server:

bash
Copy code
python api-server.py
API Endpoints
Status Endpoint:

Endpoint: /api/status
Method: GET
Description: Retrieves the status of the EEG SDK. If initialized, returns success along with a message. If not initialized, returns an error.
Start Data Acquisition Endpoint:

Endpoint: /api/start
Method: POST
Description: Initiates data acquisition. Returns success if the operation is successful, and an error if the EEG SDK is not initialized.
Stop Data Acquisition Endpoint:

Endpoint: /api/stop
Method: POST
Description: Stops data acquisition. Returns success if the operation is successful, and an error if the EEG SDK is not initialized.
Usage Example
Here is an example of how to use the EEG SDK API in Python:

python
Copy code
import requests

# Status Endpoint
status_response = requests.get('http://localhost:5001/api/status')
print(status_response.json())

# Start Data Acquisition Endpoint
start_response = requests.post('http://localhost:5001/api/start')
print(start_response.json())

# Stop Data Acquisition Endpoint
stop_response = requests.post('http://localhost:5001/api/stop')
print(stop_response.json())
Important Notes
Ensure that the necessary dependencies are installed before running the code.
The API server runs on http://localhost:5001 by default. Make sure this port is available.
Contributing
If you would like to contribute to the development of the EEG SDK, feel free to fork the repository, make your changes, and submit a pull request.
