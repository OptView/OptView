import unittest
from src.data_training.window_controller import WindowController

class TestWindowController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the path to the model file for testing

        # For testing directory
        # model_path = '../models/trained_decision_tree_model.pkl'

        # For testing file
        # model_path = '../../models/trained_decision_tree_model.pkl'

        # For Coverage testing report using terminal
        cls.model_path = 'models/trained_decision_tree_model.pkl'

        # Instantiate the WindowController with the model path
        cls.window_controller = WindowController(cls.model_path)

    def test_normal(self):
        # Normal conditions - expecting the window to be opened
        data = [20.00, 35.81, 50.0]  # Temperature, Humidity, IAQ Index
        action = self.window_controller.make_prediction(data)
        expected_output = 1  # 1 indicates open the window
        self.assertEqual(action, expected_output)

    def test_max_normal(self):
        # Edge of normal conditions - expecting the window to be opened
        data = [30.00, 60.00, 100.0]  # Temperature, Humidity, IAQ Index
        action = self.window_controller.make_prediction(data)
        expected_output = 1  # 1 indicates open the window
        self.assertEqual(action, expected_output)

    def test_min_normal(self):
        # Minimum normal conditions - expecting the window to be opened
        data = [10.00, 00.00, 00.0]  # Temperature, Humidity, IAQ Index
        action = self.window_controller.make_prediction(data)
        expected_output = 1  # 1 indicates open the window
        self.assertEqual(action, expected_output)

# The following line would run the tests if uncommented and this file is executed
# if __name__ == '__main__':
#     unittest.main()
