"""
Ten moduł przetwarza dane.
"""

import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates an additional feature.
    """
    df['BMI'] = round(df['Weight'] / (df['Height']) ** 2, 2)

    return df
