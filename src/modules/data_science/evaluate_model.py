"""
Ten moduł ocenia model.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from typing import Any

def evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame) -> Any:
    """
    Ta funkcja ocenia model.
    """
    try:
        predictions = model.predict(X_test)
        return predictions
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None
