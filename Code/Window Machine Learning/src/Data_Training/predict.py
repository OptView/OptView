import pandas as pd
import joblib

def load_model(model_path):
    """Load the trained model from a file."""
    clf = joblib.load(model_path)
    return clf

def make_prediction(clf, data):
    """Predict the action based on sensor data."""
    sample_data = pd.DataFrame([data], columns=['Temperature', 'Humidity', 'IAQ Index'])
    prediction = clf.predict(sample_data)
    return prediction[0]



# For the PDLC Glass:
# pdlc_tint = 1 if uv_light < 90 else 0

# For MQ-7 Fire Sensor:
# Window = 1 if fire_sensor > 400 else 0
