"""
file: test_data_generator.py
date: 25/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the ThingSpeakDataRetriever class.

The tests include:
    - Testing that the get_data method returns the correct data for a successful API response
    - Testing that the get_data method returns None for all values upon a failed API response

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.api_integration.test_thing_speak_data_retriever
"""

import unittest
from unittest.mock import patch, MagicMock
from src.api_integration.thing_speak_data_retriever import ThingSpeakDataRetriever

class TestThingSpeakDataRetriever(unittest.TestCase):

    def setUp(self):
        """Set up a ThingSpeakDataRetriever instance for all test methods."""
        self.channel_id = 'mock_channel_id'
        self.api_key = 'mock_api_key'
        self.data_retriever = ThingSpeakDataRetriever(self.channel_id)

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        """Test get_data method for a successful API response."""
        # Mock response object with successful data retrieval
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "channel": {
                "id": self.channel_id,
                "field1": "Temperature",
                "field2": "Humidity",
                "field3": "UV light",
                "field4": "Air Quality",
                "field5": "Smoke",
                "field6": "Window Status"
            },
            "feeds": [
                {"field1": "25.40", "field2": "47.09", "field3": "13.00",
                 "field4": "66.98", "field5": "48.00", "field6": "0",
                 "entry_id": 90666}
            ]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the method under test
        field_names, field_values, entry_id = self.data_retriever.get_data()

        # Assert the method returns the correct data
        self.assertIsNotNone(field_names)
        self.assertIsNotNone(field_values)
        self.assertIsNotNone(entry_id)
        # Assert that the last entry id is returned
        self.assertEqual(entry_id, 90666)
        # Assert that the correct API call was made
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        """Test get_data method for a failed API response."""
        # Mock response object with a failed data retrieval
        mock_response = MagicMock()
        mock_response.status_code = 500  # Internal server error
        mock_get.return_value = mock_response

        # Call the method under test
        field_names, field_values, entry_id = self.data_retriever.get_data()

        # Assert the method returns None for all values upon failure
        self.assertIsNone(field_names)
        self.assertIsNone(field_values)
        self.assertIsNone(entry_id)
        # Assert that the correct API call was made
        mock_get.assert_called_once()
