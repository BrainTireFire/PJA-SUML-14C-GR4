import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        categorical_features = df.select_dtypes(exclude="number").columns
        df.reset_index(inplace=True)

        df.rename(columns={'index': 'ID'}, inplace=True)
        one_hot_cols = categorical_features[:-1]
        df_categorical = df[one_hot_cols]

        encoder = OneHotEncoder()
        encoded_data = encoder.fit_transform(df_categorical)
        one_hot_feature_names = encoder.get_feature_names_out(one_hot_cols)
        df_encoded = pd.DataFrame(encoded_data.toarray(), columns=one_hot_feature_names)

        df_final = pd.concat([df, df_encoded], axis=1)
        df_final.drop(columns=one_hot_cols, inplace=True)
        df_final.drop('ID', axis=1, inplace=True)

        return df_final
    except Exception as e:
        print(f"Error occurred while preparing the data: {str(e)}")
        return None