# import time
# import json
# import serial
# from pylsl import StreamInfo, StreamOutlet

# class EEGSDK:
#     def __init__(self, serial_port, baud_rate=9600, lsl_stream_name='ORIC-EEG', json_file_path='eeg_data.json'):
#         self.serial_port = serial_port
#         self.baud_rate = baud_rate
#         self.serial_device = None
#         self.lsl_stream_name = lsl_stream_name
#         self.lsl_stream_info = StreamInfo(lsl_stream_name, 'EEG', 6, 250, 'float32', 'oric6ch')
#         self.lsl_outlet = StreamOutlet(self.lsl_stream_info)
#         self.json_file_path = json_file_path
#         self.latest_data = None  

     

#     def connect(self):
#         try:
#             self.serial_device = serial.Serial(self.serial_port, self.baud_rate)
#             print(f"Connected to EEG hardware via {self.serial_port}.")

#         except serial.SerialException as e:
#             print(f"Error connecting to EEG hardware: {e}")

#     def disconnect(self):
#         if self.serial_device is not None:
#             self.serial_device.close()
#             print("Disconnected from EEG hardware.")
#         else:
#             print("Not connected to EEG hardware.")

#     def start_data_acquisition(self):
#         try:
#             self.serial_device.write(b'START\n')  # Add a newline character
#             print("Started data acquisition.")

#         except serial.SerialException as e:
#             print(f"Error starting data acquisition: {e}")

#     def stop_data_acquisition(self):
#         try:
#             self.serial_device.write(b'STOP\n')  # Add a newline character
#             print("Stopped data acquisition.")

#         except serial.SerialException as e:
#             print(f"Error stopping data acquisition: {e}")


#     def retrieve_eeg_data(self):
#         try:
#             while True:
#                 data = self.serial_device.readline().decode('utf-8')
#                 try:
#                     data_point = json.loads(data)
#                     self.latest_data = data_point

#                     # Extract EEG data and push it to LSL
#                     EEG_list = list(data_point.values())[2:]
#                     if EEG_list:
#                         self.lsl_outlet.push_sample(EEG_list)

#                     # Write the data to the JSON file
#                     with open(self.json_file_path, 'a') as json_file:
#                         json.dump(data_point, json_file)
#                         json_file.write('\n')

#                     print("Received data:", data_point)

#                 except json.JSONDecodeError as e:
#                     print(f"Error decoding JSON: {e}")
#                     self.latest_data = None

#                 time.sleep(0)

#         except serial.SerialException as e:
#             print(f"Error retrieving EEG data: {e}")

#     def get_data(self):
#         return self.latest_data
    

# # Example usage:
# if __name__ == "__main__":
#     eeg_sdk = EEGSDK(serial_port='COM5', baud_rate=115200)
#     eeg_sdk.connect()
#     eeg_sdk.start_data_acquisition()

#     try:
#         for data_point in eeg_sdk.retrieve_eeg_data():
#             print(data_point)
#             # Process the data as needed

#     except KeyboardInterrupt:
#         # Stop data acquisition on keyboard interrupt
#         eeg_sdk.stop_data_acquisition()
#         eeg_sdk.disconnect()
# import time
# import json
# import serial
# from pylsl import StreamInfo, StreamOutlet

# class EEGSDK:
#     def __init__(self, serial_port, baud_rate=9600, lsl_stream_name='ORIC-EEG', json_file_path='eeg_data.json'):
#         self.serial_port = serial_port
#         self.baud_rate = baud_rate
#         self.serial_device = None
#         self.lsl_stream_name = lsl_stream_name
#         self.lsl_stream_info = StreamInfo(lsl_stream_name, 'EEG', 6, 250, 'float32', 'oric6ch')
#         self.lsl_outlet = StreamOutlet(self.lsl_stream_info)
#         self.json_file_path = json_file_path
#         self.latest_data = None
#         self.is_running = False

#     def connect(self):
#         try:
#             self.serial_device = serial.Serial(self.serial_port, self.baud_rate)
#             print(f"Connected to EEG hardware via {self.serial_port}.")

#         except serial.SerialException as e:
#             print(f"Error connecting to EEG hardware: {e}")

#     def disconnect(self):
#         if self.serial_device is not None:
#             self.serial_device.close()
#             print("Disconnected from EEG hardware.")
#         else:
#             print("Not connected to EEG hardware.")

#     def start_data_acquisition(self):
#         try:
#             self.is_running = True
#             self.serial_device.write(b'START\n')  # Add a newline character
#             print("Started data acquisition.")

#         except serial.SerialException as e:
#             print(f"Error starting data acquisition: {e}")

