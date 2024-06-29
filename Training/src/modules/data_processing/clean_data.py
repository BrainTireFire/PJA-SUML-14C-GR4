"""
Ten moduł czyści dane.
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans data by removing duplicates.
    """
    df.drop_duplicates(inplace=True)
    df.duplicated().sum()

    print('Dataset cleaned successfully')
    return df
