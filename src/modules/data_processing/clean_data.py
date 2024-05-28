import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.drop_duplicates(inplace=True)
        df.duplicated().sum()

        print('Dataset cleaned successfully')
        return df
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None