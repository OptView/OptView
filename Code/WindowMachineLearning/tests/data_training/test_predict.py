import unittest

from src.data_training.predict import make_prediction


class TestModelPrediction(unittest.TestCase):
    def test_make_prediction(self):
        data = [25.80, 50.81, 50.0] # Temperature, Humidity, IAQ Index
        action = make_prediction(data)
        expected_output = 1

        # Check if action is as expected
        self.assertEqual(action, expected_output)

if __name__ == '__main__':
    unittest.main()
