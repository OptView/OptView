import unittest

# test_predict.py
from Data_Training.predict import make_prediction, load_model


class TestModelPrediction(unittest.TestCase):
    def test_prediction(self):
        # You would need a test model or a mock here
        clf = load_model('test_trained_decision_tree_model.pkl')
        data = [25.80, 50.81, 50.0]
        action = make_prediction(clf, data)
        expected_output = 1
        # Check if action is as expected
        self.assertEqual(action, expected_output)  # replace 'expected_action' with the actual expected result

if __name__ == '__main__':
    unittest.main()
