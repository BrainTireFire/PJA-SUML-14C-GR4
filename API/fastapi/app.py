import uvicorn
import pandas as pd
import numpy as np

from libs.load_model import load_model
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class RequestJSON(BaseModel):
    age: int
    sex: int
    height: float
    weight: int
    calc: int
    favc: int
    fcvc: int
    ncp: int
    scc: int
    smoke: int
    ch2O: int
    family_history_with_overweight: int
    faf: int
    tue: int
    caec: int
    mtrans: int
    bmi: float

app = FastAPI()

@app.post('/predict', tags=["predict"])
def predict(request: RequestJSON):
    df = pd.DataFrame(request.__dict__, index=[0])
    data = np.array(df.values).reshape(1, -1)

    print(data)

    model = load_model()
    prediction_result = model.predict(data)
    prediction_proba = model.predict_proba(data)

    obesity_level_mapping = {
        0: "Insufficient_Weight",
        1: "Normal_Weight",
        2: "Obesity_Type_I",
        3: "Obesity_Type_II",
        4: "Obesity_Type_III",
        5: "Overweight_Level_I",
        6: "Overweight_Level_II"
    }

    print(prediction_result)

    predicted_label = obesity_level_mapping[prediction_result[0]]


    return jsonable_encoder({'prediction': predicted_label, 'confidence': np.max(prediction_proba) * 100})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)