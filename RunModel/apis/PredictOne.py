# apis/predictone.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from model.convert_input_format import convert_input_format
from model.runModel import predict_top7_labels

predict_router = APIRouter()

class NodeWrapper(BaseModel):
    node: Dict[str, Any]

@predict_router.post("/predict")
async def predict(alert: NodeWrapper):
    try:
        cleaned = convert_input_format(alert.dict())
        with open("log.txt", "a") as log_file:
            log_file.write(f"Received alert: {cleaned}\n")
        result = predict_top7_labels(cleaned)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
