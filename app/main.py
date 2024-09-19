# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import FraudDetectionModel

app = FastAPI(title="API de Détection de Fraude par Carte de Crédit")

# Initialiser le modèle
try:
    model = FraudDetectionModel()
except FileNotFoundError as e:
    print(e)
    model = None

class Transaction(BaseModel):
    Time:float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.post("/predict")
def predict_fraud(transaction: Transaction):
    if model is None:
        raise HTTPException(status_code=500, detail="Modèle non chargé.")
    
    input_data = transaction.dict()
    try:
        prediction = model.predict(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return prediction

@app.get("/")
def read_root():
    return {"message": "Bienvenue à l'API de Détection de Fraude par Carte de Crédit"}
