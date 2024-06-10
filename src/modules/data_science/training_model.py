"""
Ten moduł trenuje model.
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def training_model(x_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    """
    Ta funkcja trenuje model.
    """
    try:        
        model = DecisionTreeClassifier()
        model.fit(x_train, y_train)

        return model
    except Exception as e:
        print(f"Error occurred while training the data: {str(e)}")
        return None
