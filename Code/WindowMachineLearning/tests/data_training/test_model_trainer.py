"""
file: test_model_trainer.py
date: 23/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the ModelTrainer class.

The tests include:
    - Testing loading of data from a CSV file
    - Testing splitting of data into training, validation, and testing sets
    - Testing training of the model
    - Testing evaluation of the model

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.data_training.test_model_trainer
"""

import unittest
from unittest.mock import patch, MagicMock
from src.data_training.model_trainer import ModelTrainer
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class TestModelTrainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a ModelTrainer instance for all test methods."""
        cls.model_trainer = ModelTrainer('dummy/path/to/data.csv', 'dummy/path/to/model.pkl')

        # Mocking the pandas read_csv method to return a test dataframe
        cls.mock_data = pd.DataFrame({
            'Temperature': [20, 30, 35],
            'Humidity': [30, 45, 55],
            'IAQ Index': [50, 60, 70],
            'Window': [0, 1, 0]
        })
        cls.pandas_read_csv_patch = patch('pandas.read_csv', return_value=cls.mock_data)
        cls.pandas_read_csv_patch.start()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are done."""
        cls.pandas_read_csv_patch.stop()

    def test_load_data(self):
        """Test loading of data from a CSV file."""
        X, y = self.model_trainer.load_data()
        pd.testing.assert_frame_equal(X, self.mock_data.drop(columns=['Window']))
        pd.testing.assert_series_equal(y, self.mock_data['Window'])

    def test_split_data(self):
        """Test splitting of data into training, validation, and testing sets."""
        # Provide a larger dataset to accommodate splitting
        mock_data_large = pd.DataFrame({
            'Temperature': [20, 30, 35, 22, 25, 28],
            'Humidity': [30, 45, 55, 33, 37, 40],
            'IAQ Index': [50, 60, 70, 55, 65, 75],
            'Window': [0, 1, 0, 1, 0, 1]
        })
        with patch('pandas.read_csv', return_value=mock_data_large):
            X, y = self.model_trainer.load_data()
            X_train, X_val, X_test, y_train, y_val, y_test = self.model_trainer.split_data(X, y)
            # Test the split by comparing the lengths
            self.assertGreater(len(X_train), 0)
            self.assertGreater(len(X_val), 0)
            self.assertGreater(len(X_test), 0)
            self.assertGreater(len(y_train), 0)
            self.assertGreater(len(y_val), 0)
            self.assertGreater(len(y_test), 0)

    def test_train_model(self):
        """Test training of the model."""
        X, y = self.model_trainer.load_data()
        with patch.object(DecisionTreeClassifier, 'fit') as mock_fit:
            self.model_trainer.train_model(X, y)
            mock_fit.assert_called_once()

    def test_evaluate_model(self):
        """Test evaluation of the model."""
        # Mocking the model's predict method
        self.model_trainer.model = MagicMock(spec=DecisionTreeClassifier)
        self.model_trainer.model.predict = MagicMock(return_value=self.mock_data['Window'])

        X_test = self.mock_data.drop(columns=['Window'])
        y_test = self.mock_data['Window']
        metrics = self.model_trainer.evaluate_model(X_test, y_test)

        # Since we're mocking, all metrics should be perfect
        self.assertEqual(metrics['accuracy'], 1.0)
        self.assertEqual(metrics['precision'], 1.0)
        self.assertEqual(metrics['recall'], 1.0)
        self.assertEqual(metrics['f1_score'], 1.0)