#     def stop_data_acquisition(self):
#         try:
#             self.is_running = False
#             self.serial_device.write(b'STOP\n')  # Add a newline character
#             print("Stopped data acquisition.")

#         except serial.SerialException as e:
#             print(f"Error stopping data acquisition: {e}")

#     def retrieve_eeg_data(self):
#         try:
#             while self.is_running:
#                 data = self.serial_device.readline().decode('utf-8')
#                 try:
#                     data_point = json.loads(data)
#                     self.latest_data = data_point

#                     # Extract EEG data and push it to LSL
#                     EEG_list = list(data_point.values())[2:]
#                     if EEG_list:
#                         self.lsl_outlet.push_sample(EEG_list)

#                     # Write the data to the JSON file
#                     with open(self.json_file_path, 'a') as json_file:
#                         json.dump(data_point, json_file)
#                         json_file.write('\n')

#                     print("Received data:", data_point)

#                 except json.JSONDecodeError as e:
#                     print(f"Error decoding JSON: {e}")

#                 # except Exception as ex:
#                 #     print(f"Error: {ex}")

#                 time.sleep(0)

#         except serial.SerialException as e:
#             print(f"Error retrieving EEG data: {e}")

#     def get_data(self):
#          if self.latest_data is not None:
#           return self.latest_data
#          else:
#           return {"status": "error", "message": "No data available"}


#     # def get_data(self):
#     #     return self.latest_data
            

# if __name__ == "__main__":
#     eeg_sdk = EEGSDK(serial_port='COM5', baud_rate=115200)
#     eeg_sdk.connect()
#     eeg_sdk.start_data_acquisition()

#     try:
#         for data_point in eeg_sdk.retrieve_eeg_data():
#             print(data_point)
#             # Process the data as needed

#     except KeyboardInterrupt:
#         # Stop data acquisition on keyboard interrupt
#         eeg_sdk.stop_data_acquisition()
#         eeg_sdk.disconnect()
import time
import json
import serial
from pylsl import StreamInfo, StreamOutlet

class EEGSDK:
    def __init__(self, serial_port, baud_rate=9600, lsl_stream_name='ORIC-EEG', json_file_path='eeg_data.json'):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.serial_device = None
        self.lsl_stream_name = lsl_stream_name
        self.lsl_stream_info = StreamInfo(lsl_stream_name, 'EEG', 6, 250, 'float32', 'oric6ch')
        self.lsl_outlet = StreamOutlet(self.lsl_stream_info)
        self.json_file_path = json_file_path
        self.latest_data = None
        self.is_running = False

    def connect(self):
        try:
            self.serial_device = serial.Serial(self.serial_port, self.baud_rate)
            print(f"Connected to EEG hardware via {self.serial_port}.")

        except serial.SerialException as e:
            print(f"Error connecting to EEG hardware: {e}")

    def disconnect(self):
        if self.serial_device is not None:
            self.serial_device.close()
            print("Disconnected from EEG hardware.")
        else:
            print("Not connected to EEG hardware.")

    def start_data_acquisition(self):
        try:
            self.is_running = True
            self.serial_device.write(b'START\n')  # Add a newline character
            print("Started data acquisition.")

        except serial.SerialException as e:
            print(f"Error starting data acquisition: {e}")

    def stop_data_acquisition(self):
        try:
            self.is_running = False
            self.serial_device.write(b'STOP\n')  # Add a newline character
            print("Stopped data acquisition.")

        except serial.SerialException as e:
            print(f"Error stopping data acquisition: {e}")

    def retrieve_eeg_data(self):
        try:
            while self.is_running:
                data = self.serial_device.readline().decode('utf-8')
                print("Raw data:", data)  # Add this line to print raw data
                try:
                    data_point = json.loads(data)
                    self.latest_data = data_point

                    EEG_list = list(data_point.values())[2:]
                    if EEG_list:
                        self.lsl_outlet.push_sample(EEG_list)

                    with open(self.json_file_path, 'a') as json_file:
                        json.dump(data_point, json_file)
                        json_file.write('\n')

                    print("Received data:", data_point)

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")

                time.sleep(0)

        except serial.SerialException as e:
            print(f"Error retrieving EEG data: {e}")

    def get_data(self):
        if self.latest_data is not None:
            return self.latest_data
        else:
            return {"status": "error", "message": "No data available"}

# Example usage:
if __name__ == "__main__":
    eeg_sdk = EEGSDK(serial_port='COM5', baud_rate=115200)
    eeg_sdk.connect()
    eeg_sdk.start_data_acquisition()

    try:
        eeg_sdk.retrieve_eeg_data()  # Call the function directly, as it runs in a loop

    except KeyboardInterrupt:
        eeg_sdk.stop_data_acquisition()
        eeg_sdk.disconnect()
