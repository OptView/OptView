import unittest
import joblib
import os

from src.data_training.model_prediction import make_prediction, load_model


class TestComfortableDayPrediction(unittest.TestCase):

    def test_normal_temp(self):
        # For testing directory
        # model_path = '../models/trained_decision_tree_model.pkl'

        # For testing file
        # model_path = '../../models/trained_decision_tree_model.pkl'

        # For Coverage testing report using terminal
        model_path = 'models/trained_decision_tree_model.pkl'

        clf = load_model(model_path)

        data = [25.80, 50.81, 50.0]  # Temperature, Humidity, IAQ Index

        action = make_prediction(data, clf)
        expected_output = 1

        # Check if action is as expected
        self.assertEqual(action, expected_output)


# if __name__ == '__main__':
#     unittest.main()