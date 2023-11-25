"""
file: test_data_generator.py
date: 23/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the DataGenerator class.

The tests include:
    - Testing that the generator generates the correct number of samples
    - Testing that the generator generates samples of the correct format
    - Testing that the generator generates samples with correct values

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.data.test_data_generator
"""

import unittest
from src.data.data_generator import DataGenerator


class TestDataGenerator(unittest.TestCase):
    """Test the DataGenerator class."""

    @classmethod
    def setUpClass(cls):
        """Set up a DataGenerator instance and generate sample data once for all tests."""
        cls.generator = DataGenerator()
        # Generate enough samples for all conditions just once
        cls.generator.create_sample_data(1)

    def test_comfortable_day_data(self):
        """Test data generation for a comfortable day."""

        # Assuming a predictable order, get the comfortable day sample
        comfortable_day_sample = self.generator.data_samples[0]

        # Validate that the sample contains the correct format and values
        self._validate_comfortable_day_data(comfortable_day_sample)

    def test_hot_day_data(self):
        """Test data generation for a hot day."""

        # Assuming a predictable order, get the hot day sample
        hot_day_sample = self.generator.data_samples[1]

        # Validate that the sample contains the correct format and values
        self._validate_hot_day_data(hot_day_sample)

    def test_polluted_day_data(self):
        """Test data generation for a polluted day."""

        # Assuming a predictable order, get the polluted day sample
        polluted_day_sample = self.generator.data_samples[2]

        # Validate that the sample contains the correct format and values
        self._validate_polluted_day_data(polluted_day_sample)

    def test_high_humidity_day_data(self):
        """Test data generation for a high humidity day."""

        # Assuming a predictable order, get the polluted day sample
        high_humidity_day_sample = self.generator.data_samples[3]

        # Validate that the sample contains the correct format and values
        self._validate_high_humidity_day_data(high_humidity_day_sample)

    def test_cold_day_data(self):
        """Test data generation for a cold day."""

        # Assuming a predictable order, get the polluted day sample
        cold_day_sample = self.generator.data_samples[4]

        # Validate that the sample contains the correct format and values
        self._validate_cold_day_data(cold_day_sample)

    # Helper methods for validation to avoid duplication
    def _validate_comfortable_day_data(self, sample):
        self.assertEqual(len(sample), 4)  # Ensure 4 fields
        self.assertTrue(10.0 <= sample[0] <= 30.0)  # Temperature
        self.assertTrue(0.0 <= sample[1] <= 70.0)   # Humidity
        self.assertTrue(0 <= sample[2] <= 100)      # IAQ Index
        self.assertEqual(sample[3], 1)              # Window State (1 for open)

    def _validate_hot_day_data(self, sample):
        self.assertEqual(len(sample), 4)  # Ensure 4 fields
        self.assertTrue(32.0 <= sample[0] <= 55.0)  # Temperature
        self.assertTrue(0.0 <= sample[1] <= 80.0)   # Humidity
        self.assertTrue(0 <= sample[2] <= 100)      # IAQ Index
        self.assertEqual(sample[3], 0)              # Window State (0 for closed)

    # Add more helper methods for other scenarios
    def _validate_polluted_day_data(self, sample):
        self.assertEqual(len(sample), 4)  # Ensure 4 fields
        self.assertTrue(20.0 <= sample[0] <= 35.0)  # Temperature
        self.assertTrue(20.0 <= sample[1] <= 80.0)   # Humidity
        self.assertTrue(151 <= sample[2] <= 350)      # IAQ Index
        self.assertEqual(sample[3], 0)              # Window State (0 for closed)

    def _validate_high_humidity_day_data(self, sample):
        self.assertEqual(len(sample), 4)  # Ensure 4 fields
        self.assertTrue(22.0 <= sample[0] <= 38.0)  # Temperature
        self.assertTrue(80.0 <= sample[1] <= 100.0)   # Humidity
        self.assertTrue(0 <= sample[2] <= 100)      # IAQ Index
        self.assertEqual(sample[3], 0)              # Window State (0 for closed)

    def _validate_cold_day_data(self, sample):
        self.assertEqual(len(sample), 4)  # Ensure 4 fields
        self.assertTrue(-20.0 <= sample[0] <= 5.0)  # Temperature
        self.assertTrue(0.0 <= sample[1] <= 80.0)   # Humidity
        self.assertTrue(0 <= sample[2] <= 100)      # IAQ Index
        self.assertEqual(sample[3], 0)              # Window State (0 for closed)
