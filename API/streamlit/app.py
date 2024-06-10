"""
Ten moduł uruchamia aplikację streamlit.
"""

from datetime import datetime
import joblib
import numpy as np

import streamlit as st

startTime = datetime.now()

# Data
FILENAME = "model.joblib"
model = joblib.load(FILENAME)


sex_d = {0: "Female", 1: "Male"}
smoke_d = {0: "No", 1: "Yes"}
favc_d = {0: "No", 1: "Yes"}
scc_d = {0: "No", 1: "Yes"}
family_history_with_overweight_d = {0: "No", 1: "Yes"}
caec_d = {0: "Always", 1: "Frequently", 2: "No", 3: "Sometimes" }
calc_d = {0: "Always", 1: "Frequently", 2: "No", 3: "Sometimes" }
mtrans_d = {0: "Automobile", 1: "Bike", 2: "Motorbike", 3: "Public_Transportation",  4: "Walking"}
fcvc_d = {1: "Never", 2: "Sometimes", 3: "Always"}
ch2O_d = {1: "Less than a liter", 2: "Between 1 and 2 l", 3: "More than 2 l"}
ncp_d = {1: "Between 1 and 2", 2: "Three", 3: "More than Three"}
faf_d = {0: "I do not have", 1: "1 or 2 days", 2: "2  or 4 days", 3: "4 or 5 days"}
tue_d = {0: "0-2 hours", 1: "3-5 hours", 2: "More than 5 hours"}

obesity_level_mapping = {
    0: "Insufficient_Weight",
    1: "Normal_Weight",
    2: "Obesity_Type_I",
    3: "Obesity_Type_II",
    4: "Obesity_Type_III",
    5: "Overweight_Level_I",
    6: "Overweight_Level_II"
}

def main():
    """
    Ta funkcja uruchamia aplikację streamlit.
    """
    st.set_page_config(page_title="Are you overweight?")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image(
        "https://previews.123rf.com/images/yotrak/yotrak1308/yotrak130800155/21750071-cz%C5%82owiek-stoj%C4%85cy-na-skale-wagi-z-bosej-stopy.jpg")

    with overview:
        st.title("Are you overweight?")

    with left:
        sex_radio = st.radio(
            "What is your gender?",
            list(sex_d.keys()),
            format_func=lambda x: sex_d[x]
        )

        smoke_radio = st.radio(
            "Do you smoke?",
            list(smoke_d.keys()),
            format_func=lambda x: smoke_d[x]
        )

        favc_radio = st.radio(
            "Do you eat high caloric food frequently?",
            list(favc_d.keys()),
            format_func=lambda x: favc_d[x]
        )

        scc_radio = st.radio(
            "Do you monitor the calories you eat daily?",
            list(scc_d.keys()),
            format_func=lambda x: scc_d[x]
        )

        family_history_with_overweight_radio = st.radio(
            "Has a family member suffered or suffers from overweight?",
            list(family_history_with_overweight_d.keys()),
            format_func=lambda x: family_history_with_overweight_d[x]
        )

        caec_radio = st.radio(
            "Do you eat any food between meals?",
            list(caec_d.keys()),
            format_func=lambda x: caec_d[x]
        )

        mtrans_radio = st.radio(
            "Which transportation do you usually use?",
            list(mtrans_d.keys()),
            format_func=lambda x: mtrans_d[x]
        )

        faf_radio = st.radio(
            "How often do you have physical activity?",
            list(faf_d.keys()),
            format_func=lambda x: faf_d[x]
        )

    with right:
        age_slider = st.slider(
            "What is your age?",
            value=50,
            min_value=1,
            max_value=100
        )

        height_slider = st.slider(
            "What is your height? [cm]",
            min_value=100,
            max_value=250,
            value=172
        )

        weight_slider = st.slider(
            "What is your weight? [kg]",
            min_value=20,
            max_value=300,
            value=60
        )

        fcvc_radio = st.radio(
            "Do you usually eat vegetables in your meals?",
            list(fcvc_d.keys()),
            format_func=lambda x: fcvc_d[x]
        )

        ch2O_radio = st.radio(
            "How much water do you drink daily?",
            list(ch2O_d.keys()),
            format_func=lambda x: ch2O_d[x]
        )

        ncp_radio = st.radio(
            "How many main meals do you have daily?",
            list(ncp_d.keys()),
            format_func=lambda x: ncp_d[x]
        )

        tue_radio = st.radio(
            "How much time do you use technological devices?",
            list(tue_d.keys()),
            format_func=lambda x: tue_d[x]
        )

        calc_radio = st.radio(
            "How often do you drink alcohol?",
            list(calc_d.keys()),
            format_func=lambda x: calc_d[x]
        )

    if st.button("Predict"):
        data = [
            age_slider,
            sex_radio,
            height_slider / 100,
            weight_slider,
            calc_radio,
            favc_radio,
            fcvc_radio,
            ncp_radio,
            scc_radio,
            smoke_radio,
            ch2O_radio,
            family_history_with_overweight_radio,
            faf_radio,
            tue_radio,
            caec_radio,
            mtrans_radio,
            weight_slider / ((height_slider / 100) ** 2)
        ]

        data = np.array(data).reshape(1, -1)

        # print(data)

        # scaler = StandardScaler()

        prediction_result = model.predict(data)
        prediction_proba = model.predict_proba(data)

        predicted_label = obesity_level_mapping[prediction_result[0]]

        # print("prediction_result ", prediction_result)

        with prediction:
            st.header(f"Prediction: {0}".format(predicted_label))
            st.subheader(f"Confidence: {0:.2f}%".format(np.max(prediction_proba) * 100))

if __name__ == "__main__":
    main()
