"""
Ten moduł dzieli dane na zestawy treningowe i testowe.
"""
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Ta funkcja dzieli dane na zestawy treningowe i testowe.
    """
    x = df.drop(columns=['NObeyesdad'])
    y = df['NObeyesdad']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.transform(X_test)

    return x_train, x_test, y_train, y_test
