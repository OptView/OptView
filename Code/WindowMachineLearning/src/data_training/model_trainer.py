import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib


class ModelTrainer:
    print("ModelTrainer Called")

    def __init__(self, data_path, model_path):
        """
        Initialize the ModelTrainer with the path to the data and the path to save the model.

        Args:
            data_path (str): The path to the CSV file containing the data.
            model_path (str): The path to save the trained model.
        """
        self.data_path = data_path
        self.model_path = model_path
        self.model = None

    def load_data(self):
        """Load data from a CSV file."""
        data = pd.read_csv(self.data_path)
        X = data.drop(columns=['Window'])
        y = data['Window']
        return X, y

    def split_data(self, X, y):
        """Split data into training, validation, and testing sets."""
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3,
                                                            random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp,
                                                        test_size=0.5,
                                                        random_state=42)
        return X_train, X_val, X_test, y_train, y_val, y_test

    def train_model(self, X_train, y_train):
        """Train a decision tree classifier."""
        self.model = DecisionTreeClassifier(random_state=42)
        self.model.fit(X_train, y_train)

    def save_model(self):
        """Save the trained model."""
        joblib.dump(self.model, self.model_path)

    def evaluate_model(self, X_test, y_test):
        """Evaluate the model using various metrics."""
        y_pred = self.model.predict(X_test)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred)
        }
        return metrics

    def print_evaluation(self, metrics):
        """Print evaluation metrics."""
        print(f"Model Accuracy: {metrics['accuracy'] * 100:.2f}%")
        print(f"Precision: {metrics['precision'] * 100:.2f}%")
        print(f"Recall: {metrics['recall'] * 100:.2f}%")
        print(f"F1-Score: {metrics['f1_score'] * 100:.2f}%")


# Example usage:
data_path = '../data/data_samples.csv'
model_path = '../../models/trained_decision_tree_model.pkl'

trainer = ModelTrainer(data_path, model_path)

X, y = trainer.load_data()
X_train, X_val, X_test, y_train, y_val, y_test = trainer.split_data(X, y)
trainer.train_model(X_train, y_train)

trainer.save_model()

metrics = trainer.evaluate_model(X_test, y_test)
trainer.print_evaluation(metrics)
