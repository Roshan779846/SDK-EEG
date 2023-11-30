import csv
import time
import json

class EEGSDK:
    def __init__(self, csv_data_file="features_raw.csv"):
        self.csv_data_file = csv_data_file
        self.serialized_data = []

    def load_serialized_data(self):
        try:
            with open(self.csv_data_file) as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    data_point = [float(value) for value in row]
                    self.serialized_data.append(data_point)

        except FileNotFoundError:
            print(f"File {self.csv_data_file} not found.")

    def connect(self):
        self.load_serialized_data()
        print("Connected to EEG hardware.")

    def disconnect(self):
        self.load_serialized_data()
        print("Disconnected from EEG hardware.")

    def start_data_acquisition(self):
        self.load_serialized_data()
        print("Started data acquisition.")

    def stop_data_acquisition(self):
        self.load_serialized_data()
        print("Stopped data acquisition.")

    def retrieve_eeg_data(self):
        if self.serialized_data:
            for data_point in self.serialized_data:
                yield data_point
                time.sleep(1)

    def to_json(self):
        return json.dumps({"status": "success", "message": "EEG SDK is operational"})
