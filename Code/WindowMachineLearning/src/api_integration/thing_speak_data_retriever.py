"""This module retrieves data from the ThingSpeak channel.

The module contains a ThingSpeakDataRetriever class
 which can be used to retrieve data from the ThingSpeak channel.

Example usage:
    load_dotenv()
    channel_id = "2316311"  # Channel ID
    data_retriever = ThingSpeakDataRetriever(channel_id)

    field_names, field_values, entry_id = data_retriever.get_data()

    if field_names and field_values:
        print("Field Names:")
        print(field_names)
        print("\nField Values for the last entry:")
        print(field_values)
        print("\nEntry ID of the last entry:")
        print(entry_id)
"""

import requests
import os
from dotenv import load_dotenv


class ThingSpeakDataRetriever:
    print("ThingSpeakDataRetriever Called")

    def __init__(self, channel_id):
        """Initialize the ThingSpeakDataRetriever with the channel ID.

        Args: channel_id (str): The ID of the ThingSpeak channel to retrieve data
        from.
        """
        self.base_url =\
            f"https://api.thingspeak.com/channels/{channel_id}/feeds.json"
        self.api_key = os.getenv(
            'READ_API_KEY')  # Assumes the .env file has the 'READ_API_KEY'

    def get_data(self, results=2):
        """Retrieve data from the ThingSpeak channel.

        Args:
            results (int): The number of results to retrieve.

        Returns: tuple: A tuple containing field names, field values of the last
        entry, and the entry ID.
        """
        params = {
            "api_key": self.api_key,
            "results": results
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            last_entry = data['feeds'][-1]
            field_names = {f"field{i}": data['channel'][f'field{i}'] for i in
                           range(1, 7)}
            field_values = {f"field{i}": last_entry[f'field{i}'] for i in
                            range(1, 7)}
            entry_id = last_entry['entry_id']
            return field_names, field_values, entry_id
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None, None, None
