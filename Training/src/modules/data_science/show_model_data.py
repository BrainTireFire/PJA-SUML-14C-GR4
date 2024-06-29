"""
Ten moduł pokazuje dane modelu.
"""
from typing import Any

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

def show_model_data(y_test: pd.Series, predictions: Any) -> None:
    """
    Prints classification report by crossreferencing predicted and
    actual values of dependent variable.
    """
    name = "DecisionTreeClassifier"
    accuracy = accuracy_score(y_test, predictions)
    print(f"{name}: {accuracy}")
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    print("-" * 50)

    # plot_data_distribution(y_test)
