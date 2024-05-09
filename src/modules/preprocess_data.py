import pandas as pd
from typing import Tuple

def preprocess_data(df) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        df['BMI'] = round(df['Weight'] / (df['Height']) ** 2, 2)
        return df
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None, None