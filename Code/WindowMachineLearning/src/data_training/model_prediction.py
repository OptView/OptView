import pandas as pd
import joblib
import os

def load_model(model_path):
    """Load the trained model from a file."""

    clf = joblib.load(model_path)

    return clf

def make_prediction(data, clf):
    """Predict the action based on sensor data."""

    sample_data = pd.DataFrame([data], columns=['Temperature', 'Humidity', 'IAQ Index'])
    prediction = clf.predict(sample_data)

    return prediction[0]
