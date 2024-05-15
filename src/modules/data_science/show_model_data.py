import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import recall_score, accuracy_score, precision_score
from sklearn.tree import DecisionTreeClassifier
from typing import Any

def show_model_data(model: DecisionTreeClassifier, y_test: pd.Series, predictions: Any) -> None:
    try:
        recall = recall_score(y_test, predictions, average='weighted')
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions, average='weighted', zero_division=1)

        print(f"Model: {type(model).__name__}")
        print(f"Recall: {recall}")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print("-" * 50)

        # plot_data_distribution(y_test)

    except Exception as e:
        print(f'An error occurred while showing model data: {str(e)}')

# def plot_data_distribution(data: pd.Series) -> None:
#     plt.figure(figsize=(8, 6))
#     sns.histplot(data, bins=30, kde=True)
#     plt.title('Data Distribution')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.show()