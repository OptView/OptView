import pandas as pd
import joblib  # for loading the trained model

# Load the saved model
clf = joblib.load('trained_decision_tree_model.pkl')

# Predict whether to open or close the window based on new sensor data
new_data = pd.DataFrame([
    [25.80, 60.81, 50.0]  # Sample new data
], columns=['Temperature', 'Humidity', 'IAQ Index'])

prediction = clf.predict(new_data)
print("Action:", prediction[0])

# For the PDLC Glass:
# pdlc_tint = 1 if uv_light < 90 else 0

# For MQ-7 Fire Sensor:
# Window = 1 if fire_sensor > 400 else 0
