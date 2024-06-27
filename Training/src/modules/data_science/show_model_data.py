"""
Ten moduł pokazuje dane modelu.
"""
from typing import Any

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

def show_model_data(y_test: pd.Series, predictions: Any) -> None:
    """
    Ta funkcja pokazuje dane modelu.
    """
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
