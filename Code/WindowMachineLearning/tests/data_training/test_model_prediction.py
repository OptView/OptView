import unittest
import joblib
import os

from src.data_training.window_controller import make_prediction, load_model


class TestComfortableDayPrediction(unittest.TestCase):

    # this method is only run once for the entire class
    @classmethod
    def setUpClass(cls):
        # Define the model path and load the model once for all tests

        # For testing directory
        # model_path = '../models/trained_decision_tree_model.pkl'

        # For testing file
        # model_path = '../../models/trained_decision_tree_model.pkl'

        # For Coverage testing report using terminal
        cls.model_path = 'models/trained_decision_tree_model.pkl'

        cls.clf = load_model(cls.model_path)

    def test_normal(self):
        data = [20.00, 35.81, 50.0]  # Temperature, Humidity, IAQ Index
        action = make_prediction(data, self.clf)
        expected_output = 1
        self.assertEqual(action, expected_output)

    def test_max_normal(self):
        """Test Failed"""
        data = [30.00, 60.00, 100.0]  # Temperature, Humidity, IAQ Index
        action = make_prediction(data, self.clf)
        expected_output = 1
        self.assertEqual(action, expected_output)

    def test_min_normal(self):
        """Test Failed"""
        data = [10.00, 00.00, 00.0]  # Temperature, Humidity, IAQ Index
        action = make_prediction(data, self.clf)
        expected_output = 1
        self.assertEqual(action, expected_output)

# if __name__ == '__main__':
#     unittest.main()