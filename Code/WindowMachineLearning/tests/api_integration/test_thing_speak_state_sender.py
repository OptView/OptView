"""
file: test_thing_speak_state_sender.py
date: 25/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the ThingSpeakStateSender class.

The tests include:
    - Testing that the get_action method returns the correct action for a successful API response
    - Testing that the get_action method returns None for a failed API response

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.api_integration.test_thing_speak_state_sender
"""

import unittest
from unittest.mock import patch, MagicMock
import requests_mock
from src.api_integration.thing_speak_state_sender import ThingSpeakStateSender


class TestThingSpeakStateSender(unittest.TestCase):
    """Test class for the ThingSpeakStateSender class."""

    def setUp(self):
        """Set up a ThingSpeakStateSender instance for all test methods."""
        self.read_channel_id = "dummy_channel_id"
        self.write_api_key = "dummy_api_key"
        self.model_path = "dummy_model_path"

        # Mock the environment variables
        self.env_patcher = patch.dict('os.environ', {
            'WEATHER_API_KEY': 'fake_api_key'
        })
        self.env_patcher.start()

        # Mock the WindowController's constructor (__init__ method) to prevent file access
        self.window_controller_patch = patch(
            'src.data_training.window_controller.WindowController.__init__',
            return_value=None)
        self.mock_window_controller = self.window_controller_patch.start()

        self.sender = ThingSpeakStateSender(self.read_channel_id,
                                            self.write_api_key, self.model_path)

    def tearDown(self):
        # Stop the patchers
        self.window_controller_patch.stop()
        self.env_patcher.stop()

    @patch('src.api_integration.weather_checker.WeatherChecker')
    @patch('src.api_integration.thing_speak_data_retriever.ThingSpeakDataRetriever')
    @patch('src.data_training.window_controller.WindowController.make_prediction',
           return_value=1)
    def test_get_action(self, mock_make_prediction, mock_data_retriever,
                        mock_weather_checker):
        """Test get_action method for a successful API response."""

        # Configure the mocks
        mock_weather_checker.return_value.check_weather_conditions.return_value = False
        mock_data_retriever.return_value.get_data.return_value = (
        None, {'field1': -22, 'field2': 50, 'field4': 100}, None)

        # Call the method under test
        action = self.sender.get_action()

        # Verify the expected results
        self.assertIsNotNone(action)
        self.assertEqual(action, 0)

    @requests_mock.Mocker()
    def test_set_state(self, m):
        """Test set_state method for a successful API response."""

        # Configure the request mock
        m.get(self.sender.write_api_base_url, status_code=200, text='0')

        # Call the method under test
        self.sender.set_state(0)

        # Verify the expected results
        self.assertEqual(m.last_request.qs['api_key'][0], self.write_api_key)
        self.assertEqual(m.last_request.qs['field1'][0], '0')

        # Repeat the test for setting the state to '1'
        m.get(self.sender.write_api_base_url, status_code=200, text='1')
        self.sender.set_state(1)
        self.assertEqual(m.last_request.qs['field1'][0], '1')
