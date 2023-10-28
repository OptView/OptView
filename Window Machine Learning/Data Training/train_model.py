from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib  # for saving and loading the model

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

# Save the trained model
joblib.dump(clf, 'trained_decision_tree_model.pkl')

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")
