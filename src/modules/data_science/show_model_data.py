import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from typing import Any

def show_model_data(model: DecisionTreeClassifier, y_test: pd.Series, predictions: Any) -> None:
    try:
        name = "DecisionTreeClassifier"
        accuracy = accuracy_score(y_test, predictions)
        print(f"{name}: {accuracy}")
        print("Classification Report:")
        print(classification_report(y_test, predictions))
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