"""
Ten moduł tworzy API.
"""

import uvicorn
import pandas as pd
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder


from libs.load_model import load_model


class RequestJSON(BaseModel):
    """
    Ta klasa definiuje dane wejściowe.
    """
    age: int
    sex: str
    height: float
    weight: int
    calc: str
    favc: str
    fcvc: str
    ncp: str
    scc: str
    smoke: str
    ch2O: str
    family_history_with_overweight: str
    faf: str
    tue: str
    caec: str
    mtrans: str

def map_request_to_row(request: RequestJSON):
    # Define the reversed dictionaries
    sex_d_reversed = {'Female': 0, 'Male': 1}
    smoke_d_reversed = {'No': 0, 'Yes': 1}
    favc_d_reversed = {'No': 0, 'Yes': 1}
    scc_d_reversed = {'No': 0, 'Yes': 1}
    family_history_with_overweight_d_reversed = {'No': 0, 'Yes': 1}
    caec_d_reversed = {'Always': 0, 'Frequently': 1, 'No': 2, 'Sometimes': 3}
    calc_d_reversed = {'Always': 0, 'Frequently': 1, 'No': 2, 'Sometimes': 3}
    mtrans_d_reversed = {'Automobile': 0, 'Bike': 1, 'Motorbike': 2, 'Public_Transportation': 3, 'Walking': 4}
    fcvc_d_reversed = {'Never': 1, 'Sometimes': 2, 'Always': 3}
    ch2O_d_reversed = {'Less than a liter': 1, 'Between 1 and 2 l': 2, 'More than 2 l': 3}
    ncp_d_reversed = {'Between 1 and 2': 1, 'Three': 2, 'More than Three': 3}
    faf_d_reversed = {'I do not have': 0, '1 or 2 days': 1, '2  or 4 days': 2, '4 or 5 days': 3}
    tue_d_reversed = {'0-2 hours': 0, '3-5 hours': 1, 'More than 5 hours': 2}

    # Map the input values to their numeric equivalents
    mapped_row = {
        "age": request.age,
        "sex": sex_d_reversed[request.sex],
        "height": request.height,
        "weight": request.weight,
        "calc": calc_d_reversed[request.calc],
        "favc": favc_d_reversed[request.favc],
        "fcvc": fcvc_d_reversed[request.fcvc],
        "ncp": ncp_d_reversed[request.ncp],
        "scc": scc_d_reversed[request.scc],
        "smoke": smoke_d_reversed[request.smoke],
        "ch2O": ch2O_d_reversed[request.ch2O],
        "family_history_with_overweight": family_history_with_overweight_d_reversed[request.family_history_with_overweight],
        "faf": faf_d_reversed[request.faf],
        "tue": tue_d_reversed[request.tue],
        "caec": caec_d_reversed[request.caec],
        "mtrans": mtrans_d_reversed[request.mtrans],
        "bmi": request.weight / (request.height ** 2)
    }
    
    return mapped_row

app = FastAPI()

@app.post('/predict', tags=["predict"])
def predict(request: RequestJSON):
    """
    Ta funkcja przewiduje poziom otyłości.
    """

    transformed_request = map_request_to_row(request=request)

    df = pd.DataFrame(transformed_request, index=[0])
    data = np.array(df.values).reshape(1, -1)

    # print(data)

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

    # print(prediction_result)

    predicted_label = obesity_level_mapping[prediction_result[0]]

    return jsonable_encoder(
        {
            'prediction': predicted_label,
            'confidence': np.max(prediction_proba) * 100
        })


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
