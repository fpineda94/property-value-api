import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent.parent / "models" / "xgboost_model.pkl"

model = joblib.load(MODEL_PATH)

def predict(input_data: dict) -> float:
    # convertir el diccionario a array para el modelo
    values = np.array(list(input_data.values())).reshape(1, -1)
    prediction = model.predict(values)
    return float(np.exp(prediction[0]))