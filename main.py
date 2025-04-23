from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from backend.database.db import get_db_connection

app = FastAPI()

# Load the trained model
model = joblib.load("backend/models/xgboost_model.pkl")

class PredictionInput(BaseModel):
    age: float
    height: float
    weight: float
    riskAllele: float
    pValue: float
    riskFrequency: float
    orValue: float
    beta: float

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        features = np.array([[data.age, data.height, data.weight, data.riskAllele,
                              data.pValue, data.riskFrequency, data.orValue, data.beta]])
        prediction = model.predict(features)
        return {"predicted_disease": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
