import os
from joblib import dump
from sklearn.tree import DecisionTreeClassifier

def save_model(model: DecisionTreeClassifier, output_dir: str) -> None:
    try:
        if not isinstance(model, DecisionTreeClassifier):
            raise ValueError("The model is not a DecisionTreeClassifier.")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        dump(model, os.path.join(output_dir, 'model.joblib'))
        print("Model saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving the model: {str(e)}")