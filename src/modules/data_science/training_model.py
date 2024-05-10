import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, recall_score, precision_score
from sklearn.tree import DecisionTreeClassifier
from typing import Tuple

def training_model(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    try:        
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        return model
    except Exception as e:
        print(f"Error occurred while training the data: {str(e)}")
        return None
