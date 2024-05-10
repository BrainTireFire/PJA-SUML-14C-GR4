import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        for column in df.select_dtypes(include=['int64', 'float64']):
            df[column] = df[column].fillna(df[column].mean())

        for column in df.select_dtypes(include=['object']):
            df[column] = df[column].fillna(df[column].mode()[0])

        for column in df.select_dtypes(include=['object']):
            df[column] = pd.Categorical(df[column]).codes

        print('Dataset cleaned successfully')
        return df
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None