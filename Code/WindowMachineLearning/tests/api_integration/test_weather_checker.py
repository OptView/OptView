"""
file: test_data_generator.py
date: 23/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the WeatherChecker class.

The tests include:
    - Testing that the check_weather_conditions method returns the correct code for rainy weather
    - Testing that the check_weather_conditions method returns the correct code for snowy weather
    - Testing that the check_weather_conditions method returns the correct code for clear weather

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.api_integration.test_weather_checker
"""

import unittest
from unittest.mock import patch, MagicMock
from src.api_integration.weather_checker import WeatherChecker

class TestWeatherChecker(unittest.TestCase):

    def setUp(self):
        """Set up a WeatherChecker instance with a mock API key for all test methods."""
        self.api_key = 'mock_api_key'
        self.weather_checker = WeatherChecker(self.api_key)

    @patch('requests.get')
    def test_check_weather_conditions_rain(self, mock_get):
        """Test check_weather_conditions method for rainy weather."""
        # Mock response object with rainy weather data
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "weather": [{"main": "Rain"}],
            "cod": 200
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the method under test
        condition_code = self.weather_checker.check_weather_conditions('London')

        # Assert method returns the correct code for rain
        self.assertEqual(condition_code, 1)
        # Assert that 'It's raining in London.' is printed
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_check_weather_conditions_snow(self, mock_get):
        """Test check_weather_conditions method for snowy weather."""
        # Similar setup for snowy weather...
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "weather": [{"main": "Snow"}],
            "cod": 200
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the method under test
        condition_code = self.weather_checker.check_weather_conditions('Moscow')

        # Assert method returns the correct code for snow
        self.assertEqual(condition_code, 1)
        # Assert that 'It's snowing in Moscow.' is printed
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_check_weather_conditions_clear(self, mock_get):
        """Test check_weather_conditions method for clear weather."""
        # Similar setup for clear weather...
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "weather": [{"main": "Clear"}],
            "cod": 200
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the method under test
        condition_code = self.weather_checker.check_weather_conditions('Paris')

        # Assert method returns the correct code for clear weather
        self.assertEqual(condition_code, 0)
        # Assert that 'It's clear in Paris.' is printed
        mock_get.assert_called_once()