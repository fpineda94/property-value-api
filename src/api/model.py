import joblib
import numpy as np
from pathlib import Path
import json

MODEL_PATH = Path(__file__).parent.parent.parent / "models" / "xgboost_model.pkl"
COLUMNS_PATH = Path(__file__).parent.parent.parent / "models" / "columns.json"

with open(COLUMNS_PATH) as f:
    columns = json.load(f) 

model = joblib.load(MODEL_PATH)


def predict(input_data: dict) -> float:
    values = np.array([float(input_data.get(col, 0)) for col in columns]).reshape(1, -1)
    prediction = model.predict(values)
    return float(np.exp(prediction[0]))