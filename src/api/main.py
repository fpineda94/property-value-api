from fastapi import FastAPI
from src.api.model import predict

#Instancia de la clase
app = FastAPI()

@app.get("/health") #Decorador
def health():
    return {'Status': 'ok'}






@app.post("/predict")
def make_prediction(input_data: dict):
    return predict(input_data)