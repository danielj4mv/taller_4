from fastapi import FastAPI, HTTPException

from app.prediction_request import PredictionRequest

import pandas as pd

from joblib import load

app = FastAPI(docs_url="/")
app.title = "Covertype"
app.version = "0.0.1"

modelo = load('app/pipeline.joblib') 


@app.post("/predict")
async def predict(request: PredictionRequest):
    return [modelo.predict(pd.DataFrame([request.model_dump()]))]
