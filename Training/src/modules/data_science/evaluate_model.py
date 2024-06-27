"""
Ten moduł ocenia model.
"""
from typing import Any

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def evaluate_model(model: DecisionTreeClassifier, x_test: pd.DataFrame) -> Any:
    """
    Ta funkcja ocenia model.
    """
    try:
        predictions = model.predict(x_test)
        return predictions
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None
