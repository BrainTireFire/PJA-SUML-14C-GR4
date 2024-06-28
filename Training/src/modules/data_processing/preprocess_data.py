"""
Ten moduł przetwarza dane.
"""

import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates an additional feature.
    """
    try:
        df['BMI'] = round(df['Weight'] / (df['Height']) ** 2, 2)

        return df
    except Exception as e:
        print(f"Error occurred while processing the data: {str(e)}")
        return None
