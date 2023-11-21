import pandas as pd
import joblib


class WindowController:
    print("WindowController Called")

    def __init__(self, model_path):
        """
        Initialize the WindowController with a trained model.

        Args:
            model_path (str): The file path to the trained model file.
        """
        self.clf = self.load_model(model_path)

    def load_model(self, model_path):
        """Load the trained model from a file.

        Args:
            model_path (str): The file path to the trained model file.

        Returns:
            object: The loaded model object, which is an instance of the classifier used in training.
        """
        clf = joblib.load(model_path)
        return clf

    def make_prediction(self, data):
        """Predict the action to take based on sensor data.

        Args:
            data (list): The sensor data input for making a prediction, expected to be in the
                         order of ['Temperature', 'Humidity', 'IAQ Index'].

        Returns:
            int: The predicted action, where 0 means 'close the window' and 1 means 'open the window'.
        """
        sample_data = pd.DataFrame([data],
                                   columns=['Temperature', 'Humidity', 'IAQ Index'])
        prediction = self.clf.predict(sample_data)
        return prediction[0]
