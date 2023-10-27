# Train the data and predict whether to open the window or not

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Sample data
data = pd.DataFrame([
    [20.8, 60.81, 1019.14, 120.95, 5.00, 0.00, 'Open'],
    [50.0, 70.00, 1019.14, 90.00, 7.00, 0.00, 'Close'],
    # ... add more data
], columns=['Temperature', 'Humidity', 'Pressure', 'Gas Resistance', 'UV Light', 'Smoke', 'Window'])

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
    [20.80, 60.81, 1019.14, 120.95, 5.00, 0.00]
], columns=['Temperature', 'Humidity', 'Pressure', 'Gas Resistance', 'UV Light', 'Smoke'])

prediction = clf.predict(new_data)
print("Action:", prediction[0])
