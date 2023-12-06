import time 
import json
import usb.core
import usb.util

class EEGSDK:
    def __init__(self, usb_vendor_id,usb_product_id, usb_endpoint=0x81):
        self.usb_vendor_id = usb_vendor_id
        self.usb_product_id = usb_product_id
        self.usb_endpoint = usb_endpoint
        self.usb_device = None
        self.serialized_data = []

    def connect(self):
        try:
            
            self.usb_device = usb.core.find(idVendor=self.usb_vendor_id, idProduct=self.usb_product_id)
            
            if self.usb_device is not None:
                self.usb_device.set_configuration()
                print("Connected to EEG hardware via USB.")
            else:
                print("EEG hardware not found.")

        except usb.core.USBError as e:
            print(f"Error connecting to EEG hardware: {e}")
    def disconnect(self):
        if self.usb_device is not None:
            usb.util.dispose_resources(self.usb_device)
            print("Disconnected from EEG hardware.")
        else:
            print("Not connected to EEG hardware.")

    def start_data_acquisition(self):
        try:
            
            self.usb_device.write(self.usb_endpoint, b'START')
            print("Started data acquisition.")

        except usb.core.USBError as e:
            print(f"Error starting data acquisition: {e}")

    def stop_data_acquisition(self):
        try:
          
            self.usb_device.write(self.usb_endpoint, b'STOP')
            print("Stopped data acquisition.")

        except usb.core.USBError as e:
            print(f"Error stopping data acquisition: {e}")

    def retrieve_eeg_data(self):
        try:
          
            while True:
                data = self.usb_device.read(self.usb_endpoint, 64, timeout=1000)
                data_point = json.loads(data.decode('utf-8'))
                yield data_point
                time.sleep(1)

        except usb.core.USBError as e:
            print(f"Error retrieving EEG data: {e}")

    def to_json(self):
        return json.dumps({"status": "success", "message": "EEG SDK is operational"})
    
