import joblib

def load_model():
    filename = "ml_model/model.joblib"
    model = joblib.load(filename)

    return model