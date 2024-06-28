"""
Ten moduł trenuje model.
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def training_model(x_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    """
    Trains a DecisionTreeClassifier model.
    """
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    return model
