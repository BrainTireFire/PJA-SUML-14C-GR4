import pandas as pd
from typing import Tuple

def clean_data(df) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        for column in df.select_dtypes(include=['int64', 'float64']):
            df[column] = df[column].fillna(df[column].mean())
        for column in df.select_dtypes(include=['object']):
            df[column] = df[column].fillna(df[column].mode()[0])
        for column in df.select_dtypes(include=['object']):
            df[column] = pd.Categorical(df[column]).codes
        return df
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None, None