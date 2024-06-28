"""
Ten moduł ocenia model.
"""
from typing import Any

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def evaluate_model(model: DecisionTreeClassifier, x_test: pd.DataFrame) -> Any:
    """
    Performs prediction using trained model and supplier test dataset. Returns array of predicted values.
    """
    try:
        predictions = model.predict(x_test)
        return predictions
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None
