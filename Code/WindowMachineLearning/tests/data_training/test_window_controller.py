"""
file: test_data_generator.py
date: 23/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the WindowController class.

The tests include:
    - Testing that the window opens on a comfortable day
    - Testing that the window closes on a hot day
    - Testing that the window closes on a polluted day
    - Testing that the window closes on a high humidity day
    - Testing that the window closes on a cold day

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.data_training.test_window_controller
"""

import unittest
from src.data_training.window_controller import WindowController

class TestWindowController(unittest.TestCase):
    """Test the WindowController class."""

    @classmethod
    def setUpClass(cls):
        """Set up the WindowController with a model path for testing."""

        # For testing directory
        # model_path = '../models/trained_decision_tree_model.pkl'

        # For testing file
        # model_path = '../../models/trained_decision_tree_model.pkl'

        # For Coverage testing report using terminal
        cls.model_path = 'models/trained_decision_tree_model.pkl'

        # Instantiate the WindowController with the model path
        cls.window_controller = WindowController(cls.model_path)

    def test_comfortable_day_open_window(self):
        """Test that the window opens on a comfortable day."""
        data = [20.0, 35.0, 50.0]  # Temperature, Humidity, IAQ Index
        action = self.window_controller.make_prediction(data)
        expected_output = 1  # 1 indicates open the window
        self.assertEqual(action, expected_output)

    def test_hot_day_close_window(self):
        """Test that the window closes on a hot day."""
        data = [40.0, 60.0, 50.0]
        action = self.window_controller.make_prediction(data)
        expected_output = 0  # 0 indicates close the window
        self.assertEqual(action, expected_output)

    def test_polluted_day_close_window(self):
        """Test that the window closes on a polluted day."""
        data = [25.0, 50.0, 200.0]
        action = self.window_controller.make_prediction(data)
        expected_output = 0  # 0 indicates close the window
        self.assertEqual(action, expected_output)

    def test_high_humidity_day_close_window(self):
        """Test that the window closes on a high humidity day."""
        data = [30.0, 85.0, 50.0]
        action = self.window_controller.make_prediction(data)
        expected_output = 0  # 0 indicates close the window
        self.assertEqual(action, expected_output)

    def test_cold_day_close_window(self):
        """Test that the window closes on a cold day."""
        data = [-10.0, 50.0, 50.0]
        action = self.window_controller.make_prediction(data)
        expected_output = 0  # 0 indicates close the window
        self.assertEqual(action, expected_output)
