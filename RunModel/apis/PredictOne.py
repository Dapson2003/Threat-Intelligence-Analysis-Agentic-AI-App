# apis/predictone.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from model.runModel import clean_run_prediction

predict_router = APIRouter()

class NodeWrapper(BaseModel):
    node: Dict[str, Any]

@predict_router.post("/predict")
async def predict(alert: NodeWrapper):
    try:
        result = clean_run_prediction(alert.model_dump())

        # Optional logging
        with open("log.txt", "a") as f:
            f.write(f"Received alert: {alert.model_dump()}\n")

        result = clean_run_prediction(alert.model_dump())
        return result  # ✅ this now returns a proper JSON object   

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
