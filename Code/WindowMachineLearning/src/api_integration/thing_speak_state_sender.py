"""This module sends commands to ThingSpeak to set the state of the window.

The module contains a ThingSpeakStateSender class
 which can be used to send commands to ThingSpeak to set the state of the window.

Example usage:
    load_dotenv()
    read_channel_id = "2316311"  # ThingSpeak channel ID for reading data
    write_api_key = os.getenv('WRITE_API_KEY')  # ThingSpeak API key for writing data
    model_path = '../../models/trained_decision_tree_model.pkl'  # Path to the trained model

    controller = ThingSpeakStateSender(read_channel_id, write_api_key, model_path)
    action = controller.get_action()
    if action is not None:
        controller.set_state(action)
"""

import requests
from dotenv import load_dotenv
import os
from .thing_speak_data_retriever import ThingSpeakDataRetriever
from src.data_training.window_controller import WindowController

class ThingSpeakStateSender:
    """A class used to send commands to ThingSpeak to set the state of the window."""

    print("ThingSpeakStateSender Called")

    def __init__(self, read_channel_id, write_api_key, model_path):
        """Initialize the ThingSpeakStateSender with ThingSpeak channel and model paths.

        Args:
            read_channel_id (str): ThingSpeak channel ID for reading data.
            write_api_key (str): ThingSpeak API key for writing data.
            model_path (str): Path to the trained machine learning model.
        """
        self.read_channel_id = read_channel_id
        self.write_api_key = write_api_key
        self.data_retriever = ThingSpeakDataRetriever(read_channel_id)
        self.window_controller = WindowController(model_path)
        self.write_api_base_url = "https://api.thingspeak.com/update"

    def get_action(self):
        """Retrieve the latest data from ThingSpeak and predict the action."""
        _, field_values, _ = self.data_retriever.get_data()

        if field_values:
            # Extract the values needed for the WindowController
            temperature = field_values.get('field1')  # Assuming field1 is the temperature
            humidity = field_values.get('field2')  # Assuming field2 is the humidity
            air_quality = field_values.get('field4')  # Assuming field4 is the IAQ Index

            # Format the data as expected by the WindowController
            sensor_data = [float(temperature), float(humidity), float(air_quality)]

            # Make a prediction with the WindowController
            action = self.window_controller.make_prediction(sensor_data)
            return action
        else:
            print("Failed to retrieve data")
            return None

    def set_state(self, state):
        """Send a command to ThingSpeak to set the state."""
        value = "1" if state else "0"
        params = {
            "api_key": self.write_api_key,
            "field1": value
        }
        response = requests.get(self.write_api_base_url, params=params)
        print(f"Response Text: {response.text}")  # Print response text for debugging
        if response.status_code == 200:
            print(f"Successfully set state to {'On' if state else 'Off'}.")
        else:
            print(f"Failed to set state. Status code: {response.status_code}")
