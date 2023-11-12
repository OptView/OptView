# Decision Tree Classifier for Smart Window Automation

## Abstract
The `trained_decision_tree_model.pkl` is a finely-tuned decision tree classifier developed to automate the decision-making process of window operations in smart home systems based on environmental data. Trained with a vast dataset of 50 million samples covering diverse weather conditions, the model exhibits exceptional performance, achieving 100% accuracy, precision, recall, and F1-score in predicting whether a window should be open or closed.

## Model Description
The classifier is designed to make window operation decisions by analyzing environmental conditions represented in the dataset, which includes comfortable, hot, polluted, high humidity, and cold days. The training dataset is substantial, ensuring robustness and the model's generalizability across climates.

## Training Data
The training dataset consists of 50 million samples across five environmental conditions:

1. **Comfortable Day:** Temperatures up to 28°C with moderate humidity.
2. **Hot Day:** Temperatures between 32°C to 55°C with moderate to high humidity.
3. **Polluted Day:** Poor air quality with IAQ Index between 151 to 350.
4. **High Humidity Day:** Humidity levels between 80% to 100% and non-comfortable temperature ranges.
5. **Cold Day:** Temperatures ranging from -20°C to 5°C, simulating cold weather conditions.

## Model Evaluation
The classifier has been thoroughly evaluated on a test set, yielding the following metrics:

- **Accuracy:** 100%
- **Precision:** 100%
- **Recall:** 100%
- **F1-Score:** 100%

These metrics indicate the model's superior predictive capabilities.

## Validation Accuracy
The model has also been validated on a separate dataset, demonstrating a steadfast accuracy rate of 100%, ensuring the model's consistency.

## Applications
This classifier is ready for deployment in smart home environments to facilitate energy savings and enhance indoor comfort by responding intelligently to changing outdoor environmental conditions.

## Conclusion
The `trained_decision_tree_model.pkl` demonstrates the potential and effectiveness of machine learning in the domain of home automation, offering unparalleled accuracy and reliability in smart window regulation.
