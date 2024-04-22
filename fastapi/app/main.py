from fastapi import FastAPI, HTTPException

from app.prediction_request import PredictionRequest

import pandas as pd

from joblib import load

app = FastAPI(docs_url="/")
app.title = "Covertype"
app.version = "0.0.1"

modelo = load('app/pipeline.joblib') 


@app.post("/predict")
def predict(request: PredictionRequest):
    diccionario=request.model_dump()
    print(diccionario)
    dataf=pd.DataFrame([diccionario])
    print(list(modelo.predict(dataf)),type(modelo.predict(dataf)))
    return modelo.predict(dataf).tolist()
