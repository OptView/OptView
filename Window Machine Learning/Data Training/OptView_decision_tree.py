# Train the data and predict whether to open the window or not

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Load data from CSV
data = pd.read_csv('data_samples.csv')

# Separate features and target variable
X = data.drop(columns=['Window'])
y = data['Window']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Predict whether to open or close the window based on new sensor data
new_data = pd.DataFrame([
    [55.80, 60.81, 50.0]  # Sample new data
], columns=['Temperature', 'Humidity', 'IAQ Index'])

prediction = clf.predict(new_data)
print("Action:", prediction[0])

# For the PDLC Glass:
# pdlc_tint = 1 if uv_light < 90 else 0

# For MQ-7 Fire Sensor:
# Window = 1 if fire_sensor > 400 else 0

