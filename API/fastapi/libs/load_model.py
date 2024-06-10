"""
Ten moduł wczytuje model.
"""

import joblib

def load_model():
    """
    Ta funkcja wczytuje model.
    """
    filename = "ml_model/model.joblib"
    model = joblib.load(filename)

    return model
