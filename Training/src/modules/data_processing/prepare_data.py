"""
Ten moduł przygotowuje dane do analizy.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces categorical data with numbers.
    """
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    return df
